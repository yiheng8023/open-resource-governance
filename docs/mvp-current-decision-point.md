# MVP Current Decision Point

Machine-readable decision record:
[`data/mvp-current-decision-point.json`](../data/mvp-current-decision-point.json).

This is not a completion claim and not release approval.

## Current state

```text
status: mvp03_candidate_review_recorded_later_release_gates_pending
current workstream: mvp-03-release-manifest
candidate review recorded: true
```

The MVP is active, the selected batch has non-runtime adapted drafts, and the
Skills lane now has an MVP-03 release-or-routing preflight record, a
template-only review contract, a formal approval request, a recorded owner
approval event, and candidate-specific release-or-routing disposition evidence.
The current terminal consumer is still waiting for later, narrower approval
before any payload, manifest, routing projection, install, publication, or
source redistribution change.

## Decision needed

The owner must decide which later, narrower gate should be approved after
MVP-03 candidate review. The recorded candidate decisions are:

- `spec-driven-development`: `recipe-routing-proposal`;
- `documentation-and-adrs`: `merge-into-existing-approved-skill`;
- `code-review-and-quality`: `merge-into-existing-approved-skill`.

Those decisions do not mutate `skills/`, `release-manifest.json`,
`registry/routing.json`, generated routing projections, private runtime state,
or public promotion material.

This covers exactly:

- `spec-driven-development`
- `documentation-and-adrs`
- `code-review-and-quality`

It does not approve any other source, official/runtime capability, future lane,
release manifest, runtime install, routing projection, or publication action.

## Consumed approval phrase

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

## Allowed before the next gate

The following work can continue safely before the next narrower gate:

- run read-only verification;
- refresh evidence ledgers and public-safe explanations;
- check repository freshness and CI status;
- prepare proposal scaffolding for recipe/routing or merge decisions that does
  not edit `skills/`, manifest, generated routing, or live environments;
- record a preflight or authorization request that does not approve candidate
  payload or routing mutation.

## Still disallowed

Until the owner explicitly approves a later, narrower gate:

- do not edit `skills/`;
- do not update `release-manifest.json`;
- do not update generated routing projections;
- do not install or sync live Agent environments;
- do not approve, release, or publish any candidate payload;
- do not redistribute upstream source text as approved curated payload.

## If a later gate is approved

The next state depends on the approved gate. A safe generic state is:

```text
later_narrow_release_or_routing_diff_gate
```

The next evidence must include:

1. specific next-gate approval record;
2. routing projection proposal for `spec-driven-development` if that lane
   proceeds;
3. merge proposal for `documentation-and-adrs` or `code-review-and-quality` if
   those lanes proceed;
4. manifest, approved-payload, or routing diff only if separately approved;
5. verification command results;
6. explicit record that live install and publication remain unchanged unless
   separately approved.

## Why this record exists

The current decision point is intentionally small and explicit. It prevents
future continuation threads, agents, or automation from turning "adapted drafts
exist" into accidental release, routing, installation, or publication approval.
