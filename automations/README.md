# Automations

This directory tracks the source definitions for Cieran's Codex workflow automations.

All automations should be report-only by default. They may inspect local repos, summarize drift, and recommend next actions, but they must not edit files, create commits, create tags, push branches, deploy services, delete branches, or clean worktrees unless a future task explicitly changes that contract.

## Active Set

- `weekly-semver-audit`: release/versioning radar across `/Users/cieranwong/repos`.
- `weekly-repo-triage`: dirty repo, stale branch, upstream, and worktree attention digest.
- `solo-dev-core-sync-guard`: parity check for this repo, live plugin source, installed cache, global instructions, and automation specs.
- `cincaria-workflow-drift`: Cincaria reusable workflow/template drift radar.
- `cincaria-deployment-readiness`: Cincaria app deployment-readiness digest.
- `hrdcs-report-handoff`: HRDCS Finance/HR handoff sentinel for report artifacts and logs.
- `signal-shelf-local-ops`: local-first Signal Shelf readiness and scheduler brief.
- `agents-coverage-audit`: repo-level `AGENTS.md` coverage and freshness audit.
- `docs-artifact-export-reminder`: docs/report export reminder for changed canonical artifacts.
- `personal-project-archive-radar`: archive/ignore recommendations for low-signal personal repos.

## Change Policy

1. Update the checked-in `automation.toml` first.
2. Apply the matching Codex automation create/update through the Codex app automation tool.
3. Commit the source definition change through a pull request.

## Exclusions

- Ignore `/Users/cieranwong/repos/CAMDAR` in personal workflow automations unless the user explicitly asks about that repo again.
