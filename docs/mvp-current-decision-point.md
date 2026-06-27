# MVP Current Decision Point

Machine-readable decision record:
[`data/mvp-current-decision-point.json`](../data/mvp-current-decision-point.json).

This is not a completion claim and not public launch approval.

## Current state

```text
status: mvp03_release_routing_install_proof_recorded_feedback_pending
current workstream: mvp-06-feedback-retirement
candidate review recorded: true
```

The MVP is active. The selected batch has moved beyond non-runtime candidate
evidence: the owner approved the MVP-03 follow-up gates, the Skills lane
executed the release/routing/manifest update, and the private configuration
lane consumed the release and verified runtime install proof.

This record now protects the next boundary: do not turn the completed small
batch proof into approval for unrelated sources, official/runtime Skill
vendoring, public promotion, or future lane graduation.

## Decision needed

The owner must decide what happens after this small-batch proof:

- iterate another curated Skills batch;
- pause and observe the current installed proof;
- incubate another terminal consumer only after a separate graduation gate.

The consumed candidate decisions were:

- `spec-driven-development`: `recipe-routing-proposal`;
- `documentation-and-adrs`: `merge-into-existing-approved-skill`;
- `code-review-and-quality`: `merge-into-existing-approved-skill`.

Those decisions did mutate only the approved small-batch surfaces:

- `spec-driven-development` entered recipe/routing projection;
- `documentation-and-adrs` merged into `grill-with-docs`;
- `code-review-and-quality` merged into `review`;
- `release-manifest.json` stayed schema 1;
- `codex-user-config` consumed the release and verified 19 curated Skills.

This covers exactly:

- `spec-driven-development`
- `documentation-and-adrs`
- `code-review-and-quality`

It does not approve any other source, official/runtime capability, future lane,
release manifest, runtime install, routing projection, or publication action.

## Consumed approval phrases

The approval phrase already consumed for MVP-03 candidate review is:

```text
批准进入 MVP-03 release/routing 候选审查阶段
```

or:

```text
Approve MVP-03 release-or-routing candidate review only
```

Goal continuation is not approval. The recorded MVP-03 approval authorized only
candidate review, not release, routing, installation, publication, or source
redistribution.

The MVP-03 follow-up approval has been consumed for this selected small-batch
execution. The exact approval phrase was:

```text
routing projection proposal、merge proposal、approved payload diff、manifest change 或 runtime install proof全部批准。
```

## Allowed before the next gate

The following work can continue safely before the next narrower gate:

- run read-only verification;
- refresh evidence ledgers and public-safe explanations;
- check repository freshness and CI status;
- summarize public-safe runtime install proof;
- prepare lifecycle feedback and closeout scaffolding;
- record next-iteration decision options without adding new sources.

## Still disallowed

After this proof, still do not:

- pull or import new sources without a new intake gate;
- vendor official/runtime-owned Skill text;
- approve unrelated candidate payload;
- publish broad launch or promotion claims;
- update unrelated release-manifest entries;
- install unrelated live Agent runtime changes;
- redistribute upstream source text beyond reviewed adapted payload.

## Next state

The next state is:

```text
lifecycle_feedback_and_global_closeout_pending
```

The next evidence should include:

1. public-safe lifecycle feedback for the installed small batch;
2. decision to iterate Skills, pause, or incubate another terminal consumer;
3. owner-local evidence freshness check;
4. final artifact hygiene and stale-process cleanup pass;
5. global closeout verification across affected repositories;
6. explicit public promotion decision if broad promotion resumes.

## Why this record exists

The current decision point is intentionally small and explicit. It prevents
future continuation threads, agents, or automation from turning "a small batch
proof exists" into open-ended source intake, official Skill vendoring, broad
runtime mutation, or public promotion approval.
