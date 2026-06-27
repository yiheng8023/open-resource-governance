# Launch Video Brief

This brief supports a lightweight first announcement video for
`open-resource-governance`, which is a provisional repository slug and
temporary project name. It is intentionally simple, public-safe, and usable with
video-generation tools, manual screen recording, or a basic slide editor.

## Current use boundary

This is a prepared draft, not a release approval and not a publication
instruction. The selected-MVP global closeout has passed, so the brief can now
support an owner-approved publication draft. Broad social/video publication
still remains a separate owner-controlled gate with final claim review. Any
claim beyond the selected Skills MVP requires a fresh public-refresh gate.

Do not use this brief to claim that the Skills MVP is complete, that
release/routing is approved, or that downstream repositories are generally
available.

## Goal

Explain the project in plain language:

> A public-safe map and governance hub for reusable resource discovery, curated
> agent skills, portable AI-collaboration configuration, and bookmark
> taxonomies, while keeping private state private.

The video should also make the practical value visible: public outputs live on
GitHub, ordinary users can inspect them without a local setup, GitHub-native
automation validates the artifacts, and the system has a controlled renewal
loop for stale, duplicated, or superseded resources.

## Naming note

The repository slug is governance-accurate but abstract. For public messaging,
lead with a plain subtitle before the formal name:

> A public-safe map for useful resources, agent skills, AI collaboration
> configuration, and bookmark taxonomies.

Then name the repository as `open-resource-governance` for people who want to
find or star it on GitHub. State clearly that the name is temporary and may
change after public naming feedback.

## Recommended format

- Length: 15-45 seconds.
- Shape: 16:9 for YouTube or GitHub demos; 9:16 for Shorts, X, Weibo, and
  mobile-first reposts.
- Style: calm technical walkthrough, not hype.
- Visual source: GitHub repository page, README sections, repository map, and
  public/private boundary diagrams.
- Must show or mention: where public outputs live, GitHub Actions validation,
  cloud-first automation, and controlled renewal.
- Avoid: real people, private paths, credentials, browser history, private
  bookmarks, account state, paid-feature claims, production-grade claims, or
  certification claims.

## Recommended source assets

Text-only prompts are enough for a first generated clip, but a small controlled
asset pack will make the result more accurate and less generic.

Prepare only public-safe assets:

- screenshot of the public GitHub repository landing page;
- screenshot of the README section that explains the repository map;
- screenshot or simple slide for `Public core -> Private overlays`;
- screenshot of the GitHub Actions verification success, with no private tabs,
  tokens, local paths, or account-sensitive browser state visible;
- optional square project card with the title `Open Resource Governance` and
  the subtitle `Public core. Private overlays. Verifiable automation.`;
- optional 16:9 and 9:16 title cards for social reposting.

Do not use screenshots that reveal private browser bookmarks, logged-in account
menus, local machine paths, private repositories, private issues, tokens,
emails outside the intentional public contact email, or personal messages.

If no source assets are available, use the text prompt below and keep the video
abstract: repository cards, lanes, boundary lines, and verification accents.

Prepared assets are listed in
[`launch-video-assets.md`](launch-video-assets.md). Use that file as the
handoff packet for video-generation or editing tools.

## Captions, music, and marks

Use captions. Short videos are often watched muted, and captions also make the
message easier to reuse across X, Weibo, YouTube Shorts, and other feeds.

Music is optional. If used, prefer low-volume royalty-free ambient, soft lo-fi,
or light documentary synth with no vocals. Avoid copyrighted tracks and keep
the license/source note with the final export.

Use the temporary project name as a text wordmark. Do not use `®` or imply
registered trademark status unless registration is complete. If a project logo
is added later, confirm it is intended for public project use before including
it in generated assets.

## 30-second storyboard

1. **Problem, 0-5s**  
   Useful resources, agent skills, bookmarks, and AI configuration become messy
   when public structure and private state mix together.

2. **Principle, 5-10s**  
   Keep a public core and private overlays.

3. **System map, 10-20s**  
   Show the hub, resource radar, curated skills governance, configuration
   template, bookmark taxonomy, and private overlays as separate lanes. Point to
   GitHub-visible outputs such as bookmark HTML, projection reports, demo radar
   reports, and public templates.

4. **Safety, 20-25s**  
   Release gates, validation, security policy, contribution rules, and
   public/private boundaries protect the system. Mention that GitHub Actions
   validates artifacts and that stale or superseded resources can be renewed,
   merged, retired, or rejected.

5. **Call to action, 25-30s**  
   Visit the repository, read the map, and suggest public-safe improvements.

## Voiceover draft

