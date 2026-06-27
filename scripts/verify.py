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
    "scripts/verify_local_evidence_freshness.py",
    "data/repositories.json",
    "docs/license-policy.md",
    "docs/project-design.md",
    "docs/user-developer-compact.md",
    "docs/public-project-positioning-benchmark.md",
    "docs/community-feedback-model.md",
    "docs/public-private-boundary.md",
    "docs/shared-governance-baseline.md",
    "docs/mvp-plan-and-acceptance.md",
    "docs/mvp-global-closeout-verification.md",
    "docs/mvp-closeout-evidence-ledger.md",
    "docs/mvp-current-decision-point.md",
    "docs/mvp03-release-routing-closeout-2026-06-27.md",
    "docs/mvp-artifact-hygiene-review.md",
    "docs/mvp-continuous-assurance-review.md",
    "docs/mvp-persistence-continuity-review.md",
    "docs/mvp-observability-explainability-review.md",
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
    "data/shared-governance-baseline.json",
    "data/mvp-acceptance-map.json",
    "data/mvp-closeout-evidence-ledger.json",
    "data/mvp-current-decision-point.json",
    "data/mvp03-release-routing-closeout.json",
    "data/mvp-artifact-hygiene-review.json",
    "data/mvp-continuous-assurance-review.json",
    "data/mvp-persistence-continuity-review.json",
    "data/mvp-observability-explainability-review.json",
]

PRIVATE_ONLY_TERMS = [
    "token value",
    "oauth secret",
    "cookie value",
    "private key",
]

