---
name: test-and-verify
description: Use before claiming work is complete, fixed, passing, ready, or shipped; requires fresh verification evidence from relevant tests, builds, lint, typechecks, manual checks, or targeted commands, and separates verified facts from residual risk.
---

# Test And Verify

Use this skill before making any claim that work is correct or complete.

## Verification Gate

Before any completion claim:

1. Identify the claim being made.
2. Choose the strongest practical evidence for that claim.
3. Run fresh verification in the current turn when feasible.
4. Read the output and exit status.
5. Report what passed, what failed, what was not run, and why.

## Evidence Ladder

Prefer the narrowest evidence that proves the actual behavior:

- Reproduction command for the original bug.
- Focused regression test.
- Relevant unit/integration/e2e test.
- Typecheck, lint, or build.
- Browser/manual verification for UI behavior.
- Static inspection only when execution is impossible or unnecessary.

## Output Contract

Final status must include:

- `Verified`: checks run and what they proved.
- `Not verified`: checks skipped, unavailable, or blocked.
- `Residual risk`: remaining uncertainty or follow-up risk.

Never imply success from code changes alone.

## Anti-Patterns

- Saying "should work" without evidence.
- Treating lint as a substitute for build or behavior tests.
- Trusting previous runs after making changes.
- Hiding failed or skipped checks.
