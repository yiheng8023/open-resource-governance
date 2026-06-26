# open-resource-governance

English | [简体中文](README.zh-CN.md)

> `open-resource-governance` is a temporary project name and repository slug.
> It may change after public naming feedback.

![Open Resource Governance launch card](docs/assets/launch-video/title-card-16x9.png)

A public-safe starter system for organizing useful resources, research
bookmarks, AI/agent skills, and portable AI-collaboration configuration without
leaking private state.

If you have ever collected links, tools, prompts, agent skills, templates, and
automation ideas across many places, this project is about turning that mess
into a governed, reproducible, public/private-safe system.

## In one minute

This project is not a bookmark dump, prompt pack, or private configuration
backup. It is a pattern for building a small resource-governance ecosystem:

```text
private collection
-> structured records
-> public-safe projection
-> deterministic generation
-> verification
-> community feedback
-> periodic renewal
```

The first working lane is bookmarks:

- a private source repository keeps the complete browser import;
- a public repository publishes a filtered, structured, browser-importable
  bookmark catalog;
- validation scripts check that public output does not accidentally include
  private-only data;
- the same pattern can later serve resource discovery, curated skills, and
  portable AI-collaboration configuration.

## Proof, not just plans

As of 2026-06-26, the first lane is already end-to-end:

```text
389 private bookmark entries
-> filtered public-safe projection
-> 328 public-safe sources
-> generated browser-importable HTML
-> verification and user-flow simulation
```

