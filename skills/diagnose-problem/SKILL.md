---
name: diagnose-problem
description: Use when the user asks to diagnose, investigate, explain, or find the root cause of a bug, functional regression, flaky test, incident, unexpected behavior, or an unclassified performance symptom; reproduce safely, separate evidence from hypotheses, isolate the causal boundary, assess impact, and recommend the smallest fix without implementing unless requested, while handing measured resource bottlenecks to profile-performance.
---

# Diagnose Problem

Find the cause before changing the system.

## Boundaries

- Use for unexpected behavior whose causal boundary or root cause is not established.
- Do not use for a known performance bottleneck that needs profiling, a bounded diff review, or implementation of an already-approved fix.
- Keep diagnosis read-only unless the user explicitly requests the fix.

## Workflow

1. Define the expected behavior, observed behavior, frequency, affected environment, and known time boundary.
2. Inspect applicable instructions, current state, recent relevant changes, logs, tests, configuration, and dependencies before forming conclusions.
3. Reproduce the symptom with the smallest safe case. Do not mutate production data, external systems, or irreversible state merely to reproduce.
4. Record observed evidence separately from assumptions. Rank plausible hypotheses and define the cheapest falsifying check for each.
5. Test one causal boundary at a time across inputs, control flow, data flow, configuration, persistence, integrations, and runtime behavior.
6. Identify the root cause, contributing conditions, and downstream symptoms separately. If the evidence supports only a likely cause, state the confidence and missing proof.
7. Assess blast radius: affected users, data, commands, environments, versions, and adjacent behavior.
8. Apply the mutation gate:
   - For diagnosis or explanation requests, stop after the evidence-backed diagnosis and fix recommendation.
   - When the user explicitly requests a fix, implement the smallest root-cause correction that preserves unrelated behavior.
9. For implemented fixes, add or run regression evidence through `$test-and-verify`, including the original reproduction and a meaningful failure path.

## Evidence

- Label facts as observed, inferred, or still unknown.
- Prefer a minimal reproduction over a broad speculative investigation.
- Preserve failing output, inputs, versions, seeds, and timing details needed to reproduce.
- Do not call a hypothesis the root cause merely because a rerun passed or a nearby change looks suspicious.
- Stop and report the evidence gap when safe reproduction or required visibility is unavailable.

## Output Contract

Report:

- Expected and observed behavior.
- Reproduction status and exact evidence.
- Root cause and confidence.
- Contributing conditions and blast radius.
- Smallest recommended fix and regression check.
- Files or external state changed, or an explicit statement that diagnosis remained read-only.
- `Verified`, `Not verified`, and `Residual risk`.

## Stop Conditions

- Stop and report uncertainty when safe reproduction, logs, data, or required visibility are unavailable.
- Stop after the diagnosis and fix recommendation when implementation was not requested.
- Stop before shotgun edits or a broader refactor that is not required by the demonstrated cause.

## Composition

- Use `$profile-performance` after the symptom is reproducible and the question becomes where time or resources are consumed.
- Hand an authorized root-cause fix to `$implement-change`.
- Use `$test-and-verify` for regression evidence after a fix.
- Use `$review-changes` only when the request is to review a bounded proposed change.

## Anti-Patterns

- Making shotgun edits before reproducing the problem.
- Confusing correlation, a symptom, or a passing rerun with causation.
- Blaming environment, concurrency, or user error without evidence.
- Expanding a diagnosis into an unauthorized refactor.
- Hiding an incomplete diagnosis behind confident language.
