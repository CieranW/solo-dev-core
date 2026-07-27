---
name: profile-performance
description: Use when the user asks to profile, benchmark, optimize, or explain measured latency, throughput, CPU, memory, GPU, I/O, model-loading, startup, or resource-consumption problems; establish a representative baseline, select appropriate measurement tools, locate the bottleneck, compare safe options, and require equivalent before-and-after evidence before recommending or claiming an improvement.
---

# Profile Performance

Measure where time or resources are consumed before changing the system.

## Boundaries

- Use for performance and resource questions that require measurements, profiles, traces, benchmarks, or controlled load.
- Do not use for general functional bugs, bounded diff review, speculative capacity architecture, or unmeasured micro-optimization.
- Keep investigation read-only. Apply an optimization only when explicitly requested and only after evidence identifies a bottleneck.

## Workflow

1. Define the affected metric, expected level, observed level, workload, environment, and material resource constraints.
2. Reproduce the complaint safely. If the symptom or causal boundary is still ambiguous, use `$diagnose-problem` first.
3. Establish a representative baseline with stable inputs, warm-up policy, sample size, variance, and relevant runtime or hardware context.
4. Choose the least intrusive tool that can distinguish the leading hypotheses: timing, sampling profiler, allocator or memory profiler, GPU profiler, I/O trace, distributed trace, or controlled load test.
5. Measure one boundary at a time and locate the dominant cost. Separate bottlenecks from downstream waiting and measurement overhead.
6. Check common high-cost behavior as relevant: repeated model loading, unnecessary copies or conversions, blocking work, unbounded buffers, serialization, synchronization, network/storage waits, and CPU/GPU transfers.
7. Compare improvement options by expected effect, implementation cost, correctness risk, operational impact, and rollback path.
8. For analysis-only requests, stop with the evidence-backed recommendation.
9. For explicit optimization requests, hand the smallest selected change to `$implement-change`.
10. Repeat the same benchmark or profile after the change and run correctness regression checks through `$test-and-verify`.

## Evidence

- Reproduction and baseline commands, inputs, environment, and measurement conditions.
- Raw or summarized profile evidence identifying the dominant cost.
- Before-and-after results collected under equivalent conditions, including variance or limitations.
- Correctness checks showing the optimization did not change required behavior.

## Output Contract

- Metric, workload, environment, and baseline.
- Bottleneck and confidence.
- Tools used and measurement limitations.
- Options considered and selected recommendation.
- Before-and-after comparison when a change was implemented.
- Correctness evidence, rollback note, and `Verified`, `Not verified`, and `Residual risk`.

## Stop Conditions

- Stop when a safe representative baseline cannot be established; report the evidence gap instead of optimizing.
- Stop before production load, destructive tracing, costly cloud/GPU work, or privileged profiling that lacks authorization.
- Stop before implementation when no dominant bottleneck is supported by evidence.

## Composition

- Use `$diagnose-problem` first when the complaint may be a functional bug or has no reproducible boundary.
- Hand evidence-backed changes to `$implement-change`.
- Use `$test-and-verify` for correctness evidence and `$ship-check` only for an explicit readiness decision.
- Use `$architecture-review` for structural capacity or deployment-topology questions not answered by profiling.

## Anti-Patterns

- Optimizing from intuition without a baseline.
- Comparing different workloads, environments, warm-up states, or measurement modes as before and after.
- Reporting average latency when tail behavior is the complaint.
- Trading maintainability or correctness for an unmeasured micro-optimization.
- Treating profiler overhead, downstream waiting, or a single noisy run as the bottleneck.
