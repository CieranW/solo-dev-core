---
name: test-and-verify
description: Use before claiming work is complete, fixed, passing, ready, or shipped; map each claim to fresh reproducible evidence, capture relevant runtime context, handle flaky results explicitly, and separate verified facts from untested behavior and residual risk across reproductions, tests, builds, lint, typechecks, manual checks, or targeted commands.
---

# Test And Verify

Use this skill before making any claim that work is correct or complete.

## Verification Gate

Before any completion claim:

1. Identify the claim being made.
2. Identify the changed behavior, affected boundary, and meaningful failure path behind that claim.
3. Choose the strongest practical evidence that directly proves the claim.
4. Run focused checks first, then expand to broader regression checks in proportion to change risk.
5. Capture relevant runtime, tool version, test mode, fixture, seed, or environment context when it materially affects reproducibility. Never expose secrets.
6. Run verification fresh in the current turn when feasible and read the complete relevant output and exit status.
7. If code, config, fixtures, or generated output changes after a check, rerun every affected check.
8. Report what passed, what failed, what was not run, and why.

## Evidence Ladder

Prefer the narrowest evidence that proves the actual behavior:

- Reproduction command for the original bug.
- Focused regression test.
- Relevant unit/integration/e2e test.
- Typecheck, lint, or build.
- Browser/manual verification for UI behavior.
- Static inspection only when execution is impossible or unnecessary.

Do not confuse a successful command with proof of an unrelated claim. Record pre-existing or unrelated failures separately, and do not hide flaky results behind a successful rerun.

## Flaky Result Protocol

When an identical check produces inconsistent results:

1. Preserve the first failure output and execution context.
2. Rerun only to characterize reproducibility, using the same command and inputs unless testing a stated hypothesis. Use at most two additional runs unless the repository defines another protocol.
3. Report the sequence, such as `FAIL → PASS → PASS`, and classify the check as flaky rather than passing.
4. Identify timing, ordering, concurrency, shared state, network, seed, or environment differences when evidence supports them.
5. Do not rerun until green, discard failed output, or use an eventual pass as completion evidence.

## Output Contract

Final status must include:

- `Verified`: exact checks run, their result, and what each proved.
- `Not verified`: behavior or checks skipped, unavailable, destructive, too costly, or blocked.
- `Residual risk`: remaining uncertainty or follow-up risk.

Never imply success from code changes alone.

## Anti-Patterns

- Saying "should work" without evidence.
- Treating lint as a substitute for build or behavior tests.
- Running a broad suite without checking the behavior that actually changed.
- Trusting previous runs after making changes.
- Treating a flaky pass as stable evidence.
- Repeating a failed check without preserving its first failure and context.
- Hiding failed or skipped checks.
