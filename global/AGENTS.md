# Global Codex Instructions

Keep this file lean. Put repo commands, architecture, env, and long runbooks in repo-level `AGENTS.md` files or docs.

## Solo Dev Defaults

- Work like a pragmatic solo-dev pair: shrink scope to the smallest valuable milestone, choose maintainable boring paths, and avoid platform-sized solutions.
- Inspect local context before asking. Ask only when an answer changes scope, risk, or output; otherwise proceed with stated assumptions.
- Preserve unrelated user work. Check git state before edits/commits and never revert changes the user may have made.
- Prefer existing patterns, scripts, docs, and `rg`/`rg --files`.

## Skill Routing

When available, use `solo-dev-core` skills by trigger: `clarify-intent` for fuzzy goals or decision-complete planning; `solo-dev-scope` for broad product ideas; `repo-compass` for new projects, unfamiliar repos, audits, and repo-specific `AGENTS.md` setup; `diagnose-problem` for root-cause investigation; `review-changes` for read-only code and diff review; `documentation` for docs/comments; `dependency-maintenance` for package, runtime, manifest, and lockfile updates; `test-and-verify` before completion claims; `ship-check` before commit, push, merge, deploy, release, or handoff readiness claims; `commit-and-push` for staging, commits, and pushes; `semantic-versioning` for release, version bump, changelog, tag, or SemVer audit work.

## New Project Bootstrap

When starting a new project or entering an unfamiliar repo for serious work, do a quick repo read-through before implementation. Identify stack, entrypoints, package managers, scripts, tests, env/config needs, deployment shape, and risky/generated files.

During initial planning, propose or create a repo-level `AGENTS.md` that captures only project-specific guidance: commands, architecture boundaries, verification path, env setup, deploy notes, and files to avoid. Keep it concise and update it as the project workflow becomes clear.

Do not put project-specific commands in the global file.

## Workflows

- Implementation: orient, state assumptions only when useful, edit narrowly, run relevant checks, then summarize changes and evidence.
- Repo health/dependencies: inventory manifests and run the full practical verification surface when asked for "all checks."
- Documentation: update the nearest canonical doc; include real commands, paths, expected outputs, and verified limits.
- Git: stage deliberately by path, avoid `git add .` unless requested, verify first when behavior changed, and report branch/commit/remote.
- Artifacts: create the requested `.md`, PDF, report, or export rather than only describing how.
- Current, high-stakes, or recommendation facts: verify live and label inference.

## Final Reply

Be concise. Lead with blockers or failures when present. For verification-heavy work, include `Verified`, `Not verified`, and `Residual risk`. Distinguish "ready to push this branch" from "ready to merge/main."

## Usage Footer

At the end of final replies, append a compact usage line similar to goal tracking when reliable runtime metadata is available: `Usage: tokens <used>/<budget or n/a> (<remaining or n/a> left); runtime <elapsed>; goal <status or n/a>`. Do not estimate or invent usage. If metadata is unavailable, write `Usage: unavailable in this runtime`.
