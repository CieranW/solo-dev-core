---
name: implement-change
description: Use when the user has explicitly requested implementation and the change is decision-ready, or when an approved plan should now be applied; inspect current state, make the smallest coherent code, configuration, or test change, preserve unrelated behavior, record deviations, verify the affected boundary, and stop before committing, pushing, releasing, deploying, or mutating unrelated external systems.
---

# Implement Change

Apply an authorized, decision-ready change without reopening settled scope or taking ownership of Git publication.

## Boundaries

- Use for code, configuration, schema, fixture, or targeted test changes whose outcome and acceptance criteria are sufficiently clear.
- Do not use to discover root causes, compare open-ended product options, update dependencies, write docs-only changes, review a diff, or decide shipping readiness.
- Mutate only when the user requested implementation or approved the plan. Keep external production systems and irreversible state out of scope unless separately authorized.

## Workflow

1. Read applicable repository guidance and inspect status, relevant files, existing patterns, and the approved outcome.
2. Confirm the task is decision-ready. If a material decision is unresolved, stop and use `$clarify-intent`.
3. Establish the current behavior and the narrow verification path before editing when feasible.
4. Identify the smallest coherent file set and meaningful failure path.
5. Edit existing structures directly. Update the narrowest useful regression test with the behavior change.
6. Inspect the diff continuously for scope expansion, accidental generated files, public-interface drift, or unrelated cleanup.
7. Record any necessary deviation from the approved plan and why it was required.
8. Run focused checks, then practical broader checks in proportion to risk through `$test-and-verify`.
9. Report changed files, behavior, evidence, deviations, and remaining risk.
10. Stop before staging, committing, pushing, tagging, releasing, deploying, or performing unrequested external mutations.

## Evidence

- Applicable instructions and relevant existing behavior inspected.
- Complete implementation diff reviewed against the approved scope.
- Focused behavior and failure-path checks run fresh, with broader checks matched to risk.
- Deviations and unverified behavior stated explicitly.

## Output Contract

- Outcome implemented and observable behavior changed.
- Files changed and why each belongs in scope.
- Tests added or updated.
- Plan deviations.
- `Verified`, `Not verified`, and `Residual risk`.
- Explicit statement that Git publication and deployment were not performed.

## Stop Conditions

- Stop before mutation when the task is not decision-ready or authority is missing.
- Stop when implementation would require a materially broader design, irreversible migration, unrelated dependency change, or external production action.
- Stop after implementation evidence and handoff; Git and shipping operations belong to neighbouring skills.

## Composition

- Receive decision-ready work from `$clarify-intent`, `$diagnose-problem`, `$profile-performance`, `$simplify-code`, or `$architecture-review`.
- Use `$dependency-maintenance` instead for package, runtime, manifest, and lockfile work.
- Use `$documentation` for docs-only changes.
- Hand evidence gathering to `$test-and-verify`; use `$review-changes` or `$ship-check` only when their distinct trigger applies.
- Hand authorized Git operations to `$commit-and-push`.

## Anti-Patterns

- Editing before the task is decision-ready.
- Replacing working code when a narrow edit is sufficient.
- Smuggling cleanup, dependency updates, architecture changes, or release work into implementation.
- Claiming completion from the diff alone.
- Committing, pushing, or deploying as an implicit final step.
