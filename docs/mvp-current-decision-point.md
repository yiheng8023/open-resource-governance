# MVP Current Decision Point

Machine-readable decision record:
[`data/mvp-current-decision-point.json`](../data/mvp-current-decision-point.json).

This is not a completion claim and not approval.

## Current state

```text
status: awaiting_owner_approval
current workstream: mvp-02-review-adapt
candidate adapted output allowed: false
```

The MVP is active, but the next implementation step is not automatic. The
current terminal consumer is waiting at the MVP-02 owner gate.

## Decision needed

The owner must decide whether the selected candidate batch may enter
non-runtime adapted draft creation plus checklist-based review.

This covers exactly:

- `spec-driven-development`
- `documentation-and-adrs`
- `code-review-and-quality`

It does not cover any other source, official/runtime capability, future lane,
release manifest, runtime install, routing projection, or publication action.

## Safe approval phrases

Use one of these phrases to approve only the narrow next step:

```text
批准进入 MVP-02 适配草案阶段
```

or:

```text
Approve MVP-02 adapted draft creation only
```

Goal continuation is not approval. A continuation prompt keeps the MVP
objective active, but it does not authorize adapted output, release, routing,
installation, publication, or source redistribution.

## Allowed without approval

The following work can continue safely before approval:

- run read-only verification;
- refresh evidence ledgers and public-safe explanations;
- check repository freshness and CI status;
- prepare review scaffolding that does not create adapted candidate output.

## Still disallowed

Until the owner explicitly approves the next gate:

- do not create adapted candidate output;
- do not edit `skills/`;
- do not update `release-manifest.json`;
- do not update generated routing projections;
- do not install or sync live Agent environments;
- do not approve, release, or publish any candidate payload;
- do not redistribute upstream source text as approved curated payload.

## If approved

The next state becomes:

```text
adapted_output_drafting_in_non_runtime_review_surface
```

The next evidence must include:

1. adapted draft location;
2. completed checklist sections;
3. candidate-specific disposition;
4. verification command results;
5. explicit record that manifest, routing projection, and live install remain
   unchanged.

## Why this record exists

The current decision point is intentionally small and explicit. It prevents
future continuation threads, agents, or automation from turning "keep working
toward MVP closeout" into accidental approval.
