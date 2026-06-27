# MVP Plan And Acceptance Criteria

This MVP proves the governance system with one real terminal consumer before
expanding to more lanes.

The machine-readable map is
[`data/mvp-acceptance-map.json`](../data/mvp-acceptance-map.json).

## MVP thesis

The curated Skills lane is the first serious terminal-consumer MVP.

The base logic chain between private user configuration repositories and
`agent-skills-curated` has already been verified. This MVP does not restart
from zero or try to prove basic connectivity again. It uses that working chain
as the first terminal-consumer lane for iterative governance: candidate
selection, review, release, consumption, routing, feedback, lifecycle posture,
and global closeout.

If the system can move a small Skill candidate batch through discovery,
review, adaptation, release manifest, private consumer install, runtime
routing, feedback, and retirement, then the governance model has proven more
than documentation.

It has proven a real loop:

```text
candidate source
-> review and adaptation
-> deterministic release
-> private consumer install
-> capability routing and runtime use
-> feedback and lifecycle update
```

## Non-goals

This MVP does not:

- implement future terminal lanes;
- write into private/core projects;
- expose private project internals;
- import every interesting Skill or resource;
- claim monetization readiness;
- prove that every future repository can be automated.

## Workstreams

| ID | Workstream | Goal | Human gate |
| --- | --- | --- | --- |
| MVP-01 | Source candidate selection | Select a small high-value Skill candidate set | Approve candidate batch before adaptation |
| MVP-02 | Review, neutralize, and adapt | Produce public-safe, agent-neutral, portable Skill material | Approve non-runtime adapted draft creation; MVP-03 release-or-routing review requires separate approval |
| MVP-03 | Deterministic release manifest | Publish only approved Skill payloads through manifest evidence | Approve release candidate before consumer install |
| MVP-04 | Private consumer install and verification | Consume the curated release from a private configuration repository | Authorize install or restore in private runtime context |
| MVP-05 | Routing and runtime use | Verify routed use without forcing Skills for every task | Confirm high-risk or ambiguous routes |
| MVP-06 | Feedback, lifecycle, and retirement | Feed evidence back without direct private-project mutation | Approve public promotion of generalizable lessons |
| MVP-07 | Global closeout and public refresh | Verify the MVP across the repository family and update public surfaces only where evidence supports it | Approve public closeout claims and any promotion refresh |

## Current stage note

As of the current decision point, MVP-01 source candidate selection and MVP-02
review, neutralization, and non-runtime adapted draft creation have passed.
MVP-03 release-or-routing candidate review has recorded explicit owner approval
and candidate-specific disposition evidence. Goal continuation keeps this MVP
active, but it still does not authorize release, routing projection changes,
installation, publication, source redistribution, approved-payload diffs, or
manifest changes.

The active gate is recorded in
[`mvp-current-decision-point.md`](mvp-current-decision-point.md). The public
roadmap mirrors the same boundary in
[`roadmap.md`](roadmap.md).

## Acceptance criteria

### MVP-01: Source candidate selection

- Candidate source is pinned.
- Candidate reason is recorded.
- License/provenance state is recorded.
- Candidate remains non-executable before approval.

### MVP-02: Review, neutralize, and adapt

- Security review evidence exists.
- Private or vendor-specific assumptions are removed or bounded.
- Overlap and conflict review is recorded.
- Adaptation keeps source attribution and license boundaries.

### MVP-03: Deterministic release manifest

- Manifest schema remains declared.
- Manifest includes only approved payload files.
- Hash and size verification pass.
- Extra, missing, symlink, traversal, and boundary violations fail closed.

### MVP-04: Private consumer install and verification

- Consumer pin is explicit.
- Install plan is reviewable.
- Backup or rollback path exists.
- Installed files match manifest.
- Private runtime state is not published.

### MVP-05: Routing and runtime use

- `capability-router` remains a capability decision router.
- Simple tasks can use native or no-skill path.
- Approved Skill triggers work in representative scenarios.
- Candidate or unapproved Skills do not enter execution path.
- Fallback behavior is documented.

### MVP-06: Feedback, lifecycle, and retirement

