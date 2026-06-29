# Global System Topology

`open-resource-governance` is the public entry point and global index for the
resource-governance ecosystem. It should make the relationships visible without
turning every lane into one monolithic repository.

The machine-readable graph lives in [`data/topology.json`](../data/topology.json).

This is a graph, not a simple upstream/downstream chain. Some repositories
publish public-safe projections, some hold private state, some consume
candidates, and some can feed back review decisions so future discovery becomes
less noisy.

## Core distinction

```text
private source / overlay
  owns real private state, candidate pools, personal preferences, review notes

public template / projection
  owns reusable public-safe schema, docs, examples, generated outputs, validation
```

## Shared governance baseline

The repository family shares a governance baseline for public/private
boundaries, verification, update rules, review gates, and lifecycle discipline.
That baseline is documented in
[`docs/shared-governance-baseline.md`](shared-governance-baseline.md) and
[`data/shared-governance-baseline.json`](../data/shared-governance-baseline.json).

The baseline is intentionally not a universal repo template. It standardizes
the rules, not the lane-specific payloads.

## Neutrality rule

User-configuration lanes are generic in purpose but runtime-specific in
implementation. They are about agent-environment migration, cloud sync/backup,
restore, verification, rollback, and runtime integration. Concrete
implementations may be agent-specific because they represent real private
environments:

- `codex-user-config` / `codex-user-config-template`
- `claude-user-config` / `claude-user-config-template`

Codex and Claude are current characterized examples, not the boundary of the
model. Future agent or toolchain templates can be added after their runtime
files, settings, memory surfaces, hooks, tools, MCPs, plugins, permissions, and
account state have been mapped.

All other lanes should remain agent-neutral, tool-neutral, reusable, and
portable. Resource discovery, bookmarks, curated skills, validation policies,
topology, and launch governance should not be framed as Codex-only or
Claude-only.

`agent-skills-curated` is downstream only for executable Skill artifacts. It is
not the destination for every useful resource. A resource may be a bookmark
seed, reference, dataset, tool, learning source, workflow, standard, or skill
candidate; only reviewed skill candidates should enter the curated Skills lane.

## Runtime collaboration pattern

The runtime collaboration pattern is another graph layer. It is not a separate
repository and not a Codex-only claim:

```text
project / user instructions
-> continuous intent contract
-> capability decision router
-> selected capability, Skill, tool, workflow, or native reasoning
-> execution
-> event-driven revalidation
-> verification and handoff
```

Codex currently provides the first validated implementation of this pattern
through `AGENTS.md`, `intent-contract`, and `capability-router`. Other agents
should be adapted by preserving the same invariants through their own
instruction, rule, Skill, hook, prompt, or workflow surfaces.

See [`docs/intent-contract-portability.md`](intent-contract-portability.md) and
[`data/intent-contract-adapters.json`](../data/intent-contract-adapters.json).

## Current graph

The graph also includes a current MVP gate node. It is not a repository and not
release authority. It records that the curated Skills MVP has consumed the
MVP-03 follow-up approval and produced release/routing/manifest/install proof
for the selected small batch. MVP-06 lifecycle feedback is now recorded, and
the selected small-batch MVP is closed with a pause-and-observe next state.

