---
name: documentation
description: Use when creating or updating Markdown documentation, README files, runbooks, plans, specs, changelogs, notes, or when adding, reviewing, tightening, or removing inline code comments; keep docs accurate, concise, audience-aware, and comments focused on why rather than obvious what.
---

# Documentation

Use this skill whenever the work produces `.md` documentation or touches inline comments.

## Workflow

1. Identify the reader: future you, a contributor, an operator, a reviewer, or an end user.
2. Inspect nearby docs and code first so tone, structure, commands, and terminology match the repo.
3. Prefer updating the closest existing document over creating a new one, unless the topic needs a distinct durable home.
4. Make Markdown task-oriented: what the reader needs to do, why it matters, exact commands or paths, expected outputs, and troubleshooting notes when relevant.
5. Keep inline comments rare and useful. Explain intent, constraints, invariants, edge cases, or surprising decisions; do not narrate obvious code.
6. Remove or rewrite stale, misleading, redundant, or decorative comments.
7. When documentation describes commands, generated files, APIs, or behavior, verify the claim or label it as unverified.
8. If a doc is meant to track a plan or decision, include date, status, owner/context, and clear next action.

## Markdown Standards

- Use concise headings and short sections.
- Prefer concrete examples over abstract advice.
- Use real paths, commands, environment variables, and file names.
- Keep checklists actionable.
- Avoid filler, marketing copy, and duplicated repo facts.
- Do not create extra README-style companion files unless the user asked or the repo clearly needs them.

## Inline Comment Standards

Good comments explain:

- Why this path exists.
- What invariant must be preserved.
- Why an obvious alternative is unsafe.
- Non-obvious external constraints.
- Complex edge cases that tests or names do not reveal.

Bad comments:

- Repeat the line of code.
- Explain common language syntax.
- Preserve outdated behavior.
- Add personality, decoration, or apology.
- Compensate for unclear names that should be renamed instead.

## Output Contract

When finishing documentation work, report:

- Files changed or created.
- Audience and purpose.
- Any claims verified.
- Any claims intentionally left unverified.
- Inline comments added, changed, or removed and why.

## Anti-Patterns

- Creating new docs when an existing doc should be updated.
- Adding comments to make code look documented.
- Documenting aspirational behavior as current behavior.
- Letting docs drift from commands, code, or tests.
