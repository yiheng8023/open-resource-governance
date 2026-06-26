# Future Lane Incubation

This document records candidate lanes that may become useful later. It is a
planning surface, not an implementation claim.

The machine-readable candidate index is
[`data/future-lanes.json`](../data/future-lanes.json).

## Current priority

The current priority is to make the curated Skills lane reliable before
turning more candidate lanes into systems.

That means:

1. finish the Skills intake, review, routing, conflict, release, and install
   chain;
2. learn what actually needs system support;
3. promote only the future lanes that have enough evidence, maintenance budget,
   and user value.

Do not create a new lane merely because it sounds elegant.

## Candidate lanes

These directions are worth tracking:

| Lane | Purpose | Current status |
| --- | --- | --- |
| Project standards | Reusable standards, checklists, and decision rules | Candidate only |
| Knowledge graph | Public-safe topology and relationship projections | Candidate only |
| Benchmark / evaluation | Quality and usefulness evaluation recipes | Candidate only |
| Documentation system | User-facing docs, closeout evidence, diagrams, and release notes | Candidate only |
| Software architecture playbooks | Generalized architecture review and evolution playbooks | Candidate only |
| Domain-specific resource packs | Focused resource bundles generated from reviewed records | Candidate only |
| Private project absorption queue | Evidence preparation for private/core project review | Candidate only |
| Community-curated catalogs | Community-maintained public-safe resource catalogs | Candidate only |

## Graduation rule

A candidate lane should not graduate until it has:

- a clear user problem;
- a public/private boundary;
- a narrow owner and responsibility;
- a deterministic or reviewable output;
- a verification path;
- a lifecycle and retirement rule;
- enough expected value to justify maintenance.

If these conditions are missing, keep the lane as a note, not a system.

## Relationship to private/core projects

Public governance outputs may serve private or core projects, but they must not
directly mutate them or expose their internal state. A candidate lane can
prepare public-safe evidence; the private/core project must decide whether to
absorb it through its own review gate.

Do not hard-code any private/core project as the purpose of this public
ecosystem. The public model should remain neutral and reusable.

## Long-termism without overbuilding

The system should support long-term renewal, but it should avoid idealistic
overbuilding. A small generated report, checklist, or resource pack may be more
useful than a large framework that nobody maintains.

The practical rule is:

```text
prove the lane with small outputs
-> verify value
-> add governance only where needed
-> retire weak lanes early
```
