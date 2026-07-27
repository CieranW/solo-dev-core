---
name: review-changes
description: Use when the user asks for a code review, diff review, pull request review, regression audit, or correctness and security assessment of proposed changes; inspect the complete relevant change and affected call sites, report only evidence-backed actionable findings with severity and tight locations, and remain read-only unless fixes are explicitly requested.
---

# Review Changes

Find defects and material risks before judging whether a change is ready to ship.

## Boundaries

- Use for a bounded code, configuration, commit, branch, or pull-request diff.
- Do not use for broad architecture assessment, behavior-preserving simplification of existing code, implementation, or a shipping verdict.
- Keep review read-only unless fixes are explicitly requested.

## Workflow

1. Read applicable repository instructions and define the review boundary, comparison base, intended behavior, and requested risk focus.
2. Inspect repository status and the complete relevant diff, including staged, unstaged, and untracked files in scope.
3. Read enough surrounding code, call sites, tests, configuration, schemas, and contracts to understand the changed behavior rather than reviewing isolated lines.
4. Trace realistic success and failure paths across boundaries. Check correctness, data loss, security, authorization, compatibility, concurrency, error handling, performance, and user-visible regressions as relevant.
5. Validate each suspected issue against the actual code path and triggering conditions. Do not report a theoretical concern without a plausible failure scenario.
6. Assign the lowest justified severity:
   - `P0`: immediate catastrophic impact or active security/data-loss risk.
   - `P1`: likely serious correctness, security, compatibility, or outage risk.
   - `P2`: material defect with bounded impact or a realistic regression.
   - `P3`: low-impact actionable defect worth correcting.
7. Report findings first, ordered by severity. Give each finding one tight file and line range, the failure scenario, supporting evidence, and the smallest useful correction direction.
8. If no actionable finding is supported, say so explicitly and report verification gaps or residual risk instead of inventing issues.
9. Keep review read-only unless the user explicitly requests fixes. After fixes, use `$test-and-verify`; use `$ship-check` separately for readiness.

## Finding Standard

A finding must be:

- Introduced or exposed by the reviewed change, unless the user requested a broader audit.
- Actionable and materially relevant to correctness, security, reliability, compatibility, or maintainability.
- Specific enough for another developer to reproduce or verify.
- Located as tightly as the evidence permits.

Do not report formatting preferences, harmless naming differences, speculative architecture, or test requests without a concrete uncovered risk.

## Evidence

- Complete relevant diff and affected call sites inspected.
- Each finding tied to a plausible triggering condition and actual code path.
- Severity supported by realistic impact.
- Verification gaps and residual risk stated when evidence is incomplete.

## Output Contract

Return:

- Actionable findings ordered by severity, with location, scenario, evidence, and correction direction.
- Material assumptions or open questions that affect correctness.
- Verification gaps and residual risk.
- A clear statement when no actionable findings were found.
- An explicit statement that no fixes were applied unless the user requested them.

## Stop Conditions

- Stop after reporting all supported actionable findings; do not invent issues to fill the response.
- Stop before mutation during review-only requests.
- When fixes are authorized, hand them to `$implement-change` rather than weakening the review standard.

## Composition

- Use `$architecture-review` for system boundaries and structural design.
- Use `$simplify-code` for behavior-preserving complexity reduction.
- Hand authorized fixes to `$implement-change`, followed by `$test-and-verify`.
- Use `$ship-check` separately when the reviewed change needs a readiness verdict.

## Anti-Patterns

- Summarizing the diff instead of reviewing it.
- Reviewing only changed lines without tracing affected behavior.
- Reporting style noise as defects.
- Inflating severity without a realistic impact path.
- Assuming passing tests prove untested behavior.
- Applying fixes during a review-only request.
