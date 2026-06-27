# MVP-03 Release, Routing, Manifest, And Runtime Proof Closeout

Machine-readable record:
[`data/mvp03-release-routing-closeout.json`](../data/mvp03-release-routing-closeout.json).

This is a public-safe evidence summary for the curated Skills terminal-consumer
MVP. It is not a public launch approval, not a monetization claim, and not a
general claim that every future lane is complete.

## Owner approval consumed

On 2026-06-27, the owner approved the next MVP-03 follow-up gates:

```text
routing projection proposal、merge proposal、approved payload diff、manifest change 或 runtime install proof全部批准。
```

That approval was consumed only for the already-reviewed MVP batch:

- `spec-driven-development`;
- `documentation-and-adrs`;
- `code-review-and-quality`.

It did not approve new source discovery, official/runtime Skill vendoring,
public promotion, unrelated repository changes, memory updates, Hook changes,
MCP/App/Plugin install changes, or publication claims.

## Executed outcome

`agent-skills-curated` advanced from candidate disposition to an approved,
verified release/routing update at:

```text
e80d49733192bfa41c894a72da63def4801691f4
```

The execution kept the small-batch design:

- `spec-driven-development` became a recipe/routing projection, not a standalone
  new Skill directory.
- `documentation-and-adrs` was merged into the existing approved
  `grill-with-docs` Skill.
- `code-review-and-quality` was merged into the existing approved `review`
  Skill.
- `release-manifest.json` stayed at schema 1.
- The release manifest stayed at 19 curated Skills and 41 files.
- Only the approved payload files for `grill-with-docs` and `review` changed
  hash/size.
- No official/runtime-owned Skills were copied into the curated repository.
- No new third-party source was pulled in this gate.

`codex-user-config` consumed that release at:

```text
a89b61737f066118b13264510cb4dbe5566e2269
```

The private runtime install proof replaced two managed Skills and the routing
index, then verified 19 curated Skills. The live transaction was recorded at
`~/.agents/curated-skills-transaction.json`, while private runtime details stay
private.

## Verification evidence

`agent-skills-curated` verification:

```text
python -B scripts/build_topology.py
python -B scripts/build_release_manifest.py
python -B scripts/simulate_routing.py --report generated\routing-simulation-report.json
python -B scripts/verify.py
python -B scripts/build_topology.py --check
python -B scripts/build_release_manifest.py --check
python -B scripts/simulate_routing.py --all
python -B -m unittest discover -s tests -v
git diff --check
```

Result summary:

- verification passed;
- 104 routing scenarios passed;
- 182 unit tests passed;
- manifest schema remained 1.

`codex-user-config` verification:

```text
python -B scripts/skills.py plan
python -B scripts/skills.py install --apply
python -B scripts/skills.py verify
python -B scripts/verify_capability_router.py
python -B scripts/verify_skills_install.py
python -B scripts/verify.py
```

Result summary:

- install plan found 0 adds, 17 unchanged, 2 replacements, and 0 retires;
- install applied and verified 19 curated Skills;
- capability-router verification passed;
- private runtime install proof completed.

Owner-local evidence freshness:

```text
python -B scripts/verify_local_evidence_freshness.py --repo-root open-resource-governance=C:\tmp\open-resource-governance --repo-root agent-skills-curated=C:\tmp\agent-skills-curated-work --repo-root codex-user-config=C:\Projects\codex-user-config
```

Result summary:

- local evidence freshness check passed;
- `agent-skills-curated` matched `e80d49733192bfa41c894a72da63def4801691f4`;
- `codex-user-config` matched `a89b61737f066118b13264510cb4dbe5566e2269`;
- the current hub row remains self-referential and is checked through its own
  validation and Git history.

## Boundaries preserved

- Public/private boundaries remain intact.
- Candidate and approved states are no longer confused for this batch: the
  selected changes are now approved release/routing evidence, while unrelated
  candidates remain non-executable.
- The hub did not become release authority for downstream repositories.
- The curated Skills repository remains the authority for reviewed Skill
  payload, topology, routing projection, and manifest evidence.
- The private configuration repository remains the authority for install,
  verify, rollback, and runtime integration.
- Promotion, video refresh, funding claims, and broad public launch claims still
  require their own public-closeout decision.

## Next state

The terminal-consumer path is now proven for this small MVP batch through:

```text
candidate selection
-> review/adaptation
-> release/routing execution
-> deterministic manifest
-> private consumer install
-> routing verification
```

The remaining MVP work is lifecycle feedback, final cross-repository closeout,
and the next owner decision:

- iterate another curated Skills batch;
- pause and observe;
- incubate another terminal consumer only after a separate graduation gate.