```mermaid
flowchart TD
  hub["open-resource-governance<br/>public hub + global index"]

  radarPrivate["resource-radar<br/>private source / candidate pool"]
  radarPublic["resource-radar-public<br/>public template + demo projection"]

  bookmarksPrivate["research-bookmarks<br/>private complete bookmarks"]
  bookmarksPublic["research-bookmarks-public<br/>public bookmark projection"]

  skills["agent-skills-curated<br/>reviewed skill governance"]
  mvpGate["mvp-current-decision-point<br/>selected MVP closed: pause/observe"]

  codexTemplate["codex-user-config-template<br/>Codex-specific public template"]
  codexPrivate["codex-user-config<br/>private Codex environment"]
  claudeTemplate["claude-user-config-template<br/>Claude-specific public template"]
  claudePrivate["claude-user-config<br/>private Claude environment"]

  hub --> radarPublic
  hub --> bookmarksPublic
  hub --> codexTemplate
  hub --> claudeTemplate
  hub --> mvpGate

  radarPublic -. "template for" .-> radarPrivate
  radarPrivate -. "review-gated public-safe patterns" .-> radarPublic

  bookmarksPrivate -. "declassifies public subset" .-> bookmarksPublic
  bookmarksPublic -. "can seed discovery" .-> radarPrivate

  radarPrivate -. "candidate proposals only" .-> skills
  skills -. "review decisions for dedupe" .-> radarPrivate
  skills -. "release manifest consumed by" .-> codexPrivate
  mvpGate -. "indexes release/routing/install proof" .-> skills
  mvpGate -. "indexes private runtime install proof" .-> codexPrivate

  codexTemplate -. "guides private overlay" .-> codexPrivate
  codexPrivate -. "public-safe patterns only" .-> codexTemplate
  claudeTemplate -. "guides private overlay" .-> claudePrivate
  claudePrivate -. "public-safe patterns only" .-> claudeTemplate
```

## What edges mean

Edges in the graph are governance relationships, not automatic write access.

- `indexes`: the hub documents and points to a repository.
- `public-template-for-private-source`: a public repo shows reusable structure
  that private automation can adopt.
- `declassifies-public-safe-subset-to`: a private repo can publish a reviewed
  public subset.
- `can-seed-public-resource-discovery`: one public-safe projection can become
  input evidence for discovery.
- `can-propose-reviewed-candidates-to`: a discovery lane can propose candidates
  but cannot bypass downstream admission.
- `may-expose-reviewed-decisions-for-deduplication`: a reviewed downstream lane
  can publish safe decision metadata so discovery does not keep resurfacing
  already accepted or rejected candidates.
- `indexes-current-mvp-gate`: the hub points to the current MVP authorization
  boundary without turning it into release authority.
- `indexes-release-routing-install-proof`: the current decision point records
  that the selected MVP batch passed the release/routing/manifest/install proof
  path after explicit owner approval; it remains evidence indexing, not
  downstream release authority.
- `indexes-private-runtime-install-proof`: the current decision point links to
  public-safe proof that the private configuration lane consumed and verified
  the selected curated Skills release, while private runtime details remain
  private.
- `may-contribute-public-safe-patterns-to`: private practice can improve a
  public template only after review and declassification.

## Why the hub needs a graph

Without a graph, users see many repositories and cannot tell:

- which repository is public or private;
- which repository owns source truth versus public projection;
- which repository is a template versus a real private environment;
- whether an edge allows reading, proposing, installing, or writing;
- which parts are agent-specific and which are neutral.

The hub graph makes those boundaries explicit. It is not release authority for
the other repositories; each lane still owns its own validation and release
rules.

## Current public runnable projections

- `research-bookmarks-public`: public-safe bookmark taxonomy, public source
  records, projection report, and generated browser-importable HTML.
- `resource-radar-public`: public-safe radar schema, universal domain taxonomy,
  demo resources, scoring/lifecycle examples, generated reports, and validation.

These public projections are meant to be reusable even when the private source
repositories are not visible.

## Candidate future lanes

Future terminal lanes are tracked separately from the current repository graph.
They are not implemented topology nodes until they pass a graduation rule.

See [`docs/future-lane-incubation.md`](future-lane-incubation.md) and
[`data/future-lanes.json`](../data/future-lanes.json).

This keeps the public map honest: the hub can acknowledge directions such as
project standards, knowledge graph projections, benchmark/evaluation,
documentation systems, architecture playbooks, domain resource packs, private
project absorption queues, and community-curated catalogs without pretending
they are already built.
