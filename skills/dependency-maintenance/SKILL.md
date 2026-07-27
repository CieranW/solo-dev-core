---
name: dependency-maintenance
description: Use when the user asks to update, upgrade, refresh, pin, audit, or remediate dependencies, packages, runtimes, manifests, or lockfiles; inspect repository policy and the resolved graph, verify current versions and advisories from authoritative sources, choose the smallest coherent update, assess compatibility and migrations, preserve lockfile integrity, verify behavior, define rollback, and apply changes only when explicitly requested.
---

# Dependency Maintenance

Make dependency changes small, evidence-backed, and reversible.

## Boundaries

- Use for package, runtime, manifest, lockfile, compatibility, license, or dependency-advisory work.
- Do not use for feature implementation, unrelated repository cleanup, or release publication.
- Keep audits and recommendations read-only. Mutate only when an update, upgrade, pin, refresh, or remediation was explicitly requested.

## Workflow

1. Read applicable repository instructions and inspect manifests, lockfiles, package-manager configuration, runtime constraints, current branch, and dirty worktree state.
2. Classify the intent: targeted security remediation, compatibility fix, runtime migration, routine maintenance, or requested version adoption.
3. Establish the current resolved versions and a practical baseline install, build, or test result before updating when feasible.
4. Research candidate versions using current authoritative release notes, security advisories, compatibility matrices, and registry metadata. Record the relevant version and publication context; do not rely on memory for current facts.
5. Choose the smallest coherent update set that satisfies the request. Keep unrelated direct dependencies unchanged and explain unavoidable transitive movement.
6. Read breaking changes and migration guidance. Check runtime support, peer dependencies, native modules, plugins, APIs, configuration, licenses, and deployment constraints as relevant.
7. Apply the mutation gate:
   - For audit, recommendation, or plan-only requests, stop after the evidence-backed update plan.
   - For explicit update, upgrade, refresh, pin, or remediation requests, continue with the smallest authorized change.
8. Update through the repository's existing package manager and lockfile workflow. Do not hand-edit generated lockfiles or mix package managers.
9. Inspect manifest and lockfile diffs for unexpected version drift, source changes, install scripts, removed integrity data, or excessive transitive churn.
10. Run targeted verification for the affected dependency boundary, then the practical broader suite through `$test-and-verify`.
11. Confirm the resolved dependency graph contains the intended versions. Do not claim an advisory is fixed from a manifest range alone.
12. State rollback: prior manifest constraints, lockfile restoration path, migration reversal, and any data or configuration compatibility limit.

## Security Remediation

- Verify the advisory identifier, affected range, fixed range, exploit conditions, and whether the vulnerable package is reachable in this repository.
- Prefer the nearest non-breaking fixed version when it satisfies repository constraints.
- If no compatible fix exists, report mitigations and the exact upgrade blocker instead of forcing unrelated major upgrades.
- Never expose private registry credentials, tokens, or full sensitive configuration in output.

## Evidence

- Applicable repository policy, manifests, lockfiles, resolved graph, runtime constraints, and baseline inspected.
- Current version, candidate version, advisories, compatibility, and migrations checked against authoritative current sources.
- Manifest and lockfile diff reviewed for direct and transitive churn.
- Resolved post-update graph and targeted behavior verified after mutation.

## Output Contract

For every request, report:

- Maintenance intent and authoritative evidence reviewed.
- Current and proposed versions.
- Breaking changes, migrations, runtime constraints, or license impact.
- Rollback path, blockers, and residual risk.

For applied updates, also report:

- Resolved versions after the update.
- Actual direct and transitive changes, including unexpected churn.
- Verification run and result.
- Advisory status based on the resolved graph when relevant.

## Stop Conditions

- Stop after the evidence-backed plan for audit, recommendation, or plan-only requests.
- Stop when no compatible safe version exists; report the blocker and mitigations instead of forcing a broad upgrade.
- Stop before unrelated direct dependency updates, mixed package-manager output, or manual generated-lockfile edits.

## Composition

- Use `$test-and-verify` for affected-boundary and practical regression evidence.
- Use `$ship-check` only when the resulting dependency change needs a named readiness verdict.
- Hand authorized Git publication to `$commit-and-push`; do not invoke `$implement-change` for ordinary dependency updates.

## Anti-Patterns

- Refreshing every package during a targeted update.
- Editing a generated lockfile manually.
- Trusting a requested or remembered version without checking current authoritative sources.
- Claiming a vulnerability is resolved without inspecting the resolved graph.
- Mixing feature work or refactors into a dependency change.
- Editing manifests or lockfiles during an audit or plan-only request.
- Hiding install-script, runtime, migration, or transitive dependency changes.
