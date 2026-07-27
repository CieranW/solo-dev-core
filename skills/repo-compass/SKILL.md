---
name: repo-compass
description: Use when entering an unfamiliar repository, starting a new chat in an existing repo, recovering after context loss, reinstall, or handoff, auditing whether a repo is ready to work in, creating repo-specific onboarding guidance, or when the user asks to run through, map, inspect, orient, resume, or get up to speed on a codebase; infer ORIENT or RESUME mode and produce an evidence-backed working or session brief without unnecessary mutation.
---

# Repo Compass

Build a compact repository map or reconstruct enough current context to resume work safely.

## Mode

Infer the mode from the request and repository evidence. Do not ask the user to choose when the distinction is discoverable.

- `ORIENT`: use for an unfamiliar repository, new project, onboarding request, or missing reliable repository map.
- `RESUME`: use for a familiar repository, fresh chat, handoff, interrupted task, or recovery after lost context.

When uncertain, start with `RESUME` if current guidance and local history provide a usable map. Expand only the missing parts into `ORIENT`.

## Workflow

1. Locate the repository root and read every applicable `AGENTS.md` before interpreting or changing files.
2. Infer `ORIENT` or `RESUME`; state the mode briefly in the result.
3. Inspect local git status, branch, tracking ref, and available upstream divergence. In `RESUME`, inspect a bounded slice of recent commits and the relevant dirty or branch diff to identify what changed and what appears in progress. Do not fetch merely to orient; label local tracking information that may be stale.
4. In `RESUME`, look for existing plans, checkpoints, handoff notes, decision records, and task-specific docs using likely paths and names before broad searches. Prefer the nearest durable source of truth over scattered TODO comments.
5. Read the smallest useful source set for remaining gaps: README, manifests, lockfiles, config, scripts, obvious entrypoints, and focused architecture or operations docs. Reuse current `AGENTS.md` guidance or an accurate repository map instead of rereading the entire tree.
6. Identify the repository type, major languages, package managers, framework clues, deployment shape, stack, and entrypoints.
7. Map how to install, run, test, build, lint, typecheck, migrate, and develop the project. Label each command as verified, documented but unrun, or inferred.
8. Identify runtime and config requirements: env files, secret placeholders, databases, services, migrations, external tools, and generated prerequisites.
9. Note important directories, architecture boundaries, source-of-truth files, generated code, and files to avoid editing casually.
10. Reconcile repository evidence with guidance. Call out stale or conflicting docs, configuration drift, dirty work, missing context, unclear commands, failing checks, uninstalled dependencies, and stale generated assets. Prefer current executable evidence, but do not silently rewrite guidance.
11. Incorporate the user's stated next goal, success signal, and constraints into the brief while separating repository facts from preferences and assumptions.
12. If the goal remains materially fuzzy, hand the brief to `$clarify-intent`. If the goal is clear and implementation was authorized, continue after the brief without asking for redundant confirmation. Stop after the brief when orientation only was requested.
13. If durable onboarding or repository guidance is requested, update the nearest canonical `AGENTS.md` or existing runbook with concise project-specific facts. Otherwise keep the orientation phase read-only.
14. Recommend the exact next action that reduces the most uncertainty or advances the stated goal.

## Output Contract

Return a compact working or session brief with:

- Mode and repository snapshot.
- Current branch, upstream state, and work in progress.
- Recent relevant changes and continuity records in `RESUME`.
- Stack, entrypoints, architecture, and editing boundaries.
- Common commands with evidence status.
- Test and verification path.
- Config/runtime needs.
- Current objective, constraints, and explicit assumptions.
- Risks, unknowns, conflicts, and potentially stale context.
- Exact recommended next action.

## Anti-Patterns

- Reading the whole repo when manifests and entrypoints are enough.
- Rebuilding a full repository map in `RESUME` when current guidance is sufficient.
- Ignoring dirty worktree state.
- Treating a local tracking ref as freshly fetched remote evidence.
- Treating stale plans or handoff notes as current without reconciling them with git and executable sources.
- Reporting documented or inferred commands as verified.
- Mutating dependencies, configuration, or generated files merely to orient.
- Producing a long audit when the user needs working orientation.
- Asking the user to choose a mode or reconfirm clear authorized work when repository evidence resolves the question.
