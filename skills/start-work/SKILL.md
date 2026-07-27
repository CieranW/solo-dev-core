---
name: start-work
description: Use when beginning or resuming work in a repository that uses docs/PROJECT.md, especially after a fresh chat, handoff, interruption, or long gap; compose repository resumption with a read-only project-status check, identify the active milestone and drift, reject out-of-scope requests, and recommend one bounded work batch with one exact next action before implementation.
---

# Start Work

Resume a managed repository with one safe, bounded work batch.

## Boundaries

- Use when the user asks to start, resume, continue, pick up, or get back to project work.
- Keep the start phase read-only. Do not silently refresh documentation or begin implementation.
- Do not promote Next, Future, Deferred, or Abandoned work into Active.
- Do not turn a resumption brief into a broad repository audit when current guidance is sufficient.

## Workflow

1. Read applicable instructions and `docs/PROJECT.md`. If project memory is missing, stop and route to `$adopt-project`.
2. Use `$repo-compass` to infer `ORIENT` or `RESUME`; prefer `RESUME` when the project file and recent history provide usable continuity.
3. Use `$project-status` in `CHECK` mode to compare the project record with branch, commit, tree, tracking, implementation, and validation evidence.
4. Identify the active milestone, its success and stop conditions, current batch state, risks, and Exact Next Action.
5. Compare the user's requested work with Product Boundaries and the Active milestone:
   - continue when it is clearly in scope;
   - warn when it belongs in Next or Future;
   - stop for an explicit milestone decision when it would expand Active;
   - retain Deferred or Abandoned state unless its recorded trigger and a clear milestone justification are satisfied.
6. Identify drift that must be reconciled before implementation. Recommend `$project-status` in `UPDATE` mode when the stale record would make the next batch unsafe.
7. Select one coherent batch with an observable outcome, explicit non-goals, likely affected boundary, meaningful failure path, and practical verification.
8. Prefer the recorded Exact Next Action when still supported. Replace it in the brief, not the file, when repository evidence establishes a safer action.
9. If implementation was explicitly requested and the batch is decision-ready, hand it to `$implement-change` after the start brief. Otherwise stop after the recommendation.

## Evidence

- Applicable instructions, project record, status, branch, relevant history, and current implementation evidence inspected.
- Project drift and local tracking limitations identified.
- Requested work classified against Active, Next, Future, Deferred, and Abandoned state.
- Recommended batch tied to milestone success and a practical verification path.

## Output Contract

- Mode: `ORIENT` or `RESUME`.
- Repository and project-memory snapshot.
- Active milestone, drift, risks, and validation freshness.
- Scope classification of the requested work.
- One bounded work batch with outcome, non-goals, and verification.
- One exact next action.
- Explicit warning and required decision when the request is outside Active.

## Stop Conditions

- Stop and route to `$adopt-project` when `docs/PROJECT.md` is missing.
- Stop before implementation when material drift or a milestone decision remains unresolved.
- Stop after one safe batch is concrete; do not plan the whole roadmap.
- Stop before changing project documentation during the start phase.

## Composition

- Use `$repo-compass` for orientation or resumption evidence.
- Use `$project-status` in `CHECK` mode for project-memory reconciliation.
- Route missing memory to `$adopt-project`.
- Route authorized, decision-ready in-scope mutation to `$implement-change`.
- Route a requested project-record correction to `$project-status` in `UPDATE` mode.

## Anti-Patterns

- Rereading the whole repository despite a current project record.
- Beginning a Future Idea because it is adjacent to the active task.
- Silently changing the milestone to accommodate the user's latest request.
- Returning several possible batches instead of one exact next action.
- Editing project memory merely to make the start brief look current.
