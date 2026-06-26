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
    ".github/ISSUE_TEMPLATE/name-suggestion.yml",
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    "data/repositories.json",
    "docs/license-policy.md",
    "docs/project-design.md",
    "docs/public-project-positioning-benchmark.md",
    "docs/community-feedback-model.md",
    "docs/public-private-boundary.md",
    "docs/system-topology.md",
    "docs/repository-map.md",
    "docs/promotion-kit.md",
    "docs/free-promotion-playbook.md",
    "docs/launch-video-brief.md",
    "docs/launch-video-assets.md",
    "docs/naming-campaign.md",
    "docs/bookmark-lane-closeout-2026-06-26.md",
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
    "data/topology.json",
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
        "resource-radar-public",
        "agent-skills-curated",
        "codex-user-config-template",
        "codex-user-config",
        "claude-user-config-template",
        "claude-user-config",
        "research-bookmarks-public",
        "research-bookmarks",
    }
    missing = required - names
    if missing:
        fail(f"repository map missing: {', '.join(sorted(missing))}")


def verify_topology() -> None:
    data = json.loads((ROOT / "data" / "topology.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("topology.json schema_version must be 1")
    repo_data = json.loads((ROOT / "data" / "repositories.json").read_text(encoding="utf-8"))
    repo_names = {repo["name"] for repo in repo_data.get("repositories", [])}
    node_ids = {node.get("id") for node in data.get("nodes", [])}
    if not repo_names <= node_ids:
        fail(f"topology missing nodes: {', '.join(sorted(repo_names - node_ids))}")
    for edge in data.get("edges", []):
        if edge.get("from") not in node_ids or edge.get("to") not in node_ids:
            fail(f"topology edge references unknown node: {edge}")
        if "write_permission" not in edge:
            fail(f"topology edge missing write_permission: {edge}")
    principles = "\n".join(data.get("principles", []))
    if "All non-user-configuration lanes should remain agent-neutral" not in principles:
        fail("topology must state non-user-configuration neutrality")


def verify_language_links() -> None:
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    if "English | [简体中文](README.zh-CN.md)" not in english:
        fail("README.md language switch is missing or inconsistent")
    if "[English](README.md) | 简体中文" not in chinese:
        fail("README.zh-CN.md language switch is missing or inconsistent")


def verify_external_user_readme() -> None:
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    required_english = [
        "temporary project name",
        "docs/assets/launch-video/title-card-16x9.png",
        "What problem does this solve?",
        "Proof, not just plans",
        "What can you use today?",
        "What value can you reproduce?",
        "Example user journeys",
        "Sustainability",
        "research-bookmarks-public",
        "resource-radar-public",
        "codex-user-config-template",
        "claude-user-config-template",
        "389 private bookmark entries",
        "328 public-safe sources",
    ]
    required_chinese = [
        "临时项目名",
        "docs/assets/launch-video/title-card-16x9.png",
        "它解决什么问题？",
        "不是只画饼，已有跑通证据",
        "现在能用什么？",
        "你能复刻什么价值？",
        "示例用户路径",
        "可持续性",
        "research-bookmarks-public",
        "resource-radar-public",
        "codex-user-config-template",
        "claude-user-config-template",
        "389 条私有书签记录",
        "328 条公开安全来源",
    ]
    for phrase in required_english:
        if phrase not in english:
            fail(f"README.md missing external-user phrase: {phrase}")
    for phrase in required_chinese:
        if phrase not in chinese:
            fail(f"README.zh-CN.md missing external-user phrase: {phrase}")


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
    verify_topology()
    verify_language_links()
    verify_external_user_readme()
    verify_no_obvious_private_payloads()
    print("open-resource-governance verification passed")


if __name__ == "__main__":
    main()
