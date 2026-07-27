# solo-dev-core

Personal Codex plugin source for lean, evidence-backed solo-development workflows.

This repository is the durable source for skills, portable global instructions, behavioral evaluations, and automation specs. Universal engineering rules live in `global/AGENTS.md`; repository-specific facts belong in each repository's own `AGENTS.md`; task procedures live in skills.

## Operating model

1. Apply the global lean defaults on every task.
2. Select only skills whose trigger matches the request.
3. Compose neighbouring skills only when the next boundary is actually reached.
4. Gather fresh evidence before completion claims.
5. Keep Git publication, release, and deployment separately authorized.

There is no mandatory do-everything chain.

## Skills

| Need | Skill | Boundary |
| --- | --- | --- |
| Orient in a repository or resume interrupted work | `repo-compass` | Produces a compact evidence-labelled brief |
| Resolve material ambiguity or compare implementation options | `clarify-intent` | Stops at a plan unless implementation was requested |
| Shrink an oversized idea to one testable milestone | `solo-dev-scope` | Does not implement |
| Reproduce unexpected behavior and find its cause | `diagnose-problem` | Hands measured bottlenecks to profiling |
| Measure latency, throughput, memory, CPU, GPU, I/O, or loading cost | `profile-performance` | Requires a baseline and equivalent comparison |
| Review a bounded diff for actionable defects | `review-changes` | Does not become architecture or readiness review |
| Assess system boundaries, dependencies, ownership, or data flow | `architecture-review` | Read-only structural assessment |
| Reduce code, layers, branches, or dependencies without behavior change | `simplify-code` | Must prove the result is simpler and behavior-preserving |
| Apply a decision-ready code, configuration, or test change | `implement-change` | Stops before Git publication or deployment |
| Audit or update dependencies and runtimes | `dependency-maintenance` | Owns manifests, lockfiles, compatibility, and rollback |
| Create or update canonical docs and useful comments | `documentation` | Does not duplicate an existing source of truth |
| Gather fresh evidence for a concrete claim | `test-and-verify` | Produces evidence, not a readiness verdict |
| Decide readiness for one named shipping boundary | `ship-check` | Returns a verdict but performs no shipping action |
| Classify REGULAR versus RELEASE work and manage version/tag policy | `semantic-versioning` | Owns versions, changelogs, and tag approvals |
| Stage, commit, and push an intended Git change | `commit-and-push` | Always runs the SemVer gate; commit does not imply push |

## Composition examples

- Unfamiliar decision-ready feature: `repo-compass` → `implement-change` → `test-and-verify`.
- Ambiguous feature: `clarify-intent` → `implement-change` → `test-and-verify`.
- Oversized product idea: `solo-dev-scope` → `clarify-intent`; implementation remains conditional.
- Functional bug: `diagnose-problem` → `implement-change` → `test-and-verify`.
- Performance complaint: `diagnose-problem` → `profile-performance` → `implement-change` → `test-and-verify`.
- Dependency remediation: `dependency-maintenance` → `test-and-verify`.
- Bounded review: `review-changes`; use `ship-check` separately only when a readiness verdict is requested.
- Release boundary: `test-and-verify` → `ship-check` → `semantic-versioning` → `commit-and-push`.

Skip any step whose trigger is not present.

## Example invocations

- `Use $repo-compass to resume this repository and identify the exact next action.`
- `Use $clarify-intent to compare the credible options and return a decision-complete plan only.`
- `Use $profile-performance to reproduce this latency regression and locate the bottleneck without optimizing it.`
- `Use $simplify-code to identify removable layers while preserving public behavior.`
- `Use $architecture-review to assess service ownership and deployment boundaries without editing.`
- `Use $implement-change to apply this approved plan, verify it, and stop before committing.`

## Global instructions across repositories

`global/AGENTS.md` is the canonical portable global instruction file. On another machine, inspect any existing global instructions before replacing them:

```bash
diff -u ~/.codex/AGENTS.md global/AGENTS.md
mkdir -p ~/.codex
cp global/AGENTS.md ~/.codex/AGENTS.md
```

The copy is deliberate and is not performed by repository validation. Repository-specific commands, architecture, environment setup, and deployment facts must remain in that repository's `AGENTS.md`.

## Project memory contracts

