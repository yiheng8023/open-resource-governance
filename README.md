# open-resource-governance

English | [简体中文](README.zh-CN.md)

Public-safe hub for a modular resource governance system: discover useful public resources, curate agent skills, preserve portable AI-collaboration configuration, and maintain bookmark taxonomies without exposing private state.

## Repository Role

This hub explains the system, maps the related repositories, and provides public-facing documentation and promotion material.

It is a coordination and communication layer, not a runtime authority, private configuration store, bookmark dump, or Skill release channel.

## What This Repository Provides

- A public-safe overview of the resource governance system.
- A repository map for discovery, curated Skills, configuration templates, and bookmarks.
- Shared public/private boundary rules.
- License and contribution expectations.
- Free-channel promotion material for GitHub profiles, repository descriptions, and social posts.
- Closeout and launch-gate evidence for staged public release.

## What This Repository Does Not Own

- Private user configuration, memory, credentials, local paths, account state, or preferences.
- Private browser bookmarks or browsing history.
- Curated Skill release manifests or vendored Skill content.
- Resource scoring databases or discovery snapshots.
- Runtime installation, account authorization, or external-service state.

## System Map

```text
open-resource-governance
  -> public-safe hub, map, docs, promotion kit

resource-radar
  -> discovers, normalizes, scores, deduplicates, and reports public resources

agent-skills-curated
  -> governs reviewed Skill content, provenance, safety, topology, conflicts, and release manifests

codex-user-config-template
  -> public-safe template for private AI-collaboration configuration repositories

research-bookmarks-public
  -> public-safe official-source bookmark taxonomy and source directory

private overlays
  -> real user configuration, memory, bookmarks, preferences, and runtime state
```

## Relationship To Private Repositories

Use public core plus private overlay. Public repositories carry reusable structure, policy, validation, examples, and official/public-safe references. Private repositories carry personal data, preferences, account state, runtime details, and complete local workflows.

Private-to-public promotion must pass a declassification gate. Do not mirror private repositories into public repositories.

## Verification

Run:

```bash
python -B scripts/verify.py
```

GitHub Actions runs the same verification on pull requests and pushes to `main`.

Key docs:

- [`docs/repository-map.md`](docs/repository-map.md) — repository roles and relationships.
- [`docs/public-private-boundary.md`](docs/public-private-boundary.md) — public/private safety boundary.
- [`docs/public-launch-gates.md`](docs/public-launch-gates.md) — gates that must pass before public release.
- [`docs/pre-public-safety-audit.md`](docs/pre-public-safety-audit.md) — concrete safety audit before changing visibility.
- [`docs/pre-public-readiness-2026-06-26.md`](docs/pre-public-readiness-2026-06-26.md) — latest pre-public readiness evidence for the hub.
- [`docs/free-promotion-playbook.md`](docs/free-promotion-playbook.md) — free-channel launch and promotion runbook.
- [`docs/community-feedback-model.md`](docs/community-feedback-model.md) — safe issue/PR feedback model for future public collaboration.
- [`GOVERNANCE.md`](GOVERNANCE.md) — lightweight maintainer and owner-gate model.
- [`SUPPORT.md`](SUPPORT.md) — support boundaries and safe contact paths.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — public-safe collaboration expectations.
- [`docs/closeout-audit-2026-06-26.md`](docs/closeout-audit-2026-06-26.md) — latest staged closeout audit.
- [`docs/promotion-kit.md`](docs/promotion-kit.md) — free-channel promotion draft material.

## Update Rules

1. Keep this hub public-safe.
2. Prefer modular repository boundaries over one giant system.
3. Share rules, schemas, taxonomy, docs, and validation where useful.
4. Keep private state in private overlays.
5. Treat public launch as a separate release gate.

## Safety Boundaries

This repository can be made public when ready. Before publication, verify that it contains no private configuration, private bookmarks, memory, credentials, local paths, account state, personal preference data, or third-party restricted content.
