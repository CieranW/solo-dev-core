# solo-dev-core Instructions

This repo is the source of truth for Cieran's personal Codex skills and automation specs.

## Repo Shape

- `.codex-plugin/plugin.json` defines the local plugin package.
- `skills/<skill-name>/SKILL.md` holds each skill's behavior contract.
- `skills/<skill-name>/agents/openai.yaml` holds Codex app display metadata.
- `automations/<automation-id>/automation.toml` mirrors Codex automation definitions that should be preserved and evolved here.
- `global/AGENTS.md` tracks the global Codex instructions source copy.

## Workflow

- Keep skills small, reusable, and solo-dev focused.
- Put project-specific commands in that project's `AGENTS.md`, not here.
- Use `.venv` for any local validation helpers; never commit the venv.
- When changing skills, validate every `SKILL.md` has frontmatter with `name` and `description`.
- When changing automations, keep checked-in specs aligned with the live Codex automation config.
- When changing global instructions, edit `global/AGENTS.md` first, then install it to `~/.codex/AGENTS.md` deliberately.

## Verification

Useful local checks:

```bash
scripts/validate-skills
python3 -m unittest discover -s tests -p 'test_*.py'
```

Before pushing, review:

```bash
git status --short
git diff --check
```
