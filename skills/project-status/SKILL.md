---
name: project-status
description: Use when asked to reconstruct, check, reconcile, or refresh a repository's docs/PROJECT.md status outside ordinary end-of-batch closeout, including current milestone, implemented state, active work, risks, exact next action, or Last Verified metadata; compare the record with Git and implementation evidence, infer CHECK or UPDATE mode, mark uncertainty explicitly, and never treat stale documentation as authoritative.
---

# Project Status

Reconcile the canonical project record with current repository evidence.

## Boundaries

- Use for status checks, stale project records, broad reconciliation, and explicit `docs/PROJECT.md` refreshes.
- Do not use for an ordinary end-of-batch handoff or closeout; `$finish-work` owns that boundary.
- Infer `CHECK` for read-only inspection and `UPDATE` when the user asks to sync or refresh project state.
- In `UPDATE`, modify project documentation and accepted ADRs only. Do not change application code.
- Do not run a full verification suite merely to fill Last Verified or fetch remotes merely to report status.

## Workflow

1. Read applicable instructions and `docs/PROJECT.md`. If the file is missing, route initial reconstruction to `$adopt-project`.
2. Infer `CHECK` or `UPDATE` from the request. A call from `$start-work` defaults to `CHECK`; a call from `$finish-work` defaults to `UPDATE`.
3. Use `$repo-compass` in `RESUME` mode to inspect branch, status, tracking ref, bounded recent history, relevant diffs, and continuity records. Label local tracking information that may be stale.
4. Compare Last Verified commit, branch, tree state, validation level, and evidence with current Git state.
5. Reconcile Current Milestone, Verified Current State, Active Work, Next, Risks and Unknowns, and Exact Next Action against implementation and configuration evidence.
6. Treat repository evidence as stronger than the project file. Preserve documented intent when code cannot establish it, but label the distinction.
7. Classify drift:
   - `current`: recorded commit matches `HEAD`, the tree state matches, and claims remain supported;
   - `drifted`: later commits or relevant working-tree changes exist;
   - `aged`: Last Verified is older than the repository's stated threshold, or 30 days when none is stated, even without proven contradiction;
   - `incomplete`: required milestone, evidence, or next-action fields are missing;
   - `conflicted`: a recorded commit is unavailable or a material claim contradicts repository evidence;
   - `uncertain`: owner or runtime evidence is required.
8. Inspect existing validation evidence. Invoke `$test-and-verify` only when the user requested fresh validation or a concrete completion claim needs new evidence.
9. In `UPDATE`, revise only claims supported by evidence, record completed and remaining work, preserve unresolved risk, and set one exact next action.
10. Record Last Verified with the actual timestamp, commit, branch, working-tree state, validation level, and commands or inspection evidence. Never upgrade the level beyond what ran successfully.
11. Use `$documentation` for changes and run `../adopt-project/scripts/project-memory validate-project --repo <repository>`, resolving the path from this skill directory.
12. In `CHECK`, report proposed corrections without editing.

## Evidence

- Project record, applicable instructions, branch, status, local tracking state, relevant history, and diffs inspected.
- Documented claims compared with executable repository evidence.
- Verification commands and their freshness distinguished from inspection-only evidence.
- Every updated status claim supported or labelled uncertain.

## Output Contract

- Mode: `CHECK` or `UPDATE`.
- Drift classification and evidence.
- Current milestone, implemented state, active work, risks, and exact next action.
- Branch, commit, working-tree state, validation level, and local tracking limitation.
- Documentation changes in `UPDATE`, or proposed corrections in `CHECK`.
- `Verified`, `Not verified`, and `Residual risk`.

## Stop Conditions

- Stop before mutation in `CHECK`.
- Stop and route to `$adopt-project` when no usable project record exists.
- Stop before rewriting product intent when repository evidence cannot resolve an owner decision.
- Stop before claiming tests or remote freshness without corresponding evidence.

## Composition

- Use `$repo-compass` in `RESUME` mode for Git and repository continuity evidence.
- Route missing initial memory to `$adopt-project`.
- Use `$test-and-verify` only for requested or claim-matched fresh checks.
- Use `$documentation` for authorized project-record or ADR changes.
- Supply read-only reconciliation to `$start-work`. `$finish-work` owns ordinary batch closeout and uses this skill only for broader project-state drift.

## Anti-Patterns

- Treating `docs/PROJECT.md` as authoritative when code disagrees.
- Fetching, installing, or running every test to produce a status summary.
- Turning a status refresh into implementation or roadmap expansion.
- Recording a clean tree, remote state, or passing test without observing it.
- Replacing one exact next action with a backlog.
