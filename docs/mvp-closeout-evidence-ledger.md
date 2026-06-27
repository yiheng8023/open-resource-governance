# MVP Closeout Evidence Ledger

This ledger is the current evidence snapshot for the curated Skills
terminal-consumer MVP.

It is not a completion claim. It records what is already proven, what is only
baseline-ready, what is partial, and what still needs work before MVP closeout.

Machine-readable ledger:
[`data/mvp-closeout-evidence-ledger.json`](../data/mvp-closeout-evidence-ledger.json).

Current decision point:
[`docs/mvp-current-decision-point.md`](mvp-current-decision-point.md) and
[`data/mvp-current-decision-point.json`](../data/mvp-current-decision-point.json).

Gate 08 artifact hygiene review:
[`docs/mvp-artifact-hygiene-review.md`](mvp-artifact-hygiene-review.md) and
[`data/mvp-artifact-hygiene-review.json`](../data/mvp-artifact-hygiene-review.json).

Gate 09 continuous assurance review:
[`docs/mvp-continuous-assurance-review.md`](mvp-continuous-assurance-review.md)
and
[`data/mvp-continuous-assurance-review.json`](../data/mvp-continuous-assurance-review.json).

Gate 10 persistence and continuity review:
[`docs/mvp-persistence-continuity-review.md`](mvp-persistence-continuity-review.md)
and
[`data/mvp-persistence-continuity-review.json`](../data/mvp-persistence-continuity-review.json).

Gate 11 observability and explainability review:
[`docs/mvp-observability-explainability-review.md`](mvp-observability-explainability-review.md)
and
[`data/mvp-observability-explainability-review.json`](../data/mvp-observability-explainability-review.json).

## Current status

```text
status: active_in_progress
snapshot date: 2026-06-27
completion claim: false
```

The private user-configuration to `agent-skills-curated` base logic chain is
already verified. The current MVP is about proving the iterative governance loop
over that working chain:

```text
candidate batch
-> review and adaptation
-> deterministic manifest
-> private consumer install or authorized dry run
-> runtime routing proof
-> lifecycle feedback
-> global closeout
```

## Verified surfaces in this snapshot

| Repository | Visibility | Current evidence |
| --- | --- | --- |
| `open-resource-governance` | public | self-referential ledger: local verification passed; check the latest `validate` workflow for the current repository head |
| `agent-skills-curated` | private-pre-public | MVP candidate batch, MVP-02 adaptation evidence, MVP-03 approval event, and candidate-specific release/routing disposition evidence at `82a4bf8...`; validation, topology, release-manifest check, 102 routing scenarios, and 182-test suite passed locally; remote `validate` should be checked for the latest pushed head |
| `codex-user-config` | private | validation, capability-router, and curated Skills installer checks passed; remote `Validate` success at `4c887aeb...` |
| `resource-radar` | private | local verification passed; remote `validate` success at `f5a36fda...` |
| `resource-radar-public` | public | local verification passed; remote `Validate` success at `a6adf587...` |
| `research-bookmarks` | private | private bookmark baseline verification passed; remote `validate` success at `1f71fcb7...` |
| `research-bookmarks-public` | public | local verification passed; remote `validate` success at `1ed42910...` |
| `codex-user-config-template` | public | local verification passed; remote `validate` success at `f1c3e7f9...` |
| `claude-user-config-template` | public | remote `validate` success at `bcf2778b...`; local verification not re-run in this snapshot |
| `claude-user-config` | private | remote `validate` success at `9dd7d668...`; local verification not re-run in this snapshot |

## Workstream status

| Workstream | Status | Meaning |
| --- | --- | --- |
| MVP-01 source candidate selection | passed | first candidate batch selected, pinned, rationalized, and kept non-executable; later release/runtime gates remain separate workstreams |
| MVP-02 review, neutralize, and adapt | passed | pre-adaptation review evidence, bounded approval, non-runtime adapted drafts, checklist-based draft review evidence, MVP-03 preflight, a template-only review contract, formal MVP-03 approval request, MVP-03 approval event, and MVP-03 candidate review exist; release payload, routing projection, runtime install, publication, and lifecycle feedback are still pending |
| MVP-03 deterministic release manifest | partial | release-or-routing candidate review is recorded: `spec-driven-development` is a recipe/routing proposal candidate, while `documentation-and-adrs` and `code-review-and-quality` are merge-into-existing-approved-Skill candidates; no payload, manifest, routing projection, or live install has been approved |
| MVP-04 private consumer install | baseline-ready | consumer installer verification passes; batch-specific install or dry-run evidence is pending |
| MVP-05 routing and runtime use | baseline-ready | capability-router verification passes; representative batch routing scenarios are pending |
| MVP-06 feedback, lifecycle, and retirement | pending | runtime feedback and lifecycle decisions for the next batch are pending |
| MVP-07 global closeout and public refresh | in progress | this ledger starts the cross-repository evidence trail |

