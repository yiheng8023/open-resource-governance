# Community Feedback Model

This repository is designed for public-safe collaboration. Feedback should
improve reusable structure without exposing private overlays or weakening
owner-controlled release gates.

## Feedback goals

Useful feedback should improve:

- repository role clarity;
- public/private boundaries;
- resource-governance architecture;
- launch gates;
- validation;
- promotion material;
- naming clarity while YIYUAN Meridian uses the `open-resource-governance`
  repository slug;
- contribution safety.

## Feedback channels

Use issue templates for:

- boundary questions;
- public-safe resource lane suggestions;
- documentation improvements.
- name suggestions.

Use pull requests for:

- public-safe documentation changes;
- validation improvements;
- repository map corrections;
- promotion or onboarding improvements.

Do not use public issues or PRs for:

- secrets, tokens, cookies, OAuth, credentials, or account state;
- private configuration;
- private bookmarks or raw browser exports;
- personal memory snapshots or raw conversations;
- local machine paths;
- runtime logs or caches;
- copied third-party content bodies without redistribution permission.

## Triage labels

Recommended labels:

- `boundary`
- `question`
- `resource-lane`
- `suggestion`
- `documentation`
- `naming`
- `safety`
- `needs-owner-decision`
- `private-overlay`
- `not-public-safe`

These labels are intended to exist as repository metadata so issue templates can
route feedback cleanly during early community participation.

## Response policy

If a public issue appears to contain private state:

1. stop discussing the sensitive details publicly;
2. ask the reporter to remove or rotate affected information where applicable;
3. move security-sensitive concerns to a private advisory channel when possible;
4. do not quote the sensitive content in follow-up comments.

If a suggestion belongs to a downstream repository, classify it as a downstream
lane and do not silently change this hub's authority.

## Owner gates

The following remain owner-controlled:

- changing repository visibility;
- enabling funding links;
- pinning repositories on a profile;
- publishing social posts;
- opening Discussions;
- adding maintainers or automation with write access.