STALE_STAGE_PHRASES = [
    "MVP-02 through MVP-06",
    "MVP-02 still has an approval gate",
    "MVP-02 approval request is not approval",
    "approve adapted Skill for curated release",
    "mvp03_candidate_review_recorded_later_release_gates_pending",
    "no payload, manifest, routing projection, or live install has been approved",
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
    node_map = {node.get("id"): node for node in data.get("nodes", [])}
    mvp_gate = node_map.get("mvp-current-decision-point")
    if not mvp_gate:
        fail("topology must include the current MVP decision point gate")
    if mvp_gate.get("kind") != "governance_gate":
        fail("MVP decision point must be modeled as a governance_gate")
    if mvp_gate.get("state") != "selected_mvp_closed_pause_observe":
        fail("MVP decision point topology node has stale state")
    if mvp_gate.get("not_release_authority") is not True:
        fail("MVP decision point topology node must not be release authority")
    edge_keys = {
        (edge.get("from"), edge.get("to"), edge.get("relation"))
        for edge in data.get("edges", [])
    }
    required_edges = {
        ("open-resource-governance", "mvp-current-decision-point", "indexes-current-mvp-gate"),
        ("mvp-current-decision-point", "agent-skills-curated", "indexes-release-routing-install-proof"),
        ("mvp-current-decision-point", "codex-user-config", "indexes-private-runtime-install-proof"),
    }
    missing_edges = required_edges - edge_keys
    if missing_edges:
        fail(f"topology missing MVP gate edges: {sorted(missing_edges)}")
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
    system_topology = (ROOT / "docs" / "system-topology.md").read_text(encoding="utf-8")
    repository_map = (ROOT / "docs" / "repository-map.md").read_text(encoding="utf-8")
    for phrase in [
        "current MVP gate node",
        "not release authority",
        "selected MVP closed: pause/observe",
        "indexes release/routing/install proof",
        "indexes private runtime install proof",
    ]:
        if phrase not in system_topology:
            fail(f"system topology missing MVP gate phrase: {phrase}")
    for phrase in [
        "Current MVP gate",
        "governance gate rather than a repository",
        "not release authority",
        "not authority to approve unrelated manifests",
        "not authority to add unrelated generated routing",
        "not permission for unrelated private runtime installation",
    ]:
        if phrase not in repository_map:
            fail(f"repository map missing MVP gate phrase: {phrase}")


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
        "Where are the outputs?",
        "Cloud-first automation and renewal",
        "System map at a glance",
        "public repository should explain itself",
        "docs/system-topology.md",
        "System context",
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
        "GitHub-native and cloud-first",
        "local checkout is optional",
        "controlled metabolism",
        "renew, retire, merge, or reject",
        "resource-radar-public/outputs/demo-report.md",
        "research-bookmarks-public/data/projection-report.json",
    ]
    required_chinese = [
        "临时项目名",
        "docs/assets/launch-video/title-card-16x9.png",
        "它解决什么问题？",
        "不是只画饼，已有跑通证据",
        "产出在哪里？",
        "云端优先自动化与新陈代谢",
        "全局关系速览",
        "每个公开子仓都应该能",
        "docs/system-topology.md",
        "系统位置",
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
        "GitHub 原生、云端优先",
        "普通用户消费公开产物不依赖本地环境",
        "受控新陈代谢",
        "更新、合并、退役或拒绝",
        "resource-radar-public/outputs/demo-report.md",
        "research-bookmarks-public/data/projection-report.json",
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
        "Current MVP gate",
        "MVP-01 source candidate selection has passed",
        "MVP-02 review, neutralization, and non-runtime adapted draft creation has",
        "MVP-03 release/routing follow-up execution has passed",
        "Private consumer install and routing verification have passed",
        "spec-driven-development` is represented as a recipe/routing projection",
        "release-manifest.json` remains schema 1 with 19 curated Skills and 41 files",
        "does not approve new source discovery",
    ]
    for phrase in required_roadmap_phrases:
        if phrase not in roadmap:
            fail(f"roadmap missing current public/private status phrase: {phrase}")
    required_design_phrases = [
        "not a simple upstream/downstream hierarchy",
        "Output and automation model",
        "GitHub Actions validation",
        "local checkout is useful for contributors",
        "Metabolism and self-iteration",
        "detect drift, duplication, decay, or better alternatives",
        "Public expression consistency",
        "where the public outputs live",
        "Promotion should point to evidence-backed outputs",
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


def verify_shared_governance_baseline() -> None:
    data = json.loads((ROOT / "data" / "shared-governance-baseline.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("shared-governance-baseline.json schema_version must be 1")
    if data.get("status") != "active_baseline":
        fail("shared governance baseline must be active_baseline")
    required_principles = [
        "shared baseline, lane-specific implementation",
        "public-safe by default",
        "private overlays stay private",
        "automation prepares and verifies; human gates decide high-impact promotion",
        "funding does not buy approval",
        "process artifacts must not become hidden authority",
        "retained artifacts require ongoing quality, health, security, and compliance posture",
        "maintained lanes need durable state, continuity anchors, and recovery paths",
        "important decisions should be observable and explainable through public-safe evidence",
    ]
    principles = data.get("principles", [])
    for phrase in required_principles:
        if phrase not in principles:
            fail(f"shared governance baseline missing principle: {phrase}")
    required_loop = [
        "discover_or_import",
        "normalize",
        "classify",
        "generate",
        "verify",
        "review_gate",
        "publish_or_keep_private",
        "lifecycle_check",
        "update_or_retire",
    ]
    if data.get("automation_loop") != required_loop:
        fail("shared governance automation loop changed unexpectedly")
    if data.get("lifecycle_posture") != [
        "artifact_hygiene",
        "continuous_assurance",
        "persistence_and_continuity",
        "observability_and_explainability",
    ]:
        fail("shared governance lifecycle posture changed unexpectedly")
    lane_examples = data.get("lane_specific_examples", {})
    for lane in ["bookmarks", "resource_radar", "curated_skills", "user_configuration", "future_lanes"]:
        if lane not in lane_examples:
            fail(f"shared governance baseline missing lane examples: {lane}")
    doc = (ROOT / "docs" / "shared-governance-baseline.md").read_text(encoding="utf-8")
    required_doc_phrases = [
        "Consistency does not mean sameness",
        "Shared automation loop",
        "Review gates",
        "Lifecycle posture",
        "artifact hygiene",
        "continuous assurance",
        "persistence and continuity",
        "observability and explainability",
        "Skills MVP",
        "standardize the rules",
    ]
    for phrase in required_doc_phrases:
        if phrase not in doc:
            fail(f"shared governance doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/shared-governance-baseline.md" not in readme:
        fail("README.md must link shared governance baseline")


def verify_mvp_acceptance_map() -> None:
    data = json.loads((ROOT / "data" / "mvp-acceptance-map.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("mvp-acceptance-map.json schema_version must be 1")
    if data.get("status") != "selected_mvp_closed_pause_observe":
        fail("MVP plan should record the selected MVP closeout state")
    if data.get("mvp_name") != "curated-skills-terminal-consumer-mvp":
        fail("unexpected MVP name")
    if data.get("known_baselines") != [
        "the private user-configuration to agent-skills-curated base logic chain has already been verified",
        "the MVP verifies iterative governance over the working chain, not basic connectivity from zero",
    ]:
        fail("MVP known baselines must preserve verified chain posture")
    workstreams = data.get("workstreams", [])
    if len(workstreams) != 7:
        fail("MVP must define seven workstreams")
    required_workstream_ids = {f"mvp-0{index}" for index in range(1, 8)}
    actual_ids = {item.get("id")[:6] for item in workstreams}
    if actual_ids != required_workstream_ids:
        fail("MVP workstream IDs must be mvp-01 through mvp-07")
    for item in workstreams:
        if not item.get("acceptance"):
            fail(f"MVP workstream missing acceptance criteria: {item.get('id')}")
        if not item.get("human_gate"):
            fail(f"MVP workstream missing human gate: {item.get('id')}")
    mvp_07 = next((item for item in workstreams if item.get("id") == "mvp-07-global-closeout"), None)
    mvp_07_acceptance = " ".join(mvp_07.get("acceptance", [])) if mvp_07 else ""
    if "owner-approved drafts after selected-MVP closeout" not in mvp_07_acceptance:
        fail("MVP-07 acceptance must reflect post-closeout promotion material status")
    if "publication remains owner-gated and claim-gated" not in mvp_07_acceptance:
        fail("MVP-07 acceptance must keep publication owner-gated and claim-gated")
    gates = data.get("closeout_gates", [])
    if len(gates) != 11:
        fail("MVP must define eleven closeout gates")
    gate_map = {gate.get("id"): gate for gate in gates}
    gate_02_workstreams = set(gate_map.get("gate-02-boundaries-held", {}).get("mapped_workstreams", []))
    for required_workstream in [
        "mvp-01-source-candidate",
        "mvp-02-review-adapt",
        "mvp-03-release-manifest",
        "mvp-04-consumer-install",
        "mvp-06-feedback-retirement",
    ]:
        if required_workstream not in gate_02_workstreams:
            fail(f"Gate 02 must map boundary evidence from {required_workstream}")
    doc = (ROOT / "docs" / "mvp-plan-and-acceptance.md").read_text(encoding="utf-8")
    required_doc_phrases = [
        "curated Skills lane",
        "base logic chain",
        "has already been verified",
        "does not restart",
        "Non-goals",
        "Acceptance criteria",
        "Closeout gates",
        "Stage exit",
        "small batch",
        "Global closeout",
        "Current stage note",
        "MVP-03 release/manifest execution",
        "lifecycle feedback",
        "mvp-current-decision-point.md",
        "roadmap.md",
        "Evidence from MVP-01, MVP-02, MVP-03, MVP-04, MVP-06",
        "artifact hygiene",
        "continuous assurance",
        "persistence and continuity",
        "observability and explainability",
    ]
    for phrase in required_doc_phrases:
        if phrase not in doc:
            fail(f"MVP plan doc missing phrase: {phrase}")
    if "docs/mvp-plan-and-acceptance.md" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        fail("README.md must link MVP plan")
    closeout_doc = (ROOT / "docs" / "mvp-global-closeout-verification.md").read_text(encoding="utf-8")
    required_closeout_phrases = [
        "cross-repository verification",
        "Promotion is downstream of proof",
        "video",
        "topology",
        "README",
        "Evidence rule",
        "Process artifact hygiene",
        "Continuous assurance rule",
        "Persistence and continuity rule",
        "Observability and explainability rule",
    ]
    for phrase in required_closeout_phrases:
        if phrase not in closeout_doc:
            fail(f"MVP global closeout doc missing phrase: {phrase}")
    if "docs/mvp-global-closeout-verification.md" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        fail("README.md must link MVP global closeout verification")


def verify_user_developer_compact() -> None:
    compact = (ROOT / "docs" / "user-developer-compact.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    required_compact_phrases = [
        "User sovereignty",
        "Output access",
        "without asking the maintainer",
        "reconstructing the private environment",
        "Ordinary users should not need a local development environment",
        "Developers and contributors should have enough information",
        "Participation value",
        "Metabolism and renewal",
        "observe -> detect drift -> update lifecycle state -> regenerate -> verify -> review -> publish or defer",
        "Human gates still decide high-impact acceptance",
        "Communication and promotion rights",
        "what public outputs exist",
        "what is generated and verified by automation",
        "宣传不是只讲愿景",
        "Private overlays remain optional and owner-controlled",
        "No automation should install, publish, pay, connect accounts, change visibility, or mutate private state without explicit authorization",
        "Funding, sponsorship, and promotion should not buy approval",
        "The selected-MVP closeout proves one terminal-consumer loop",
        "用户始终拥有自己的私有配置",
        "公开产出应能直接在 GitHub 上找到",
        "普通用户查看公开结果不应依赖本地环境",
        "任何安装、发布、付款、账号连接、可见性变更或私有状态变更，都需要明确授权",
        "共建的价值不是把私人材料倒进公开仓库",
        "项目应具备受控新陈代谢能力",
    ]
    for phrase in required_compact_phrases:
        if phrase not in compact:
            fail(f"user/developer compact missing phrase: {phrase}")
    for name, text in {
        "README.md": readme,
        "README.zh-CN.md": readme_zh,
        "CONTRIBUTING.md": contributing,
    }.items():
        if "docs/user-developer-compact.md" not in text:
            fail(f"{name} must link user/developer compact")


def verify_mvp_closeout_evidence_ledger() -> None:
    acceptance = json.loads((ROOT / "data" / "mvp-acceptance-map.json").read_text(encoding="utf-8"))
    ledger = json.loads((ROOT / "data" / "mvp-closeout-evidence-ledger.json").read_text(encoding="utf-8"))
    if ledger.get("schema_version") != 1:
        fail("mvp-closeout-evidence-ledger.json schema_version must be 1")
    if ledger.get("mvp_name") != acceptance.get("mvp_name"):
        fail("MVP closeout ledger must reference the active MVP")
    if ledger.get("status") != "selected_mvp_closed_pause_observe":
        fail("MVP closeout ledger should record selected MVP closeout")
    if ledger.get("not_completion_claim") is not True:
        fail("MVP closeout ledger must explicitly avoid completion claims")
    surfaces = ledger.get("verified_surfaces", [])
    if len(surfaces) < 8:
        fail("MVP closeout ledger must record enough verified surfaces")
    for surface in surfaces:
        for key in ("repository", "visibility", "head", "local_verification", "remote_ci"):
            if key not in surface:
                fail(f"MVP closeout ledger surface missing {key}: {surface}")
    expected_workstreams = {item["id"] for item in acceptance.get("workstreams", [])}
    actual_workstreams = {item.get("id") for item in ledger.get("workstream_status", [])}
    if actual_workstreams != expected_workstreams:
        fail("MVP closeout ledger workstreams must match acceptance map")
    expected_gates = {item["id"] for item in acceptance.get("closeout_gates", [])}
    actual_gates = {item.get("id") for item in ledger.get("closeout_gate_status", [])}
    if actual_gates != expected_gates:
        fail("MVP closeout ledger gates must match acceptance map")
    allowed_statuses = {"pending", "partial", "baseline_ready", "in_progress", "passed"}
    for section_name in ("workstream_status", "closeout_gate_status"):
        for item in ledger.get(section_name, []):
            if item.get("status") not in allowed_statuses:
                fail(f"MVP closeout ledger has unexpected status in {section_name}: {item}")
            if not item.get("evidence"):
                fail(f"MVP closeout ledger item missing evidence: {item}")
    stale_next_evidence_phrases = [
        "Later workstreams still need release",
        "Later lifecycle and global closeout evidence are still needed",
        "before final closeout",
    ]
    for item in ledger.get("workstream_status", []):
        next_evidence = item.get("next_required_evidence", "")
        for phrase in stale_next_evidence_phrases:
            if phrase in next_evidence:
                fail(f"MVP ledger contains stale next-required evidence for {item.get('id')}: {phrase}")
    workstream_status = {item.get("id"): item.get("status") for item in ledger.get("workstream_status", [])}
    expected_stage_status = {
        "mvp-01-source-candidate": "passed",
        "mvp-02-review-adapt": "passed",
        "mvp-03-release-manifest": "passed",
        "mvp-04-consumer-install": "passed",
        "mvp-05-routing-runtime": "passed",
        "mvp-06-feedback-retirement": "passed",
        "mvp-07-global-closeout": "passed",
    }
    for workstream_id, expected_status in expected_stage_status.items():
        if workstream_status.get(workstream_id) != expected_status:
            fail(f"MVP closeout ledger has stale stage status for {workstream_id}")
    if not ledger.get("next_actions"):
        fail("MVP closeout ledger must record next actions")
    doc = (ROOT / "docs" / "mvp-closeout-evidence-ledger.md").read_text(encoding="utf-8")
    for phrase in [
        "not a universal completion claim",
        "selected_mvp_closed_pause_observe",
        "Verified surfaces",
        "Workstream status",
        "Gate status",
        "Next gated work",
        "pause and observe",
        "Owner-local evidence freshness check",
        "verify_local_evidence_freshness.py",
    ]:
        if phrase not in doc:
            fail(f"MVP closeout evidence ledger doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/mvp-closeout-evidence-ledger.md" not in readme:
        fail("README.md must link MVP closeout evidence ledger")
    for phrase in [
        "Current MVP status",
        "MVP-01 source candidate selection: passed",
        "MVP-02 review, neutralization, and non-runtime adapted draft creation: passed",
        "MVP-03 release/routing follow-up execution: passed",
        "Private consumer install and routing verification: passed",
        "MVP-06 lifecycle feedback and radar dedupe metadata: passed",
        "MVP-07 selected-MVP global closeout: passed",
    ]:
        if phrase not in readme:
            fail(f"README.md missing current MVP status phrase: {phrase}")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    for phrase in [
        "当前 MVP 状态",
        "MVP-01 来源候选选择：已通过",
        "MVP-02 审查、中立化和非运行时适配草案创建：已通过",
        "MVP-03 release/routing 后续执行",
        "私有消费者安装与路由验证",
        "MVP-06 生命周期反馈与资源雷达去重元数据",
        "MVP-07 selected-MVP 全局收官",
    ]:
        if phrase not in readme_zh:
            fail(f"README.zh-CN.md missing current MVP status phrase: {phrase}")
    closeout_doc = (ROOT / "docs" / "mvp-global-closeout-verification.md").read_text(encoding="utf-8")
    if "mvp-closeout-evidence-ledger.md" not in closeout_doc:
        fail("global closeout doc must link MVP closeout evidence ledger")
    if "verify_local_evidence_freshness.py" not in closeout_doc:
        fail("global closeout doc must mention owner-local evidence freshness check")


def verify_mvp_current_decision_point() -> None:
    decision = json.loads((ROOT / "data" / "mvp-current-decision-point.json").read_text(encoding="utf-8"))
    ledger = json.loads((ROOT / "data" / "mvp-closeout-evidence-ledger.json").read_text(encoding="utf-8"))
    if decision.get("schema_version") != 1:
        fail("mvp-current-decision-point.json schema_version must be 1")
    if decision.get("mvp_name") != ledger.get("mvp_name"):
        fail("MVP current decision point must reference the active MVP")
    if decision.get("status") != "selected_mvp_closed_pause_observe":
        fail("MVP current decision point must record selected MVP closeout state")
    if decision.get("not_completion_claim") is not True:
        fail("MVP current decision point must explicitly avoid completion claims")
    if decision.get("not_public_launch_approval") is not True:
        fail("MVP current decision point must explicitly avoid public launch approval")
    if decision.get("current_workstream") != "mvp-07-global-closeout":
        fail("MVP current decision point must point to selected MVP closeout")
    if decision.get("source_repository") != "agent-skills-curated":
        fail("MVP current decision point must source the Skills lane")
    skills_surface = next(
        (surface for surface in ledger.get("verified_surfaces", []) if surface.get("repository") == "agent-skills-curated"),
        None,
    )
    if not skills_surface:
        fail("MVP ledger missing agent-skills-curated surface")
    if decision.get("source_head") != skills_surface.get("head"):
        fail("MVP current decision point source_head must match ledger Skills head")
    config_surface = next(
        (surface for surface in ledger.get("verified_surfaces", []) if surface.get("repository") == "codex-user-config"),
        None,
    )
    if not config_surface:
        fail("MVP ledger missing codex-user-config surface")
    if decision.get("consumer_head") != config_surface.get("head"):
        fail("MVP current decision point consumer_head must match ledger config head")
    expected_candidates = [
        "spec-driven-development",
        "documentation-and-adrs",
        "code-review-and-quality",
    ]
    if decision.get("candidate_ids") != expected_candidates:
        fail("MVP current decision point candidate_ids changed")
    expected_phrases = [
        "批准进入 MVP-03 release/routing 候选审查阶段",
        "Approve MVP-03 release-or-routing candidate review only",
        "routing projection proposal、merge proposal、approved payload diff、manifest change 或 runtime install proof全部批准。",
    ]
    if decision.get("safe_approval_phrases") != expected_phrases:
        fail("MVP current decision point safe approval phrases changed")
    if decision.get("last_approval_event_recorded") != "mvp03-followup-owner-approval-2026-06-27-release-routing-manifest-install-proof":
        fail("MVP current decision point must record the consumed MVP-03 follow-up approval event")
    expected_permissions = {
        "candidate_review_recorded": True,
        "approved_payload_executed_for_selected_batch": True,
        "release_manifest_executed_for_selected_batch": True,
        "routing_projection_executed_for_selected_batch": True,
        "live_install_executed_for_selected_batch": True,
        "source_text_redistribution_allowed": False,
    }
    if decision.get("current_permissions") != expected_permissions:
        fail("MVP current decision point permission/proof state mismatch")
    required_disallowed = {
        "pull or import new sources without a new intake gate",
        "vendor official/runtime-owned Skill text",
        "approve unrelated candidate payload",
        "publish broad launch or promotion claims",
        "update unrelated release-manifest entries",
        "install unrelated live Agent runtime changes",
        "redistribute upstream source text beyond reviewed adapted payload",
    }
    if set(decision.get("still_disallowed", [])) != required_disallowed:
        fail("MVP current decision point still_disallowed changed")
    required_reasons = {
        "MVP-03 follow-up approval has been consumed for this small batch only",
        "the selected changes are approved release/routing/install evidence, not open-ended source approval",
        "public promotion and next-lane graduation remain separate human authorization boundaries",
        "selected small-batch MVP closeout is complete, but future batches and public promotion remain separate gates",
    }
    if set(decision.get("why_this_matters", [])) != required_reasons:
        fail("MVP current decision point why_this_matters changed")
    doc = (ROOT / "docs" / "mvp-current-decision-point.md").read_text(encoding="utf-8")
    for phrase in [
        "not a universal completion claim and not public launch approval",
        "MVP-03 follow-up approval has been consumed",
        "pause_and_observe_before_next_gated_batch",
        "Approve MVP-03 release-or-routing candidate review only",
        "批准进入 MVP-03 release/routing 候选审查阶段",
        "routing projection proposal、merge proposal、approved payload diff、manifest change 或 runtime install proof全部批准。",
    ]:
        if phrase not in doc:
            fail(f"MVP current decision point doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    if "docs/mvp-current-decision-point.md" not in readme:
        fail("README.md must link MVP current decision point")
    if "docs/mvp-current-decision-point.md" not in readme_zh:
        fail("README.zh-CN.md must link MVP current decision point")
    closeout_doc = (ROOT / "docs" / "mvp-global-closeout-verification.md").read_text(encoding="utf-8")
    if "mvp-current-decision-point.md" not in closeout_doc:
        fail("global closeout doc must link MVP current decision point")
    ledger_doc = (ROOT / "docs" / "mvp-closeout-evidence-ledger.md").read_text(encoding="utf-8")
    if "mvp-current-decision-point.md" not in ledger_doc:
        fail("MVP ledger doc must link MVP current decision point")


def verify_mvp03_release_routing_closeout() -> None:
    data = json.loads((ROOT / "data" / "mvp03-release-routing-closeout.json").read_text(encoding="utf-8"))
    ledger = json.loads((ROOT / "data" / "mvp-closeout-evidence-ledger.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("mvp03-release-routing-closeout.json schema_version must be 1")
    if data.get("mvp_name") != ledger.get("mvp_name"):
        fail("MVP-03 closeout record must reference the active MVP")
    if data.get("status") != "release_routing_manifest_install_proof_recorded":
        fail("MVP-03 closeout record has stale status")
    if data.get("not_completion_claim") is not True:
        fail("MVP-03 closeout record must avoid completion claims")
    if data.get("not_public_launch_approval") is not True:
        fail("MVP-03 closeout record must avoid public launch approval")
    skills_surface = next(
        (surface for surface in ledger.get("verified_surfaces", []) if surface.get("repository") == "agent-skills-curated"),
        None,
    )
    config_surface = next(
        (surface for surface in ledger.get("verified_surfaces", []) if surface.get("repository") == "codex-user-config"),
        None,
    )
    if not skills_surface or not config_surface:
        fail("MVP-03 closeout needs Skills and config ledger surfaces")
    if data.get("source_head") != skills_surface.get("head"):
        fail("MVP-03 closeout source_head must match ledger")
    if data.get("consumer_head") != config_surface.get("head"):
        fail("MVP-03 closeout consumer_head must match ledger")
    manifest = data.get("manifest", {})
    if manifest.get("schema_version") != 1:
        fail("MVP-03 closeout manifest schema must remain 1")
    if manifest.get("skill_count") != 19 or manifest.get("file_count") != 41:
        fail("MVP-03 closeout manifest counts changed unexpectedly")
    runtime = data.get("runtime_install_proof", {})
    plan = runtime.get("plan", {})
    if runtime.get("installed_curated_skills") != 19:
        fail("MVP-03 closeout runtime install proof must verify 19 Skills")
    if plan != {"add": 0, "unchanged": 17, "replace": 2, "retire": 0}:
        fail("MVP-03 closeout install plan counts changed")
    expected_boundaries = {
        "no memory update",
        "no Hook enablement",
        "no MCP/App/Plugin install state change",
        "no public promotion approval",
        "no new source discovery",
        "no official/runtime-owned Skill vendoring",
        "hub remains index and evidence surface, not downstream release authority",
    }
    if set(data.get("boundaries_preserved", [])) != expected_boundaries:
        fail("MVP-03 closeout boundaries changed")
    doc = (ROOT / "docs" / "mvp03-release-routing-closeout-2026-06-27.md").read_text(encoding="utf-8")
    for phrase in [
        "Owner approval consumed",
        "release-manifest.json` stayed at schema 1",
        "104 routing scenarios passed",
        "182 unit tests passed",
        "19 curated Skills",
        "Boundaries preserved",
        "lifecycle feedback",
    ]:
        if phrase not in doc:
            fail(f"MVP-03 closeout doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    if "docs/mvp03-release-routing-closeout-2026-06-27.md" not in readme:
        fail("README.md must link MVP-03 release/routing closeout")
    if "docs/mvp03-release-routing-closeout-2026-06-27.md" not in readme_zh:
        fail("README.zh-CN.md must link MVP-03 release/routing closeout")


def verify_mvp_artifact_hygiene_review() -> None:
    data = json.loads((ROOT / "data" / "mvp-artifact-hygiene-review.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("mvp-artifact-hygiene-review.json schema_version must be 1")
    if data.get("mvp_name") != "curated-skills-terminal-consumer-mvp":
        fail("artifact hygiene review must reference the active MVP")
    if data.get("status") != "passed_for_selected_mvp_closeout":
        fail("artifact hygiene review must pass for selected MVP closeout")
    if data.get("not_completion_claim") is not True:
        fail("artifact hygiene review must explicitly avoid completion claims")
    required_principles = [
        "No process artifact is authority by accident.",
        "Generated artifacts are derived projections, not hand-maintained truth.",
        "Promotion material is downstream of proof.",
        "The MVP-03 follow-up approval is batch-limited and does not authorize unrelated source, runtime, or public-promotion expansion.",
    ]
    for phrase in required_principles:
        if phrase not in data.get("principles", []):
            fail(f"artifact hygiene review missing principle: {phrase}")
    required_classes = {
        "promoted_evidence",
        "archived_context",
        "deleted_residue",
        "ignored_non_authority",
        "generated_derived",
        "private_source",
    }
    actual_classes = {item.get("id") for item in data.get("artifact_classes", [])}
    if not required_classes <= actual_classes:
        fail(f"artifact hygiene review missing classes: {', '.join(sorted(required_classes - actual_classes))}")
    repo_data = json.loads((ROOT / "data" / "repositories.json").read_text(encoding="utf-8"))
    repo_names = {repo["name"] for repo in repo_data.get("repositories", [])}
    postures = data.get("repository_posture", [])
    posture_repos = {item.get("repository") for item in postures}
    if repo_names - posture_repos:
        fail(f"artifact hygiene review missing repository posture: {', '.join(sorted(repo_names - posture_repos))}")
    for posture in postures:
        for key in (
            "repository",
            "visibility",
            "authority_surfaces",
            "promoted_evidence",
            "archived_context",
            "generated_derived",
            "deleted_residue",
            "ignored_non_authority",
            "next_review",
        ):
            if key not in posture:
                fail(f"artifact hygiene posture missing {key}: {posture}")
        if posture["repository"] not in repo_names:
            fail(f"artifact hygiene posture references unknown repository: {posture['repository']}")
    result = data.get("current_result", {})
    if result.get("gate_08_status") != "passed_for_selected_mvp_closeout":
        fail("artifact hygiene review must record Gate 08 selected-MVP pass")
    if not result.get("post_closeout_follow_up"):
        fail("artifact hygiene review must record post-closeout follow-up")
    doc = (ROOT / "docs" / "mvp-artifact-hygiene-review.md").read_text(encoding="utf-8")
    for phrase in [
        "No process artifact is authority by accident",
        "promoted evidence",
        "archived context",
        "deleted residue",
        "ignored non-authority",
        "Generated artifacts are derived",
        "MVP-03 follow-up approval is batch-limited",
        "Gate 08 passes for selected MVP closeout",
    ]:
        if phrase not in doc:
            fail(f"artifact hygiene review doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/mvp-artifact-hygiene-review.md" not in readme:
        fail("README.md must link MVP artifact hygiene review")
    closeout_doc = (ROOT / "docs" / "mvp-global-closeout-verification.md").read_text(encoding="utf-8")
    if "mvp-artifact-hygiene-review.md" not in closeout_doc:
        fail("global closeout doc must link MVP artifact hygiene review")


def verify_mvp_continuous_assurance_review() -> None:
    data = json.loads((ROOT / "data" / "mvp-continuous-assurance-review.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("mvp-continuous-assurance-review.json schema_version must be 1")
    if data.get("mvp_name") != "curated-skills-terminal-consumer-mvp":
        fail("continuous assurance review must reference the active MVP")
    if data.get("status") != "passed_for_selected_mvp_closeout":
        fail("continuous assurance review must pass for selected MVP closeout")
    if data.get("not_completion_claim") is not True:
        fail("continuous assurance review must explicitly avoid completion claims")
    required_principles = [
        "A green CI run is snapshot evidence, not a permanent certificate.",
        "Code, schemas, docs, generated artifacts, images, workflows, and governance records can all decay.",
        "Quality, health, security, compliance, freshness, reproducibility, and boundary integrity require recurring review.",
        "Funding, promotion, or repository visibility must not bypass assurance gates.",
    ]
    for phrase in required_principles:
        if phrase not in data.get("principles", []):
            fail(f"continuous assurance review missing principle: {phrase}")
    required_dimensions = {
        "quality",
        "health",
        "security",
        "compliance",
        "freshness",
        "reproducibility",
        "public_private_boundary",
        "runtime_authority",
    }
    actual_dimensions = {item.get("id") for item in data.get("assurance_dimensions", [])}
    if not required_dimensions <= actual_dimensions:
        fail(f"continuous assurance review missing dimensions: {', '.join(sorted(required_dimensions - actual_dimensions))}")
    repo_data = json.loads((ROOT / "data" / "repositories.json").read_text(encoding="utf-8"))
    repo_names = {repo["name"] for repo in repo_data.get("repositories", [])}
    assurance_items = data.get("repository_assurance", [])
    assurance_repos = {item.get("repository") for item in assurance_items}
    if repo_names - assurance_repos:
        fail(f"continuous assurance review missing repository assurance: {', '.join(sorted(repo_names - assurance_repos))}")
    for item in assurance_items:
        for key in (
            "repository",
            "visibility",
            "current_evidence",
            "required_dimensions",
            "risk_if_stale",
            "cadence_hint",
        ):
            if key not in item:
                fail(f"continuous assurance item missing {key}: {item}")
        if item["repository"] not in repo_names:
            fail(f"continuous assurance item references unknown repository: {item['repository']}")
        unknown_dimensions = set(item["required_dimensions"]) - required_dimensions
        if unknown_dimensions:
            fail(f"continuous assurance item has unknown dimensions: {item['repository']}")
    result = data.get("current_result", {})
    if result.get("gate_09_status") != "passed_for_selected_mvp_closeout":
        fail("continuous assurance review must record Gate 09 selected-MVP pass")
    if not result.get("post_closeout_follow_up"):
        fail("continuous assurance review must record post-closeout follow-up")
    doc = (ROOT / "docs" / "mvp-continuous-assurance-review.md").read_text(encoding="utf-8")
    for phrase in [
        "A green CI run is snapshot evidence",
        "Assurance dimensions",
        "quality",
        "health",
        "security",
        "compliance",
        "freshness",
        "reproducibility",
        "public/private boundary",
        "runtime authority",
        "Event-driven cadence",
        "Gate 09 passes for selected MVP closeout",
    ]:
        if phrase not in doc:
            fail(f"continuous assurance review doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/mvp-continuous-assurance-review.md" not in readme:
        fail("README.md must link MVP continuous assurance review")
    closeout_doc = (ROOT / "docs" / "mvp-global-closeout-verification.md").read_text(encoding="utf-8")
    if "mvp-continuous-assurance-review.md" not in closeout_doc:
        fail("global closeout doc must link MVP continuous assurance review")


def verify_mvp_persistence_continuity_review() -> None:
    data = json.loads((ROOT / "data" / "mvp-persistence-continuity-review.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("mvp-persistence-continuity-review.json schema_version must be 1")
    if data.get("mvp_name") != "curated-skills-terminal-consumer-mvp":
        fail("persistence continuity review must reference the active MVP")
    if data.get("status") != "passed_for_selected_mvp_closeout":
        fail("persistence continuity review must pass for selected MVP closeout")
    if data.get("not_completion_claim") is not True:
        fail("persistence continuity review must explicitly avoid completion claims")
    required_principles = [
        "Repository truth beats chat memory for continuation.",
        "A lane must be resumable after context loss, environment change, agent switch, or interrupted automation.",
        "Private overlays remain private, but public-safe recovery anchors should explain how the system resumes.",
        "No single private machine, assistant thread, or memory store should be the only way to recover the MVP state.",
    ]
    for phrase in required_principles:
        if phrase not in data.get("principles", []):
            fail(f"persistence continuity review missing principle: {phrase}")
    required_scenarios = {
        "context_loss",
        "environment_change",
        "agent_switch",
        "interrupted_work",
        "repository_split_or_projection",
        "automation_failure",
    }
    actual_scenarios = {item.get("id") for item in data.get("continuity_scenarios", [])}
    if not required_scenarios <= actual_scenarios:
        fail(f"persistence continuity review missing scenarios: {', '.join(sorted(required_scenarios - actual_scenarios))}")
    repo_data = json.loads((ROOT / "data" / "repositories.json").read_text(encoding="utf-8"))
    repo_names = {repo["name"] for repo in repo_data.get("repositories", [])}
    continuity_items = data.get("repository_continuity", [])
    continuity_repos = {item.get("repository") for item in continuity_items}
    if repo_names - continuity_repos:
        fail(f"persistence continuity review missing repository continuity: {', '.join(sorted(repo_names - continuity_repos))}")
    for item in continuity_items:
        for key in (
            "repository",
            "visibility",
            "anchors",
            "recoverable_scenarios",
            "verify_command",
            "known_gap",
        ):
            if key not in item:
                fail(f"persistence continuity item missing {key}: {item}")
        if item["repository"] not in repo_names:
            fail(f"persistence continuity item references unknown repository: {item['repository']}")
        unknown_scenarios = set(item["recoverable_scenarios"]) - required_scenarios
        if unknown_scenarios:
            fail(f"persistence continuity item has unknown scenarios: {item['repository']}")
        if not item["anchors"]:
            fail(f"persistence continuity item must list recovery anchors: {item['repository']}")
    result = data.get("current_result", {})
    if result.get("gate_10_status") != "passed_for_selected_mvp_closeout":
        fail("persistence continuity review must record Gate 10 selected-MVP pass")
    if not result.get("post_closeout_follow_up"):
        fail("persistence continuity review must record post-closeout follow-up")
    doc = (ROOT / "docs" / "mvp-persistence-continuity-review.md").read_text(encoding="utf-8")
    for phrase in [
        "Repository truth beats chat memory",
        "Continuity scenarios",
        "context loss",
        "environment change",
        "agent switch",
        "interrupted work",
        "repository split",
        "automation failure",
        "Current recovery anchors",
        "Public/private continuity boundary",
        "Gate 10 passes for selected MVP closeout",
    ]:
        if phrase not in doc:
            fail(f"persistence continuity review doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/mvp-persistence-continuity-review.md" not in readme:
        fail("README.md must link MVP persistence continuity review")
    closeout_doc = (ROOT / "docs" / "mvp-global-closeout-verification.md").read_text(encoding="utf-8")
    if "mvp-persistence-continuity-review.md" not in closeout_doc:
        fail("global closeout doc must link MVP persistence continuity review")


def verify_mvp_observability_explainability_review() -> None:
    data = json.loads((ROOT / "data" / "mvp-observability-explainability-review.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("mvp-observability-explainability-review.json schema_version must be 1")
    if data.get("mvp_name") != "curated-skills-terminal-consumer-mvp":
        fail("observability explainability review must reference the active MVP")
    if data.get("status") != "passed_for_selected_mvp_closeout":
        fail("observability explainability review must pass for selected MVP closeout")
    if data.get("not_completion_claim") is not True:
        fail("observability explainability review must explicitly avoid completion claims")
    required_principles = [
        "Important decisions should be explainable from public-safe evidence.",
        "Automation output is not self-explanatory unless it records inputs, rules, outcome, verification, and next state.",
        "Private evidence can be summarized, but private payloads must not be exposed to make a decision explainable.",
        "Observability should be proportional: lightweight for routine checks and structured for trust-boundary decisions.",
    ]
    for phrase in required_principles:
        if phrase not in data.get("principles", []):
            fail(f"observability explainability review missing principle: {phrase}")
    required_contract = {
        "what_changed",
        "input_evidence",
        "rule_or_gate_applied",
        "decision_owner_or_trigger",
        "chosen_outcome",
        "rejected_or_deferred_alternatives",
        "verification_result",
        "next_state",
        "public_private_boundary",
    }
    actual_contract = set(data.get("explanation_contract", []))
    if not required_contract <= actual_contract:
        fail(f"observability explainability review missing contract fields: {', '.join(sorted(required_contract - actual_contract))}")
    required_events = {
        "source_selection",
        "candidate_review",
        "release_manifest",
        "install_or_rollback",
        "runtime_routing",
        "feedback_lifecycle",
        "artifact_cleanup",
        "public_refresh",
    }
    actual_events = {item.get("id") for item in data.get("decision_events", [])}
    if not required_events <= actual_events:
        fail(f"observability explainability review missing events: {', '.join(sorted(required_events - actual_events))}")
    repo_data = json.loads((ROOT / "data" / "repositories.json").read_text(encoding="utf-8"))
    repo_names = {repo["name"] for repo in repo_data.get("repositories", [])}
    observable_items = data.get("repository_observability", [])
    observable_repos = {item.get("repository") for item in observable_items}
    if repo_names - observable_repos:
        fail(f"observability explainability review missing repository observability: {', '.join(sorted(repo_names - observable_repos))}")
    for item in observable_items:
        for key in (
            "repository",
            "visibility",
            "observable_surfaces",
            "covered_events",
            "known_gap",
        ):
            if key not in item:
                fail(f"observability explainability item missing {key}: {item}")
        if item["repository"] not in repo_names:
            fail(f"observability explainability item references unknown repository: {item['repository']}")
        unknown_events = set(item["covered_events"]) - required_events
        if unknown_events:
            fail(f"observability explainability item has unknown events: {item['repository']}")
        if not item["observable_surfaces"]:
            fail(f"observability explainability item must list observable surfaces: {item['repository']}")
    result = data.get("current_result", {})
    if result.get("gate_11_status") != "passed_for_selected_mvp_closeout":
        fail("observability explainability review must record Gate 11 selected-MVP pass")
    if not result.get("post_closeout_follow_up"):
        fail("observability explainability review must record post-closeout follow-up")
    doc = (ROOT / "docs" / "mvp-observability-explainability-review.md").read_text(encoding="utf-8")
    for phrase in [
        "Important decisions should be explainable",
        "Explanation contract",
        "what changed",
        "input evidence",
        "rule, gate, or policy",
        "Decision events",
        "runtime routing",
        "artifact cleanup",
        "public refresh",
        "Current observable surfaces",
        "Public/private explainability boundary",
        "Gate 11 passes for selected MVP closeout",
    ]:
        if phrase not in doc:
            fail(f"observability explainability review doc missing phrase: {phrase}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "docs/mvp-observability-explainability-review.md" not in readme:
        fail("README.md must link MVP observability explainability review")
    closeout_doc = (ROOT / "docs" / "mvp-global-closeout-verification.md").read_text(encoding="utf-8")
    if "mvp-observability-explainability-review.md" not in closeout_doc:
        fail("global closeout doc must link MVP observability explainability review")


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


def verify_promotion_publication_boundary() -> None:
    promotion = (ROOT / "docs" / "promotion-kit.md").read_text(encoding="utf-8")
    brief = (ROOT / "docs" / "launch-video-brief.md").read_text(encoding="utf-8")
    assets = (ROOT / "docs" / "launch-video-assets.md").read_text(encoding="utf-8")
    playbook = (ROOT / "docs" / "free-promotion-playbook.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    required_by_file = {
        "promotion-kit.md": (
            promotion,
            [
                "planning references",
                "preparation only",
                "not proof of universal completion",
                "owner-controlled gate",
                "selected-MVP closeout",
                "fresh public-refresh gate",
                "Do not promote only the idea. Point people to the outputs.",
                "Ordinary users can inspect the public outputs without setting up a local",
                "GitHub-native automation generates or validates the public artifacts",
                "controlled renewal loop",
            ],
        ),
        "launch-video-brief.md": (
            brief,
            [
                "prepared draft, not a release approval",
                "selected-MVP global closeout has passed",
                "owner-controlled gate",
                "final claim review",
                "fresh public-refresh gate",
                "Do not use this brief to claim that the Skills MVP is complete",
                "where public outputs live",
                "GitHub Actions validation",
                "cloud-first automation",
                "controlled renewal",
                "ordinary users can inspect them without a local setup",
            ],
        ),
        "launch-video-assets.md": (
            assets,
            [
                "prepared material only",
                "not proof of completion",
                "instruction to publish",
            ],
        ),
        "free-promotion-playbook.md": (
            playbook,
            [
                "broad social or video refresh",
                "current MVP",
                "selected-MVP global closeout has passed",
                "owner-approved publication gate",
                "fresh public-refresh gate",
            ],
        ),
        "README.md": (
            readme,
            [
                "publication remains gated",
            ],
        ),
        "README.zh-CN.md": (
            readme_zh,
            [
                "实际发布仍受闸门约束",
            ],
        ),
    }
    for name, (text, phrases) in required_by_file.items():
        for phrase in phrases:
            if phrase not in text:
                fail(f"{name} missing promotion publication boundary phrase: {phrase}")
    stale_status_phrases = [
        "Before MVP global closeout",
        "wait for MVP global closeout",
        "should wait for MVP global",
        "after MVP global closeout, unless",
        "MVP global closeout and evidence-backed public refresh",
    ]
    for name, text in {
        "promotion-kit.md": promotion,
        "launch-video-brief.md": brief,
        "free-promotion-playbook.md": playbook,
    }.items():
        for phrase in stale_status_phrases:
            if phrase in text:
                fail(f"{name} contains stale pre-closeout promotion status phrase: {phrase}")


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


def verify_no_stale_stage_phrases() -> None:
    checked_suffixes = {".md", ".json", ".py", ".yml", ".yaml"}
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() not in checked_suffixes:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == "scripts/verify.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for phrase in STALE_STAGE_PHRASES:
            if phrase in text:
                fail(f"stale stage phrase found in {rel}: {phrase}")


def main() -> None:
    verify_required_files()
    verify_repository_map()
    verify_topology()
    verify_language_links()
    verify_external_user_readme()
    verify_current_public_private_status()
    verify_future_lane_incubation()
    verify_shared_governance_baseline()
    verify_mvp_acceptance_map()
    verify_user_developer_compact()
    verify_mvp_closeout_evidence_ledger()
    verify_mvp_current_decision_point()
    verify_mvp03_release_routing_closeout()
    verify_mvp_artifact_hygiene_review()
    verify_mvp_continuous_assurance_review()
    verify_mvp_persistence_continuity_review()
    verify_mvp_observability_explainability_review()
    verify_support_entry()
    verify_promotion_publication_boundary()
    verify_no_obvious_private_payloads()
    verify_no_stale_stage_phrases()
    print("open-resource-governance verification passed")


if __name__ == "__main__":
    main()
