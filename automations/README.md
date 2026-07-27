# Automations

This directory tracks the source definitions for Cieran's Codex workflow automations.

All automations should be report-only by default. They may inspect local repos, summarize drift, and recommend next actions, but they must not edit files, create commits, create tags, push branches, deploy services, delete branches, or clean worktrees unless a future task explicitly changes that contract.

Codex cron automations bind to one saved local project. Broad portfolio jobs use
`solo-dev-core` as their execution anchor while their prompts explicitly inspect
`/Users/cieranwong/repos`; Cincaria-wide jobs use the saved Cincaria project.
The checked-in `cwds` record that live anchor, not the full prompt scan scope.

## Active Set

`weekly-engineering-director-digest` is the only shared engineering automation.
It runs late Friday. A two-run trial through 2026-08-10 uses `gpt-5.6-sol` with
medium reasoning while retaining strict investigation and output caps. The run
starts with inexpensive portfolio signals, deep-inspects no more than five
repositories, stops after five supported actions, and emits at most 300 words.
A quiet week produces one sentence.

Specialized audits remain available as manual Codex requests. They are not
scheduled independently because the repeated reports cost more attention and
tokens than they return.

## Change Policy

1. Update the checked-in `automation.toml` first.
2. Apply the matching Codex automation create/update through the Codex app automation tool.
3. Commit the source definition change through a pull request.

## Exclusions

- Ignore `/Users/cieranwong/repos/CAMDAR` in personal workflow automations unless the user explicitly asks about that repo again.
