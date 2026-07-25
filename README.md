# solo-dev-core

Personal Codex plugin source for reusable solo-developer workflows.

This repository is the durable home for skills and automation specs. The local installed copy under `~/.codex/plugins/solo-dev-core` can be refreshed from this repo, but future edits should start here.

The tracked global Codex instruction source lives at `global/AGENTS.md`. The repo root `AGENTS.md` is intentionally repo-specific guidance for working on this repository.

## Skills

- `clarify-intent`: tighten fuzzy requests before implementation.
- `solo-dev-scope`: shrink broad product ideas to the smallest valuable milestone.
- `repo-compass`: map unfamiliar repos and create concise repo-level guidance.
- `documentation`: write Markdown docs and useful inline comments.
- `test-and-verify`: run practical checks before completion claims.
- `ship-check`: assess whether a branch is ready to push or merge.
- `commit-and-push`: stage, commit, and push Git work safely, routing release work through semantic versioning.
- `semantic-versioning`: recommend, prepare, and audit SemVer releases.

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
python - <<'PY'
from pathlib import Path
for path in sorted(Path("skills").glob("*/SKILL.md")):
    text = path.read_text()
    assert text.startswith("---\n"), path
    head = text.split("---", 2)[1]
    assert "name:" in head and "description:" in head, path
print("skill frontmatter ok")
PY
git diff --check
```
