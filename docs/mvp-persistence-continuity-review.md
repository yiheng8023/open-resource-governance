# MVP Persistence And Continuity Review

Machine-readable review:
[`data/mvp-persistence-continuity-review.json`](../data/mvp-persistence-continuity-review.json).

This review supports MVP Gate 10. It is not a completion claim.

## Review status

```text
review id: mvp-persistence-continuity-review-2026-06-27
status: active_in_progress
completion claim: false
```

## Core rule

Repository truth beats chat memory for continuation.

The system must be resumable after a long break, context loss, a different
agent, a new machine, a repository split, or a failed automation run. Private
memory and chat history can help, but they must not be the only way to recover
state.

## Continuity scenarios

| Scenario | Meaning |
| --- | --- |
| context loss | a new thread can recover current state without replaying the whole conversation |
| environment change | a fresh machine can identify the relevant repositories, scripts, and projections |
| agent switch | Codex, Claude, another agent, or a human can read the same map and boundaries |
| interrupted work | partial MVP work can resume from status, evidence, and next-required-proof records |
| repository split or projection | private source and public projection pairs remain traceable |
| automation failure | failed validation, generation, sync, or publication can be diagnosed |

## Current recovery anchors

The main public recovery path starts here:

```text
open-resource-governance
-> README
-> repository map + system topology
-> MVP plan and acceptance map
-> MVP evidence ledger
-> Gate-specific review surfaces
```

Lane-specific recovery then follows each repository's own README, validation
script, registry, manifest, report, or template.

Important current anchors:

- `open-resource-governance`: repository map, topology, MVP plan, evidence
  ledger, and gate reviews.
- `agent-skills-curated`: registry, release manifest, MVP-02 gate/checklist
  evidence, topology build, tests, and manifest validation.
- private configuration repositories: private AGENTS/README, verify scripts,
  install/rollback guidance, and runtime-specific boundaries.
- `resource-radar` / `resource-radar-public`: private candidate truth versus
  public schema/demo projection.
- `research-bookmarks` / `research-bookmarks-public`: private bookmark baseline
  versus public-safe source catalog and generated browser-importable HTML.
- configuration templates: reusable public structure, not private state.

## Public/private continuity boundary

Public repositories should help a maintainer understand the system and rebuild
their own private overlay. They must not expose the owner's private memory,
preferences, credentials, local paths, account state, raw private bookmarks, or
private candidate pools.

Private repositories own real recovery for the owner's environment. Public
templates and projections explain the pattern without pretending to be the
owner's backup.

## Gate 10 result

Gate 10 is now stronger because continuity scenarios, recovery anchors,
verification commands, and known gaps are explicit and checked by repository
validation.

Gate 10 still cannot pass until later MVP evidence exists and a final
continuity drill confirms the system can resume from current repository truth
after MVP-03 through MVP-06 have produced real release, consumption, runtime,
and feedback evidence.
