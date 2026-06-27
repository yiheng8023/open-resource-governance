# MVP Current Decision Point

Machine-readable decision record:
[`data/mvp-current-decision-point.json`](../data/mvp-current-decision-point.json).

This is not a universal completion claim and not public launch approval.

## Current state

```text
status: selected_mvp_closed_pause_observe
current workstream: mvp-07-global-closeout
candidate review recorded: true
```

The selected small-batch MVP is closed with a pause-and-observe decision. The
owner approved the MVP-03 follow-up gates, the Skills lane executed the
release/routing/manifest update, the private configuration lane consumed the
release and verified runtime install proof, and the curated Skills lane
recorded public-safe lifecycle feedback.

This record protects the next boundary: do not turn the completed small-batch
proof into approval for unrelated sources, official/runtime Skill vendoring,
public promotion, or future lane graduation.

## Current decision

The decision is:

```text
pause and observe before the next gated batch
```

A future curated Skills batch, another terminal consumer, or a broad public
promotion refresh requires a fresh gate.

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
- `agent-skills-curated` recorded MVP-06 lifecycle feedback and resource-radar
  dedupe metadata.

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
- summarize selected-MVP closeout evidence;
- record next-iteration options without adding new sources.

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
pause_and_observe_before_next_gated_batch
```

The next evidence should include:

1. fresh intake/review/approval/release/install/lifecycle evidence for any new
   curated Skills batch;
2. a separate graduation gate for any new terminal consumer;
3. a fresh public refresh gate if broad promotion resumes;
4. event-driven artifact hygiene, assurance, continuity, and explainability
   review before material topology expansion.

## Why this record exists

The current decision point is intentionally small and explicit. It prevents
future continuation threads, agents, or automation from turning "a small batch
proof exists" into open-ended source intake, official Skill vendoring, broad
runtime mutation, or public promotion approval.
