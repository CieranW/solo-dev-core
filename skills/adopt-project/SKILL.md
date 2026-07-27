---
name: adopt-project
description: Use when onboarding an existing repository into the solo-dev-core project-memory system, when asked to create or reconstruct docs/PROJECT.md, or when registering a repository for later portfolio review; inspect repository evidence, select one credible current milestone, preserve links to detailed sources, create the canonical project record, update an explicitly available registry when requested, surface uncertainty for owner review, and avoid application-code changes.
---

# Adopt Project

Establish concise, evidence-backed project memory for an existing repository.

## Boundaries

- Use for initial adoption, reconstruction of missing project memory, and explicit repository registration.
- Create or update only `docs/PROJECT.md`, optional decision records, and an explicitly authorized logical registry or machine-local path mapping.
- Do not change application code, dependencies, generated files, Git history, or existing `AGENTS.md` unless separately requested.
- Do not invent a roadmap from scattered TODOs or turn every implementation note into a Future Idea.

## Workflow

1. Use `$repo-compass` in `ORIENT` mode to inspect applicable instructions, Git state, bounded history, source-of-truth documents, commands, configuration, and important repository boundaries.
2. Inspect existing product, architecture, plan, roadmap, issue, handoff, and decision documents. Search focused TODO and FIXME references for durable product or technical intent, not routine cleanup.
3. Separate observed repository facts, documented claims, reasonable inference, and owner decisions. Prefer executable and Git evidence when documentation disagrees.
4. Reconstruct the North Star and Product Boundaries. Link existing detailed documents rather than copying their contents.
5. Select the smallest credible Current Milestone from active branches, recent work, current behavior, and stated intent. Use `$solo-dev-scope` when the apparent direction is still several products or milestones.
6. Use `$clarify-intent` only when a material owner choice would change the milestone, product boundary, or adoption result. Otherwise record low-risk uncertainty explicitly.
7. Resolve this skill's directory, then build `docs/PROJECT.md` from the bundled canonical `assets/PROJECT.md`. Populate every section, retain one Exact Next Action, and keep unsupported claims marked uncertain or unverified.
8. Classify discovered work as Active, Next, Future, Deferred, or Abandoned. Do not promote an item merely because it is interesting or technically adjacent.
9. When the user explicitly requests portfolio registration and supplies or authorizes a writable canonical registry, add or reconcile the project using a stable kebab-case ID, display name, and canonical remote. Record the absolute clone path only in its ignored local mapping.
10. If a requested canonical registry is unavailable or not writable, complete valid project-local memory but report portfolio registration as incomplete and name the exact registry action still required.
11. Use `$documentation` for the project record and any accepted ADR. Create an ADR only for a durable decision whose rationale will matter later.
12. Run the bundled `scripts/project-memory validate-project --repo <repository>` relative to this skill directory. Validate registry files only when their explicit paths are available.
13. Present uncertain conclusions and proposed milestone boundaries for owner review. Do not commit or push.

## Evidence

- Applicable instructions, Git state, relevant history, implementation entrypoints, and existing continuity sources inspected.
- Project claims tied to repository evidence or labelled documented, inferred, uncertain, or unverified.
- Current milestone bounded by an observable outcome and stop condition.
- Project document and ADRs validated; an explicitly requested logical registry and local mapping validated when available.

## Output Contract

- Adopted repository and project ID when registered.
- North Star, boundaries, selected milestone, and exact next action.
- Files created or updated, including registry and local-only mapping state.
- Existing detailed sources retained by link.
- Uncertain conclusions requiring owner review.
- Validation commands and results.
- Explicit confirmation that application code, commits, and pushes were untouched.

## Stop Conditions

- Stop before mutation when the user did not authorize adoption.
- Stop for one material owner decision when no credible milestone or product boundary can be selected safely.
- Stop before claiming project-local adoption when the project file is invalid. Report requested portfolio registration separately when its registry is invalid or unavailable.
- Stop after the validated record and owner-review summary; implementation is a separate boundary.

## Composition

- Use `$repo-compass` for repository reconstruction.
- Use `$solo-dev-scope` only when the direction must be reduced to one milestone.
- Use `$clarify-intent` only for unresolved material choices.
- Use `$documentation` for the canonical project file and accepted ADRs.
- Hand later status reconciliation to `$project-status` and later resumption to `$start-work`.
- Hand cross-repository visibility for registered projects to `$portfolio-review`.

## Anti-Patterns

- Changing application code during adoption.
- Creating separate vision, backlog, roadmap, parking-lot, and milestone files.
- Treating README claims or TODO comments as authoritative without repository evidence.
- Hiding uncertainty to make the project record look complete.
- Recording machine-specific paths in the committed registry.
- Automatically committing or pushing the adoption changes.
