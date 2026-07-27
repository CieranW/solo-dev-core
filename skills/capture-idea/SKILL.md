---
name: capture-idea
description: Use when a product, architecture, operational, or technical idea arises during other work and should be preserved without implementation, roadmap promotion, or active-milestone expansion; inspect docs/PROJECT.md and related evidence, detect duplicate or related ideas, add one structured Future Idea with value, dependencies, a concrete reconsideration trigger and reason deferred, leave Active and Next unchanged, and return to the previously active task.
---

# Capture Idea

Preserve a useful idea without letting it hijack the current milestone.

## Boundaries

- Use for ideas that are valuable enough to retain but are not approved Active work.
- Modify only the canonical `docs/PROJECT.md` Future Ideas section.
- Do not change Current Milestone, Active Work, Next, application code, architecture, dependencies, or Git state.
- Do not plan, prototype, research deeply, or implement supporting architecture "just in case."

## Workflow

1. Record the task and exact next action that were active before idea capture so they can be resumed.
2. Read applicable instructions and `docs/PROJECT.md`. Route missing initial project memory to `$adopt-project`.
3. Inspect the Current Milestone, Product Boundaries, Active Work, Next, existing Future Ideas, Deferred items, Decisions, and related implementation components.
4. Search existing idea titles, descriptions, dependencies, reconsideration triggers, ADRs, and related components for a duplicate or a narrower expression of the same intent.
5. When the idea is a duplicate, update the existing entry only with genuinely new value, dependency, trigger, or relationship evidence. Do not create another entry.
6. When it is distinct, create one `FI-YYYYMMDD-short-title` entry under Future Ideas with:
   - Idea;
   - Value;
   - Dependencies;
   - Reconsider when;
   - Why deferred;
   - Related decisions or components;
   - Captured.
7. Make the reconsideration trigger concrete and observable. Prefer a dependency completion, measured threshold, owner decision, date, or repeated-cost signal over "when there is time."
8. State why the idea is not active now in terms of the approved milestone, missing evidence, unsatisfied dependency, operational burden, or opportunity cost.
9. Preserve links to related ADRs and components without writing a speculative design. Capturing an idea is not itself an architecture decision.
10. Use `$documentation` for the narrow edit and run `../adopt-project/scripts/project-memory validate-project --repo <repository>`, resolving the path from this skill directory.
11. Confirm Current Milestone, Active Work, and Next did not change.
12. Return the captured ID or updated duplicate, then restate the original task and its exact next action.

## Evidence

- Current scope, existing ideas, deferred work, decisions, and related components inspected.
- Duplicate decision supported by title, intent, dependency, trigger, or component overlap.
- New entry contains every required field and a concrete reconsideration trigger.
- Project memory validates and Active, Next, and implementation files remain unchanged.

## Output Contract

- Result: new Future Idea ID or existing entry updated.
- Duplicate and related-item assessment.
- Value, dependencies, reconsideration trigger, and reason deferred.
- Files changed and project-memory validation result.
- Explicit confirmation that Active, Next, implementation, commit, and push state were unchanged.
- Original task and exact action to resume.

## Stop Conditions

- Stop and route to `$adopt-project` when no canonical project record exists.
- Stop before capture when the idea is actually required to complete the approved milestone; classify that as current-scope clarification instead.
- Stop before changing Active or Next without an explicit milestone or roadmap decision.
- Stop after the validated entry and resumption handoff.

## Composition

- Route missing project memory to `$adopt-project`.
- Use `$project-status` in `CHECK` mode only when stale state prevents trustworthy scope classification.
- Use `$documentation` for the Future Ideas edit.
- Hand periodic deduplication, obsolescence, and state movement to `$roadmap-review`.
- Never invoke `$implement-change` from idea capture.

## Anti-Patterns

- Implementing a small part of the idea while "only capturing" it.
- Adding foundations, interfaces, or dependencies for possible future use.
- Copying the same idea under several names.
- Using vague value, dependency, or "someday" trigger text.
- Moving the idea into Next because it sounds compelling.
- Forgetting to return to the interrupted task.
