---
name: clarify-intent
description: Use when a request is ambiguous or needs a decision-complete plan before implementation, including unclear goals, scope, success criteria, constraints, audience, tradeoffs, ownership, or execution approach; inspect discoverable context, ask only high-impact questions, define boundaries and verification, and block mutating work only while material ambiguity remains.
---

# Clarify And Plan

Turn a fuzzy request into a safe, actionable task and the smallest plan needed to execute it.

## Boundaries

- Use for material ambiguity, decision-complete planning, or comparing implementation options before mutation.
- Do not use to shrink a platform-sized idea, diagnose a failure, review a diff, or reopen decisions after an implementation-ready plan exists.
- Keep planning read-only unless the user also requested implementation and all material decisions are resolved.

## Workflow

1. Inspect discoverable context first: files, configs, docs, current state, prior messages, and available tools that can answer factual questions.
2. Determine whether the user wants advice, a plan, implementation, or a combination. Treat an explicit implementation request as authority to continue once the task is decision-ready.
3. Separate discoverable facts from preference and tradeoff decisions. Do not ask the user for facts that inspection can establish. Treat "use your judgment" as delegated preference authority, not permission to invent missing technical or operational constraints.
4. Define the working outcome, success criteria, scope boundaries, constraints, and material unknowns.
5. For a broad product or feature idea likely to balloon, use `$solo-dev-scope` to select one valuable first milestone, then resume planning here.
6. Ask only questions whose answers materially change the work, risk, scope, or output. When blocked, ask one decision at a time, starting with the answer that reduces the most downstream uncertainty. Do not bundle independent scope, integration, and preference decisions into one question. Include a recommended default when useful.
7. If ambiguity is minor and risk is low, proceed with explicit, reversible assumptions.
8. Produce the smallest decision-complete plan: ordered outcomes, affected areas, dependencies, verification, and meaningful risks. When a real trade-off remains, compare only the credible options, recommend the smallest adequate design, and explain why. Avoid speculative file lists, architecture, or stack choices before the existing environment, integration boundaries, and operating constraints support them.
9. Apply the mutation gate:
   - If the user requested clarification or planning only, stop after the plan.
   - If the user requested implementation and the plan is decision-ready, continue without asking for redundant confirmation.
   - If a material decision remains unresolved, stop before mutation and ask for that decision.
10. Persist the plan only when the work spans multiple sessions or owners, the user requests a durable artifact, or losing context would be costly. Otherwise keep the plan inline.

## Decision Readiness

A task is decision-ready when:

- The desired outcome and observable success criteria are clear.
- In-scope and out-of-scope work are bounded enough to prevent material surprise.
- Required constraints, authority, and irreversible choices are known.
- Remaining assumptions are low-risk, explicit, and recoverable.
- The next action and its verification path are concrete.

## Plan Persistence

For durable plans:

- Prefer an existing issue, plan, or decision document over creating a new source of truth.
- Use `$documentation` to record the outcome, scope, non-goals, decisions, assumptions, verification path, owner or context, and current status.
- Maintain a compact checkpoint with completed work, current work, blockers, changed decisions, verification evidence, and the exact next action.
- Refresh the checkpoint after a material milestone and before a handoff or expected context break.
- Mark durable plan state complete or archive it according to repository convention. Do not delete durable records unless the user explicitly asks.

Do not create plan documents for small, single-session tasks.

## Evidence

- Discoverable repository and operating context inspected before asking questions.
- Outcome, success criteria, constraints, scope, and non-goals stated.
- Material decisions resolved or surfaced explicitly with their consequences.
- Verification path matched to the planned behavior.

## Output Contract

When blocked on clarification, include:

- What is already known from context.
- The decision that matters now and why it changes the work.
- The recommended default and its tradeoff.

When decision-ready, scale the response to the task and include:

- Outcome and success criteria.
- Scope and non-goals.
- Decisions and assumptions.
- Ordered implementation plan.
- Verification approach.
- Risks, dependencies, or unresolved low-risk unknowns.
- Next action: stop at the plan or continue with implementation.

## Stop Conditions

- Stop before mutation when the user requested planning only or a material decision remains unresolved.
- Stop asking once the task is decision-ready; do not require redundant approval for already-authorized implementation.
- Stop expanding the plan when the requested outcome has a safe, verifiable path.

## Composition

- Receive repository facts from `$repo-compass`.
- Use `$solo-dev-scope` first when the request is too large for one safe milestone.
- Own implementation-option comparison; do not create or invoke a separate design-first workflow.
- Hand decision-ready mutation to `$implement-change` and evidence gathering to `$test-and-verify`.

## Anti-Patterns

- Asking where something is before searching for it.
- Treating a product preference as a repo fact.
- Choosing a stack before discovering the existing environment and integration boundaries.
- Planning around an unresolved decision that would materially change the plan.
- Producing platform-sized plans for small tasks.
- Creating durable plan artifacts for work that can finish in one session.
- Asking many low-value questions that do not change the work.
- Bundling several independent decisions into one clarification question.
- Asking for confirmation after the user already authorized implementation and no material ambiguity remains.
