---
name: ship-check
description: Use when the user asks whether a defined change is ready to commit, push, open a pull request, merge, hand off, deploy, or release, or when repository policy explicitly requires a readiness verdict; consume the complete change and fresh verification evidence, inspect operational impact and rollback, and return one boundary-specific verdict without performing Git or deployment actions.
---

# Ship Check

Use this skill to decide whether work is ready to hand off or ship.

## Boundaries

- Use for an explicit readiness question or repository-required gate with a named boundary.
- Do not invoke automatically for every implementation, test run, commit, or push when no readiness verdict is requested or required.
- Keep the check read-only. Do not stage, commit, push, tag, merge, deploy, or release.

## Workflow

1. Define the exact boundary being judged: ready to commit, push, open a PR, merge, hand off, deploy, or release.
2. Inspect the complete relevant diff, staged state, untracked files, and repository status before summarizing.
3. Confirm the intended behavior, user-facing impact, and acceptance criteria.
4. Consume fresh claim-matched verification from `$test-and-verify`; invoke it when evidence is missing, but do not repeat its protocol inside this skill.
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

## Evidence

- Complete relevant diff, repository state, intended behavior, and acceptance criteria inspected.
- Fresh claim-matched verification supplied by `$test-and-verify`.
- Configuration, migration, dependency, compatibility, security, user, and operational impact assessed as relevant.
- Rollback or recovery evidence matched to the named boundary.

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

## Stop Conditions

- Stop and ask for the boundary when "ready" could mean materially different actions.
- Stop with `BLOCKED` when required evidence, decisions, migration safety, or recovery planning is missing.
- Stop after the verdict; the skill does not perform the shipping action.

## Composition

- Consume evidence from `$test-and-verify`.
- Use `$review-changes` separately for bounded-diff defect findings.
- Hand release classification and tag decisions to `$semantic-versioning`.
- Hand authorized staging, commits, and branch pushes to `$commit-and-push`.
- Deployment execution remains outside this skill.

## Anti-Patterns

- Shipping from memory without checking the diff.
- Treating passing tests as the only readiness signal.
- Conflating ready to push a branch with ready to merge or deploy it.
- Omitting migration or environment changes.
- Deploying without defined smoke checks, monitoring signals, or rollback triggers.
- Saying "ready" while known blockers remain.
