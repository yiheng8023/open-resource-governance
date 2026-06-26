# Bookmark Lane Closeout — 2026-06-26

## Decision

The bookmark lane is split into two repositories:

```text
research-bookmarks
  -> private canonical source for complete browser imports, overlays, audits, and declassification inputs

research-bookmarks-public
  -> public-safe structured source catalog and generated browser-importable bookmark HTML

resource-radar
  -> discovery, scoring, lifecycle, summaries, and broader projections
```

`resource-radar` can consume filtered bookmark inputs, but it does not own raw private bookmark truth.

## Current Evidence

`research-bookmarks`:

- visibility: private;
- imported baseline: 389 private links, 95 folders;
- validation:
  - `python -B scripts/verify.py`
  - `python -B scripts/simulate_user_flow.py`
- GitHub Actions: `validate` succeeded on `main`.

`research-bookmarks-public`:

- visibility: public;
- public projection: 328 public-safe links, 44 bookmark folders;
- validation:
  - `python -B scripts/build_public_bookmarks.py`
  - `python -B scripts/verify.py`
  - `python -B scripts/simulate_user_flow.py`
- GitHub Actions: `validate` succeeded on pull request and `main`.

`resource-radar`:

- bookmark exporter check: `python -B scripts/export_bookmarks.py --check`;
- bookmark projection test: `python -B tests/test_bookmark_projection.py`;
- repository verify: `python -B scripts/verify.py`;
- full script-style tests: every `tests/test_*.py` passed.

## Boundary

- Complete raw bookmark imports stay private.
- Public HTML is generated from structured public-safe data.
- The generated HTML is a user-facing artifact, not the long-term source of truth.
- Future automated replenishment should flow through structured records and exporter checks.
- Private-to-public promotion requires filtering, review, regeneration, and verification.

