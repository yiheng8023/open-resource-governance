# User And Developer Compact

This project is meant to be useful to people who want reusable public resource
governance without giving up control of their private context.

The compact below is not a legal agreement. It is the public operating promise
for this repository: users and contributors should be able to understand what
the project does, what it does not do, how to participate, and what value they
can reasonably expect.

## User sovereignty

Users remain the authority over their private state.

- The public repositories must not require private configuration, private
  bookmarks, memory, credentials, browser history, local paths, account state,
  or personal preferences.
- Public examples should be reusable patterns, not disguised personal data.
- Private overlays remain optional and owner-controlled.
- No automation should install, publish, pay, connect accounts, change visibility, or mutate private state without explicit authorization.
- Users should be able to run validation and inspect the evidence behind public
  claims.

## Output access

Users should be able to find useful outputs without asking the maintainer or
reconstructing the private environment.

- Public hub docs, topology, launch material, and governance explanations live
  in this repository.
- Public bookmark outputs live in `research-bookmarks-public`, including the
  structured source catalog, projection report, and browser-importable HTML.
- Public resource-radar examples live in `resource-radar-public`, including
  schemas, policies, demo resources, and demo reports.
- Public configuration patterns live in template repositories; private
  overlays stay private.
- GitHub Actions validation should make public artifacts reviewable from the
  repository itself.

Ordinary users should not need a local development environment to inspect the
public outputs. Local setup is optional for contributors who want to run checks
before submitting changes.

## Developer rights and expectations

Developers and contributors should have enough information to decide whether
the project is worth their time.

- The README should explain the purpose, scope, value loop, repository map, and
  current MVP status in external-user language.
- Contribution paths should identify safe first issues, naming feedback,
  taxonomy improvements, documentation improvements, validation checks, and
  public/private boundary examples.
- Evidence-backed claims should point to docs, data, scripts, generated
  reports, or verification output.
- Experimental, planned, deferred, private, and approved surfaces should not be
  mixed together.
- Funding, sponsorship, and promotion should not buy approval, ranking,
  inclusion, or exemption from review gates.

## Participation value

Community participation should create shared value without forcing private
state into public.

Contributors can help by:

- making the project easier for first-time users to understand;
- improving taxonomy, repository maps, and lifecycle language;
- adding validation rules that catch stale claims, private-data leaks, or
  boundary drift;
- suggesting better naming while the current project name is temporary;
- proposing public-safe resource lanes or examples without copying restricted
  content;
- reporting confusing claims, missing evidence, or unclear authority
  boundaries.

The value returned to users and contributors is:

- a reusable public/private separation pattern;
- a repeatable evidence-first resource governance loop;
- safer collaboration around resource discovery, bookmarks, curated Skills, and
  AI-configuration templates;
- clearer boundaries between public templates and private overlays;
- a community-readable record of why a resource, claim, or lane was accepted,
  deferred, rejected, or gated.

## Metabolism and renewal

The project should keep improving after publication.

Useful resources decay: links break, repositories move, licenses change,
duplicates appear, better sources emerge, and agent capabilities overlap. The
system should therefore support a visible renewal loop:

```text
observe -> detect drift -> update lifecycle state -> regenerate -> verify -> review -> publish or defer
```

This is the project's metabolism. Automation can find drift, generate reports,
and run checks. Human gates still decide high-impact acceptance, visibility,
funding, promotion, and private-overlay changes.

## Communication and promotion rights

Public communication should help users and developers understand the project
without private context. Launch copy, README text, screenshots, and videos
should answer:

- what public outputs exist;
- where to inspect them on GitHub;
- what is generated and verified by automation;
- what remains a human gate;
- what is still future work or a temporary name.

Promotion should not hide uncertainty behind polished language. If a public
claim cannot be connected to a visible output, a validation result, or a stated
future gate, the claim should be revised before publication.

中文补充：宣传不是只讲愿景，而要让用户知道“现在能看到什么、在哪里看、
自动化验证了什么、哪些仍需人工闸门、哪些只是未来计划”。

## Limits

This repository does not promise complete coverage, production maturity,
security certification, legal advice, monetization readiness, or automatic
approval of community suggestions.

The selected-MVP closeout proves one terminal-consumer loop. Future batches,
future consumers, public-promotion refreshes, and funding activation still need
their own gates and evidence.

## 简体中文摘要

本仓库的基本承诺是：公开部分应该让用户和开发者看得懂、能复查、能参与，
但不能要求用户牺牲自己的私有上下文。

- 用户始终拥有自己的私有配置、记忆、书签、账号状态、本地路径和个人偏好的控制权。
- 公开仓库只承载可复用的规则、模板、证据、验证和公开安全示例。
- 公开产出应能直接在 GitHub 上找到；普通用户查看公开结果不应依赖本地环境。
- 任何安装、发布、付款、账号连接、可见性变更或私有状态变更，都需要明确授权。
- 开发者应该能从 README、贡献指南、仓库地图、验证脚本和证据文档中理解：
  项目做什么、不做什么、现在证明了什么、未来还需要哪些 gate。
- 共建的价值不是把私人材料倒进公开仓库，而是一起改进分类、验证、文档、
  公开/私有边界、命名、资源 lane 和证据链。
- 项目应具备受控新陈代谢能力：观察漂移、更新生命周期、重新生成、验证、
  审查后发布或暂缓。
