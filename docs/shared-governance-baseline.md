# Shared Governance Baseline

This baseline defines what should be consistent across the repository family
without forcing every lane to look identical.

The machine-readable baseline is
[`data/shared-governance-baseline.json`](../data/shared-governance-baseline.json).

## Core idea

```text
shared governance baseline
+ lane-specific implementation
+ private overlays
```

The repositories should share governance logic, verification posture, safety
boundaries, and update discipline. They should not share private data, real
runtime state, personal preferences, or lane-specific implementation details.

## What should be consistent

Public-facing repositories should usually provide:

- a clear README with language switch when bilingual docs exist;
- repository role and explicit non-role;
- public/private boundary;
- layout or artifact map;
- verification command;
- update rules;
- safety boundary;
- license and notice;
- contribution guidance;
- security reporting path;
- support or contact path;
- GitHub Actions validation when practical.

Private repositories should usually provide:

- explicit private source truth;
- a public projection or public template path when applicable;
- secret and local-state exclusion rules;
- declassification rules;
- verification for the private workflow;
- no blind bidirectional sync with public repositories;
- backup, restore, and rollback when runtime state is managed.

## What should remain different

Consistency does not mean sameness.

Each lane keeps its own implementation:

| Lane | Difference that should remain |
| --- | --- |
| Bookmarks | taxonomy, public source catalog, browser-importable HTML exporter |
| Resource radar | resource schema, quality scoring, lifecycle state, candidate reports |
| Curated Skills | source pinning, license/provenance review, safety review, release manifest |
| User configuration | runtime install policy, memory boundary, backup/restore, local verification |
| Future lanes | candidate-only incubation, graduation rule, small-output-first proof |

Do not flatten these differences into one generic repo template. The goal is a
shared baseline, not a monoculture.

## Shared automation loop

Most lanes can reuse this abstract loop:

```text
discover/import
-> normalize
-> classify
-> generate
-> verify
-> review gate
-> publish or keep private
-> lifecycle check
-> update or retire
```

The concrete implementation differs by lane:

- bookmarks generate browser-importable HTML;
- resource radar generates candidate reports;
- curated Skills generates release evidence and manifests;
- configuration templates generate safe scaffolding;
- private configuration repositories verify real runtime state;
- future lanes stay candidate-only until they prove value.

## Shared checks

Cross-repository checks should look for:

- missing language switch;
- missing role or non-role;
- missing public/private boundary;
- missing verification path;
- candidate material described as approved;
- generated artifacts described as hand-edited truth;
- support or sponsorship described as bypassing review;
- private project names, internal stages, local paths, credentials, memory, or
  account state leaking into public repositories;
- automation that mutates another repository without an explicit review gate.

## Review gates

Automation can prepare, classify, generate, and verify. Human review is needed
before:

- publishing a public projection;
- promoting a candidate to approved;
- adding a direct funding/payment link;
- exposing private or core project information;
- changing a repository's role or trust boundary;
- writing into another repository;
- turning a candidate lane into a maintained system.

## Relationship to the Skills MVP

The curated Skills lane is the first serious terminal-consumer MVP for this
governance system. If that lane can prove the full loop from discovery to
review, release, install, routing, runtime use, feedback, and retirement, then
other terminal consumers can be added with much less guesswork.

See [`mvp-plan-and-acceptance.md`](mvp-plan-and-acceptance.md) for the execution
map and acceptance criteria.

See [`mvp-global-closeout-verification.md`](mvp-global-closeout-verification.md)
for the cross-repository closeout and public-refresh gate.

Until then, keep future lanes lightweight and candidate-only.

## Practical rule

```text
standardize the rules
not the private state

share the loop
not the lane-specific payload

verify the output
do not pretend the whole system is finished
```
