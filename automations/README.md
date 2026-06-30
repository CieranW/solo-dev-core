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

## Pending Schedule Interview

These automations are implemented but paused until their cadence and timing are confirmed:

- `automation-health-check`: live-vs-source automation parity and schedule overlap report.
- `open-pr-and-ci-failure-digest`: GitHub PR, CI, and stale review branch digest.
- `local-secret-and-env-drift-audit`: local secret/env/example/gitignore drift audit.
- `large-and-generated-file-radar`: large, generated, cache, export, and database file radar.
- `dependency-refresh-radar`: Python/Node/Java/Docker dependency refresh report.
- `new-repo-onboarding-detector`: new or under-onboarded repo detector.
- `todo-fixme-debt-digest`: TODO/FIXME/HACK debt digest.
- `backup-and-export-freshness-reminder`: backup/export/artifact freshness reminder.

## Change Policy

1. Update the checked-in `automation.toml` first.
2. Apply the matching Codex automation create/update through the Codex app automation tool.
3. Commit the source definition change through a pull request.

## Exclusions

- Ignore `/Users/cieranwong/repos/CAMDAR` in personal workflow automations unless the user explicitly asks about that repo again.
