# Repository Map

## Hub

- `open-resource-governance`: public-safe explanation, map, shared boundaries, and promotion material.

## Discovery lane

- `resource-radar`: broad public resource discovery, quality signals, lifecycle state, deduplication, and reports.

## Curated Skills lane

- `agent-skills-curated`: reviewed Skill content, source pinning, license/provenance review, safety review, adaptation, topology, conflict handling, and release manifests.

## Configuration lane

- `codex-user-config-template`: public-safe template for users to create private AI-collaboration configuration repositories.
- private `codex-user-config`: real user preferences, memory snapshots, local install policy, verification, backup, rollback, and runtime integration.

## Bookmark lane

- `research-bookmarks`: private source of truth for complete bookmark imports, private overlays, audits, and declassification inputs.
- `research-bookmarks-public`: public-safe structured source catalog and generated browser-importable bookmark HTML.
- `resource-radar`: can consume filtered bookmark sources for wider discovery, lifecycle, scoring, and projections, but does not own raw private bookmark truth.

## Relationship rule

No repository should silently mutate another repository's private state. Cross-repo automation should consume public-safe contracts, generate reviewable outputs, and stop at promotion or permission gates.
