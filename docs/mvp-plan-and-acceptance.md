# MVP Plan And Acceptance Criteria

This MVP proves the governance system with one real terminal consumer before
expanding to more lanes.

The machine-readable map is
[`data/mvp-acceptance-map.json`](../data/mvp-acceptance-map.json).

## MVP thesis

The curated Skills lane is the first serious terminal-consumer MVP.

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
| MVP-02 | Review, neutralize, and adapt | Produce public-safe, agent-neutral, portable Skill material | Approve adapted Skill for curated release |
| MVP-03 | Deterministic release manifest | Publish only approved Skill payloads through manifest evidence | Approve release candidate before consumer install |
| MVP-04 | Private consumer install and verification | Consume the curated release from a private configuration repository | Authorize install or restore in private runtime context |
| MVP-05 | Routing and runtime use | Verify routed use without forcing Skills for every task | Confirm high-risk or ambiguous routes |
| MVP-06 | Feedback, lifecycle, and retirement | Feed evidence back without direct private-project mutation | Approve public promotion of generalizable lessons |

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

## Closeout gates

| Gate | Meaning | Required evidence |
| --- | --- | --- |
| Gate 01: chain complete | Candidate to private runtime consumption is proven | Workstreams MVP-01 through MVP-05 pass |
| Gate 02: boundaries held | Public/private, candidate/approved, automation/human boundaries held | Evidence from MVP-01, MVP-03, MVP-04, MVP-06 |
| Gate 03: runtime useful | Skills improve real work without over-triggering | Routing and runtime evidence from MVP-05 |
| Gate 04: feedback loop | Runtime evidence can update governance safely | Lifecycle evidence from MVP-06 |
| Gate 05: next lane ready | Another terminal consumer can be evaluated | Closeout summary explains whether to incubate another lane |

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
6. the closeout report says whether to iterate Skills again or incubate another
   terminal consumer.
