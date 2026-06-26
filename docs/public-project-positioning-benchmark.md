# Public Project Positioning Benchmark

This note records the outside-facing benchmark used to rewrite the README and
project narrative. It exists so future copy changes do not drift back into
internal-only audit language.

## Sources checked

- GitHub Docs — [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- GitHub Docs — [Displaying a sponsor button in your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)
- PostHog — [GitHub repository](https://github.com/PostHog/posthog)
- Supabase — [GitHub repository](https://github.com/supabase/supabase)
- Cal.com — [GitHub repository](https://github.com/calcom/cal.com)
- n8n — [GitHub repository](https://github.com/n8n-io/n8n)
- Sentry — [GitHub repository](https://github.com/getsentry/sentry)

These examples are not copied. They are used to calibrate what technically
strong GitHub visitors expect to see before they trust, star, fork, contribute,
or sponsor a project.

## Pattern observed

Successful public projects tend to make five things obvious before deep
architecture:

1. **What it is** — one sentence that names the product or system category.
2. **Why it matters** — the concrete pain or job-to-be-done.
3. **What works now** — screenshots, live artifacts, install commands, demos,
   docs, or proof that the project is not only an idea.
4. **How to start** — the shortest useful path for a new user.
5. **How to trust it** — license, security policy, contribution path, support,
   verification, and boundaries.

Internal audits, governance logs, and launch-gate evidence are useful, but they
should support the story after the user understands the project. They should
not be the first thing a new visitor sees.

## README standard for this repository

The public README should answer these questions in order:

1. What is this project?
2. What problem does it solve?
3. What proof exists today?
4. What can I use immediately?
5. How does the system work?
6. How do I run or inspect it?
7. How do I adapt it for my own workflow?
8. How can I contribute?
9. Why might I support or sponsor it?
10. Where are the deeper governance docs?

## Sponsorship and sustainability lesson

Sponsorship should not be framed as charity for an unclear project. It should
come after demonstrated value:

```text
clear problem
-> working artifact
-> trustworthy boundary
-> contribution surface
-> maintenance cost
-> optional support path
```

For this project, the strongest near-term sponsorship rationale is not access
to private data or a hosted service. It is support for turning private
experiments into public-safe templates, validation, generated artifacts,
examples, and maintainable automation that other people can reuse.

## What this changed

The README was rewritten away from an internal repository-audit sequence and
toward an external user journey:

- temporary name notice;
- visual project card;
- one-minute explanation;
- proof that the bookmark lane already runs end-to-end;
- clear pain points;
- current usable artifacts;
- reproducible value table;
- quick start;
- user journeys;
- contribution and sustainability paths;
- deeper docs moved to a documentation index.

## Anti-patterns to avoid

- Starting with a long list of internal docs before explaining the user value.
- Saying "governance" without showing what is governed.
- Saying "automation" without showing generated artifacts and checks.
- Saying "public/private boundary" without showing why users should care.
- Asking for sponsorship before proving usefulness.
- Overpromising unreleased private lanes as if they were public products.
