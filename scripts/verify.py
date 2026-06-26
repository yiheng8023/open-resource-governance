from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "NOTICE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md",
    "SECURITY.md",
    "SUPPORT.md",
    ".github/FUNDING.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/boundary-question.yml",
    ".github/ISSUE_TEMPLATE/resource-lane-suggestion.yml",
    ".github/ISSUE_TEMPLATE/docs-improvement.yml",
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    "data/repositories.json",
    "docs/license-policy.md",
    "docs/community-feedback-model.md",
    "docs/public-private-boundary.md",
    "docs/repository-map.md",
    "docs/promotion-kit.md",
    "docs/free-promotion-playbook.md",
    "docs/launch-video-brief.md",
    "docs/launch-video-assets.md",
    "docs/contact-and-social.md",
    "docs/assets/launch-video/github-repository-home.png",
    "docs/assets/launch-video/readme-system-map.png",
    "docs/assets/launch-video/github-actions-verify-success.png",
    "docs/assets/launch-video/public-core-private-overlays.png",
    "docs/assets/launch-video/title-card-16x9.png",
    "docs/assets/launch-video/title-card-9x16.png",
    "docs/assets/launch-video/project-card-square.png",
    "docs/owner-launch-decision.md",
    "docs/post-public-launch-verification-2026-06-26.md",
    "docs/pre-public-safety-audit.md",
    "docs/pre-public-readiness-2026-06-26.md",
    "docs/public-launch-gates.md",
    "docs/roadmap.md",
    "docs/closeout-audit-2026-06-26.md",
]

PRIVATE_ONLY_TERMS = [
    "token value",
    "oauth secret",
    "cookie value",
    "private key",
]


def fail(message: str) -> None:
    raise SystemExit(f"verify failed: {message}")


def require_file(path: str) -> None:
    candidate = ROOT / path
    if not candidate.is_file():
        fail(f"missing required file: {path}")


def verify_required_files() -> None:
    for path in REQUIRED_FILES:
        require_file(path)


def verify_repository_map() -> None:
    data = json.loads((ROOT / "data" / "repositories.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("repositories.json schema_version must be 1")
    names = set()
    for repo in data.get("repositories", []):
        for key in ("name", "role", "visibility_stage", "public_safe", "owns"):
            if key not in repo:
                fail(f"repository entry missing {key}")
        if repo["name"] in names:
            fail(f"duplicate repository name: {repo['name']}")
        names.add(repo["name"])
    required = {
        "open-resource-governance",
        "resource-radar",
        "agent-skills-curated",
        "codex-user-config-template",
        "research-bookmarks-public",
    }
    missing = required - names
    if missing:
        fail(f"repository map missing: {', '.join(sorted(missing))}")


def verify_language_links() -> None:
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    if "English | [简体中文](README.zh-CN.md)" not in english:
        fail("README.md language switch is missing or inconsistent")
    if "[English](README.md) | 简体中文" not in chinese:
        fail("README.zh-CN.md language switch is missing or inconsistent")


def verify_no_obvious_private_payloads() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == "scripts/verify.py":
            continue
        if path.suffix.lower() in {".jsonl", ".sqlite", ".db", ".pem", ".key"}:
            fail(f"private/runtime-like file type is not allowed: {rel}")
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in PRIVATE_ONLY_TERMS:
            if term in text:
                fail(f"private-only term found in {rel}: {term}")


def main() -> None:
    verify_required_files()
    verify_repository_map()
    verify_language_links()
    verify_no_obvious_private_payloads()
    print("open-resource-governance verification passed")


if __name__ == "__main__":
    main()
