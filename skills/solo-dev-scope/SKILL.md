---
name: solo-dev-scope
description: Use for broad feature ideas, app/site/tool requests, product concepts, or tasks likely to balloon; reduce the idea to one testable first milestone with a proof signal, effort ceiling, timebox, kill condition, constraints, non-goals, deferred work, operational tradeoffs, and observable acceptance criteria for a solo developer.
---

# Solo Dev Scope

Use this skill to keep work valuable, small, and maintainable for one developer.

## Boundaries

- Use for broad product, feature, app, site, or tool ideas whose first increment is not yet safely bounded.
- Do not use for a decision-ready implementation, a local bug, a bounded diff, or routine maintenance.
- Keep the workflow read-only; it selects a milestone rather than implementing one.

## Workflow

1. Identify the user's real outcome and the observable signal that would prove the idea is useful.
2. Inspect known product, repository, time, budget, and operational constraints before proposing scope.
3. Set an effort ceiling and a realistic timebox before expanding the design. Shrink the milestone if it cannot fit.
4. Define a kill or pivot condition: the missing proof, unacceptable burden, or elapsed effort that should stop further investment.
5. Select the smallest end-to-end slice that produces the proof signal; do not define an MVP as a disconnected collection of components.
6. Separate the core workflow from polish, scale, automation, integrations, and speculative extensibility.
7. Define one first milestone that can be built, tested, operated, and understood in one pass.
8. Include operational burden in decisions: auth, payments, hosting, background jobs, migrations, observability, data ownership, support, and recovery.
9. State non-goals and deferred work explicitly. Include the evidence or trigger that would justify revisiting important deferred work.
10. Prefer boring, maintainable choices over expansive architecture.
11. Write observable acceptance criteria, including a meaningful failure or recovery path when relevant.
12. When implementation planning is requested, hand the narrowed milestone to `$clarify-intent` for a decision-complete plan.

## Evidence

- User outcome and observable proof signal identified.
- Relevant time, budget, repository, product, and operational constraints inspected.
- Effort ceiling, timebox, kill condition, non-goals, and revisit triggers stated.
- Acceptance criteria cover one end-to-end workflow and a meaningful failure or recovery path.

## Output Contract

For scoped work, provide:

- Core user outcome.
- Proof signal.
- Relevant constraints.
- Effort ceiling and timebox.
- Kill or pivot condition.
- First milestone.
- Non-goals.
- Deferred work and revisit triggers.
- Acceptance criteria.
- Operational burden accepted.
- Key tradeoff chosen and why.

## Stop Conditions

- Stop once one testable end-to-end milestone fits the effort ceiling.
- Stop and shrink again when the proposed milestone still contains several independent products or workflows.
- Stop before implementation; planning continues through `$clarify-intent` only when requested.

## Composition

- Use `$repo-compass` first when repository or operating context is missing.
- Hand the selected milestone to `$clarify-intent` for decision-complete planning.
- Do not invoke implementation, review, verification, or shipping skills during scoping alone.

## Anti-Patterns

- Designing a platform when a focused tool is enough.
- Calling a component inventory an MVP without an end-to-end user workflow.
- Continuing past the effort ceiling without new evidence or an explicit rescope.
- Adding accounts, billing, dashboards, or automation before the first workflow works.
- Hiding operational complexity.
- Letting visuals or architecture drive scope instead of the user outcome.
