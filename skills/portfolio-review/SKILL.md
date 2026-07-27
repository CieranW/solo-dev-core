---
name: portfolio-review
description: Use when reviewing status, risks, verification freshness, next actions, or scope triggers across multiple registered repositories; read a logical project registry and machine-local path mapping, tolerate repositories unavailable on the current machine, inspect each available docs/PROJECT.md, optionally inspect local Git state without fetching or mutation, and return a read-only portfolio view with stale records, dirty trees, local-ahead branches, missing milestones, and potentially satisfied Future Idea triggers.
---

# Portfolio Review

Build a trustworthy cross-repository status view without centralizing project detail or changing any repository.

## Boundaries

- Treat the logical registry as identity and remote metadata only; detailed state stays in each repository's `docs/PROJECT.md`.
- Treat the machine-local path mapping as optional, ignored configuration that may differ across machines.
- Keep the workflow read-only. Do not edit project records, application files, registries, Git state, remotes, issues, or branches.
- Inspect local Git only when requested or clearly useful. Never fetch, pull, checkout, commit, push, or refresh remote state.
- Report unavailable and unadopted repositories instead of failing the whole review.

## Workflow

1. Resolve the explicit logical registry and optional machine-local path mapping. When no mapping is supplied, use `paths.local.json` beside the registry only if it exists.
2. Resolve this skill's directory and run:

   ```bash
   scripts/portfolio-review --registry <projects.json> [--paths <paths.local.json>] [--inspect-git] --format json
   ```

3. Stop on invalid registry or mapping structure. Do not guess identities or paths from unrelated clones.
4. For every registered project, classify its local availability:
   - `available`: mapped directory exists;
   - `unmapped`: no path is configured on this machine;
   - `missing`: a configured path is unavailable.
5. For available projects, inspect the canonical `docs/PROJECT.md`. Report missing or malformed project memory as a project-level flag while continuing the portfolio scan.
6. Summarize the Current Milestone name and status, Last Verified time and validation level, Risks and Unknowns, and Exact Next Action.
7. Flag stale records using the requested threshold, defaulting to 30 days. Treat unverified or unparsable Last Verified values as uncertain rather than recent.
8. When Git inspection is enabled, report the local branch, dirty state, configured upstream, and commits ahead of the locally recorded upstream. State that no fetch occurred, so remote freshness is not proven.
9. Inspect Future Idea reconsideration triggers. Treat reached dates as deterministic candidates; compare other triggers with current project evidence and label them `potentially satisfied` unless the evidence proves the condition.
10. Rank attention without rewriting priorities:
    - unavailable or missing project state;
    - blocked or missing milestone;
    - dirty or locally ahead Git state;
    - stale or unverified records;
    - significant risks;
    - potentially satisfied idea triggers.
11. Return one exact portfolio-level next action, normally the highest-impact reconciliation or local setup step. Keep repository-specific next actions visible but do not execute them.

## Evidence

- Logical registry and any selected local mapping validated before review.
- Every registered project represented, including unavailable clones.
- Portfolio claims tied to `docs/PROJECT.md`, local filesystem evidence, or optional local Git commands.
- Staleness threshold and as-of date reported.
- Git findings explicitly limited to local evidence with no fetch.
- Trigger candidates include the recorded trigger and the evidence supporting or limiting the assessment.

## Output Contract

- Registry, local mapping, as-of date, staleness threshold, and Git-inspection mode.
- Totals for registered, available, unavailable, missing-project-file, stale, dirty, ahead, missing-milestone, and trigger-candidate projects.
- One row per project with milestone, status, last verification, validation level, risks, next action, Git summary, and flags.
- Unavailable repositories and the exact mapping or clone action needed.
- Potentially satisfied Future Idea triggers separated from proven conditions.
- One exact portfolio-level next action.
- Explicit confirmation that no repository, registry, Git state, commit, or remote was changed.

## Stop Conditions

- Stop before scanning when the logical registry or selected local mapping is invalid.
- Continue past unavailable repositories, missing project files, malformed project memory, non-Git directories, and individual Git inspection failures.
- Stop before any repair, adoption, status update, roadmap update, commit, fetch, or push.
- Stop after the read-only report and one exact next action.

## Composition

- Receive adopted project identities from `$adopt-project`.
- Route missing project memory to `$adopt-project` as a separate authorized task.
- Route stale or inaccurate project records to `$project-status` in `UPDATE` mode only after explicit authorization.
- Route potentially satisfied idea triggers to `$roadmap-review`; do not promote them here.
- Use `$start-work` only after the owner selects one repository and asks to resume it.

## Anti-Patterns

- Treating the registry as a central backlog or copying project detail into it.
- Failing the whole review because one repository is not cloned.
- Fetching remotes or modifying repositories to make the report look current.
- Calling a branch synchronized merely because local ahead count is zero.
- Treating a plausible trigger as proven without repository evidence.
- Automatically repairing records or starting the most interesting project.
