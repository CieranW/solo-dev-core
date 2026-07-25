---
name: semantic-versioning
description: Use when deciding, preparing, auditing, or applying semantic versions; triggers for release, bump version, tag, changelog, latest tag, version drift, package version, are we ready for v1, or what version should this be; recommends SemVer changes, updates version files and changelogs when asked, and requires approval before creating or pushing tags.
---

# Semantic Versioning

Use this skill to keep releases boring, traceable, and consistent across repos.

## Default Policy

Codex may recommend versions, draft changelogs, and prepare version-file edits.
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
4. Recommend the next version and explain the evidence.
5. If preparing a release, update the version source and `CHANGELOG.md` with dated release notes.
6. Run relevant verification or state why verification is not available.
7. Use `ship-check` before release readiness claims.
8. After release files are prepared, hand staging, the release commit, and the normal branch push to `commit-and-push`. Keep version decisions and all tag approval or tag operations in this skill.
9. Ask before creating the tag. Ask again before pushing the tag.

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

## Release Output Contract

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

## Anti-Patterns

- Creating or pushing tags without explicit approval.
- Bumping versions from vibes instead of commit evidence.
- Mixing unrelated package versions accidentally.
- Updating changelog without checking actual changes.
- Treating docs-only edits as a release unless the repo publishes docs.
