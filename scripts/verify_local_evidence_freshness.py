from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "mvp-closeout-evidence-ledger.json"
HEX_SHA = re.compile(r"^[0-9a-f]{40}$")


def parse_repo_root(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("expected NAME=PATH")
    name, raw_path = value.split("=", 1)
    name = name.strip()
    if not name:
        raise argparse.ArgumentTypeError("repository name is empty")
    return name, Path(raw_path).expanduser()


def run_git_head(path: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git rev-parse failed in {path}")
    return result.stdout.strip()


def default_candidates(repo_name: str) -> list[Path]:
    if repo_name == ROOT.name:
        return [ROOT]
    parent = ROOT.parent
    return [
        parent / repo_name,
        parent / f"{repo_name}-work",
    ]


def resolve_repo_root(repo_name: str, explicit_roots: dict[str, Path]) -> Path | None:
    if repo_name in explicit_roots:
        return explicit_roots[repo_name]
    for candidate in default_candidates(repo_name):
        if (candidate / ".git").exists():
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only owner-local check that compares MVP ledger repository "
            "heads with local checkouts when those checkouts are available."
        )
    )
    parser.add_argument(
        "--repo-root",
        action="append",
        default=[],
        type=parse_repo_root,
        metavar="NAME=PATH",
        help="Map a ledger repository name to a local checkout path.",
    )
    parser.add_argument(
        "--strict-missing",
        action="store_true",
        help="Fail if a ledger repository has no local checkout.",
    )
    args = parser.parse_args()

    explicit_roots = dict(args.repo_root)
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))

    failures: list[str] = []
    checked: list[str] = []
    skipped: list[str] = []

    for surface in ledger.get("verified_surfaces", []):
        repo_name = surface.get("repository")
        recorded_head = str(surface.get("head", ""))
        if not repo_name:
            failures.append("ledger surface missing repository name")
            continue
        if recorded_head.startswith("self-referential"):
            skipped.append(f"{repo_name}: self-referential ledger row")
            continue
        if not HEX_SHA.match(recorded_head):
            failures.append(f"{repo_name}: recorded head is not a 40-character SHA")
            continue

        repo_root = resolve_repo_root(repo_name, explicit_roots)
        if repo_root is None:
            message = f"{repo_name}: local checkout not found"
            if args.strict_missing:
                failures.append(message)
            else:
                skipped.append(message)
            continue
        if not repo_root.exists():
            failures.append(f"{repo_name}: mapped checkout does not exist: {repo_root}")
            continue

        try:
            actual_head = run_git_head(repo_root)
        except RuntimeError as exc:
            failures.append(f"{repo_name}: {exc}")
            continue

        if actual_head != recorded_head:
            failures.append(
                f"{repo_name}: ledger head {recorded_head} != local head {actual_head}"
            )
        else:
            checked.append(f"{repo_name}: {actual_head}")

    for item in checked:
        print(f"checked {item}")
    for item in skipped:
        print(f"skipped {item}")

    if failures:
        for item in failures:
            print(f"freshness failed: {item}", file=sys.stderr)
        return 1

    print("local evidence freshness check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
