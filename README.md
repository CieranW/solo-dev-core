# solo-dev-core

Personal Codex plugin source for reusable solo-developer workflows.

This repository is the durable home for skills and automation specs. The local installed copy under `~/.codex/plugins/solo-dev-core` can be refreshed from this repo, but future edits should start here.

The tracked global Codex instruction source lives at `global/AGENTS.md`. The repo root `AGENTS.md` is intentionally repo-specific guidance for working on this repository.

## Skills

- `clarify-intent`: resolve material ambiguity and produce decision-complete plans.
- `solo-dev-scope`: shrink broad product ideas to one testable first milestone.
- `repo-compass`: orient in unfamiliar repos or resume work with compact evidence-backed briefs.
- `diagnose-problem`: reproduce unexpected behavior and isolate evidence-backed root causes.
- `review-changes`: find actionable correctness, security, and regression defects in diffs.
- `documentation`: maintain canonical Markdown docs and useful inline comments.
- `dependency-maintenance`: make targeted, compatibility-aware package and runtime updates.
- `test-and-verify`: match completion claims to fresh verification evidence.
- `ship-check`: judge readiness for a commit, push, merge, deploy, release, or handoff.
- `commit-and-push`: run a SemVer decision gate, then prepare and push the right commit.
- `semantic-versioning`: choose regular or release commits and prepare evidence-based SemVer releases.

## Automations

- `weekly-semver-audit`: weekly report-only scan of `/Users/cieranwong/repos` for versioning health.
- `weekly-repo-triage`: weekly repo hygiene and attention digest.
- `solo-dev-core-sync-guard`: weekly source-of-truth parity check for skills, global instructions, cache, and automation specs.
- `cincaria-workflow-drift`: weekly Cincaria workflow/template drift radar.
- `cincaria-deployment-readiness`: weekly deployment-readiness digest for core Cincaria apps.
- `hrdcs-report-handoff`: weekly HRDCS Finance/HR report handoff sentinel.
- `signal-shelf-local-ops`: weekly local-first Signal Shelf operations brief.
- `agents-coverage-audit`: monthly repo-level `AGENTS.md` coverage audit.
- `docs-artifact-export-reminder`: weekly documentation artifact export reminder.
- `personal-project-archive-radar`: monthly personal repo archive/ignore radar.
- `automation-health-check`: weekly live-vs-source automation parity report.
- `open-pr-and-ci-failure-digest`: weekly GitHub PR and CI digest.
- `local-secret-and-env-drift-audit`: weekly local secret/env/example drift audit.
- `large-and-generated-file-radar`: weekly large/generated/cache/export file radar.
- `dependency-refresh-radar`: monthly dependency refresh report.
- `new-repo-onboarding-detector`: weekly new or under-onboarded repo detector.
- `todo-fixme-debt-digest`: weekly TODO/FIXME/HACK debt digest.
- `backup-and-export-freshness-reminder`: weekly backup/export freshness reminder.

All automations run at local midnight, staggered Monday through Friday, and use high reasoning by default for deeper overnight analysis.

Automation definitions are tracked in `automations/`. The live Codex automation should be kept aligned with the checked-in file when its prompt, schedule, model, or scope changes.

CAMDAR is intentionally excluded from personal workflow automations unless explicitly requested again.

## Global Instructions

- `global/AGENTS.md`: source copy for `~/.codex/AGENTS.md`.
- Root `AGENTS.md`: repo-local instructions for this source repository.

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Python package install is currently required for the repo itself.

## Validation

```bash
scripts/validate-skills
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

`scripts/validate-skills` uses only the Python standard library. It checks skill
frontmatter and folder alignment, UI metadata, plugin and README coverage,
explicit `$skill-name` references, eval definitions, and potentially ambiguous
description overlap.

`evals/scenarios.json` contains reusable forward-test prompts and behavioral
invariants. Run material skill revisions against the relevant scenarios in fresh
agent contexts; the validator checks the scenario schema and references but does
not substitute deterministic lint for model evaluation.
