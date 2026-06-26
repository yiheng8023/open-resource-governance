# MVP Observability And Explainability Review

Machine-readable review:
[`data/mvp-observability-explainability-review.json`](../data/mvp-observability-explainability-review.json).

This review supports MVP Gate 11. It is not a completion claim.

## Review status

```text
review id: mvp-observability-explainability-review-2026-06-27
status: active_in_progress
completion claim: false
```

## Core rule

Important decisions should be explainable from public-safe evidence.

Automation output is not self-explanatory. A report, generated file, green CI
check, routing result, release manifest, or promotion update only becomes
trustworthy when a maintainer can inspect what changed, why it changed, which
input and rule applied, how it was verified, and what state comes next.

## Explanation contract

For important decisions, preserve enough evidence to answer:

- what changed;
- which input evidence was used;
- which rule, gate, or policy applied;
- who or what triggered the decision;
- which outcome was chosen;
- what was rejected or deferred;
- how the outcome was verified;
- what next state follows;
- which public/private boundary applied.

## Decision events

| Event | Explanation focus |
| --- | --- |
| source selection | why a source, bookmark, repo, or Skill candidate entered review |
| candidate review | why a candidate is pending, rejected, adapted, reference-only, approved, deprecated, or retired |
| release manifest | why a payload is included or excluded |
| install or rollback | why a private consumer action is safe and reversible |
| runtime routing | why native capability, curated Skill, recipe, confirmation, fallback, or no-skill path was selected |
| feedback lifecycle | why runtime evidence changes accepted/rejected/deprecated/retired/dedupe state |
| artifact cleanup | why an artifact is promoted, archived, deleted, or ignored |
| public refresh | why README, docs, topology, promotion material, support wording, or launch assets changed |

## Current observable surfaces

The public hub currently explains:

- repository map and topology;
- MVP plan and acceptance map;
- closeout evidence ledger;
- artifact hygiene review;
- continuous assurance review;
- persistence and continuity review;
- this observability and explainability review;
- validation script requirements;
- GitHub Actions status.

Lane-specific evidence stays in the lane that owns it. Private lanes can
publish public-safe summaries, but they must not leak private payloads merely to
make a decision more visible.

## Public/private explainability boundary

Explainability does not mean exposing everything.

Private evidence may be summarized when needed. The public record should show
the decision class, rule, result, and verification posture without exposing
private memory, credentials, account state, local paths, private bookmark
imports, raw candidate pools, personal preferences, or private project details.

## Gate 11 result

Gate 11 is now stronger because the explanation contract, decision event
classes, repository-level observable surfaces, and known explanation gaps are
explicit and checked by repository validation.

Gate 11 still cannot pass until later MVP evidence exists and the final
explainability review confirms that release, install, routing, runtime
feedback, lifecycle, cleanup, assurance, continuity, and public closeout claims
all point to concrete evidence rather than prose-only assertions.

