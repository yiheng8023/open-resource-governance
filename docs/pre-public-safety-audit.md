# Pre-Public Safety Audit

Run this audit immediately before changing repository visibility to public.

## 1. Scope confirmation

Confirm the repository is intended to be public.

For this repository family:

- `open-resource-governance`: public candidate first.
- `codex-user-config-template`: public candidate after template review.
- `research-bookmarks-public`: public candidate after source-policy review.
- `resource-radar`: public candidate after generated outputs and source records are reviewed.
- `agent-skills-curated`: public candidate only after third-party redistribution boundaries are confirmed.
- private overlays: not public candidates by default.

## 2. File inventory

Review the file tree for risky classes:

- credentials or account state;
- raw memory snapshots;
- raw conversations;
- browser exports;
- local runtime logs;
- cache files;
- database files;
- local machine paths;
- private notes or subjective preferences;
- third-party content bodies without redistribution permission.

## 3. Secret scan

At minimum, run the repository verification command.

For stronger review, also use a dedicated secret scanner before publication.
If a scanner finds anything unclear, stop and review manually.

## 4. License review

Confirm:

- `LICENSE` exists;
- `NOTICE` exists;
- license-policy documentation exists when content is mixed;
- third-party resources are linked or referenced instead of copied unless
  redistribution is permitted;
- generated outputs do not embed restricted source content.

## 5. Relationship review

Confirm the repository does not claim another repository's authority.

Examples:

- the hub does not own radar scoring;
- radar does not approve curated Skills;
- curated Skills do not install into live user environments;
- configuration templates are not real private configuration;
- bookmark-public is not a full browser export.

## 6. Verification evidence

Record:

- verification command;
- result;
- target branch;
- commit or main revision;
- GitHub Actions run if available.

Do not use an old green check as evidence for a newer commit.

## 7. Publication step

Only after the above gates pass should the owner change visibility.

Changing visibility is an owner decision. It must not happen as a side effect
of a documentation update, validation run, or automation test.

## 8. Post-public check

After publication:

1. open the public URL in a logged-out or private browser context;
2. confirm README rendering;
3. confirm no private files are visible;
4. confirm Actions status;
5. confirm repository topics;
6. pin only if the public page looks correct.
