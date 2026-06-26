# Owner Launch Decision Packet

This packet is the final owner-controlled handoff before any public launch or
free-channel promotion. It is not an instruction for automation to change
visibility, enable funding, pin repositories, or publish social posts.

## Current launch posture

| Field | Value |
| --- | --- |
| Repository | `yiheng8023/open-resource-governance` |
| Target branch | `main` |
| Launch target | current `main` containing this packet |
| Verified pre-packet baseline | `c50ac77be6c3f5d8b83d28bce526069f95706981` |
| Current visibility | private |
| Launch state | owner gate pending |

The revision above was the last verified pre-public hub revision before this
packet was added. This packet intentionally changes the next `main` revision.
Re-run verification and re-check the exact current main revision immediately
before changing visibility.

## Non-negotiable owner confirmation

Changing a repository from private to public is externally visible and cannot
be treated as a routine documentation or validation side effect. Public
exposure may be copied, indexed, cached, or linked by others.

Before making the hub public, the owner should explicitly confirm this exact
intent in the active execution context:

```text
Make yiheng8023/open-resource-governance public now.
```

Do not interpret general readiness language, closeout language, or promotion
planning as this confirmation.

## Final pre-public checklist

Run this checklist on the exact target revision:

1. Confirm `git status --short --branch` is clean on `main`.
2. Confirm `git rev-parse HEAD` is the intended target revision.
3. Run `python -B scripts/verify.py`.
4. Confirm GitHub Actions is green for the target revision.
5. Re-read `docs/pre-public-safety-audit.md`.
6. Confirm no private configuration, memory, bookmark export, credential,
   local path, account state, personal preference, or restricted third-party
   content exists in the repository.
7. Confirm the GitHub repository still has the intended topics.
8. Confirm downstream repositories remain private unless separately approved.

## Launch sequence after confirmation

1. Change only `open-resource-governance` visibility first.
2. Open the public repository URL in a logged-out or private browser context.
3. Confirm README rendering, file tree, Actions status, topics, and issue
   templates.
4. Pin the hub on the GitHub profile only after the public page looks correct.
5. Use `docs/promotion-kit.md` or `docs/free-promotion-playbook.md` for the
   first free-channel message.
6. Publish downstream repositories one at a time only after each passes its own
   public launch gates.

## Do not do during first launch

- Do not make every related repository public in one batch.
- Do not publish private overlays.
- Do not enable funding links as a side effect of the visibility change.
- Do not claim production maturity, full automation, legal approval, security
  certification, or complete resource coverage.
- Do not import third-party bodies or private bookmark exports during launch.

## First post-public verification

After the hub becomes public, record:

- public URL;
- target revision;
- verification command and result;
- GitHub Actions URL;
- logged-out/private-browser README check result;
- whether the repository was pinned;
- whether any social post was published.

Keep the first launch small. The success condition is a clean public-safe hub,
not maximum exposure on day one.
