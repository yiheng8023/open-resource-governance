# Contributing

Contributions should improve the public-safe system map, documentation,
validation, repository relationship model, launch gates, community feedback
model, or promotion material.

Before contributing, read `docs/user-developer-compact.md`. It explains user
sovereignty, developer expectations, participation value, and the limits of the
current selected-MVP closeout.

Do not contribute private configuration, memory, bookmarks, browsing history,
account state, credentials, local paths, private notes, or personal preferences.

## Good first contribution areas

- Clarify repository roles and boundaries.
- Improve public/private safety rules.
- Improve validation checks.
- Improve issue templates, pull request guidance, or documentation structure.
- Suggest public-safe resource lanes without copying restricted content.
- Improve promotion copy while keeping claims evidence-based.

## Not accepted here

- Private overlays or personal runtime state.
- Raw browser exports or personal bookmark dumps.
- Credentials, tokens, cookies, OAuth material, or account state.
- Third-party content bodies without clear redistribution permission.
- Large automation changes that add write access, external service calls, or
  dependency risk without prior maintainer discussion.
- Claims of production maturity, security certification, legal advice, or
  complete resource coverage that are not supported by repository evidence.

## Issue routing

Use issues for public-safe questions, documentation gaps, repository-boundary
questions, and resource-lane suggestions. If the topic contains sensitive
material, do not open a public issue; use the security/private reporting path in
`SECURITY.md`.

If a suggestion belongs to a downstream repository, describe the downstream lane
instead of trying to make this hub own that repository's authority.

## Pull request flow

1. Keep the change small and public-safe.
2. Explain which repository boundary, document, validation rule, or launch gate
   the change improves.
3. Include provenance for external material and prefer links or summaries over
   copying full third-party content.
4. Run validation before requesting review.
5. Expect maintainer review for boundary, safety, visibility, funding,
   promotion, or automation changes.

## Pull request checklist

- [ ] The change is public-safe.
- [ ] Repository boundaries remain clear.
- [ ] Private-to-public promotion rules are not weakened.
- [ ] License and provenance are clear.
- [ ] `python -B scripts/verify.py` passes.

For issue and pull request routing, see `docs/community-feedback-model.md`.
