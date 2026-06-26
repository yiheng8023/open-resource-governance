# Repository Map

## Hub

- `open-resource-governance`: public-safe explanation, map, shared boundaries, and promotion material.

## Discovery lane

- `resource-radar`: broad public resource discovery, quality signals, lifecycle state, deduplication, and reports.
- planned public projection/template: a future `resource-radar-public` or equivalent public-safe package should expose reusable schema, demo fixtures, scoring/lifecycle examples, and validation without the private candidate pool.

## Curated Skills lane

- `agent-skills-curated`: reviewed Skill content, source pinning, license/provenance review, safety review, adaptation, topology, conflict handling, and release manifests.

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
