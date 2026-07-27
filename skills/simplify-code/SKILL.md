---
name: simplify-code
description: Use when the user asks to simplify, reduce, consolidate, delete, de-layer, or make existing code easier to maintain while preserving externally observable behavior; establish a behavior baseline, identify removable branches, layers, duplication, dependencies, or indirection, recommend the smallest reduction, and require evidence that the result is both behavior-preserving and genuinely simpler.
---

# Simplify Code

Reduce maintenance burden without turning simplification into a redesign.

## Boundaries

- Use for existing code whose behavior should remain stable while implementation complexity is reduced.
- Do not use for bounded diff defect review, open-ended architecture assessment, feature implementation, or cosmetic rewrites.
- Remain read-only for assessment requests. Apply changes only when the user explicitly asks for simplification or approves the proposed reduction.

## Workflow

1. Define the code boundary, externally observable behavior, public interfaces, and constraints that must remain stable.
2. Inspect call sites, tests, runtime configuration, and ownership boundaries before proposing changes.
3. Establish a practical behavior baseline, including a meaningful failure path.
4. Identify concrete maintenance burden: obsolete code, duplicate behavior, needless branches, pass-through layers, speculative abstractions, unnecessary files, or avoidable dependencies.
5. Rank deletion and consolidation opportunities by benefit, behavior risk, migration cost, and verification strength.
6. Recommend the smallest coherent simplification and state explicit non-goals. Do not use arbitrary line, function, or module size limits as the justification.
7. For read-only requests, stop with the recommendation and evidence.
8. For authorized mutation, hand the bounded plan to `$implement-change`.
9. Compare the before and after structure using concrete removals and retained behavior, then verify through `$test-and-verify`.

## Evidence

- Baseline behavior, public interfaces, call sites, and relevant tests inspected.
- Specific burden tied to realistic maintenance or failure cost.
- Before-and-after evidence such as removed code paths, layers, dependencies, files, or duplicate implementations.
- Fresh behavior and failure-path verification after mutation.

## Output Contract

- Simplification boundary and behavior that must remain stable.
- Concrete maintenance burden.
- Recommended reduction, non-goals, and rejected broader changes.
- Before-and-after structural comparison when implemented.
- Verification, compatibility impact, and `Verified`, `Not verified`, and `Residual risk`.

## Stop Conditions

- Stop when required behavior or public-interface expectations are unknown.
- Stop when the proposed work becomes a feature, migration, broad architecture redesign, or unrelated cleanup.
- Stop before mutation when the evidence does not show that the result will be simpler.

## Composition

- Use `$review-changes` instead for defect review of a bounded diff.
- Use `$architecture-review` when the question is primarily about system boundaries, ownership, deployment topology, or component existence.
- Hand authorized changes to `$implement-change`, then use `$test-and-verify`.
- Use `$ship-check` only when the simplified change needs an explicit readiness verdict.

## Anti-Patterns

- Reformatting or renaming code without reducing a demonstrated burden.
- Replacing one abstraction with several smaller abstractions.
- Measuring simplicity only by line counts or file size.
- Changing public behavior to make the implementation easier.
- Adding compatibility layers that leave the old and new paths alive indefinitely.
