---
name: finish-work
description: Use when ending, closing, handing off, or checkpointing a meaningful development batch in a repository with docs/PROJECT.md; inspect the complete change and validation evidence, update implemented and remaining state, preserve risks and future ideas, identify durable ADR candidates, record one exact next action and truthful Last Verified metadata, and stop before Git staging or publication.
---

# Finish Work

Close a meaningful work batch with truthful, durable project continuity.

## Boundaries

- Use after a development batch, before a handoff, or before an expected context break.
- Update project documentation and accepted ADRs only; do not alter implementation merely to finish the record.
- Do not stage, commit, push, tag, release, deploy, or imply those actions are authorized.
- Do not claim a milestone complete or tests passing from intended behavior, previous runs, or user prose alone.

## Workflow

1. Read applicable instructions and `docs/PROJECT.md`. Route a missing initial record to `$adopt-project`.
2. Inspect the complete relevant working-tree and branch diff, status, bounded recent history, and the batch's stated objective.
3. Compare changed behavior with the Current Milestone, Success and Stop Conditions, Active Work, and Product Boundaries.
4. Inspect fresh validation results. Use `$test-and-verify` when a completion claim lacks claim-matched evidence and running the relevant check is safe and proportionate.
5. Separate implemented and verified work, implemented but unverified work, incomplete work, unrelated dirty changes, and newly discovered risks.
6. Update Verified Current State only with supported claims. Update Active Work with completed and remaining work and keep the milestone open unless its success conditions are actually met.
7. Set Next and Exact Next Action to one concrete continuation step that another session can execute without rediscovery.
8. Capture newly discovered out-of-scope ideas under Future Ideas with value, dependencies, a concrete reconsideration trigger, reason deferred, related context, and capture date. Do not change Active.
9. Preserve intentionally postponed work under Deferred. Retain `State: Abandoned` only when the rejected history matters.
10. Identify decisions whose rationale will matter later. Link existing ADRs, create an ADR from `../adopt-project/assets/ADR.md` relative to this skill directory only when the durable decision and rationale are settled, or report the exact ADR candidate still needing a decision.
11. Record unresolved risks and uncertainty without converting them into vague backlog items.
12. Update Last Verified with the observed timestamp, commit, branch, working-tree state, validation level, and exact successful, failed, skipped, or unrun evidence.
13. Use `$documentation` for the record and run `../adopt-project/scripts/project-memory validate-project --repo <repository>`, resolving the path from this skill directory.
14. Optionally recommend a logical commit sequence based on the complete diff, but do not stage or commit.

## Evidence

- Complete relevant diff, status, batch objective, project record, and milestone conditions inspected.
- Validation evidence matched to each completion claim, with failures and unrun checks retained.
- Project-record changes tied to implementation or documented owner intent.
- New Future Ideas remain outside Active and include reconsideration triggers.
- Updated project memory validates successfully.

## Output Contract

- Batch outcome and milestone status.
- Completed, remaining, unverified, and unrelated work.
- Documentation and ADR changes.
- New Future Ideas, Deferred items, decisions, risks, and uncertainty.
- Exact next action.
- Optional commit sequence recommendation.
- `Verified`, `Not verified`, and `Residual risk`.
- Explicit statement that staging, commit, push, release, and deployment were not performed.

## Stop Conditions

- Stop and route to `$adopt-project` when no project record exists.
- Stop before claiming completion when required evidence failed, is stale, or did not run.
- Stop before creating an ADR when the decision or rationale is not settled.
- Stop after the validated continuity update; Git publication remains separate.

## Composition

- Use `$test-and-verify` for missing fresh completion evidence.
- Use `$documentation` for `docs/PROJECT.md` and accepted ADR changes.
- Use `$project-status` update semantics when broader project-state reconciliation is required.
- Route a later authorized checkpoint to `$commit-and-push`; do not invoke it implicitly.

## Anti-Patterns

- Marking work complete because the diff looks plausible.
- Recording tests as passed without exact successful evidence.
- Moving newly discovered ideas into Active or Next automatically.
- Creating an ADR for every local implementation choice.
- Leaving several possible next actions instead of one.
- Treating a finish workflow as authorization to commit or push.
