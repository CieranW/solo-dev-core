---
name: semantic-versioning
description: Use when deciding, preparing, auditing, or applying semantic versions, and as the required pre-commit gate for commit-and-push; triggers when release classification or version state is at issue, including regular-versus-release decisions, bumps, tags, changelogs, latest tags, version drift, package versions, v1 milestones, or choosing the next version, but not for a general shipping-readiness verdict.
---

# Semantic Versioning

Use this skill to keep releases boring, traceable, and consistent across repos.

## Boundaries

- Use for REGULAR-versus-RELEASE decisions, version recommendations, version-file or changelog preparation, and tag operations.
- Do not invoke standalone for general readiness, staged-diff review, ordinary branch publication, or deployment. The required pre-commit gate still applies when `$commit-and-push` invokes this skill.
- Version and changelog mutation is allowed only for a supported release decision. Tag creation and tag push each require explicit approval.

## Default Policy

Codex may recommend versions, draft changelogs, and prepare version-file edits.
When `$commit-and-push` invokes this skill, return an evidence-based `RELEASE` or `REGULAR` decision before staging. A commit-and-push request authorizes version and changelog preparation after a `RELEASE` decision, but not tag creation or pushing.
Codex must ask before creating Git tags.
Codex must ask before pushing Git tags.
Codex must never force-push tags.

## Workflow

1. Inspect repo state:
   - `git status --short`
   - current branch
   - latest reachable tag matching `v*`
   - commits since latest tag
2. Detect project type and version source:
   - Python: `pyproject.toml`
   - Node: `package.json`
   - Java/Maven: `pom.xml`
   - fallback: `VERSION`
   - mixed repos: identify each package and whether releases are unified or per-package
3. Classify changes since the latest tag:
   - `MAJOR`: breaking API, CLI, config, data, migration, contract, or compatibility change
   - `MINOR`: backward-compatible feature or notable new capability
   - `PATCH`: bug fix, docs, internal improvement, dependency maintenance, or non-breaking polish
4. When used as the pre-commit gate, decide `RELEASE` or `REGULAR` using the rules below and explain the evidence.
5. For `REGULAR`, stop release preparation and return without changing version files, changelogs, or tags.
6. For `RELEASE`, recommend the next version, prepare the version source and `CHANGELOG.md` with dated release notes, and explain the bump.
7. Run relevant verification or state why verification is not available.
8. Use `$ship-check` before release readiness claims.
9. Hand staging, the commit, and the normal branch push back to `$commit-and-push`. Keep version decisions and all tag approval or tag operations in this skill.
10. Ask before creating the tag. Ask again before pushing the tag.

## Pre-Commit Decision Rules

Return `RELEASE` only when the evidence supports releasing now:

- The repo has a versioned release target or explicit release convention.
- The reviewed changes form a coherent releasable unit.
- The current push is a release boundary under the user's request or the repo's documented workflow, or accumulated unreleased changes are ready to publish.
- The package scope and version source are unambiguous.

Return `REGULAR` when any of these apply:

- The repo has no versioning or release convention.
- The work is a checkpoint, work in progress, or a feature-branch push without a release-on-push policy.
- The changes are docs-only, tests-only, or internal-only and the repo does not publish them.
- A SemVer bump could describe the changes if released, but there is no evidence that a release should happen now.

Ask the user when package scope, release target, or breaking-change impact would materially change the decision. Do not use uncertainty alone as a reason to release.

## Version Source Rules

- Prefer the native package manifest over adding a new `VERSION` file.
- Keep `pyproject.toml`, `package.json`, and `pom.xml` versions aligned only when the repo releases as one product.
- Do not invent versioning for throwaway experiments unless the user asks.
- For pre-1.0 projects, treat `0.x.y` as unstable but still meaningful:
  - breaking pre-1.0 changes normally bump minor
  - backward-compatible features bump minor
  - fixes bump patch
- Use tags in the form `vMAJOR.MINOR.PATCH`, for example `v1.4.2`.

## Changelog Rules

Use `CHANGELOG.md` for release-capable repos.
Prefer this shape:

```md
## vX.Y.Z - YYYY-MM-DD

### Added
### Changed
### Fixed
### Removed
```

Only include sections that have entries.
Do not document aspirational work as released.
Reference notable commits, PRs, or issue numbers when visible.

## Evidence

- Repository version source, release convention, latest reachable tag, current branch, and relevant changes inspected.
- Release boundary, package scope, compatibility impact, and SemVer classification supported by repository evidence.
- Version and changelog diffs matched to actual changes.
- Relevant verification and `$ship-check` verdict available before release-readiness claims.

## Output Contract

For pre-commit decisions, report:

- Decision: `RELEASE` or `REGULAR`.
- Repository and change evidence reviewed.
- Why a release is or is not necessary now.

For version recommendations, report:

- Current version and latest tag.
- Commits or changes reviewed.
- Recommended next version and why.
- Files that would change.
- Verification needed before tagging.

For prepared releases, report:

- Version files changed.
- Changelog entry added.
- Verification run and result.
- Release commit status.
- Tag status: not created, created locally, or pushed.
- Any blocker or residual risk.

## Stop Conditions

- Stop after a `REGULAR` gate decision without touching versions, changelogs, or tags.
- Stop and ask when package scope, release target, or breaking-change impact would materially change the decision.
- Stop before creating or pushing a tag without the corresponding explicit approval.

## Composition

- Act as the mandatory pre-commit gate when invoked by `$commit-and-push`.
- Use `$ship-check` for a release-readiness verdict.
- Hand release staging, commit, and normal branch push back to `$commit-and-push`.
- Keep tag decisions and tag operations in this skill.

## Anti-Patterns

- Creating or pushing tags without explicit approval.
- Bumping versions from vibes instead of commit evidence.
- Mixing unrelated package versions accidentally.
- Updating changelog without checking actual changes.
- Treating docs-only edits as a release unless the repo publishes docs.
- Confusing "what the next version would be" with "a release is necessary now."
