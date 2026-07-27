---
name: roadmap-review
description: Use when periodically reviewing, pruning, deduplicating, or reprioritizing Next, Future Ideas, Deferred, or Abandoned work in docs/PROJECT.md; inspect current implementation and milestone evidence, detect obsolete ideas and satisfied dependencies or reconsideration triggers, infer REVIEW or APPLY mode, recommend justified state movements, and never promote an item into Active solely because it is interesting.
---

# Roadmap Review

Reassess future and deferred work without expanding current scope by momentum.

## Boundaries

- Use for explicit roadmap reviews, future-idea cleanup, deferred-work reassessment, and dependency-trigger checks.
- Infer `REVIEW` for recommendations only and `APPLY` when the user asks to update the canonical project record.
- In `APPLY`, modify only `docs/PROJECT.md` and accepted durable ADRs. Do not change implementation.
- Never promote an item into Active without an explicit milestone decision and evidence that it belongs in the approved milestone.

## Scope States

- `Active`: approved work required by the current milestone.
- `Next`: the probable next milestone, supported by a clear sequencing reason.
- `Future`: valuable but uncommitted work with a reconsideration trigger.
- `Deferred`: intentionally postponed work whose value may remain.
- `Abandoned`: explicitly rejected work retained only when its history prevents repeated rediscovery.

## Workflow

1. Read applicable instructions and `docs/PROJECT.md`. Route missing initial project memory to `$adopt-project`.
2. Infer `REVIEW` or `APPLY` from the request. Do not mutate merely because review findings are obvious.
3. Use `$project-status` in `CHECK` mode to inspect Current Milestone progress, current implementation, risks, Last Verified freshness, and material drift.
4. Inventory Next, Future Ideas, Deferred, and Abandoned entries with their IDs, intent, value, dependencies, triggers, reasons, decisions, and related components.
5. Deduplicate entries by underlying outcome and dependency, not title alone. Preserve the strongest value statement, evidence, trigger, and history under one stable ID.
6. Identify obsolete ideas when the need disappeared, the implementation already satisfies it, a decision rejected it, the product boundary changed, or the expected value no longer justifies its burden.
7. Check whether dependencies or reconsideration triggers are satisfied. Mark semantic or externally unverified triggers as potentially satisfied rather than proven.
8. Recommend state changes only with a clear reason:
   - Future to Next when it is the justified probable next milestone;
   - Next to Future when sequencing or evidence weakened;
   - Future or Deferred to Deferred when postponement is intentional;
   - any non-Active item to Abandoned when rejection history matters;
   - deletion only when the user explicitly requests it and no historical value remains.
9. Require an explicit milestone decision before any move to Active. State which current success condition, dependency, or risk justifies the change and what existing Active scope would be displaced.
10. Do not create an ADR for ordinary prioritization. Identify an ADR only when the review settles a durable product boundary, compatibility, data, deployment, or architecture decision whose rationale will matter later.
11. In `APPLY`, use `$documentation` to make the smallest coherent state changes, preserve stable IDs and links, retain unresolved uncertainty, and keep one Exact Next Action.
12. Run `../adopt-project/scripts/project-memory validate-project --repo <repository>` after an update, resolving the path from this skill directory.

## Evidence

- Current milestone progress, implementation state, validation freshness, and roadmap entries inspected.
- Duplicate, obsolete, satisfied-trigger, and state-movement findings tied to evidence.
- Active promotion requires explicit approval and a milestone or dependency justification.
- Applied project-memory changes validate and do not touch implementation files.

## Output Contract

- Mode: `REVIEW` or `APPLY`.
- Duplicate groups and proposed canonical entries.
- Obsolete, satisfied, potentially satisfied, and still-blocked items.
- Recommended movements among Next, Future, Deferred, and Abandoned with reasons.
- Active-promotion decisions explicitly approved, blocked, or not proposed.
- ADR candidates, uncertainty, files changed, validation result, and one exact next action.

## Stop Conditions

- Stop and route to `$adopt-project` when no canonical project record exists.
- Stop before mutation in `REVIEW`.
- Stop before moving anything to Active without an explicit milestone decision.
- Stop before deleting historical entries without explicit authorization.
- Stop after the validated roadmap update or recommendation set; implementation is separate.

## Composition

- Use `$project-status` in `CHECK` mode for current evidence.
- Route missing project memory to `$adopt-project`.
- Use `$documentation` only in `APPLY`.
- Receive individually captured ideas from `$capture-idea`.
- Hand an approved milestone change to `$clarify-intent` when implementation planning is still materially ambiguous.

## Anti-Patterns

- Promoting an item because it is exciting, easy, or recently discussed.
- Treating a prose trigger as satisfied without evidence.
- Turning Future Ideas into an undifferentiated backlog.
- Rewriting stable IDs or erasing rejected-decision history casually.
- Creating ADRs for ordinary sequencing choices.
- Changing implementation during roadmap review.
