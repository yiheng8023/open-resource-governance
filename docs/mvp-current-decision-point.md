# MVP Current Decision Point

Machine-readable decision record:
[`data/mvp-current-decision-point.json`](../data/mvp-current-decision-point.json).

This is not a completion claim and not release approval.

## Current state

```text
status: mvp03_preflight_ready_awaiting_owner_approval
current workstream: mvp-03-release-manifest
release review scaffolding allowed: true, preflight-only
```

The MVP is active, the selected batch has non-runtime adapted drafts, and the
Skills lane now has an MVP-03 release-or-routing preflight record. The current
terminal consumer is still waiting for owner approval before entering the
release-or-routing candidate review gate.

## Decision needed

The owner must decide whether the reviewed adapted drafts may enter MVP-03
release-or-routing candidate review. That future gate may decide whether a
draft remains reference-only, becomes a recipe/routing proposal, merges into an
existing approved Skill, becomes a release payload candidate, or is rejected.

This covers exactly:

- `spec-driven-development`
- `documentation-and-adrs`
- `code-review-and-quality`

It does not approve any other source, official/runtime capability, future lane,
release manifest, runtime install, routing projection, or publication action.

## Safe approval phrases

The next narrow approval phrase is:

```text
批准进入 MVP-03 release/routing 候选审查阶段
```

or:

```text
Approve MVP-03 release-or-routing candidate review only
```

Goal continuation is not approval. A continuation prompt keeps the MVP
objective active, but it does not authorize release, routing, installation,
publication, or source redistribution.

## Allowed without approval

The following work can continue safely before the next gate:

- run read-only verification;
- refresh evidence ledgers and public-safe explanations;
- check repository freshness and CI status;
- prepare release-or-routing review scaffolding that does not edit `skills/`,
  manifest, generated routing, or live environments;
- record a preflight or authorization request that does not approve candidate
  payload.

## Still disallowed

Until the owner explicitly approves the next gate:

- do not edit `skills/`;
- do not update `release-manifest.json`;
- do not update generated routing projections;
- do not install or sync live Agent environments;
- do not approve, release, or publish any candidate payload;
- do not redistribute upstream source text as approved curated payload.

## If the next gate is approved

The next state becomes:

```text
release_or_routing_candidate_review
```

The next evidence must include:

1. MVP-03 release-or-routing gate approval record;
2. decision per draft: release payload, recipe/routing change, reference-only,
   merge into existing approved Skill, or reject;
3. manifest, approved-payload, or routing diff only if separately approved;
4. verification command results;
5. explicit record that live install and publication remain unchanged unless
   separately approved.

## Why this record exists

The current decision point is intentionally small and explicit. It prevents
future continuation threads, agents, or automation from turning "adapted drafts
exist" into accidental release, routing, installation, or publication approval.
