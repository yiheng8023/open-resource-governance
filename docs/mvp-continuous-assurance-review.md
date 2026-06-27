# MVP Continuous Assurance Review

Machine-readable review:
[`data/mvp-continuous-assurance-review.json`](../data/mvp-continuous-assurance-review.json).

This review supports MVP Gate 09. It is not a universal completion claim; it
passes the selected Skills MVP closeout and remains subject to future review.

## Review status

```text
review id: mvp-continuous-assurance-review-2026-06-27
status: active_in_progress
completion claim: false
```

## Core rule

A green CI run is snapshot evidence, not a permanent certificate.

The MVP now has multiple public and private repositories, generated artifacts,
docs, screenshots, templates, workflows, and governance records. Any one of
them can decay. Continuous assurance exists to prevent yesterday's valid
evidence from becoming tomorrow's misleading claim.

## Assurance dimensions

| Dimension | What can decay |
| --- | --- |
| quality | readability, maintainability, coherence, user value |
| health | declared checks, generated outputs, workflow status |
| security | secrets, permissions, dependency/script behavior, supply-chain posture |
| compliance | license, provenance, attribution, payment, privacy, public-safe boundaries |
| freshness | links, counts, screenshots, reports, claims, external references |
| reproducibility | generated outputs, manifests, topology, reports, exports |
| public/private boundary | private overlays, local paths, memory, credentials, account state |
| runtime authority | install, routing, release, rollback, and approval boundaries |

## Repository-level posture

This pass records which dimensions each repository must keep watching:

- `open-resource-governance`: public claims, maps, support wording, promotion
  material, and governance evidence.
- `agent-skills-curated`: candidate/approved boundaries, source provenance,
  release manifests, generated topology, tests, and runtime authority.
- private user-configuration repositories: real runtime state, memory,
  preferences, hooks, commands, install/rollback behavior, and declassification
  boundaries.
- `resource-radar`: candidate scoring, source metadata, lifecycle state,
  licensing, freshness, and dedupe quality.
- `resource-radar-public`: public schema, demo fixtures, and deterministic demo
  reports without pretending to publish the private candidate pool.
- `research-bookmarks`: complete private imports, overlays, declassification
  inputs, and personal browsing boundaries.
- `research-bookmarks-public`: public source catalog, taxonomy, projection
  report, and generated browser-importable HTML.
- configuration templates: reusable structure and placeholders, not real
  private user configuration.

## Event-driven cadence

Continuous assurance does not require busywork on every small edit. Re-check at
meaningful events:

- before public README or promotion claim changes;
- before publishing a public projection or regenerated export;
- before candidate adaptation, release-candidate manifest, install, rollback,
  or runtime routing evidence;
- before absorbing private patterns into public templates;
- after source policy, license, payment, security, or automation-boundary
  changes;
- before global closeout.

## Gate 09 result

Gate 09 passes for selected MVP closeout because assurance dimensions,
repository-level watch points, lifecycle evidence, and current validation
results are explicit and checked by repository validation.

This is not a permanent certificate. Repeat cross-repository assurance before
any new candidate batch, terminal consumer, public launch refresh, repository
visibility change, or accepted stale-risk exception.
