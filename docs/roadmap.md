# Roadmap

## Stage 1: Public-safe foundation

- Establish repository map.
- Define public/private boundaries.
- Add license policy.
- Add validation.
- Prepare promotion material.

## Stage 2: Public launch

- Make the hub public.
- Decide which downstream repositories are ready for public visibility.
- Add repository topics and profile pins.
- Open Discussions only when moderation capacity exists.
- Run the public-launch gates for each repository before changing visibility.
- Use the free-promotion playbook for launch sequencing.

## Stage 3: Automation hardening

- Share schemas and validation patterns where useful.
- Add public-safe release gates.
- Improve declassification workflows.
- Keep private overlays private.
- Maintain a shared governance baseline so repeated automation logic can be
  reused without flattening lane-specific differences.

## Stage 4: Community contribution

- Accept issues and PRs for public-safe rules, taxonomy, source policy, validation, and documentation.
- Keep subjective preferences and private data out of the public core.

## Stage 5: Candidate lane incubation

- Keep future directions as candidate lanes until they prove value.
- Prioritize the curated Skills lane before building additional terminal lanes.
- Use the curated Skills terminal-consumer MVP plan as the next execution map.
- Treat MVP closeout as a cross-repository evidence gate, not a single
  repository pass. README, topology, index, and promotion updates should happen
  only where the closeout evidence supports them.
- Track possible lanes such as project standards, public-safe knowledge graph
  projections, benchmark/evaluation recipes, documentation systems, software
  architecture playbooks, domain-specific resource packs, private project
  absorption queues, and community-curated catalogs.
- Do not expose or mutate private/core projects from public repositories.
- Promote a candidate lane only after it has a public/private boundary,
  verification path, owner, lifecycle rule, and maintenance budget.

## Current staged status

As of 2026-06-27, the public/private split is no longer a single hub-only
launch. The current visible map is:

- `open-resource-governance` is public and pinned on the owner's GitHub profile.
- `research-bookmarks` is private and owns complete bookmark imports, private
  overlays, audits, and declassification inputs.
- `research-bookmarks-public` is public and owns the generated public-safe
  bookmark projection.
- `resource-radar` is private and owns the real candidate pool, review notes,
  account-coupled automation, snapshots, and lifecycle reports.
- `resource-radar-public` is public and owns the reusable radar schema, demo
  fixtures, scoring/lifecycle examples, generated demo reports, and validation.
- `codex-user-config` and `claude-user-config` are private user-environment
  sources.
- `codex-user-config-template` and `claude-user-config-template` are public
  templates for reusable configuration structure.
- `agent-skills-curated` remains gated by its own release decision because it
  may govern executable Skill content, provenance, topology, conflicts, and
  release manifests.

Future releases should still pass per-repository public/private boundary
review. A public template or projection does not make the paired private source
public, and a private source does not make the public projection incomplete.

## Current MVP gate

The active MVP is the curated Skills terminal-consumer loop. The current
repository truth is:

- MVP-01 source candidate selection has passed.
- MVP-02 review, neutralization, and non-runtime adapted draft creation has
  passed.
- MVP-03 deterministic release / routing review is still waiting for explicit
  owner approval before candidate-specific release-or-routing review.

Until that approval is recorded, the adapted drafts remain non-runtime evidence:

- They are not approved payloads.
- They are not release-manifest entries.
- They are not generated routing projections.
- They are not live Agent installs.

Safe work may continue on verification, evidence freshness, public-safe
explanations, and template-only review scaffolding.