The project-memory foundation keeps detailed state in the repository that owns
it. A managed repository uses one concise `docs/PROJECT.md`, based on
`templates/PROJECT.md`, plus optional durable decisions under
`docs/decisions/` using `templates/ADR.md`.

Validate a managed repository without modifying it:

```bash
scripts/project-memory validate-project --repo /path/to/repository
```

The project file must retain the template's 13 ordered sections. Future Ideas
use `FI-YYYYMMDD-short-title` identifiers and must record value, dependencies, a
concrete reconsideration trigger, the reason for deferral, related context, and
the capture date. ADR filenames use `ADR-YYYYMMDD-short-title.md`.

`registry/projects.json` is the committed logical registry. It stores only a
project ID, display name, and canonical remote in `host/owner/repository` form.
Machine-specific absolute paths belong in the ignored
`registry/paths.local.json`; start from
`registry/paths.local.example.json`.

Validate the logical registry alone or together with a local mapping:

```bash
scripts/project-memory validate-registry
scripts/project-memory validate-registry --paths registry/paths.local.example.json
```

Successful commands print a summary and exit zero. Schema, identifier, ADR, or
mapping errors are written to standard error and exit nonzero. The validator is
read-only and uses only the Python standard library.

## Plugin installation and refresh

The local personal marketplace must point at the machine's `solo-dev-core` source copy. Marketplace configuration is machine-local and is not tracked here.

After updating that source copy:

```bash
codex plugin add solo-dev-core@personal
codex plugin list
```

The repository manifest uses a Codex cachebuster so reinstalling picks up changed skills. Start a new task after reinstalling so Codex loads the refreshed package. This repository does not automatically install the plugin, change marketplace configuration, or overwrite `~/.codex/AGENTS.md`.

## Adding or changing a skill

1. Confirm the behavior is repeatable, multi-step, task-specific, and not a short global rule or an existing skill mode.
2. Inspect neighbouring descriptions and evaluations before choosing the name and trigger.
3. Initialize new skills with the system `skill-creator`; add no optional resources unless repeated work justifies them.
4. Keep frontmatter trigger-oriented and the body limited to task-specific procedure.
5. Include `Boundaries`, `Workflow`, `Evidence`, `Output Contract`, `Stop Conditions`, and `Composition`.
6. Update `agents/openai.yaml`, this routing table, behavioral evaluations, and cross-skill references together.
7. Run the complete validation surface below.

Do not create per-language or per-platform skills merely to repeat the global lean defaults. Add references only when detailed guidance is repeatedly needed and can be loaded conditionally.

## Behavioral evaluations

`evals/scenarios.json` records:

- ordered expected skill compositions;
- skills that must not trigger;
- expected mutation policy;
- required output characteristics;
- failure indicators.

The validator checks structure, references, and coverage. Forward-test material routing changes in isolated fresh contexts; deterministic validation does not prove model behavior by itself.

## Maintenance checklist

- Keep global principles in `global/AGENTS.md` and project facts in repository-level `AGENTS.md`.
- Preserve working skill behavior unless evidence justifies a boundary change.
- Keep descriptions distinct and UI metadata aligned.
- Maintain at least one behavioral scenario for every skill.
- Review compositions for unnecessary automatic steps.
- Refresh the plugin cachebuster after material plugin changes.
- Compare the tracked source with installed plugin and global-instruction copies before claiming parity.
- Do not commit generated caches, virtual environments, credentials, or unrelated work.

## Validation

No package install is required for repository validation:

```bash
scripts/validate-skills --strict-overlap
scripts/project-memory validate-registry
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

Both validation scripts use the Python standard library. `scripts/validate-skills`
validates skill contracts, frontmatter, UI metadata, README coverage,
cross-skill references, evaluation routing and mutation schema, and description
overlap. `scripts/project-memory` validates project-memory documents, optional
ADRs, the logical registry, and machine-local path mappings.

## Decisions

- `clarify-intent` owns design-option comparison; no `design-first` skill.
- `review-changes` remains a bounded-diff defect review.
- Performance, simplification, architecture assessment, and decision-ready implementation have distinct skills because their evidence and stop conditions differ.
- `commit-and-push` retains its mandatory SemVer gate.
- No language-specific skills, broad reference catalogue, new runtime dependencies, or mandatory workflow chain were added.

## Automations

Automation definitions remain separate under `automations/`. See `automations/README.md` for the active set, schedules, mutation policy, and change procedure.
