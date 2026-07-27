---
name: architecture-review
description: Use when the user asks for an architecture, system-design, module-boundary, dependency, ownership, data-flow, deployment-topology, coupling, or operational-complexity assessment of an existing system; examine whether components should exist, move, merge, split, or be deleted, report evidence-backed structural recommendations, and remain read-only unless implementation is separately requested.
---

# Architecture Review

Assess whether the current structure supports the system's real responsibilities and operating constraints.

## Boundaries

- Use for existing-system structure that spans components, modules, services, data flows, ownership, deployments, or operational boundaries.
- Do not use for defect review of a bounded diff, feature design before requirements are clear, local code simplification, or implementation.
- Keep the review read-only. A request to apply recommendations must cross into a separately bounded implementation workflow.

## Workflow

1. Define the system boundary, decision being supported, current constraints, and desired qualities.
2. Read applicable guidance and inspect the smallest useful structural evidence: entrypoints, module or service boundaries, dependency declarations, interfaces, schemas, deployment configuration, and operations docs.
3. Map responsibilities, ownership, control flow, data flow, state, external integrations, and deployment/runtime boundaries.
4. Identify concrete coupling, duplicated ownership, hidden shared state, circular dependencies, coordination cost, failure propagation, and operational burden.
5. Ask whether each component should exist in its current form and location. Evaluate deletion, merging, movement, or splitting only against demonstrated constraints.
6. Compare the smallest viable options, including retaining the current structure, and state trade-offs and migration risk.
7. Recommend an ordered, bounded direction with non-goals and decision triggers for deferred work.
8. Report the evidence gap where runtime behavior, ownership, or operational constraints are not observable.

## Evidence

- Structural recommendations tied to actual source, configuration, dependency, data-flow, deployment, or operational evidence.
- Current and proposed responsibilities and ownership made explicit.
- Trade-offs, migration constraints, and retained-current-state option assessed.
- Facts, inference, and unknowns separated.

## Output Contract

- Review boundary and decision supported.
- Current responsibility, dependency, data-flow, and deployment map.
- Evidence-backed structural findings.
- Options considered, recommended direction, and non-goals.
- Migration or operational risks, unknowns, and explicit read-only status.

## Stop Conditions

- Stop when the system boundary or supported decision is too ambiguous to evaluate safely.
- Stop before editing files, moving components, changing deployments, or beginning migrations.
- Stop expanding once the requested structural decision has enough evidence; do not turn the review into a complete platform redesign.

## Composition

- Use `$clarify-intent` when the supported decision or constraints are materially ambiguous.
- Use `$review-changes` for a bounded code or pull-request diff.
- Use `$simplify-code` for local behavior-preserving complexity reduction.
- Hand an approved structural change to `$implement-change`, followed by `$test-and-verify`.
- Use `$ship-check` only when a concrete change is being judged for a named shipping boundary.

## Anti-Patterns

- Reviewing architecture without a decision or system boundary.
- Treating diagram neatness, file size, or service count as proof of quality.
- Recommending microservices, platforms, queues, registries, or shared frameworks without operational evidence.
- Ignoring ownership, deployment, data migration, recovery, or support burden.
- Applying recommendations during a review-only request.
