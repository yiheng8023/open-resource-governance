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

- `research-bookmarks-public`: official-source taxonomy and bookmark portability conventions.
- private bookmarks repository: full personal bookmarks, notes, non-official resources, browser exports, and preferences.

## Relationship rule

No repository should silently mutate another repository's private state. Cross-repo automation should consume public-safe contracts, generate reviewable outputs, and stop at promotion or permission gates.
