# Project Design And User Value

`open-resource-governance` is a temporary project name. The name may change
after public feedback, but the design problem is stable: how can one person or
small team collect useful resources, keep private state private, publish useful
public artifacts, and let others improve the system without turning everything
into an unreviewed pile?

## External user perspective

A new visitor should be able to answer five questions quickly:

1. What is this?
2. What problem does it solve?
3. What can I use right now?
4. How does it avoid leaking private data?
5. Why should I contribute, star, share, or sponsor it?

This repository is the public answer to those questions. The private
repositories and automation lanes are implementation details until they are
public-safe enough for reuse.

## Product thesis

Modern AI-assisted work creates a new kind of personal infrastructure:

- browser bookmarks;
- GitHub stars and lists;
- useful repositories;
- prompts and agent skills;
- local configuration;
- memory snapshots;
- automation scripts;
- review notes and release evidence.

Without governance, this becomes private clutter. With reckless automation, it
becomes public noise. The project tries to keep the useful middle:

```text
enough structure to be reusable
enough automation to stay fresh
enough human review to stay safe
enough modularity to avoid a giant fragile system
```

## Core value loops

### 1. Public/private resource loop

```text
private complete source
-> structured candidate records
-> public/private classification
-> public-safe projection
-> deterministic export
-> verification
-> publish
```

Example: a full private browser bookmark import can become a smaller public
bookmark catalog and generated browser-importable HTML without exposing
private-only entries.

### 2. Discovery and renewal loop

```text
source discovery
-> normalization
-> quality signals
-> deduplication
-> lifecycle state
-> human review
-> downstream lane decision
```

This is the planned `resource-radar` role. It should not blindly collect
everything. It should help humans see better candidates with evidence.

The public template for this lane is now `resource-radar-public`: it exposes a
public-safe schema, demo fixtures, scoring/lifecycle examples, deterministic
demo reports, and validation without publishing the private candidate pool.

### 3. Curated skill loop

```text
candidate skill source
-> license and provenance check
-> safety and portability review
-> overlap and conflict review
-> adaptation or rejection
-> release manifest
-> consumer install path
```

This is the planned `agent-skills-curated` role. It is intentionally slower
than raw discovery because executable agent behavior needs stronger gates.

### 4. Portable configuration loop

```text
public template
-> private overlay
-> local verification
-> reviewed memory or config snapshot
-> private backup
-> future restore
```

This keeps reusable configuration ideas separate from personal preferences,
account state, credentials, local paths, and memory. The loop applies per agent:

| Agent | Private source | Public template |
| --- | --- | --- |
| Codex | `codex-user-config` | `codex-user-config-template` |
| Claude Code | `claude-user-config` | `claude-user-config-template` |

## Why separate repositories?

The system is split because each lane has different trust and release rules:

| Lane | Public value | Private risk |
| --- | --- | --- |
| Hub | Explains the system and shared rules | Low, if kept generic |
| Bookmarks | Public-safe catalog and browser HTML | Raw browser export may reveal personal behavior |
| Resource radar | Discovery and scoring patterns | Candidate data may include noisy or unreviewed sources |
| Curated skills | Reusable reviewed agent workflows | Skill content can affect execution behavior |
| Config templates | Portable setup pattern for Codex and Claude | Real user config and memory are private |

One giant repository would make these boundaries harder to review. Modular
repositories make the trust boundary visible.

## What makes this different from a list of links?

A plain list answers: "What links did someone collect?"

This system tries to answer:

- where did the item come from?
- why is it in this lane?
- is it public-safe?
- is it official, community, private-only, local-only, or low-trust fallback?
- can it be regenerated deterministically?
- what validation prevents accidental exposure?
- which downstream lane should consume it?
- when should it be reviewed again?

That extra structure is the difference between a bookmark pile and a governed
resource system.

## What can users build from this?

Users can copy the pattern and build:

- a public-safe bookmark catalog generated from private browser exports;
- a personal research resource map with public and private layers;
- a curated GitHub discovery pipeline with human review gates;
- a public-safe resource-radar template for broad resource discovery, scoring,
  lifecycle tracking, and downstream projections;
- a reusable agent-skill intake and release workflow;
- a portable AI-collaboration configuration template;
- a small-team knowledge governance system with automation but without
  accidental private-data leakage.

## Contribution surface

Useful contributions do not need to be huge. Good contributions include:

- clearer first-time-user docs;
- taxonomy improvements;
- validation rules that catch privacy mistakes;
- safer examples for public/private splitting;
- resource-source policy improvements;
- benchmark ideas for resource quality signals;
- naming suggestions while the project name is temporary;
- issue templates and review checklists;
- generated artifact usability improvements.

## Sponsorship rationale

The project is public-good infrastructure rather than a hosted SaaS. Sponsorship
would help cover:

- maintainer time for public-safe declassification and documentation;
- GitHub Actions and future automation costs;
- API or data costs if broader resource discovery is added;
- examples, tutorials, screenshots, and launch videos;
- review bandwidth for community suggestions.

The immediate return for sponsors is not account access or private data. The
return is a better public toolkit that more people can reuse.

## Anti-goals

This project should not become:

- a dump of someone's private bookmarks;
- a scraped content mirror;
- a repository that claims commercial license safety without review;
- an automatic installer for arbitrary third-party agent code;
- a single monorepo that hides trust boundaries;
- a popularity-only ranking system;
- a place where automation publishes without human gates.

## Current maturity

As of the current public launch stage:

- the hub is public;
- the bookmark public projection is public;
- the full private bookmark source remains private;
- `resource-radar-public` is public as the reusable resource-radar template;
- `resource-radar` remains the private-source lane for real candidate pools and
  account-coupled automation;
- curated skills remain a staged/private-pre-public lane;
- Codex and Claude configuration templates are the public-safe way to share
  portable setup patterns without exposing private configuration sources.

Outside the user-configuration lane, the system should remain agent-neutral and
tool-neutral. Resource discovery, bookmarks, curated skills, schemas,
validation, and topology should be reusable beyond Codex, Claude, or any single
runtime.

The project is useful now as a reference pattern and public bookmark lane. It is
not yet a complete packaged product.

## 中文摘要

这个项目的重点不是“收集很多链接”，而是把资源、书签、Skills、AI 协作配置
变成一套可治理、可验证、可公开协作、又不泄露隐私的系统。它的核心价值闭环是：

```text
收集 -> 结构化 -> 过滤 -> 生成 -> 验证 -> 审查 -> 发布 -> 更新
```

用户可以复刻这套模式来搭建自己的公开/私有书签系统、资源发现雷达、
curated skills 治理流程或 AI 协作配置模板。仓库拆分不是复杂化，而是为了让
不同 trust boundary 清晰可见：公开核心放规则和投影，私有 overlay 放个人状态。
