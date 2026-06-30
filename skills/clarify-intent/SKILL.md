---
name: clarify-intent
description: Use when a request has ambiguous goal, scope, success criteria, constraints, audience, tradeoffs, ownership, or implementation intent; inspect discoverable context first, ask only high-impact questions, and block mutating work when material ambiguity remains.
---

# Clarify Intent

Use this skill to turn a fuzzy request into a safe, actionable task.

## Workflow

1. Inspect discoverable context first: files, configs, docs, current state, prior messages, and available tools that can answer factual questions.
2. Separate discoverable facts from preference/tradeoff questions.
3. Ask only questions whose answers materially change the work, risk, scope, or output.
4. Prefer one concise question at a time; use concrete options when the decision has clear tradeoffs.
5. Restate the working goal, in-scope work, out-of-scope work, constraints, and success criteria before mutating files or external state.
6. If the task is low-risk and ambiguity is minor, proceed with explicit assumptions.
7. If material ambiguity remains, do not implement; ask or propose a decision-complete plan.

## Output Contract

When clarification is needed, include:

- What is already known from context.
- The one to three decisions that matter now.
- The recommended default when the user does not answer.

Before implementation, state:

- Goal.
- Success criteria.
- Scope boundaries.
- Assumptions.

## Anti-Patterns

- Asking where something is before searching for it.
- Treating a product preference as a repo fact.
- Implementing broad ideas before success criteria are known.
- Asking many low-value questions that do not change the work.
