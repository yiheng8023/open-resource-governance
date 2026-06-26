# Public Launch Gates

These gates must pass before changing any repository from private to public or
before publishing promotion material that links to it.

## Gate 1: Repository scope

The repository must clearly state what it owns and what it does not own.

It must not become a dumping ground for private configuration, private
bookmarks, runtime state, raw chat history, personal preferences, or
unreviewed third-party bodies.

## Gate 2: Public/private scan

Before publication, verify that the repository contains none of the following:

- credentials, tokens, cookies, OAuth state, cryptographic key material, or
  session state;
- personal memory snapshots, private notes, raw conversations, or subjective
  preference data;
- local machine paths, account-specific URLs, browser history, runtime logs, or
  cache files;
- private browser exports or non-official personal bookmark collections;
- third-party content whose license does not permit redistribution.

## Gate 3: License and provenance

The repository must include:

- `LICENSE`;
- `NOTICE`;
- a license-policy document when the repository has mixed code, docs,
  generated outputs, third-party links, or upstream references;
- source/provenance rules for imported or referenced third-party material.

Default policy for this repository family:

- repo-owned code, scripts, schemas, workflows, and tests: Apache-2.0;
- repo-owned public documentation and taxonomy prose: CC BY 4.0 where marked;
- third-party content: original upstream license, never overridden by this
  repository's license.

## Gate 4: Verification

The repository must have a repeatable verification command and a green GitHub
Actions check on the target branch.

Verification should cover the repository's actual public-risk surface. A green
test is not enough if it does not check the relevant boundary.

## Gate 5: Relationship map

The repository must name its relationship to the rest of the family without
claiming authority it does not have.

Minimum relationship rules:

- `open-resource-governance` is the hub and promotion layer only.
- `resource-radar` discovers, normalizes, scores, deduplicates, and reports
  public resources.
- `agent-skills-curated` owns reviewed Skill intake, adaptation, topology,
  conflicts, and release manifests.
- `codex-user-config-template` is a template, not a live configuration.
- `research-bookmarks-public` is a public-safe official-source directory, not a
  full personal bookmark export.
- private overlays own real personal configuration, memory, bookmarks,
  preferences, and runtime state.

## Gate 6: Promotion readiness

Before promotion:

1. make the hub public first;
2. link only repositories that have passed their own gates;
3. keep funding links optional and transparent;
4. use free channels first, such as GitHub profile, pinned repositories, topics,
   README links, release notes, Discussions, and short social posts;
5. avoid claiming production maturity, commercial backing, or complete coverage
   before evidence exists.

## Current release boundary

As of 2026-06-26, `open-resource-governance` has passed its owner-controlled
launch gate and is public. Downstream repositories and private overlays remain
separate owner-controlled release decisions. Changing any additional
repository visibility must not be performed as a side effect of documentation,
validation, promotion, or local closeout.