The public artifact lives in
[`research-bookmarks-public`](https://github.com/yiheng8023/research-bookmarks-public):

- structured source catalog:
  [`data/public-sources.json`](https://github.com/yiheng8023/research-bookmarks-public/blob/main/data/public-sources.json)
- generated browser-importable HTML:
  [`exports/research-engineering-bookmarks-public.html`](https://github.com/yiheng8023/research-bookmarks-public/blob/main/exports/research-engineering-bookmarks-public.html)

That matters because the project is not asking users to trust a diagram. It
shows a working public/private split with generated output and checks.

## What problem does this solve?

Useful resources usually decay in four ways:

1. They are scattered across browser bookmarks, GitHub stars, notes, chats, and
   local folders.
2. Private preferences, account state, local paths, and public references get
   mixed together.
3. "Good resource" decisions are hard to reproduce, review, or share.
4. Automation can collect more material than a human can safely judge.

This project provides a lightweight governance pattern for that problem:

```text
collect broadly
-> classify and score
-> keep private overlays private
-> publish only public-safe projections
-> verify generated artifacts
-> review high-impact changes before release
```

## Who is this for?

- Developers and AI-tool users who want a portable resource system instead of a
  random pile of bookmarks and agent files.
- Maintainers who want to share public-safe rules, schemas, and examples while
  keeping personal configuration private.
- Researchers, builders, and small teams who want automation to help discover
  useful resources without turning into an unreviewed content dump.
- Future contributors who want to improve the taxonomy, validation, resource
  discovery, bookmark projection, or curated-skill governance lanes.

## What can you use today?

This repository is the public hub. It explains the system and verifies the
public-safe governance layer.

Current usable pieces:

- A public-safe system map for related repositories and lanes.
- A public/private boundary model for keeping personal data out of public
  artifacts.
- A launch and contribution scaffold: license, conduct, support, security,
  feedback templates, and verification.
- Public launch assets and copy for explaining the project.
- A companion public bookmark projection in
  [`research-bookmarks-public`](https://github.com/yiheng8023/research-bookmarks-public),
  including structured public sources and generated browser-importable HTML.

Some lanes are intentionally private until they are ready to be released or
generalized. Private lanes may contain personal imports, review evidence, local
state, or pre-public automation work.

## What value can you reproduce?

You can use this project as a reference implementation for:

| Goal | What this system gives you |
| --- | --- |
| Publish useful resources without leaking private state | Public/private boundary rules and validation checks |
| Turn browser bookmarks into a maintainable catalog | Structured source records plus generated importable HTML |
| Keep GitHub discovery from becoming noise | A planned resource-radar lane with scoring, lifecycle, deduplication, and human gates |
| Share AI/agent skills across environments safely | A curated-skills lane with provenance, safety review, topology, conflict handling, and release manifests |
| Make AI collaboration portable | A configuration-template lane that separates reusable structure from private preferences |
| Let other people improve the system | Contribution, issue, security, conduct, naming, and launch docs |

The important idea is not any single script. The value is the closed loop:

```text
collect -> structure -> filter -> generate -> verify -> review -> publish -> renew
```

That loop is what makes the work reusable instead of just being one person's
private pile of links and notes.

## How the system works

The design is modular. This hub does not try to become one giant repository.
Each lane has a narrower responsibility:

```text
open-resource-governance
  public hub, docs, repository map, launch materials, shared safety rules

resource-radar
  discovery, normalization, scoring, deduplication, lifecycle reports

research-bookmarks
  private complete bookmark source, overlays, audits, declassification inputs

research-bookmarks-public
  public-safe bookmark catalog and generated browser-importable HTML

agent-skills-curated
  reviewed third-party Skill content, provenance, topology, conflicts, releases

codex-user-config-template
  public-safe template ideas for portable AI-collaboration configuration
```

The core rule is:

```text
public core + private overlays
```

Public repositories should contain reusable structure, rules, schemas,
documentation, examples, official/public-safe references, and generated
artifacts that have passed checks. Private repositories can keep personal
bookmarks, configuration, memory, preferences, account state, local paths, and
work-in-progress decisions.

## Quick start

Clone the hub and run the verification check:

```bash
git clone https://github.com/yiheng8023/open-resource-governance.git
cd open-resource-governance
python -B scripts/verify.py
```

Then read these in order:

1. [`docs/repository-map.md`](docs/repository-map.md) — what each repository
   owns.
2. [`docs/public-private-boundary.md`](docs/public-private-boundary.md) — what
   can and cannot be public.
3. [`docs/roadmap.md`](docs/roadmap.md) — what is planned next.
4. [`docs/naming-campaign.md`](docs/naming-campaign.md) — how the temporary
   name may be changed.

If you only want the bookmark output, start with
[`research-bookmarks-public`](https://github.com/yiheng8023/research-bookmarks-public).

## Example user journeys

### I just want useful links

Open [`research-bookmarks-public`](https://github.com/yiheng8023/research-bookmarks-public),
review the public catalog, and import the generated HTML into your browser if
it matches your needs.

### I want to build my own public/private bookmark system

Use the bookmark lane as a model:

1. keep your complete browser export private;
2. convert selected sources into structured public-safe records;
3. generate a browser-importable public HTML file;
4. run validation before publishing;
5. keep personal preferences and local-only entries private.

### I want to help improve the project

Start with small, reviewable changes:

- improve a taxonomy label;
- suggest a better temporary project name;
- add a safer validation check;
- propose a public-safe resource category;
- clarify the docs for first-time users.

### I want to sponsor or support it

The useful public work is currently docs, taxonomy, validation, generated
artifacts, and examples. Support helps turn private experiments into reusable,
public-safe templates and automation that other people can actually run.

## Design principles

1. Public-safe by default: do not publish private configuration, private
   bookmarks, memory, credentials, local paths, account state, or personal
   preference data.
2. Modular lanes over one giant system: each repository owns a clear part of
   the workflow.
3. Automation with gates: generated artifacts should be deterministic and
   verified; high-impact promotion still requires human review.
4. Useful, not maximal: the goal is better coverage, discovery, and judgment,
   not collecting everything.
5. Evidence over vibes: important claims should have scripts, reports, or
   review records behind them.

## What this repository does not do

This hub does not:

- store private user configuration or native memory;
- import a full private bookmark archive;
- release curated Skill payloads;
- install or configure runtime tools;
- prove that every related private lane is ready for public release;
- replace project-specific review, licensing review, or security review.

## Contributing

Good first contributions include:

- clearer wording for external users;
- taxonomy and repository-map improvements;
- safer public/private boundary examples;
- naming suggestions while the project name is temporary;
- validation checks that prevent accidental private data exposure;
- feedback on the bookmark and resource-discovery lanes.

See [`CONTRIBUTING.md`](CONTRIBUTING.md),
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), and
[`SECURITY.md`](SECURITY.md).

## Sustainability

The project is currently maintained as an independent public-good experiment.
If it helps you, the most useful support right now is:

- star the repository;
- share a concrete use case;
- open a focused issue;
- suggest a better name;
- contribute docs, taxonomy, validation, or examples.

Funding channels may be added later after the public model is clearer.

## Documentation index

- [`docs/project-design.md`](docs/project-design.md) — external-user design
  rationale, value loops, user journeys, and contribution surface.
- [`docs/public-project-positioning-benchmark.md`](docs/public-project-positioning-benchmark.md)
  — public README and sustainability positioning benchmark.
- [`docs/repository-map.md`](docs/repository-map.md) — repository roles and
  relationships.
- [`docs/public-private-boundary.md`](docs/public-private-boundary.md) —
  public/private safety boundary.
- [`docs/public-launch-gates.md`](docs/public-launch-gates.md) — gates before
  public release.
- [`docs/free-promotion-playbook.md`](docs/free-promotion-playbook.md) —
  free-channel launch and promotion runbook.
- [`docs/launch-video-brief.md`](docs/launch-video-brief.md) — short launch
  video script, storyboard, and AI video prompt.
- [`docs/launch-video-assets.md`](docs/launch-video-assets.md) — prepared
  public-safe launch image assets.
- [`docs/bookmark-lane-closeout-2026-06-26.md`](docs/bookmark-lane-closeout-2026-06-26.md)
  — bookmark lane split, verification, and public/private closeout evidence.
- [`docs/contact-and-social.md`](docs/contact-and-social.md) — public-safe
  contact routes and future social-link policy.

## Safety boundary

This repository is public. Every update must remain public-safe. Do not add
private configuration, private bookmarks, memory, credentials, local paths,
account state, personal preference data, browser/session data, or third-party
restricted content.
