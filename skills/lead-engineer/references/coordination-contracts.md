# Coordination Contracts

Read this reference only after `$lead-engineer` selects coordinated work or needs a continuity or lesson-proposal payload.

## Contents

- Delegation decision
- Specialist perspectives
- Assignment and response contracts
- Synthesis and conflict resolution
- Existing quality boundaries
- Continuity payload
- Shared-lesson proposal
- Worked examples

## Delegation decision

Use the minimum number of read-only investigations that can materially change the plan.

Delegate when:

- two or more questions have distinct evidence sources or can be falsified independently;
- the task crosses technical domains and the lead lacks enough evidence in one of them;
- security, data integrity, migration, deployment, compatibility, or rollback risk needs a separate perspective;
- credible alternatives benefit from adversarial comparison;
- an implemented medium, large, or high-risk change warrants review by someone other than its implementer.

Do not delegate when:

- one local behavior and one focused check settle the task;
- every perspective would inspect the same files and repeat the same reasoning;
- the lead already has sufficient evidence;
- specialist output cannot affect scope, design, risk treatment, or validation;
- integration overhead is greater than the expected information gain.

Use one investigation for one specialist evidence gap, two for genuinely independent boundaries, and three only when three distinct domains or risks can proceed without overlap. Without subagents, run the same questions serially and label the result as lead analysis or self-review.

## Specialist perspectives

Perspectives are temporary lenses, not permanent agents or mandatory roles.

| Perspective | Select when | Typical role lenses |
| --- | --- | --- |
| Structure and product | Boundaries, ownership, coupling, user outcome, or scope are contested | Software architect, product or scope reviewer, UX reviewer |
| Application and data | Runtime behavior, interfaces, persistence, schemas, pipelines, or model behavior need focused evidence | Backend engineer, frontend engineer, database engineer, data engineer, machine-learning engineer |
| Platform and operations | Delivery, environments, infrastructure, failure visibility, support, or contributor workflow may change | Infrastructure or platform engineer, DevOps engineer, release engineer, observability engineer, developer-experience engineer |
| Assurance | A separate risk or defect perspective is valuable | Security reviewer, performance reviewer, QA or test engineer, accessibility reviewer, independent code reviewer |
| Knowledge | Durable instructions, user-facing explanation, or documentation correctness need review | Technical writer, documentation reviewer |

Select the narrowest credible lens. A role name never expands task authority.

## Assignment contract

Give every specialist:

```text
Decision supported:
Precise question:
Read-only boundary:
Relevant context and constraints:
Evidence sources to inspect:
Expected output:
Non-goals:
Stop condition:
```

The expected output should request:

- observed facts with evidence paths;
- inferences and confidence;
- material unknowns;
- trade-offs or failure modes;
- one bounded recommendation;
- any condition that would change the recommendation.

Do not provide the preferred answer, hidden diagnosis, or unrelated repository history. Give enough context to avoid rediscovery, but preserve an independent perspective when independence is the purpose.

## Synthesis and conflict resolution

The lead returns one integrated decision:

```text
Agreements:
Disagreements:
Evidence strength and gaps:
Decision:
Why it fits the objective and constraints:
Rejected alternative:
Risk treatment:
Next owner or skill:
```

Resolve conflicts using, in order:

1. the user's objective, constraints, and authority;
2. observed repository or runtime evidence;
3. reversibility, data and security safety, and compatibility;
4. the smallest design that fully satisfies the requirement;
5. solo-maintenance and operational burden.

Do not vote, average incompatible recommendations, or let the most detailed report win by default. Preserve a conflict as an explicit decision or blocker when the evidence cannot resolve it.

## Existing quality boundaries

The lead selects boundaries; existing skills retain their procedures:

- Changed behavior or a completion claim → `$test-and-verify`.
- Structural ownership or deployment-boundary decision → `$architecture-review`.
- Bounded post-change defect review → `$review-changes`.
- Named commit, merge, handoff, deploy, or release readiness question → `$ship-check`.

A security, data, migration, deployment, compatibility, or rollback signal may warrant a separate read-only perspective even for a small change. It does not automatically require every gate.

## Continuity payload

Emit this payload before an expected context break or handoff:

```text
Current objective:
Branch and working-tree state:
Completed:
Changed:
Validation performed:
Unresolved questions:
Risks:
Deferred ideas:
Exact next action:
Resume files and commands:
Do not repeat:
```

By default this is output only. Persist it only with explicit authority. Use `$finish-work` when closing a meaningful batch in a repository with `docs/PROJECT.md`; use `$documentation` for another canonical issue, plan, or equivalent record. Reconcile it with current Git and executable evidence on resume; it is a cache, not proof that prior validation remains current.

## Shared-lesson proposal

When a project reveals guidance that may generalize, produce a proposal containing:

- originating project, event, and evidence;
- project-specific context that must not leak into the core;
- generalized claim and intended trigger;
- counterexamples, domain limits, and non-goals;
- comparison with existing shared guidance;
- one contrasting workflow that could falsify the proposal;
- proposed destination in `solo-dev-core`.

Stop at the proposal. Do not automatically edit shared guidance. Validation in real and contrasting workflows, independent review, and accept, revise, or reject decisions belong to a later authorized promotion workflow.

## Worked examples

### Tiny direct fix

Request: correct one obvious null check in one module, preserve behavior, and run the focused regression test.

Decision: `tiny`, normal risk, `direct`, zero specialists. Hand the authorized change to `$implement-change`, then gather focused evidence through `$test-and-verify`. Do not create a durable plan or handoff.

### Medium multi-boundary feature

Request: add an API field that affects persistence and a frontend consumer.

Decision: `medium`, elevated compatibility risk, `coordinate`. Assign one read-only investigation to trace schema and API compatibility and another to trace the consumer and test surface. The lead synthesizes both into one plan and owns the implementation boundary. If subagents are unavailable, run the two questions serially and do not call the second pass independent.

### Large conflict and handoff

Request: stage a production authentication migration. A security perspective recommends immediate token invalidation; an operations perspective recommends a compatibility window to reduce outage risk.

Decision: `large`, high risk, `coordinate`. The lead resolves the conflict against the threat model, compatibility requirement, rollback evidence, and user authority rather than averaging the advice. Decompose implementation into safe stages. Before stopping, emit the continuity payload with the chosen decision, rejected option, validation evidence, exact next action, resume commands, and work that must not be repeated.
