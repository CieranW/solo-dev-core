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
| Coordinate explicit multi-boundary or materially risky work | `lead-engineer` | Classifies, delegates read-only investigations, synthesizes, and routes |
| Adopt an existing repository into project memory | `adopt-project` | Creates the canonical project record and registry entries without application changes |
| Reconcile project records with repository evidence | `project-status` | Checks read-only or updates project documentation only |
| Resume one bounded batch from durable project state | `start-work` | Produces one in-scope next action before implementation |
| Close a batch and preserve truthful continuity | `finish-work` | Updates project memory and stops before Git publication |
| Preserve an idea without expanding active scope | `capture-idea` | Adds or updates one Future Idea and returns to the interrupted task |
| Reassess future and deferred work | `roadmap-review` | Recommends or applies justified state changes without automatic Active promotion |
| Review status across registered repositories | `portfolio-review` | Reads project memory and optional local Git state without modifying repositories |
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

- Explicit coordinated feature: `lead-engineer` → bounded read-only investigations → `implement-change` → `test-and-verify`; review remains risk-based.
- Explicit coordinated epic: `lead-engineer` → `solo-dev-scope`; only the selected milestone continues.
- Existing repository adoption: `adopt-project` → `repo-compass` → conditional `solo-dev-scope` or `clarify-intent` → `documentation`.
- Managed repository resumption: `start-work` → `repo-compass` → `project-status`; only an authorized in-scope batch continues to `implement-change`.
- Batch closeout: `finish-work` → conditional `test-and-verify` → `documentation`; Git publication remains separate.
- Scope-safe idea interruption: `capture-idea` → `documentation` → resume the original task.
- Periodic roadmap reassessment: `roadmap-review` → `project-status` CHECK → conditional `documentation`; Active promotion requires an explicit milestone decision.
- Cross-repository review: `portfolio-review` → conditional owner-selected `project-status`, `roadmap-review`, or `start-work`; the review itself stays read-only.
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

- `Use $lead-engineer to coordinate this multi-boundary migration, keep specialist work read-only, and return one integrated plan.`
- `Use $adopt-project to reconstruct this repository into docs/PROJECT.md without changing application code.`
- `Use $project-status to reconcile docs/PROJECT.md with the current branch and working tree.`
- `Use $start-work to resume this repository and identify one bounded in-scope batch.`
- `Use $finish-work to close this batch, update project memory, and preserve one exact next action.`
- `Use $capture-idea to preserve this idea without changing Active or Next, then return to the current task.`
- `Use $roadmap-review to deduplicate and reassess Future and Deferred work without promoting anything automatically.`
- `Use $portfolio-review to inspect registered projects, including unavailable clones and optional local Git state, without changing them.`
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
it. A managed repository uses one concise `docs/PROJECT.md`, based on the
bundled `skills/adopt-project/assets/PROJECT.md`, plus optional durable
decisions under `docs/decisions/` using the bundled `ADR.md`.

Validate a managed repository without modifying it:

```bash
scripts/project-memory validate-project --repo /path/to/repository
```

The project file must retain the template's 13 ordered sections. Future Ideas
use `FI-YYYYMMDD-short-title` identifiers and must record value, dependencies, a
concrete reconsideration trigger, the reason for deferral, related context, and
the capture date. ADR filenames use `ADR-YYYYMMDD-short-title.md`.

Use ADRs only for durable product-boundary, public-contract, data, security,
deployment, compatibility, migration, dependency, or architecture decisions
whose rationale will matter later. Do not create ADRs for routine
prioritization, naming, local refactors, or reversible implementation details.
Every ADR records status, context, decision, rationale, alternatives,
consequences, and a revisit trigger.

`registry/projects.json` is the committed logical registry. It stores only a
project ID, display name, and canonical remote in `host/owner/repository` form.
Machine-specific absolute paths belong in the ignored
`registry/paths.local.json`; start from
`registry/paths.local.example.json`.

Validate the logical registry alone or together with a local mapping:

```bash
scripts/project-memory validate-registry --registry registry/projects.json
scripts/project-memory validate-registry --registry registry/projects.json --paths registry/paths.local.example.json
```

Successful commands print a summary and exit zero. Schema, identifier, ADR, or
mapping errors are written to standard error and exit nonzero. The validator is
read-only and uses only the Python standard library.

Create a read-only portfolio report from the installed skill:

```bash
skills/portfolio-review/scripts/portfolio-review \
  --registry registry/projects.json \
  --paths registry/paths.local.json \
  --inspect-git
```

The report includes every registered project, tolerates unmapped or missing
clones, and flags stale records, missing milestones, dirty trees, locally ahead
branches, and date-based Future Idea trigger candidates. Git inspection is
optional and never fetches, so ahead counts reflect only local upstream refs.

## Plugin installation and refresh

This Git repository is the portable source. Personal marketplace registration, its configured source path, installed caches, live global instructions, local project paths, and enabled automations are machine-local and are not tracked here.

On a new machine, prefer pointing the personal marketplace directly at a reviewed checkout of this repository. An existing machine may retain a separate local plugin source for compatibility, but that copy must be deliberately reconciled to the intended Git revision before reinstalling; changing this repository alone does not update it.

After the configured marketplace source contains the intended cachebuster version:

```bash
codex plugin add solo-dev-core@personal
codex plugin list
```

The manifest cachebuster identifies the plugin payload, not a separate SemVer release. Confirm the resolved version and source with `codex plugin list`, then start a new task so Codex loads the refreshed package. To roll back, restore a known reviewed Git revision or matching legacy source copy and reinstall its recorded cachebuster.

Initial marketplace creation and routine reinstall are different operations. Follow the current plugin-creator bootstrap flow only when no local marketplace entry exists; do not rewrite an existing marketplace path during routine refresh. This repository does not automatically install the plugin, change marketplace configuration, overwrite `~/.codex/AGENTS.md`, or activate automations.

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
scripts/project-memory validate-registry --registry registry/projects.json
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

Both validation scripts use the Python standard library. `scripts/validate-skills`
validates skill contracts, frontmatter, UI metadata, README coverage,
cross-skill references, evaluation routing and mutation schema, and description
overlap. `scripts/project-memory` validates project-memory documents, optional
ADRs, the logical registry, and machine-local path mappings.

## Decisions

- `lead-engineer` is an opt-in coordinator for explicit or materially risky multi-boundary work, not a universal task router.
- `docs/PROJECT.md` is the only routine project-memory record; adoption, status, start, and finish workflows keep its responsibilities distinct.
- Start-work remains read-only, while project-status owns explicit record reconciliation and finish-work owns batch closeout.
- Capture-idea never changes Active or Next, and roadmap-review cannot promote work to Active without an explicit milestone decision.
- Portfolio-review reads distributed project state and optional local Git evidence but never repairs repositories or centralizes their detailed status.
- ADRs preserve durable rationale, not ordinary prioritization or implementation history.
- `clarify-intent` owns design-option comparison; no `design-first` skill.
- `review-changes` remains a bounded-diff defect review.
- Performance, simplification, architecture assessment, and decision-ready implementation have distinct skills because their evidence and stop conditions differ.
- `commit-and-push` retains its mandatory SemVer gate.
- Specialist perspectives remain temporary read-only lenses; domain packs, permanent role skills, and delegated mutation are deferred.
- No language-specific skills, broad reference catalogue, new runtime dependencies, or mandatory workflow chain were added.

## Automations

Automation definitions remain separate under `automations/`. See `automations/README.md` for the active set, schedules, mutation policy, and change procedure.
