---
name: documentation
description: Use when creating or updating Markdown documentation, README files, runbooks, plans, specs, changelogs, notes, or when adding, reviewing, tightening, or removing inline code comments; keep docs accurate, concise, audience-aware, and comments focused on why rather than obvious what.
---

# Documentation

Use this skill whenever the work produces `.md` documentation or touches inline comments.

## Boundaries

- Use for Markdown, runbooks, plans, specs, changelogs, notes, and inline comments.
- Do not use for implementing code behavior, deciding architecture, or creating a second source for an existing fact.
- Mutate documentation only when creation or updates were requested; keep audits and reviews read-only.

## Workflow

1. Identify the document's job and reader: guide, reference, runbook, plan, decision record, contributor note, operator note, or end-user documentation.
2. Identify the source of truth for every material claim before writing.
3. Inspect nearby docs and code first so tone, structure, commands, and terminology match the repository.
4. Prefer updating the closest canonical document over creating a new one. Link to the canonical source instead of duplicating facts across files.
5. Make task-oriented Markdown concrete: what the reader needs to do, why it matters, exact commands or paths, expected outputs, and troubleshooting notes when relevant.
6. Verify commands, generated files, APIs, configuration, and behavior, or label the claim as documented but unverified.
7. Validate changed relative links and referenced repository paths when practical.
8. Run deterministic, non-destructive command snippets in the relevant environment when practical. Inspect and label stateful, destructive, privileged, platform-specific, or credential-dependent examples instead of executing them casually.
9. Keep inline comments rare and useful. Explain intent, constraints, invariants, edge cases, or surprising decisions; do not narrate obvious code.
10. Remove or rewrite stale, misleading, redundant, or decorative documentation and comments.
11. Review the resulting diff for contradictions, duplicated sources of truth, broken links, stale adjacent text, and accidental secrets or machine-specific values.
12. For plans and decisions, include date, status, owner or context, decisions, unresolved questions, and the next action.

## Markdown Standards

- Use concise headings and short sections.
- Prefer concrete examples over abstract advice.
- Use real paths, commands, environment variables, and file names.
- Keep checklists actionable.
- Distinguish current behavior, proposed behavior, and historical context.
- Prefer stable links and identifiers over brittle line numbers or transient output.
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

## Evidence

- Intended reader and document job identified.
- Material claims traced to code, configuration, commands, or another canonical source.
- Changed paths, links, commands, and examples checked or labelled unverified.
- Resulting diff reviewed for duplication, stale adjacent text, and accidental sensitive or machine-specific data.

## Output Contract

When finishing documentation work, report:

- Files changed or created.
- Audience and purpose.
- Canonical source updated or established.
- Any claims verified.
- Any claims intentionally left unverified.
- Links, paths, and command snippets checked, including anything deliberately not executed.
- Inline comments added, changed, or removed and why.

## Stop Conditions

- Stop before creating a new document when an existing canonical source should be updated.
- Stop before running stateful, destructive, privileged, network-dependent, or credential-dependent examples without authority.
- Stop once the intended reader can complete the documented task without duplicated or speculative material.

## Composition

- Record durable plans from `$clarify-intent` only when persistence is justified.
- Document approved outputs from implementation, dependency, architecture, or shipping workflows without taking over their decisions.
- Use `$test-and-verify` when documentation makes executable behavior claims.
- Hand Git publication to `$commit-and-push` only when requested.

## Anti-Patterns

- Creating new docs when an existing doc should be updated.
- Copying the same operational fact into multiple canonical-looking documents.
- Adding comments to make code look documented.
- Documenting aspirational behavior as current behavior.
- Publishing command examples that were neither run nor labeled as unverified.
- Letting docs drift from commands, code, or tests.