```text
Open Resource Governance is the temporary name for a small public-safe hub for a bigger idea:
useful resources, agent skills, AI collaboration configuration, and bookmark
taxonomies should be reusable without leaking private state.

The model is simple: public core, private overlays, clear release gates, and
cloud-first verifiable automation.

Public outputs are visible on GitHub, from generated bookmark HTML to
resource-radar demo reports and public configuration templates. Ordinary users
can inspect them without a local setup.

The system is designed to keep renewing itself: detect stale links, duplicates,
license drift, and better sources; then update, merge, retire, or reject through
review gates.

This repository maps the lanes, explains the boundaries, and gives contributors
a safe place to improve the system. The name may change after public naming feedback.
```

## Chinese voiceover draft

```text
Open Resource Governance 是这个项目的暂定名。它是一个公开安全的总入口，用来承载一个更大的想法：
有价值的资源、agent skills、AI 协作配置和书签分类，应该可以复用，
但不能泄露私人状态。

核心模型很简单：公开核心，私有 overlay，清晰发布闸门，云端优先的可验证自动化。

公开产物可以直接在 GitHub 上查看，包括生成的书签 HTML、资源雷达 demo 报告和公开配置模板。
普通用户不需要本地环境也能检查这些结果。

系统还要持续新陈代谢：发现坏链、重复、许可漂移和更优来源，再通过审查闸门更新、合并、退役或拒绝。

这个仓库负责解释各条链路、边界和贡献方式，让后续协作更安全。名称未来可能根据公开征名反馈变更。
```

## Video AI prompt

```text
Create a clean 30-second technical launch video for an open-source GitHub
project currently using the temporary name "Open Resource Governance". Make it
clear that the name is provisional and may change after public naming feedback.

Use case: public-safe explainer draft and announcement candidate for GitHub, X,
Weibo, and YouTube Shorts.
Scene/background: minimal dark-mode developer workspace with abstract repository
cards, diagrams, and public/private boundary lines. No real people.
Subject: a modular open-source governance hub that connects resource discovery,
curated agent skills, portable AI collaboration configuration, and bookmark
taxonomy.
Action: show messy resources becoming organized into separate public-safe lanes:
hub, resource radar, curated skills governance, config template, bookmark
taxonomy, and private overlays. Show GitHub-visible outputs, GitHub Actions
validation, and a renewal loop that updates, merges, retires, or rejects stale
resources.
Camera: smooth screen-recording inspired motion, slow zooms, simple diagram
transitions.
Lighting/mood: calm, trustworthy, technical, low-hype.
Color palette: dark background, soft blue, green verification accents, warm
white text.
Style/format: modern GitHub/open-source explainer, clean typography, no brand
logos except generic repository-card shapes.
Timing/beats: problem 0-5s, principle 5-10s, system map 10-20s, safety gates
20-25s, call to action 25-30s.
Text:
"Public core"
"Private overlays"
"Release gates"
"Verifiable automation"
"GitHub outputs"
"Renew stale resources"
"Open Resource Governance (temporary name)"
Constraints: no real people, no private data, no credentials, no account pages,
no browser history, no exaggerated claims, no security certification claims, no
claim that the temporary name is final.
Avoid: hype, fake dashboards, noisy cyber visuals, corporate stock footage.
```

## Short launch captions

English:

```text
I just opened Open Resource Governance (temporary name):
a public-safe hub for resource discovery, curated agent skills, portable AI
collaboration configuration, and bookmark taxonomy.

Principle: public core, private overlays, release gates, verifiable automation.
Public outputs live on GitHub, and ordinary users can inspect them without local
setup. The goal is controlled renewal, not a one-time resource dump.
The name may change after public naming feedback.
```

Optional link line:

```text
GitHub: https://github.com/yiheng8023/open-resource-governance
```

Optional contact line:

```text
Contact: https://github.com/yiheng8023/open-resource-governance/blob/main/docs/contact-and-social.md
```

Chinese:

```text
我刚公开了 Open Resource Governance（暂定名）：
一个公开安全的总入口，用来治理资源发现、精选 agent skills、AI 协作配置模板和书签分类。

原则：公开核心，私有 overlay，发布闸门，可验证自动化。
公开产物在 GitHub 上可直接查看，普通用户不需要本地环境。
目标不是一次性资源堆砌，而是受控新陈代谢。
名称未来可能根据公开征名反馈变更。
```

可选链接行：

```text
GitHub: https://github.com/yiheng8023/open-resource-governance
```

可选联系入口：

```text
联系方式: https://github.com/yiheng8023/open-resource-governance/blob/main/docs/contact-and-social.md
```
