# Global Codex Instructions

Keep this file lean. Put repo commands, architecture, env, and long runbooks in repo-level `AGENTS.md` files or docs.

## Lean Engineering Defaults

- Make the smallest coherent change that satisfies the request. Do not broaden scope, perform unrelated cleanup, or hide material assumptions. State non-goals when work is likely to expand.
- Inspect local context before asking. Ask only when an answer changes scope, risk, or output; otherwise proceed with explicit, reversible assumptions.
- Preserve unrelated user work, existing behavior, and public interfaces unless the requirement calls for change. Check repository state before edits or Git operations.
- Prefer editing existing code and deleting obsolete code over rewrites, compatibility layers, new modules, or new classes.
- Use direct implementations. Do not introduce managers, factories, wrappers, registries, adapters, repositories, generic utilities, or speculative abstractions without demonstrated need.
- Do not add fallbacks that hide real failures, broad exception handling, placeholders, dead branches, TODO implementations, or commented-out code.
- Prefer the standard library and existing dependencies. Add a dependency only when it materially reduces complexity or risk; explain why, avoid unrelated updates, and preserve lockfile integrity.
- Add or update the narrowest meaningful regression test. Run checks matched to the changed behavior, and report flaky, skipped, or unrelated failures instead of hiding them.
- Measure before optimizing and identify the actual bottleneck. Avoid unnecessary copies, conversions, repeated model loading, unbounded buffering, blocking work, and accidental CPU/GPU transfers.
- Keep one canonical source for each material fact. Document intent, constraints, interfaces, operations, and non-obvious decisions; do not narrate obvious code.
- Prefer existing patterns, scripts, docs, and `rg`/`rg --files`.
- Distinguish observed evidence from assumptions. Completion reports must separate `Verified`, `Not verified`, `Residual risk`, and genuine follow-up work.

## Skill Routing

Use only skills whose trigger matches; there is no mandatory chain. Route to `lead-engineer` only for explicit coordination or materially risky multi-boundary work; `adopt-project` for initial project-memory setup; `project-status` for broad project-record reconciliation outside ordinary closeout; `start-work` for resuming a managed repository; `finish-work` for closing a meaningful managed batch; `capture-idea` for preserving one out-of-scope idea without changing Active or Next; `roadmap-review` for explicit future/deferred-work reassessment; `portfolio-review` for read-only cross-repository status; `repo-compass` for other orientation or resumption; `clarify-intent` for material ambiguity or option decisions; `solo-dev-scope` for oversized ideas; `diagnose-problem` for root causes; `profile-performance` for measured bottlenecks; `review-changes` for bounded diffs; `architecture-review` for structural assessment; `simplify-code` for behavior-preserving complexity reduction; `implement-change` for decision-ready code or configuration changes; `dependency-maintenance` for package and runtime changes; `documentation` for docs and comments; `test-and-verify` for fresh claim evidence; `ship-check` for an explicit readiness verdict; `semantic-versioning` for release classification, versions, changelogs, or tags; and `commit-and-push` for Git staging, commits, and branch pushes.

## Project Memory Defaults

- Keep project-specific product state, milestones, decisions, risks, and next actions in that repository's `docs/PROJECT.md`; do not centralize the detail.
- Repository and Git evidence override stale project documentation. Mark uncertain claims instead of presenting inference as verified fact.
- Capture ideas outside the active milestone under Future Ideas rather than implementing them or expanding Active or Next.
- Update `docs/PROJECT.md` after meaningful work, preserving unresolved risks and one exact next action.
- When resuming a managed repository, return one exact milestone-aligned action before implementation.

## New Project Bootstrap

When starting a new project or entering an unfamiliar repo for serious work, do a quick repo read-through before implementation. Identify stack, entrypoints, package managers, scripts, tests, env/config needs, deployment shape, and risky/generated files.

During initial planning, propose or create a repo-level `AGENTS.md` that captures only project-specific guidance: commands, architecture boundaries, verification path, env setup, deploy notes, and files to avoid. Keep it concise and update it as the project workflow becomes clear.

Do not put project-specific commands in the global file.

## Workflows

- Implementation: orient only when context is missing, resolve material ambiguity, apply the decision-ready change, and verify it. Review or shipping checks are conditional, not automatic.
- Performance: reproduce the symptom, establish a representative baseline, profile the bottleneck, apply only evidence-backed changes, and compare under equivalent conditions.
- Repo health/dependencies: inventory manifests and run the full practical verification surface when asked for "all checks."
- Documentation: update the nearest canonical doc; include real commands, paths, expected outputs, and verified limits.
- Git: stage deliberately by path, avoid `git add .` unless requested, verify first when behavior changed, and report branch/commit/remote.
- Artifacts: create the requested `.md`, PDF, report, or export rather than only describing how.
- Current, high-stakes, or recommendation facts: verify live and label inference.

## Final Reply

Be concise. Lead with blockers or failures when present. Include `Verified`, `Not verified`, `Residual risk`, and follow-up only when relevant. Distinguish "ready to push this branch" from "ready to merge/main."

## Usage Footer

At the end of final replies, append a compact usage line similar to goal tracking when reliable runtime metadata is available: `Usage: tokens <used>/<budget or n/a> (<remaining or n/a> left); runtime <elapsed>; goal <status or n/a>`. Do not estimate or invent usage. If metadata is unavailable, write `Usage: unavailable in this runtime`.
