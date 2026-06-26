# Governance

This repository is maintained by the owner as a public-safe hub. Governance is
intentionally lightweight until community participation justifies more
structure.

## Authority model

- The owner controls funding links, profile pinning, social posts, maintainer
  access, downstream repository visibility, and public launch timing for each
  related repository.
- This hub explains the repository family but does not own downstream runtime
  state, private overlays, resource-radar scoring, or curated Skill release
  decisions.
- Downstream repositories keep their own authority boundaries.

## Decision types

| Decision | Authority |
| --- | --- |
| Documentation clarification | Maintainer review |
| Repository map correction | Maintainer review |
| Public/private boundary change | Owner review |
| Launch gate change | Owner review |
| Funding or promotion change | Owner review |
| Downstream repository visibility change | Owner only |
| Maintainer access | Owner only |

## Contribution flow

1. Use the issue templates for public-safe questions or suggestions.
2. Use pull requests for bounded documentation, validation, or map changes.
3. Keep private overlays and sensitive material out of public issues and PRs.
4. Run `python -B scripts/verify.py` before requesting review.

## Evolution

If the project grows, governance may add:

- maintainer roles;
- review SLAs;
- release cadence;
- security response process;
- public roadmap labels;
- community moderation rules.

Until then, the owner gate remains the final authority for safety-sensitive,
visibility-changing, or externally visible actions.