- Runtime result is summarized as public-safe evidence or kept private.
- Accepted, rejected, deprecated, or retired state is recorded.
- Resource radar can consume safe decision metadata for dedupe.
- Lessons update shared governance only when generalizable.

### MVP-07: Global closeout and public refresh

- Per-repository verification status is recorded.
- Topology, repository map, shared baseline, and indexes are reviewed.
- README and public docs distinguish planned, proven, and deferred claims.
- Promotion and video material remain postponed until evidence-backed refresh.
- Process artifacts are classified as promoted evidence, archived context,
  deleted residue, or explicitly ignored non-authority.
- Temporary scaffolds, stale drafts, raw experiments, and obsolete reports do
  not become a second truth source.
- Retained artifacts have an ongoing quality, health, security, and compliance
  posture instead of a one-time pass/fail label.
- Code, schemas, reports, docs, images, automation, and governance records are
  all treated as lifecycle artifacts that can decay and require re-checking.
- Durable state, continuity anchors, and recovery paths are recorded so the
  system can resume across time, environments, agents, and interrupted threads.
- Important automation, routing, scoring, promotion, rejection, cleanup, and
  release decisions are observable and explainable through public-safe evidence.
- Next-step decision is recorded: iterate Skills, pause, or incubate another
  terminal consumer.

## Closeout gates

| Gate | Meaning | Required evidence |
| --- | --- | --- |
| Gate 01: chain complete | Candidate to private runtime consumption is proven | Workstreams MVP-01 through MVP-05 pass |
| Gate 02: boundaries held | Public/private, candidate/approved, automation/human boundaries held | Evidence from MVP-01, MVP-02, MVP-03, MVP-04, MVP-06 |
| Gate 03: runtime useful | Skills improve real work without over-triggering | Routing and runtime evidence from MVP-05 |
| Gate 04: feedback loop | Runtime evidence can update governance safely | Lifecycle evidence from MVP-06 |
| Gate 05: next lane ready | Another terminal consumer can be evaluated | Closeout summary explains whether to incubate another lane |
| Gate 06: global verification | Hub, Skills lane, private consumer, discovery feedback, and affected templates/projections are verified | Evidence from MVP-07 |
| Gate 07: public refresh | README, docs, topology, indexes, and promotion material are updated only for evidence-backed claims | Evidence from MVP-07 |
| Gate 08: artifact hygiene | Temporary/process artifacts are promoted, archived, deleted, or marked non-authoritative | Cleanup and residue review from MVP-07 |
| Gate 09: continuous assurance | Retained artifacts have ongoing quality, health, security, and compliance posture | Lifecycle assurance review from MVP-07 |
| Gate 10: persistence and continuity | Durable state, continuity anchors, and recovery paths can resume work across time, environments, agents, and interruptions | Continuity evidence from MVP-07 |
| Gate 11: observability and explainability | Important automation, routing, scoring, promotion, rejection, cleanup, and release decisions are inspectable and explainable | Public-safe evidence from MVP-07 |

## Execution discipline

Do not try to finish every possible Skill.

Pick a small batch and prove the loop. A tiny complete loop is more valuable
than a large incomplete catalog.

```text
small batch
-> hard review
-> deterministic release
-> private consumption
-> runtime proof
-> feedback
-> closeout
```

## Stage exit

This MVP is complete only when:

1. every workstream has passed its acceptance criteria;
2. every closeout gate has evidence;
3. no public document exposes private/core project identity or internals;
4. no candidate or unapproved Skill is treated as executable;
5. install, rollback, routing, and feedback behavior are verified;
6. global closeout verifies the affected repository family, not only the Skills
   repository;
7. topology, indexes, README, and promotion material are updated only where the
   evidence supports an update;
8. video and broader promotion remain optional and post-closeout;
9. obsolete process artifacts are removed, archived, or marked non-authoritative
   instead of becoming repository sediment;
10. retained artifacts are covered by ongoing quality, health, security, and
    compliance review instead of one-time validation theater;
11. durable state, continuity anchors, and recovery paths are sufficient to
    resume the system after context loss, environment change, or agent switch;
12. important automation, routing, scoring, promotion, rejection, cleanup, and
    release decisions are observable and explainable through public-safe
    evidence;
13. the closeout report says whether to iterate Skills again, pause, or incubate
   another terminal consumer.
