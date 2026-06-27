# Repository Map

## Hub

- `open-resource-governance`: public-safe explanation, map, shared boundaries, and promotion material.

## Discovery lane

- `resource-radar`: private broad resource discovery source, candidate pool,
  quality signals, lifecycle state, deduplication, and reports.
- `resource-radar-public`: public-safe resource radar template/projection with
  reusable schema, demo fixtures, scoring/lifecycle examples, deterministic
  demo reports, and validation without the private candidate pool.

The discovery lane is generic. It is not agent-specific and should not be
limited to software engineering, skills, Codex, or Claude.

## Curated Skills lane

- `agent-skills-curated`: reviewed Skill content, source pinning, license/provenance review, safety review, adaptation, topology, conflict handling, and release manifests.

This is the downstream terminal for reviewed executable Skill artifacts only.
It should receive skill/MCP/agent-runtime candidates from discovery, but broad
references, bookmarks, tools, datasets, and learning resources should remain in
their own lanes unless explicitly reviewed as Skill material.

## Configuration lane

Configuration follows the same private-source / public-template rule as bookmarks:

| Agent | Private source | Public template | Boundary |
| --- | --- | --- | --- |
| Codex | `codex-user-config` | `codex-user-config-template` | private memory, preferences, live install state, credentials, local paths stay private |
| Claude Code | `claude-user-config` | `claude-user-config-template` | private memory, commands, hooks, account state, credentials, local paths stay private |

Public templates provide structure, placeholder examples, docs, and validation. Private sources own the real user environment.

## Bookmark lane

- `research-bookmarks`: private source of truth for complete bookmark imports, private overlays, audits, and declassification inputs.
- `research-bookmarks-public`: public-safe structured source catalog and generated browser-importable bookmark HTML.
- `resource-radar`: can consume filtered bookmark sources for wider discovery, lifecycle, scoring, and projections, but does not own raw private bookmark truth.

## Relationship rule

No repository should silently mutate another repository's private state. Cross-repo automation should consume public-safe contracts, generate reviewable outputs, and stop at promotion or permission gates.

The system is a graph of lanes and projections, not a single linear hierarchy.
Read edges as allowed knowledge flow, candidate proposals, public-safe
projections, or review-gated promotion paths, not as ownership transfer.

For the full graph, see [`docs/system-topology.md`](system-topology.md) and the
machine-readable index at [`data/topology.json`](../data/topology.json).

## Current MVP gate

The topology also indexes
[`mvp-current-decision-point.md`](mvp-current-decision-point.md) as a
governance gate rather than a repository. That node records that the curated
Skills MVP has consumed explicit owner approval for the MVP-03 follow-up gates
and produced release/routing/manifest/install proof for the selected small
batch. MVP-06 lifecycle feedback is now recorded and the selected MVP is closed
with a pause-and-observe next state. Broad public promotion and next-lane
graduation remain separate gates.

This gate is intentionally narrow:

- It is not release authority.
- It is not authority to approve unrelated manifests.
- It is not authority to add unrelated generated routing.
- It is not permission for unrelated private runtime installation.
