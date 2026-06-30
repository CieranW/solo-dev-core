---
name: ship-check
description: Use before commits, PRs, releases, handoffs, deploys, or readiness claims; review diff, verification evidence, config and migration notes, user-facing behavior, rollback or recovery options, and unresolved risks.
---

# Ship Check

Use this skill to decide whether work is ready to hand off or ship.

## Workflow

1. Inspect the diff or changed files before summarizing.
2. Confirm the intended behavior and user-facing impact.
3. Run or cite fresh verification from `test-and-verify`.
4. Check for migration, config, dependency, environment, or deployment changes.
5. Check for docs, tests, fixtures, generated files, or screenshots that should accompany the change.
6. Identify rollback or recovery steps when the change affects persistent data, production behavior, integrations, or deployment.
7. State blockers and residual risk plainly.

## Output Contract

Readiness report must include:

- Change summary.
- Verification evidence.
- Release notes or user impact.
- Config/migration/dependency notes.
- Rollback or recovery note when relevant.
- Blockers or residual risk.

## Anti-Patterns

- Shipping from memory without checking the diff.
- Treating passing tests as the only readiness signal.
- Omitting migration or environment changes.
- Saying "ready" while known blockers remain.
