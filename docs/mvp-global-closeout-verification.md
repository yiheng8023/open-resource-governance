# MVP Global Closeout Verification

MVP closeout is not a single-repository pass. The curated Skills lane may be
the terminal-consumer MVP, but its closeout must verify the whole governance
loop.

The current evidence ledger is
[`mvp-closeout-evidence-ledger.md`](mvp-closeout-evidence-ledger.md). Treat it
as the selected-MVP closeout evidence snapshot, not as a universal completion
claim.

The current decision point is
[`mvp-current-decision-point.md`](mvp-current-decision-point.md). Treat it as
the pause-and-observe state after selected-MVP closeout, not as approval for a
new batch, a new terminal consumer, or broad public promotion.

Owner-local ledger freshness can be checked with
`scripts/verify_local_evidence_freshness.py`. This read-only check compares
ledger repository heads with local checkouts when those checkouts are
available. It is intentionally separate from public CI because private
repositories and owner-local paths are not public validation inputs.

The current artifact hygiene review is
[`mvp-artifact-hygiene-review.md`](mvp-artifact-hygiene-review.md). Treat it as
Gate 08 evidence for selected-MVP closeout, not as a permanent residue cleanup
certificate.

The current continuous assurance review is
[`mvp-continuous-assurance-review.md`](mvp-continuous-assurance-review.md).
Treat it as Gate 09 evidence for selected-MVP closeout, not as a permanent
health certificate.

The current persistence and continuity review is
[`mvp-persistence-continuity-review.md`](mvp-persistence-continuity-review.md).
Treat it as Gate 10 evidence for selected-MVP closeout, not as a final recovery
guarantee for all future changes.

The current observability and explainability review is
[`mvp-observability-explainability-review.md`](mvp-observability-explainability-review.md).
Treat it as Gate 11 evidence for selected-MVP closeout, not as proof that every
future decision is already instrumented.

## Closeout principle

```text
single terminal-consumer MVP
-> cross-repository verification
-> topology/index updates
-> docs and promotion refresh
-> decision for the next iteration
```

The selected-MVP global closeout has passed. Do not promote, market, or
video-launch broader claims beyond this evidence without a fresh public refresh
gate.

## Required closeout surfaces

| Surface | What to verify |
| --- | --- |
| `open-resource-governance` | MVP gates, topology, repository map, shared baseline, README, roadmap, promotion material |
| `agent-skills-curated` | candidate/approved boundary, review evidence, manifest determinism, lifecycle decisions |
| private user configuration repositories | pinned consumer release, install, verify, rollback, runtime routing |
| `resource-radar` / `resource-radar-public` | safe decision metadata, dedupe, lifecycle feedback, public-safe reports if needed |
| bookmark repositories | taxonomy/source updates only if the MVP discovers durable public resources |
| configuration templates | reusable install/routing/rollback patterns only if generalizable |

## Global closeout checklist

- [x] All MVP workstreams pass acceptance criteria for the selected small batch.
- [x] All closeout gates have evidence for the selected MVP scope.
- [x] Public/private boundaries remain intact.
- [x] Candidate and approved states are not confused.
- [x] No public document exposes private/core project identity or internals.
- [x] Runtime install, rollback, routing, and fallback behavior are verified for
      the selected release.
- [x] Resource radar can consume safe decision metadata where useful.
- [x] Topology, repository map, shared governance baseline, and indexes are
      updated only where needed.
- [x] README and docs are updated from "planned" to "proven" only for the
      evidence-backed parts.
- [x] Promotion copy and video material remain prepared material only; broad
      publication remains separately gated.
- [x] Process artifacts are classified as promoted evidence, archived context,
      deleted residue, or explicitly ignored non-authority.
- [x] Temporary scaffolds, stale drafts, raw experiments, and obsolete reports
      are not left as repository sediment.
- [x] Retained artifacts have an ongoing quality, health, security, and
      compliance posture.
- [x] Code, schemas, reports, docs, images, automation, and governance records
      are treated as lifecycle artifacts that can decay and require re-checking.
- [x] Durable state, continuity anchors, and recovery paths are recorded so the
      system can resume across time, environments, agents, and interruptions.
- [x] Important automation, routing, scoring, promotion, rejection, cleanup, and
      release decisions are observable and explainable through public-safe
      evidence.
- [x] Owner-local evidence freshness check exists as the read-only freshness
      mechanism; available local heads were checked during this run.
- [x] The closeout report decides to pause and observe before the next gated
      Skills batch or terminal consumer.

## Promotion rule

Promotion is downstream of proof.

After selected-MVP global closeout:

- update README with evidence-backed claims;
- keep project images, launch copy, and social snippets bounded to the evidence;
- decide whether a video is now worth making through a separate public refresh
  gate;
- update support/sponsorship wording only if the project value proposition has
  become clearer.

## Evidence rule

Every global closeout claim should point to at least one of:

- a verification command result;
- a release manifest;
- a public-safe report;
- a reviewed closeout note;
- a lifecycle decision record;
- a topology or index update;
- a private evidence reference that is summarized without exposing private
  content.

## Process artifact hygiene

Process artifacts are useful while thinking, testing, and launching. They become
harmful when they outlive their purpose and start competing with real authority
surfaces.

At closeout, classify each meaningful process artifact as one of:

- promoted evidence: keep it because it proves a gate, decision, or release;
- archived context: keep it because it explains history, but mark it as
  non-authoritative;
- deleted residue: remove it because it is stale, duplicated, misleading, or
  reproducible from better sources;
- ignored non-authority: leave it only when harmless and explicitly outside the
  governed truth path.

Do not let temporary reports, raw screenshots, exploratory scripts, copied chat
fragments, stale drafts, or launch scaffolds become hidden second truth sources.

## Continuous assurance rule

Closeout is a checkpoint, not a permanent certificate.

Every retained artifact class should remain subject to proportionate recurring
assurance:

- code quality and maintainability;
- repository and workflow health;
- security and supply-chain posture;
- license, provenance, privacy, and compliance boundaries;
- documentation freshness and claim accuracy;
- public/private boundary drift;
- generated artifact determinism and reproducibility.

Apply the same idea beyond code. A README, topology map, launch image, schema,
report, generated index, workflow, or governance note can become stale,
misleading, unsafe, or non-compliant just like source code can.

## Persistence and continuity rule

The system should survive ordinary loss of context.

For every maintained lane, keep enough durable state to resume after:

- a long break;
- a new machine or runtime environment;
- a different AI agent or human maintainer;
- an interrupted thread;
- a repository split, rename, or public/private projection update;
- a failed automation run or partial release.

Continuity anchors may include repository maps, topology files, manifests,
decision records, generated indexes, verification reports, release notes,
restore instructions, and public-safe summaries. Do not rely on chat history,
private memory, or one person's memory as the only continuation mechanism.

## Observability and explainability rule

The system should not behave like a black box.

For important decisions, preserve enough public-safe evidence to answer:

- what changed;
- when it changed;
- which input or source influenced the decision;
- which rule, score, gate, or human approval applied;
- why the chosen outcome was preferred over alternatives;
- what was deferred, rejected, retired, or cleaned up;
- how to reproduce, verify, or challenge the decision.

This applies to automation, routing, scoring, source selection, candidate
rejection, approval, release, cleanup, lifecycle state, and public promotion.
The explanation should be proportional: lightweight for routine checks,
structured for release or trust-boundary decisions.
