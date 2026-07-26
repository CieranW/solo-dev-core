---
name: repo-compass
description: Use when entering an unfamiliar repository, recovering context after reinstall or context loss, auditing whether a repo is ready to work in, creating repo-specific onboarding guidance, or when the user asks to run through, map, inspect, or orient around a codebase; produce an evidence-backed working runbook without unnecessary mutation.
---

# Repo Compass

Use this skill to build a compact working map of a repository.

## Workflow

1. Locate the repository root and read every applicable `AGENTS.md` before interpreting or changing files.
2. Identify git status and branch, major languages, package managers, framework clues, deployment shape, and repository type.
3. Read the smallest useful set of files: README, manifests, lockfiles, config, scripts, obvious entrypoints, and focused architecture or operations docs.
4. Map how to install, run, test, build, lint, typecheck, migrate, and develop the project. Label each command as verified, documented but unrun, or inferred.
5. Identify runtime and config requirements: env files, secret placeholders, databases, services, migrations, external tools, and generated prerequisites.
6. Note important directories, architecture boundaries, source-of-truth files, generated code, and files to avoid editing casually.
7. Call out current risks and unknowns: dirty worktree, missing docs, unclear commands, failing checks, uninstalled dependencies, stale generated assets, or configuration drift.
8. If durable onboarding or repo guidance is requested, update the nearest canonical `AGENTS.md` or existing runbook with concise project-specific facts. Otherwise keep orientation read-only.
9. Recommend the smallest next action that would reduce the most uncertainty.

## Output Contract

Return a concise runbook with:

- Repository snapshot, stack, and entrypoints.
- Common commands with evidence status.
- Test and verification path.
- Config/runtime needs.
- Architecture and editing boundaries.
- Current repo state, risks, and unknowns.
- Recommended next action.

## Anti-Patterns

- Reading the whole repo when manifests and entrypoints are enough.
- Ignoring dirty worktree state.
- Reporting documented or inferred commands as verified.
- Mutating dependencies, configuration, or generated files merely to orient.
- Producing a long audit when the user needs working orientation.
