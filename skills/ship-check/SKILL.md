---
name: ship-check
description: Use before commits, PRs, merges, releases, handoffs, deploys, or readiness claims; define the exact shipping boundary, review the complete change and verification evidence, inspect config and migration impact, user-facing behavior, rollback or recovery options, and return an explicit readiness verdict with unresolved risks.
---

# Ship Check

Use this skill to decide whether work is ready to hand off or ship.

## Workflow

1. Define the exact boundary being judged: ready to commit, push, open a PR, merge, hand off, deploy, or release.
2. Inspect the complete relevant diff, staged state, untracked files, and repository status before summarizing.
3. Confirm the intended behavior, user-facing impact, and acceptance criteria.
4. Run or cite fresh claim-matched verification from `$test-and-verify`.
5. Check for migration, config, dependency, environment, compatibility, security, or deployment changes.
6. Check for docs, tests, fixtures, generated files, screenshots, release notes, or operator steps that should accompany the change.
7. Identify rollback or recovery steps when the change affects persistent data, production behavior, integrations, or deployment.
8. Separate blockers from acceptable residual risk and name the owner or next action for each blocker when known.
9. Return one verdict:
   - `READY`: the stated boundary is supported by evidence with no material unresolved risk.
   - `READY WITH RESIDUAL RISK`: no blocker remains, but important uncertainty must be carried explicitly.
   - `BLOCKED`: a missing decision, failed check, incomplete change, or unacceptable risk prevents the stated boundary.

## Deploy Aftercare

For deploy readiness, define before deployment:

- Immediate smoke checks for the changed user and operator paths.
- A monitoring window sized to the change risk, with the metrics, logs, traces, queues, or business signals to watch.
- Observable rollback triggers, not vague concern.
- The rollback or recovery action and the person or system responsible for initiating it.
- Any forward-only migration or compatibility boundary that limits rollback.

Treat missing aftercare as a blocker when the change can affect persistent data, availability, security, billing, integrations, or a large user population. Otherwise carry it as explicit residual risk.

## Output Contract

Readiness report must include:

- Target boundary and verdict.
- Change summary.
- Verification evidence.
- Release notes or user impact.
- Config/migration/dependency notes.
- Rollback or recovery note when relevant.
- Deploy smoke checks, monitoring window, rollback trigger, and owner when the target boundary is deployment.
- Blockers or residual risk.
- Required next action when not `READY`.

## Anti-Patterns

- Shipping from memory without checking the diff.
- Treating passing tests as the only readiness signal.
- Conflating ready to push a branch with ready to merge or deploy it.
- Omitting migration or environment changes.
- Deploying without defined smoke checks, monitoring signals, or rollback triggers.
- Saying "ready" while known blockers remain.
