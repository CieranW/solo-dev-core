---
name: repo-compass
description: Use when entering an unfamiliar repository, recovering context after reinstall or context loss, auditing whether a repo is ready to work in, or when the user asks to run through, map, inspect, or orient around a codebase.
---

# Repo Compass

Use this skill to build a compact working map of a repository.

## Workflow

1. Identify repo root, git status, major languages, package managers, and framework clues.
2. Read the smallest useful set of files: README, manifests, lockfiles, config, scripts, AGENTS.md, and obvious entrypoints.
3. Map how to run, test, build, lint, and develop the project.
4. Identify runtime/config requirements: env files, secrets placeholders, databases, services, migrations, or external tools.
5. Note important directories, ownership boundaries, generated code, and files to avoid editing casually.
6. Call out current risks: dirty worktree, missing docs, unclear commands, failing checks, uninstalled dependencies, or stale generated assets.

## Output Contract

Return a concise runbook with:

- Stack and entrypoints.
- Common commands.
- Test and verification path.
- Config/runtime needs.
- Current repo state and risks.
- Recommended next action.

## Anti-Patterns

- Reading the whole repo when manifests and entrypoints are enough.
- Ignoring dirty worktree state.
- Reporting guesses as facts.
- Producing a long audit when the user needs working orientation.
