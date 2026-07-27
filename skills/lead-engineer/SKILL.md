---
name: lead-engineer
description: Use when the user explicitly asks Codex to lead, coordinate, delegate, or orchestrate engineering work, or when one task has multiple independently investigable technical boundaries plus material security, data, migration, deployment, or compatibility risk; classify complexity and risk, choose direct work, bounded read-only specialist investigation, or milestone decomposition, synthesize conflicts, and route execution to existing skills without becoming a mandatory task router.
---

# Lead Engineer

Coordinate complex engineering work while retaining one clear owner for scope, decisions, integration, and evidence.

## Boundaries

- Use for explicit lead-engineer, coordination, delegation, or orchestration requests and for genuinely multi-boundary work with material cross-boundary risk.
- Do not use merely because a task is ambiguous, broad, architectural, review-oriented, or ready for implementation. Those cases remain with their existing skills.
- Do not invoke for a local, obvious, reversible change unless the user explicitly requests coordination.
- Keep delegated work read-only. The lead owns synthesis and integration; existing implementation skills own authorized mutation.
- Do not silently update project memory, install domain packs, change external systems, or promote project guidance into this shared core.

## Workflow

1. Confirm the objective, observable success, constraints, authority, and relevant repository evidence. Use `$start-work` when beginning or resuming a repository that has adopted `docs/PROJECT.md`; otherwise use `$repo-compass` only when repository context is missing.
2. Classify the task by the highest material driver, not by estimated minutes:
   - `tiny`: one local, clear, reversible behavior with straightforward verification;
   - `small`: one component and a coherent, low-risk file set;
   - `medium`: several connected boundaries, material ambiguity, or difficult validation;
   - `large`: multiple components or domains with architectural, security, data, migration, deployment, or compatibility impact;
   - `epic`: several large outcomes, repositories, migrations, or unresolved architectural stages.
3. Record risk separately as `normal`, `elevated`, or `high`. Irreversible data change, authentication, privacy, public compatibility, production migration, difficult rollback, or broad operational impact raises the strategy even when the diff may be small.
4. Choose one action:
   - `direct`: use zero specialists for tiny or small work and for larger work whose questions are not independently investigable;
   - `coordinate`: use the minimum useful bounded investigations for medium or large work when their expected value exceeds coordination cost;
   - `decompose`: hand epic work to `$solo-dev-scope` for one testable milestone and stop before wholesale implementation.
5. Resolve material ambiguity through `$clarify-intent`. Do not use delegation to avoid a user decision that only the user can make.
6. When coordinating, read [coordination-contracts.md](references/coordination-contracts.md). Define non-overlapping read-only assignments, normally one to three, and continue useful lead work while they run.
7. Synthesize observations, disagreements, evidence strength, unknowns, and trade-offs. Decide against the user's outcome, repository constraints, reversibility, risk, and solo-maintenance burden; specialists do not decide scope.
8. Produce the smallest decision-complete plan and route each next boundary to its existing owner. Do not copy those skills' procedures into this workflow.
9. After authorized implementation, select only relevant evidence and review boundaries. A separate reviewer is warranted for medium or large changes and high-risk overrides when available; otherwise label the result as self-review.
10. Before an expected context break, emit a compact continuity payload. In a managed repository, route an authorized batch closeout to `$finish-work`; otherwise persist only when the user authorized durable documentation and `$documentation` identifies the canonical record.
11. When a project reveals a potentially reusable lesson, emit a promotion proposal with origin evidence, a generalized claim, domain-specific limits, and overlap with current guidance. Stop before changing `solo-dev-core`.

## Strategy Heuristics

- Delegate when two or more questions can be answered independently, distinct technical domains need evidence, credible options need adversarial comparison, or a risk warrants a separate reviewer perspective.
- Work directly when the change is local and obvious, all investigations need the same context, specialists would duplicate work, or integration cost exceeds expected information gain.
- Prefer read-only analysis in parallel. Never assign overlapping writers.
- When subagents are unavailable, investigate the same bounded questions serially and state that the passes were not independent.
- Classification changes process, not scope. High risk adds relevant evidence or review; it does not authorize unrelated work.

## Evidence

- Objective, constraints, classification drivers, risk overrides, and repository evidence identified.
- Direct, coordinate, or decompose strategy justified in proportion to the task.
- Delegated findings tied to bounded evidence and separated from inference and unknowns.
- Conflicts resolved explicitly by the lead rather than averaged or silently ignored.
- Existing skills selected only for boundaries their contracts own.

## Output Contract

Scale the output to the work. For coordinated or decomposed tasks, report:

- Objective, success signal, constraints, and non-goals.
- Size, risk, material drivers, and chosen strategy.
- Direct-work rationale or specialist assignments and why each is useful.
- Synthesis: agreements, conflicts, evidence strength, unknowns, decision, and rejected alternatives.
- Decision-complete plan, relevant quality or review boundaries, and existing skills selected next.
- Continuity payload when a context break is likely.
- `Verified`, `Not verified`, and `Residual risk` when implementation or validation occurred.

For tiny direct work, keep classification implicit unless it explains an important decision.

## Stop Conditions

- Stop before mutation when authority is missing or a material user decision remains unresolved.
- Stop epic work after selecting one milestone; do not implement an undifferentiated program.
- Stop delegating when another investigation would repeat evidence or add more integration cost than information.
- Stop before a specialist edits files, expands scope, or mutates external state.
- Stop before calling self-review independent review.
- Stop before persisting continuity or changing shared guidance without explicit authorization.

## Composition

- Use `$start-work` for a managed-repository resumption and `$repo-compass` for other missing repository context; neither is a mandatory first step.
- Use `$solo-dev-scope` for epic decomposition and `$clarify-intent` for unresolved decisions.
- Route authorized changes to `$implement-change` or another existing mutation owner.
- Route claim evidence to `$test-and-verify`, bounded defect review to `$review-changes`, structural assessment to `$architecture-review`, and a named readiness verdict to `$ship-check`.
- Use `$finish-work` for an authorized managed-repository closeout and `$documentation` for other authorized continuity or decision records.

## Anti-Patterns

- Running every task through this skill.
- Treating file count, estimated duration, or a numeric score as the classification.
- Creating permanent role agents or one skill per specialist perspective.
- Delegating several versions of the same investigation.
- Letting specialists make scope decisions or merge conflicting advice.
- Duplicating verification, review, readiness, or project-memory contracts.
- Automatically converting future ideas or reusable lessons into current scope.
