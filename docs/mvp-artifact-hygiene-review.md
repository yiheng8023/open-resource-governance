# MVP Artifact Hygiene Review

Machine-readable review:
[`data/mvp-artifact-hygiene-review.json`](../data/mvp-artifact-hygiene-review.json).

This review supports MVP Gate 08. It is not a completion claim.

## Review status

```text
review id: mvp-artifact-hygiene-review-2026-06-27
status: active_in_progress
completion claim: false
```

## Core rule

No process artifact is authority by accident.

The system now has enough documents, screenshots, reports, ledgers, templates,
and generated outputs that cleanup is not cosmetic. Without artifact hygiene,
old thinking notes, launch drafts, screenshots, demo outputs, and copied review
fragments can become hidden second truth sources.

## Classification vocabulary

| Class | Meaning | Handling |
| --- | --- | --- |
| promoted evidence | proves a gate, decision, release, verification result, or boundary | keep and link from the right authority surface |
| archived context | explains history but is not current authority | keep only with dated/contextual wording |
| deleted residue | stale, duplicated, misleading, or superseded material | remove after confirming it is not current evidence |
| ignored non-authority | harmless material outside the truth path | do not cite as proof |
| generated derived | reproducible output from declared source data/scripts | verify determinism and link to the source |
| private source | real private state or overlay | keep private; expose only public-safe summaries/projections |

## Current repository posture

The current pass records repository-level posture rather than final file-by-file
closeout. That is intentional: MVP-02 adaptation and MVP-03 release/routing
execution are now recorded, while lifecycle feedback and global closeout may
still create new review artifacts.

Important current interpretations:

- `open-resource-governance` owns the public map, shared rules, MVP plan,
  evidence ledger, and this hygiene review. Dated launch notes and promotion
  drafts remain archived context or ignored non-authority unless refreshed
  after proof.
- `agent-skills-curated` owns candidate, review, transition-gate, checklist,
  approval-request, manifest, and release evidence. Candidate Skills are review
  material only until approved; the current small batch crossed that boundary
  only after explicit follow-up approval.
- `codex-user-config` and `claude-user-config` are private source repositories.
  Their real memory, preferences, commands, hooks, local state, credentials,
  and account state are not public truth.
- `resource-radar` is a private discovery source. Candidate volume is not
  quality proof.
- `resource-radar-public` is a public template/projection. Demo reports are
  generated examples, not the private candidate pool.
- `research-bookmarks` is the private bookmark source. It owns complete imports
  and private overlays.
- `research-bookmarks-public` owns the public-safe source catalog, taxonomy,
  projection report, and generated browser-importable HTML.
- Configuration templates are public-safe examples. Template placeholders are
  not real user configuration.

## Generated artifacts are derived

Generated artifacts are allowed, but only as projections. A generated report,
HTML export, topology projection, routing index, or media asset must point back
to the data, script, or review process that produced it. It must not become a
hand-edited second authority.

## MVP-03 follow-up approval is batch-limited

The consumed MVP-02 approval authorized only non-runtime adapted draft
creation. The later MVP-03 follow-up approval authorized release/routing,
approved-payload diff, manifest change, and runtime install proof only for the
selected small batch. It does not approve new sources, official/runtime Skill
vendoring, unrelated `skills/` edits, unrelated manifest changes, source
redistribution beyond reviewed adapted payload, or public promotion.

## Gate 08 result

Gate 08 is now stronger than before because the classification vocabulary and
repository-level artifact posture are explicit and checked by repository
validation.

Gate 08 still cannot pass until lifecycle/global-closeout evidence exists and
the final residue sweep confirms that stale drafts, obsolete reports, temporary
scaffolds, raw experiments, and promotion material have been promoted,
archived, deleted, or marked non-authoritative.
