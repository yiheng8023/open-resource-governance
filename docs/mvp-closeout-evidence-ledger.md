# MVP Closeout Evidence Ledger

This ledger is the selected-MVP evidence snapshot for the curated Skills
terminal-consumer loop.

It is not a universal completion claim. It records the selected small-batch MVP
closeout, the evidence that supports it, and the next gates required before any
new batch, terminal consumer, or broad public-promotion refresh.

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
status: selected_mvp_closed_pause_observe
snapshot date: 2026-06-27
universal completion claim: false
```

The private user-configuration to `agent-skills-curated` base logic chain was
already verified before this closeout. This MVP proves iterative governance
over that working chain:

```text
candidate batch
-> review and adaptation
-> deterministic manifest
-> private consumer install or authorized dry run
-> runtime routing proof
-> lifecycle feedback
-> selected-MVP global closeout
```

The selected small batch has traversed the full loop for this MVP scope. The
next state is **pause and observe before the next gated batch**.

## Verified surfaces in this snapshot

| Repository | Visibility | Current evidence |
| --- | --- | --- |
| `open-resource-governance` | public | self-referential ledger: local verification passed before commit; check the latest `validate` workflow for the containing head |
| `agent-skills-curated` | private-pre-public | MVP candidate batch, MVP-02 adaptation evidence, MVP-03 release/routing execution, schema-1 manifest evidence, MVP-06 lifecycle feedback, 104 routing scenarios, and 182-test suite passed locally at `74c8c17...`; remote `validate` should be checked for the latest pushed head |
| `codex-user-config` | private | pinned and consumed `agent-skills-curated` `e80d497...`; install replaced `grill-with-docs`, `review`, and routing index; 19 curated Skills verified at `a89b617...`; current pushed head `f6b5e5f...` adds reviewed Codex memory sync only; local `scripts/verify.py` and `scripts/memory.py verify` passed; remote `Validate` run `28286557860` was blocked before job start by GitHub billing/spending-limit status |
| `resource-radar` | private | local verification passed; remote `validate` success at `f5a36fda...` |
| `resource-radar-public` | public | local verification passed after adding README System context; remote `Validate` success at `08534786...` |
| `research-bookmarks` | private | private bookmark baseline verification passed; remote `validate` success at `1f71fcb7...` |
| `research-bookmarks-public` | public | local verification passed after adding README System context; remote `validate` success at `ab1eaf62...` |
| `codex-user-config-template` | public | local verification passed after adding README System context; remote `validate` success at `1dd900ee...` |
| `claude-user-config-template` | public | local verification passed after adding README System context; remote `validate` success at `0d3d96df...` |
| `claude-user-config` | private | remote `validate` success at `9dd7d668...`; local verification not re-run in this snapshot |

## Workstream status

| Workstream | Status | Meaning |
| --- | --- | --- |
| MVP-01 source candidate selection | passed | first candidate batch selected, pinned, rationalized, and kept non-executable until approved gates |
| MVP-02 review, neutralize, and adapt | passed | review, neutralization, adaptation, candidate disposition, and follow-up execution evidence exist for the selected small batch |
| MVP-03 deterministic release manifest | passed | approved payload/routing changes were executed; manifest remains schema 1 with 19 curated Skills and 41 files |
| MVP-04 private consumer install | passed | private consumer pinned and installed the selected curated release; 19 curated Skills verified |
| MVP-05 routing and runtime use | passed | 104 routing scenarios passed and the private capability-router verification passed after routing index replacement |
| MVP-06 feedback, lifecycle, and retirement | passed | lifecycle decisions and resource-radar dedupe metadata are recorded in `agent-skills-curated` |
| MVP-07 global closeout and public refresh | passed | selected-MVP closeout is recorded; future batches, terminal consumers, and broad promotion remain gated |

## Gate status

| Gate | Status | Current interpretation |
| --- | --- | --- |
| Gate 01 chain complete | passed | selected batch traversed candidate selection, review/adaptation, release/routing execution, deterministic manifest, private consumer install, routing verification, lifecycle feedback, and closeout |
| Gate 02 boundaries held | passed | selected batch crossed into approved release/routing/install state only after explicit follow-up approval; unrelated candidates, official/runtime Skill text, public promotion, and broad runtime changes remain disallowed |
| Gate 03 runtime useful | passed | 104 routing scenarios passed and private consumer verification passed after routing index replacement |
| Gate 04 feedback loop | passed | public-safe lifecycle feedback and radar dedupe metadata are recorded without direct private-project mutation |
| Gate 05 next lane ready | passed | the decision is pause and observe; another curated Skills batch or terminal consumer requires a fresh gate |
| Gate 06 global verification | passed | verified surfaces are captured above and local verification passed for the selected MVP evidence path |
| Gate 07 public refresh | passed | public docs now claim only the selected-MVP closeout; video/social promotion remains optional and separately gated |
| Gate 08 artifact hygiene | passed | artifact hygiene review records classification vocabulary, repository-level posture, derived/generated boundaries, and event-driven residue review |
| Gate 09 continuous assurance | passed | assurance review records quality, health, security, compliance, freshness, reproducibility, public/private boundary, and runtime authority as recurring dimensions |
| Gate 10 persistence and continuity | passed | continuity review records recovery anchors, scenarios, verification commands, known gaps, and the pause-and-observe next state |
| Gate 11 observability and explainability | passed | explanation review records decision events, observable surfaces, known gaps, and evidence-backed closeout claims |

## Owner-local evidence freshness check

The normal public `scripts/verify.py` check validates the ledger shape and
required evidence surfaces. It intentionally does not require access to every
private repository in the owner's environment.

The owner-local freshness check compares recorded ledger heads against local
checkouts that are available on the maintainer's machine:

```bash
python -B scripts/verify_local_evidence_freshness.py \
  --repo-root codex-user-config=/path/to/codex-user-config
```

This check is read-only. It detects stale cross-repository evidence, such as a
ledger row pointing at an older `agent-skills-curated` commit after the Skills
lane has advanced. Missing private checkouts are reported as skipped unless a
maintainer explicitly supplies them.

## Next gated work

No immediate next batch is approved by this closeout. The next state is:

```text
pause and observe
```

Future work requires fresh evidence and a fresh gate when it changes material
scope:

1. New curated Skills batch: fresh intake, review, approval, release, install,
   routing, lifecycle, and closeout evidence.
2. New terminal consumer: separate graduation gate.
3. Broad public-promotion refresh: explicit public refresh gate.
4. Material topology expansion: repeat artifact hygiene, assurance,
   continuity, and explainability review.

This is a closed MVP checkpoint, not a permanent certificate.
