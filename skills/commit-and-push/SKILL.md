---
name: commit-and-push
description: Use when the user asks to commit, push, stage changes, save work to git, make a checkpoint, publish a branch, or prepare commits; inspect status and diffs, run semantic-versioning as a pre-commit gate, stage deliberately, review the staged diff for scope, secrets, generated files, and binaries, verify when appropriate, commit in logical groups, and confirm the pushed remote ref.
---

# Commit And Push

Use this skill when preparing, committing, or pushing Git changes.

## Workflow

1. Inspect repository state before changing Git state:
   - `git status --short`
   - `git branch --show-current`
   - relevant `git diff` or `git diff --stat`
2. Identify user changes versus agent changes. Never discard, overwrite, or hide unrelated user work.
3. Use `$semantic-versioning` as the first decision gate before staging:
   - Require an explicit `RELEASE` or `REGULAR` decision supported by the repo's version source, release convention, latest tag, accumulated changes, and intended push boundary.
   - For `RELEASE`, let `semantic-versioning` choose the bump, prepare the version and changelog edits, and run release checks. Ask only when the release target, package scope, or bump is materially ambiguous.
   - For `REGULAR`, leave versions, changelogs, and tags untouched.
   - Never create or push a tag without the separate approvals required by `$semantic-versioning`.
4. Decide whether changes belong in one commit or multiple focused commits. Keep unrelated work out of a release commit.
5. Stage files deliberately by path. Do not use `git add .` unless the user explicitly asks and the diff has been reviewed.
6. Review the exact staged commit before committing:
   - Run `git diff --cached --check`.
   - Inspect `git diff --cached --stat` and the complete relevant `git diff --cached`.
   - Confirm staged paths match the intended commit and exclude unrelated work, secrets, credentials, caches, generated files, exports, and unexpected binaries.
7. Run relevant verification before committing when changes affect behavior, builds, docs commands, generated outputs, tests, or release metadata.
8. Write a concise commit message that reflects the staged diff.
9. After committing, confirm the commit hash and `git status --short`.
10. Push only to the intended branch and remote. If upstream is missing, use `git push -u origin <branch>` after confirming the branch name is appropriate.
11. Read the push result and confirm the local commit matches the intended upstream tracking ref before claiming success.
12. Report commit hash, branch, remote, verification run, staged-diff review, upstream confirmation, and any uncommitted files left behind.

## Commit Message Defaults

Prefer short imperative messages:

- `Add solo dev documentation skill`
- `Fix CSV report upload validation`
- `Update attendance workbook generation`
- `Release v1.4.0`

Use conventional commit prefixes only when the repo already uses them or the user asks.

## Push Safety

Before pushing:

- Confirm the current branch is not unexpected.
- Check whether the branch is protected or shared when that is visible.
- Confirm the remote and upstream ref are the intended destination before pushing.
- Do not force-push unless the user explicitly asks and the risk is stated.
- If push fails because the remote is ahead, stop and report the divergence; do not auto-rebase unless requested.

## Output Contract

Final response must include:

- Commit hash and message.
- Branch and remote pushed.
- Staged-diff review and upstream-ref confirmation.
- Verification run and result.
- Files intentionally left uncommitted, if any.
- Push status or blocker.
- SemVer gate decision (`RELEASE` or `REGULAR`) and concise evidence.
- For `RELEASE`, the previous and next version, version and changelog files changed, and tag status.

## Anti-Patterns

- Running `git add .` before reviewing changes.
- Committing without reading the staged diff.
- Combining unrelated work into one commit.
- Committing generated/cache files accidentally.
- Staging credentials, secrets, private exports, or unexpected binaries.
- Skipping the SemVer gate because the user did not explicitly say "release."
- Treating a possible SemVer classification as proof that a release is necessary now.
- Bumping a version from vibes instead of repository and change evidence.
- Claiming push succeeded without reading command output.
- Claiming the remote is updated without confirming the upstream ref.
- Force-pushing as a convenience.
