# Intent Contract Portability

This document defines the portable form of the `intent-contract` pattern.
It is not Codex-only, Claude-only, or Skill-only. Codex is the first validated adapter
in this repository family; other agents should preserve the same
collaboration invariants through their own instruction, rule, Skill, hook, or
workflow mechanisms.

## Core claim

`intent-contract` is a continuous human-AI collaboration control layer:

```text
project / user instructions
-> intent contract
-> capability decision
-> selected capability, Skill, tool, workflow, or native reasoning
-> execution
-> event-driven intent revalidation
-> event-driven capability rerouting when needed
-> verification and handoff
```

It is not merely an entry prompt. It should be rechecked when task meaning,
scope, authority, risk, evidence, phase, or user instructions materially change.

## Portable invariants

Any adapter should preserve these invariants even when the local mechanism is
not called a Skill:

1. Preserve the raw user request as the source input.
2. Bind goal, target, mode, scope, authority boundary, expected output, and
   verification surface before side-effecting work.
3. Fast-path simple, low-risk, clearly scoped requests.
4. Ask the smallest blocking question when a missing fact changes the next safe
   action or authority boundary.
5. Treat brainstorming, reminders, future options, and candidate ideas as
   discussion material unless the user explicitly authorizes execution.
6. Revalidate intent at event-driven checkpoints: new user correction, phase
   boundary, new evidence, failure/blocker, capability-class switch, write or
   external-effect boundary, and final verification.
7. Keep capability selection separate from intent binding. A router can choose
   native reasoning, official/runtime capability, curated Skill, recipe/DAG,
   ask-user, no-skill, or safe fallback only after the task is bound.
8. Do not use keyword matches alone as proof of intent, authority, or
   capability eligibility.

## Adapter matrix

| Environment | Likely instruction / rule surface | Skill-like surface | Current status | Adapter note |
| --- | --- | --- | --- | --- |
| Codex | `AGENTS.md`, project instructions | Skills, tools, plugins, MCP, apps, hooks | validated first adapter | `AGENTS.md -> intent-contract Skill -> capability-router Skill -> tools/Skills/native work -> checkpoints` |
| Claude Code | `CLAUDE.md`, imported files, project memory | Skills, slash commands, hooks | design reference; needs local validation | Import or mirror the core contract through `CLAUDE.md` and use Claude Skills/hooks where available. |
| Cursor | project rules, user rules, repository instructions | rule-triggered workflows and tool use | design reference; needs local validation | Map core invariants into rules; do not assume a Codex-style Skill loader. |
| Windsurf / Cascade | rules, memories, workflows | workflows and tool orchestration | design reference; needs local validation | Use rules for persistent invariants and workflows for repeatable execution checks. |
| Cline | `.clinerules/`, compatible rule files, custom instructions | Skills/plugins/MCP-style tools where available | design reference; needs local validation | Keep the contract in rules and use Skills only when the runtime actually supports them. |
| Roo Code | `.roo/rules/`, `.roorules`, mode-specific rules | modes and tools | design reference; needs local validation | Keep the contract in global or mode-specific rules; adapt reroute checkpoints per mode. |
| GitHub Copilot | repository custom instructions, path-specific instructions, agent instruction files | Copilot coding agent/tooling | design reference; needs local validation | Use repository instructions for the invariant; do not assume explicit Skill selection. |
| Generic LLM / agent | system prompt, project prompt, checklist | none or provider-specific | fallback adapter | Make the contract visible for higher-risk work and use a checklist when no Skill mechanism exists. |

The matrix is intentionally conservative. It records likely carrier surfaces,
not a claim that every provider will auto-load the contract in every product
surface, model version, account state, or conversation.

## Codex reference implementation

The current validated Codex chain is:

```text
AGENTS.md baseline
-> intent-contract Skill
-> capability-router Skill
-> selected capability / Skill / tool / native reasoning
-> execution
-> event-driven intent checkpoints
-> event-driven routing checkpoints
-> verification / handoff
```

This is the reference implementation for the current MVP. It must not be
documented as the only valid implementation.

## Acceptance criteria for future adapters

Before a new agent adapter is described as validated, it should have:

- documented instruction surfaces and load order;
- a minimal installation or configuration path;
- a positive probe or scenario showing the contract is active;
- negative cases showing that simple tasks fast-path and ambiguous tasks ask
  rather than over-act;
- event-driven checkpoint cases, not only first-turn intake cases;
- permission-boundary cases before writes, installs, publishes, account
  connections, memory updates, commits, pushes, deletes, migrations, releases,
  and rollbacks;
- a clear statement of what the adapter cannot prove.

## Public/private boundary

This standard can be public. Runtime-specific private configuration, personal
memory, account state, local paths, credentials, private hooks, and private
project context must stay in the paired private configuration repositories.

Public templates may show placeholders and rules. Private repositories own the
real environment state.

## Source basis

This matrix should be refreshed when provider behavior changes. Current public
reference surfaces include:

- [`AGENTS.md`](https://agents.md/)
- [Claude Code memory docs](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Windsurf Cascade memories and rules](https://docs.windsurf.com/windsurf/cascade/memories)
- [Cline rules](https://docs.cline.bot/features/cline-rules)
- [Roo Code custom instructions](https://docs.roocode.com/features/custom-instructions/)
- [GitHub Copilot repository instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
