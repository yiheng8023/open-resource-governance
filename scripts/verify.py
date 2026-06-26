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
    "docs/support-and-sponsorship.md",
    "docs/funding-options-matrix.md",
    "docs/future-lane-incubation.md",
    "docs/private-project-consumption-model.md",
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
    "data/future-lanes.json",
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
    if "graph of lanes" not in principles:
        fail("topology must state graph-not-linear relationship model")
    if "terminal reviewed consumer for executable Skill artifacts" not in principles:
        fail("topology must state curated Skills terminal-consumer boundary")


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
        "support-and-sponsorship",
        "funding-options-matrix",
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
        "support-and-sponsorship",
        "funding-options-matrix",
        "389 条私有书签记录",
        "328 条公开安全来源",
    ]
    for phrase in required_english:
        if phrase not in english:
            fail(f"README.md missing external-user phrase: {phrase}")
    for phrase in required_chinese:
        if phrase not in chinese:
            fail(f"README.zh-CN.md missing external-user phrase: {phrase}")


def verify_current_public_private_status() -> None:
    roadmap = (ROOT / "docs" / "roadmap.md").read_text(encoding="utf-8")
    project_design = (ROOT / "docs" / "project-design.md").read_text(encoding="utf-8")
    required_roadmap_phrases = [
        "resource-radar` is private",
        "resource-radar-public` is public",
        "codex-user-config` and `claude-user-config` are private",
        "codex-user-config-template` and `claude-user-config-template` are public",
        "does not make the paired private source",
    ]
    for phrase in required_roadmap_phrases:
        if phrase not in roadmap:
            fail(f"roadmap missing current public/private status phrase: {phrase}")
    required_design_phrases = [
        "not a simple upstream/downstream hierarchy",
        "public radar template",
        "public configuration-template family",
        "not yet a complete packaged product",
    ]
    for phrase in required_design_phrases:
        if phrase not in project_design:
            fail(f"project design missing relationship/maturity phrase: {phrase}")


def verify_future_lane_incubation() -> None:
    data = json.loads((ROOT / "data" / "future-lanes.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("future-lanes.json schema_version must be 1")
    if data.get("status") != "candidate_only":
        fail("future lanes must remain candidate_only")
    lanes = data.get("lanes", [])
    required_ids = {
        "project-standards",
        "knowledge-graph",
        "benchmark-evaluation",
        "documentation-system",
        "software-architecture-playbooks",
        "domain-specific-resource-packs",
        "private-project-absorption-queue",
        "community-curated-catalogs",
    }
    ids = {lane.get("id") for lane in lanes}
    missing = required_ids - ids
    if missing:
        fail(f"future lanes missing ids: {', '.join(sorted(missing))}")
    for lane in lanes:
        if lane.get("stage") != "candidate":
            fail(f"future lane must stay candidate: {lane.get('id')}")
        if lane.get("implementation_status") != "not_implemented":
            fail(f"future lane must not claim implementation: {lane.get('id')}")
    public_docs = "\n".join(
        (ROOT / path).read_text(encoding="utf-8")
        for path in [
            "docs/future-lane-incubation.md",
            "docs/private-project-consumption-model.md",
            "docs/project-design.md",
            "docs/system-topology.md",
        ]
    )
    required_phrases = [
        "candidate",
        "curated Skills lane",
        "private/core projects",
        "directly mutate",
        "Human review is required",
        "not implemented topology nodes",
    ]
    for phrase in required_phrases:
        if phrase not in public_docs:
            fail(f"future/private project docs missing phrase: {phrase}")
    forbidden_private_project_terms = ["YIYUAN", "ASSETS"]
    combined = public_docs + json.dumps(data, ensure_ascii=False)
    for term in forbidden_private_project_terms:
        if term.lower() in combined.lower():
            fail(f"private project identifier leaked into public lane docs: {term}")


def verify_support_entry() -> None:
    funding = (ROOT / ".github" / "FUNDING.yml").read_text(encoding="utf-8")
    support = (ROOT / "docs" / "support-and-sponsorship.md").read_text(encoding="utf-8")
    matrix = (ROOT / "docs" / "funding-options-matrix.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/support-and-sponsorship.md" not in funding:
        fail("FUNDING.yml must point to the support and sponsorship page")
    required_support_phrases = [
        "formal payment channels",
        "not claimed as active",
        "does not buy approval",
        "Future funding activation gate",
    ]
    for phrase in required_support_phrases:
        if phrase not in support:
            fail(f"support page missing required phrase: {phrase}")
    required_matrix_phrases = [
        "GitHub Sponsors + fiscal host",
        "Open Collective / fiscal host",
        "Ko-fi",
        "Buy Me a Coffee",
        "Afdian",
        "Alipay / WeChat",
        "No-pay-to-approve policy",
        "payout path",
    ]
    for phrase in required_matrix_phrases:
        if phrase not in matrix:
            fail(f"funding matrix missing required phrase: {phrase}")
    if "docs/support-and-sponsorship.md" not in readme:
        fail("README.md must link the support and sponsorship page")
    if "docs/funding-options-matrix.md" not in readme:
        fail("README.md must link the funding options matrix")


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
    verify_current_public_private_status()
    verify_future_lane_incubation()
    verify_support_entry()
    verify_no_obvious_private_payloads()
    print("open-resource-governance verification passed")


if __name__ == "__main__":
    main()