## Gate status

| Gate | Status | Current interpretation |
| --- | --- | --- |
| Gate 01 chain complete | partial | base chain is verified and the next candidate batch is selected, pre-reviewed, adapted into non-runtime drafts, and reviewed through MVP-03 candidate disposition; it has not traversed release, private consumption, and runtime use |
| Gate 02 boundaries held | partial | current validators pass; selected candidate batch, pre-adaptation review, MVP-02 transition gate, checklist, approval request, preflight readiness record, post-approval execution plan, approval event, adapted draft review, MVP-03 preflight, MVP-03 review template, MVP-03 approval request, MVP-03 approval event, and MVP-03 candidate review are explicitly not approved payload, not releasable, not routable, not installable, and not source-redistributed |
| Gate 03 runtime useful | partial | router/installer verification passes; representative runtime proof is pending |
| Gate 04 feedback loop | pending | no new batch feedback has been recorded |
| Gate 05 next lane ready | pending | no final closeout decision exists |
| Gate 06 global verification | in progress | verified surfaces are captured above |
| Gate 07 public refresh | pending | intentionally postponed until evidence supports new claims |
| Gate 08 artifact hygiene | in progress | artifact hygiene review now records classification vocabulary and repository-level posture; final residue sweep still needs to happen after later MVP evidence exists |
| Gate 09 continuous assurance | in progress | continuous assurance review now records dimensions and repository-level stale-risk posture; final cross-repository assurance still needs later MVP evidence |
| Gate 10 persistence and continuity | in progress | persistence and continuity review now records continuity scenarios, recovery anchors, verification commands, and known gaps; final recovery drill still needs later MVP evidence |
| Gate 11 observability and explainability | in progress | observability and explainability review now records explanation contract, decision event classes, observable surfaces, and known gaps; final explainability pass still needs later MVP evidence |

## Owner-local evidence freshness check

The normal public `scripts/verify.py` check validates the ledger shape and
required evidence surfaces. It intentionally does not require access to every
private repository in the owner's environment.

Before MVP closeout, run the owner-local freshness check to compare recorded
ledger heads against local checkouts that are available on the maintainer's
machine:

```bash
python -B scripts/verify_local_evidence_freshness.py \
  --repo-root codex-user-config=/path/to/codex-user-config
```

This check is read-only. It detects stale cross-repository evidence, such as a
ledger row pointing at an older `agent-skills-curated` commit after the Skills
lane has advanced. Missing private checkouts are reported as skipped unless a
maintainer explicitly supplies them.

## Next evidence required

1. Confirm a separate, narrower MVP-03 follow-up gate if any recorded candidate
   decision may advance beyond review evidence.
2. Prepare only reviewable proposal diffs for the recorded decisions: routing
   proposal for `spec-driven-development`, merge proposal for
   `documentation-and-adrs`, and merge proposal for `code-review-and-quality`.
3. Produce release-candidate manifest evidence only if separately approved.
4. Consume the release from the private configuration workflow or an authorized
   dry run.
5. Run representative routing/runtime scenarios.
6. Feed lifecycle outcomes back into the governance loop.
7. Complete the final residue sweep after later MVP evidence exists, using the
   artifact hygiene review as the Gate 08 control surface.
8. Complete final cross-repository assurance after later MVP evidence exists,
   using the continuous assurance review as the Gate 09 control surface.
9. Complete final continuity drill after later MVP evidence exists, using the
   persistence and continuity review as the Gate 10 control surface.
10. Complete final explainability review after later MVP evidence exists, using
    the observability and explainability review as the Gate 11 control surface.
11. Run the owner-local evidence freshness check before closeout so local
    repository heads and ledger heads do not silently drift apart.

Until those steps are complete, the MVP remains active and in progress.
