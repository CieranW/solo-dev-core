---
name: solo-dev-scope
description: Use for broad feature ideas, app/site/tool requests, product concepts, or tasks likely to balloon; reduce the idea to the smallest useful version with clear non-goals, first milestone, deferred work, and acceptance criteria for a solo developer.
---

# Solo Dev Scope

Use this skill to keep work valuable, small, and maintainable for one developer.

## Workflow

1. Identify the user's real outcome and the smallest version that proves it.
2. Separate core workflow from nice-to-have surface area.
3. Define one first milestone that can be built, tested, and understood in one pass.
4. State non-goals and deferred work explicitly.
5. Prefer boring, maintainable choices over expansive architecture.
6. Include operational burden in decisions: auth, payments, hosting, background jobs, migrations, observability, and support.
7. Convert the scope into acceptance criteria before implementation.

## Output Contract

For scoped work, provide:

- Core user outcome.
- First milestone.
- Non-goals.
- Deferred list.
- Acceptance criteria.
- Key tradeoff chosen.

## Anti-Patterns

- Designing a platform when a focused tool is enough.
- Adding accounts, billing, dashboards, or automation before the first workflow works.
- Hiding operational complexity.
- Letting visuals or architecture drive scope instead of the user outcome.
