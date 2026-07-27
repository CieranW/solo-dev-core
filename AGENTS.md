# solo-dev-core Instructions

This repo is the source of truth for Cieran's personal Codex skills and automation specs.

Codex is always the Engineering Director for this repository under the contract in `global/AGENTS.md`. Skills support that role; none activates or replaces it.

## Repo Shape

- `.codex-plugin/plugin.json` defines the local plugin package.
- `skills/<skill-name>/SKILL.md` holds each skill's behavior contract.
- `skills/<skill-name>/agents/openai.yaml` holds Codex app display metadata.
- `automations/<automation-id>/automation.toml` mirrors Codex automation definitions that should be preserved and evolved here.
- `global/AGENTS.md` is the portable source for global lean-engineering instructions.

## Workflow

- Keep skills small, reusable, and solo-dev focused.
- Put project-specific commands in that project's `AGENTS.md`, not here.
- Use `.venv` for any local validation helpers; never commit the venv.
- Keep universal engineering rules in `global/AGENTS.md`; skills should contain only task-specific procedure and evidence.
- Every skill must have precise trigger metadata plus `Boundaries`, `Workflow`, `Evidence`, `Output Contract`, `Stop Conditions`, and `Composition` sections.
- Keep `agents/openai.yaml`, README routing, evaluations, and cross-skill references aligned with each skill.
- When changing automations, keep checked-in specs aligned with the live Codex automation config.
- When changing global instructions, edit `global/AGENTS.md` first, then install it to `~/.codex/AGENTS.md` deliberately.
- When changing the plugin, refresh the manifest cachebuster through the plugin-creator helper; do not hand-edit personal marketplace configuration.

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
