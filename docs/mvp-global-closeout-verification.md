# MVP Global Closeout Verification

MVP closeout is not a single-repository pass. The curated Skills lane may be
the terminal-consumer MVP, but its closeout must verify the whole governance
loop.

## Closeout principle

```text
single terminal-consumer MVP
-> cross-repository verification
-> topology/index updates
-> docs and promotion refresh
-> decision for the next iteration
```

Do not promote, market, or video-launch the project as "proven" before this
global closeout passes.

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

- [ ] All MVP workstreams pass acceptance criteria.
- [ ] All closeout gates have evidence.
- [ ] Public/private boundaries remain intact.
- [ ] Candidate and approved states are not confused.
- [ ] No public document exposes private/core project identity or internals.
- [ ] Runtime install, rollback, routing, and fallback behavior are verified.
- [ ] Resource radar can consume safe decision metadata where useful.
- [ ] Topology, repository map, shared governance baseline, and indexes are
      updated only where needed.
- [ ] README and docs are updated from "planned" to "proven" only for the
      evidence-backed parts.
- [ ] Promotion copy and video material are refreshed only after the evidence
      exists.
- [ ] The closeout report decides whether to iterate Skills again, pause, or
      incubate another terminal consumer.

## Promotion rule

Promotion is downstream of proof.

Before the MVP is globally closed out:

- keep video production optional and postponed;
- avoid "complete product" language;
- describe the system as planned, staged, or in-progress where appropriate.

After global closeout:

- update README with evidence-backed claims;
- refresh project images, launch copy, and social snippets;
- decide whether a video is now worth making;
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
