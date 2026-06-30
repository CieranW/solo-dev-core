# solo-dev-core Instructions

This repo is the source of truth for Cieran's personal Codex skills and automation specs.

## Repo Shape

- `.codex-plugin/plugin.json` defines the local plugin package.
- `skills/<skill-name>/SKILL.md` holds each skill's behavior contract.
- `skills/<skill-name>/agents/openai.yaml` holds Codex app display metadata.
- `automations/<automation-id>/automation.toml` mirrors Codex automation definitions that should be preserved and evolved here.

## Workflow

- Keep skills small, reusable, and solo-dev focused.
- Put project-specific commands in that project's `AGENTS.md`, not here.
- Use `.venv` for any local validation helpers; never commit the venv.
- When changing skills, validate every `SKILL.md` has frontmatter with `name` and `description`.
- When changing automations, keep checked-in specs aligned with the live Codex automation config.

## Verification

Useful local checks:

```bash
find skills -name SKILL.md -maxdepth 2 -print
python - <<'PY'
from pathlib import Path
for path in sorted(Path("skills").glob("*/SKILL.md")):
    text = path.read_text()
    assert text.startswith("---\n"), path
    head = text.split("---", 2)[1]
    assert "name:" in head and "description:" in head, path
print("skill frontmatter ok")
PY
```

Before pushing, review:

```bash
git status --short
git diff --check
```

