# Security Policy

Do not disclose private configuration, secrets, memory, bookmarks, account
details, local paths, browser/session data, or other sensitive material in
public issues, pull requests, discussions, screenshots, logs, or examples.

## Supported scope

This repository is a public-safe governance hub. Security reports are in scope
when they affect:

- repository validation scripts;
- GitHub Actions workflows;
- issue or pull request templates;
- public/private boundary rules;
- documentation that could cause contributors to disclose sensitive data;
- automation or governance guidance that could weaken safety gates.

Downstream repositories keep their own security boundaries and release gates.
If a report belongs downstream, describe the affected repository or lane without
copying private content into this hub.

## Reporting a vulnerability or private-data exposure

Use GitHub security advisories when available. If advisories are unavailable,
contact the repository owner privately through an owner-controlled channel.
Public-safe contact routes are listed in `docs/contact-and-social.md`.

When reporting:

- describe the affected file, workflow, or rule;
- explain the impact and reproduction path at a high level;
- omit credentials, tokens, cookies, OAuth material, private configuration,
  memory snapshots, personal bookmarks, account state, or local machine paths;
- include a public-safe minimal example if one is needed.

## Public issues are not for sensitive reports

If a public issue or pull request accidentally includes sensitive material:

1. stop discussing the sensitive content publicly;
2. remove or redact the material where possible;
3. rotate or revoke affected credentials or sessions if applicable;
4. move the remaining discussion to a private reporting path.

## Response expectations

This is an owner-maintained early public project. Response is best effort and
may not follow a formal service-level agreement. The maintainer will prioritize
reports that protect public/private boundaries, repository automation, and
contributors from accidental disclosure.

## Out of scope

- Requests for legal advice or security certification.
- Vulnerabilities in unrelated third-party services.
- Social engineering, spam, or speculative reports without a concrete affected
  file, workflow, or rule.
- Reports that require exposing private overlays or personal data to reproduce.
