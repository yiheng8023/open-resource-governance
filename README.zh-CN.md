# open-resource-governance

[English](README.md) | 简体中文

这是一个公开安全的模块化资源治理体系总入口：发现有价值的公开资源、治理 agent skills、保留可迁移 AI 协作配置、维护书签分类，同时不暴露私有状态。

## 仓库职责

本仓库负责解释体系、映射关联仓库，并提供公开侧文档与推广素材。

它是协调与传播层，不是运行时权威、私有配置仓、书签导出仓或 Skill 发布通道。

## 本仓库提供什么

- 公开安全的资源治理体系概览。
- 发现、精选 Skills、配置模板、书签目录之间的仓库地图。
- 共享的公开/私有边界规则。
- 许可证与贡献约定。
- 可用于 GitHub profile、仓库简介和社媒的免费推广文案。
- 分阶段公开发布所需的收官审计与发布闸门证据。

## 本仓库不负责什么

- 私有用户配置、记忆、凭据、本机路径、账号状态或偏好。
- 私有浏览器书签或浏览历史。
- 精选 Skill release manifest 或 Skill 正文。
- 资源评分数据库或发现快照。
- 运行时安装、账号授权或外部服务状态。

## 体系地图

```text
open-resource-governance
  -> 公开安全总入口、地图、文档、推广素材

resource-radar
  -> 发现、归一化、评分、去重和报告公开资源

agent-skills-curated
  -> 治理已审查 Skill 正文、来源、安全、拓扑、冲突和 release manifest

codex-user-config-template
  -> 私有 AI 协作配置仓的公开安全模板

research-bookmarks-public
  -> 公开安全官方来源书签分类与来源目录

private overlays
  -> 真实用户配置、记忆、书签、偏好和运行时状态
```

## 与私有仓库的关系

采用公开核心 + 私有 overlay。公开仓承载可复用结构、策略、验证、示例和官方/公开安全来源；私有仓承载个人数据、偏好、账号状态、运行时细节和完整本地工作流。

私有到公开必须经过脱敏闸门。不要把私有仓直接镜像到公开仓。

## 验证方式

运行：

```bash
python -B scripts/verify.py
```

GitHub Actions 会在 pull request 和推送到 `main` 时运行同样的验证。

关键文档：

- [`docs/repository-map.md`](docs/repository-map.md) — 仓库角色与关系。
- [`docs/public-private-boundary.md`](docs/public-private-boundary.md) — 公开/私有安全边界。
- [`docs/public-launch-gates.md`](docs/public-launch-gates.md) — 公开发布前必须通过的闸门。
- [`docs/pre-public-safety-audit.md`](docs/pre-public-safety-audit.md) — 改可见性前的具体安全审计。
- [`docs/pre-public-readiness-2026-06-26.md`](docs/pre-public-readiness-2026-06-26.md) — 总入口仓最新公开前 readiness 证据。
- [`docs/free-promotion-playbook.md`](docs/free-promotion-playbook.md) — 免费渠道首发与推广 runbook。
- [`docs/community-feedback-model.md`](docs/community-feedback-model.md) — 未来公开协作的安全 issue/PR 反馈模型。
- [`GOVERNANCE.md`](GOVERNANCE.md) — 轻量维护者与 owner gate 模型。
- [`SUPPORT.md`](SUPPORT.md) — 支持边界与安全联系路径。
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — 公开安全协作期望。
- [`docs/closeout-audit-2026-06-26.md`](docs/closeout-audit-2026-06-26.md) — 最新分阶段收官审计。
- [`docs/promotion-kit.md`](docs/promotion-kit.md) — 免费渠道推广文案草案。

## 更新规则

1. 保持总入口公开安全。
2. 优先模块化仓库边界，不做巨型一体化系统。
3. 能共享的规则、schema、分类、文档和验证就共享。
4. 私有状态留在私有 overlay。
5. 公开发布作为单独 release gate。

## 安全边界

本仓库未来可以公开。公开前必须确认不包含私有配置、私有书签、记忆、凭据、本机路径、账号状态、个人偏好或第三方受限内容。
