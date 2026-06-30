---
name: commit-and-push
description: Use when the user asks to commit, push, stage changes, save work to git, make a checkpoint, publish a branch, or prepare commits; inspect status and diffs first, stage deliberately, avoid `git add .`, verify when appropriate, commit in logical groups, and push safely to the intended remote branch.
---

# Commit And Push

Use this skill when preparing, committing, or pushing Git changes.

## Workflow

1. Inspect repository state before changing Git state:
   - `git status --short`
   - `git branch --show-current`
   - relevant `git diff` or `git diff --stat`
2. Identify user changes versus agent changes. Never discard, overwrite, or hide unrelated user work.
3. Decide whether changes belong in one commit or multiple focused commits.
4. Stage files deliberately by path. Do not use `git add .` unless the user explicitly asks and the diff has been reviewed.
5. Run relevant verification before committing when changes affect behavior, builds, docs commands, generated outputs, or tests.
6. Write a concise commit message that reflects the actual diff.
7. After committing, confirm `git status --short`.
8. Push only to the intended branch and remote. If upstream is missing, use `git push -u origin <branch>` after confirming the branch name is appropriate.
9. Report commit hash, branch, remote, verification run, and any uncommitted files left behind.

## Commit Message Defaults

Prefer short imperative messages:

- `Add solo dev documentation skill`
- `Fix CSV report upload validation`
- `Update attendance workbook generation`

Use conventional commit prefixes only when the repo already uses them or the user asks.

## Push Safety

Before pushing:

- Confirm the current branch is not unexpected.
- Check whether the branch is protected or shared when that is visible.
- Do not force-push unless the user explicitly asks and the risk is stated.
- If push fails because the remote is ahead, stop and report the divergence; do not auto-rebase unless requested.

## Output Contract

Final response must include:

- Commit hash and message.
- Branch and remote pushed.
- Verification run and result.
- Files intentionally left uncommitted, if any.
- Push status or blocker.

## Anti-Patterns

- Running `git add .` before reviewing changes.
- Combining unrelated work into one commit.
- Committing generated/cache files accidentally.
- Claiming push succeeded without reading command output.
- Force-pushing as a convenience.
