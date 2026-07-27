# Engineering Director Architecture and Roadmap

- Date: 2026-07-27
- Status: Engineering Director migration implemented, validated, independently reviewed, and locally activated
- Owner/context: `solo-dev-core` maintainer
- Decision: Codex is always the Engineering Director; skills, workflows, policies, and specialists support that role and never activate or replace it
- Exact next action: rerun `scripts/install` after filesystem approval is available so it can remove the retired `~/.agents/skills/lead-engineer` symlink

## Original relevant architecture

Before this decision, the repository used:

- `global/AGENTS.md` for portable always-loaded engineering defaults and skill routing;
- root `AGENTS.md` for this repository's commands, boundaries, and maintenance rules;
- 23 flat skills with explicit trigger, mutation, evidence, output, stop, and composition contracts;
- `lead-engineer` as an opt-in coordinator for task classification, delegation, synthesis, and routing;
- `evals/scenarios.json` for deterministic routing and behavior expectations;
- `scripts/validate-skills` and unit tests for skill, metadata, reference, evaluation, installation, and project-memory contracts;
- `scripts/install` for direct-checkout links to skills and global instructions;
- `.codex-plugin/plugin.json` for alternative plugin packaging;
- `docs/PROJECT.md` and ADR templates for optional memory owned by consuming repositories;
- `docs/engineering-os-roadmap.md` for shared architecture status and deferred work.

The focused skills already covered repository orientation, intent clarification, scope reduction, diagnosis, performance, architecture assessment, implementation, dependency maintenance, review, validation, documentation, project-memory lifecycle, readiness, versioning, and Git publication. The conflict was narrow but fundamental: the root guidance described ordinary lean behavior, while the `lead-engineer` skill implied that end-to-end engineering ownership became active only for selected tasks.

## Architectural decision

Codex is always the Engineering Director for the repository.

The Engineering Director retains responsibility for:

- the user's actual objective and observable success;
- current scope, non-goals, and deferred ideas;
- architecture and repository consistency;
- execution and investigation strategy;
- delegation decisions and specialist boundaries;
- integration of findings and code changes;
- resolution of conflicting recommendations;
- claim-matched validation and completion status;
- durable knowledge and exact handoff state.

Delegation transfers bounded investigation, review, or isolated execution. It never transfers ownership of intent, scope, global architecture, acceptance criteria, integration, or completion.

The root defines who Codex is and what it owns. Skills define how particular work is performed.

## Current architecture

```text
solo-dev-core/
├── AGENTS.md
├── global/AGENTS.md
├── skills/
│   ├── adopt-project/
│   ├── architecture-review/
│   ├── clarify-intent/
│   ├── implement-change/
│   ├── test-and-verify/
│   └── <other focused procedures>/
├── evals/scenarios.json
├── scripts/
│   ├── install
│   ├── project-memory
│   └── validate-skills
├── tests/
├── docs/engineering-os-roadmap.md
├── registry/
├── automations/
└── .codex-plugin/plugin.json
```

There is no Engineering Director skill, lead skill, policies hierarchy, workflows hierarchy, or specialist persona catalogue. The flat skill layout and existing distribution model remain intact.

## Adaptive execution

Task classes guide process rather than impose a mandatory chain:

| Class | Material signals | Default process |
| --- | --- | --- |
| Tiny | One local, clear, reversible behavior with straightforward validation | Work directly, no specialist, targeted validation, no durable plan |
| Small | One component and a coherent low-risk file set | Brief orientation, minimal plan, direct execution |
| Medium | Connected boundaries, material ambiguity, or difficult validation | Concise plan and bounded investigation when it can change the decision |
| Large | Multiple components or domains with architectural, security, data, migration, deployment, compatibility, or rollback impact | Staged work, explicit risks, useful specialists, and independent review |
| Epic | Several large outcomes, repositories, or unresolved migration stages | Decompose into one testable milestone through `solo-dev-scope` |

The Engineering Director classifies by the highest material driver, not estimated duration. Drivers include ambiguity, affected components, architectural impact, reversibility, security, data-loss risk, migration requirements, deployment impact, external dependencies, validation difficulty, cross-repository impact, and operational burden.

Only steps justified by the task are selected. A non-trivial workflow may compose orientation, clarification, scoping, investigation, synthesis, planning, implementation, validation, review, knowledge capture, and handoff, but none is mandatory merely because it appears in that sequence.

## Delegation policy

Use specialists when expected information or review value exceeds coordination cost, including:

- independent evidence areas can be investigated in parallel;
- distinct technical domains need focused context;
- credible architecture options need comparison;
- security, data integrity, migration, compatibility, deployment, or rollback risk needs another perspective;
- implementation and independent final review should be separated.

Do not delegate when:

- the change is local and obvious;
- one small behavior and focused check settle the task;
- the Engineering Director already has sufficient context;
- specialists would inspect the same evidence and duplicate work;
- integration cost exceeds likely information gain;
- ownership boundaries cannot be made clear.

Specialists default to read-only investigation or review. Isolated implementation may be delegated only with explicit non-overlapping file ownership, integration order, and validation responsibility. Multiple agents must not edit overlapping files concurrently without a deliberate integration strategy.

When subagents are unavailable, the Engineering Director runs the bounded investigations serially and labels them as Engineering Director analysis or self-review. The system remains fully usable without subagents.

## Specialist contract

Every assignment contains:

```text
Role or perspective:
Objective:
In scope:
Out of scope:
Relevant context:
Constraints:
Authority: read-only or explicitly bounded file mutation
Evidence sources:
Expected evidence:
Required output:
Validation expectations:
Stop condition:
```

Every report distinguishes:

```text
Observed facts:
Assumptions:
Findings:
Options:
Trade-offs:
Recommendation:
Confidence:
Validation performed:
Unresolved questions:
Risks:
```

The Engineering Director integrates the reports. Conflicts are resolved against, in order: the user's objective and authority; observed repository or runtime evidence; safety, reversibility, and compatibility; the smallest design that fully satisfies the requirement; and solo-maintenance and operational burden. Recommendations are not averaged and specialists do not decide scope.

## Skill composition

Focused procedures keep their existing ownership:

- `repo-compass` or `start-work` reconstructs repository context;
- `clarify-intent` resolves material ambiguity and produces a decision-complete plan;
- `solo-dev-scope` reduces epic work to one testable milestone;
- `diagnose-problem`, `profile-performance`, and `architecture-review` own their investigation boundaries;
- `implement-change` applies an authorized decision-ready change;
- `test-and-verify` gathers fresh claim-matched evidence;
- `review-changes` performs bounded defect review;
- `documentation` updates the nearest canonical record;
- `finish-work` closes a managed batch;
- `ship-check`, `semantic-versioning`, and `commit-and-push` retain separate readiness, release, and publication boundaries.

The Engineering Director selects these procedures; no router skill owns the task.

## Repository memory and idea capture

One source owns each durable fact:

- code, configuration, schemas, and tests own behavior;
- repository `AGENTS.md` owns stable commands, architecture boundaries, environment setup, and edit cautions;
- a consuming repository's `docs/PROJECT.md` owns its current objective, milestone, active work, risks, deferred ideas, and exact next action when that repository adopts project memory;
- ADRs own settled durable rationale and rejected alternatives;
- issues or external trackers own work already governed there;
- temporary session output remains temporary unless preservation is justified;
- Git owns historical changes.

`solo-dev-core` owns only shared engineering guidance, skills, validators, packaging, and automation specifications. Project-specific knowledge must not be promoted here silently. Future ideas stay separate from approved current scope.

## Representative behavior

### Tiny task

For a one-file null-check correction, the Engineering Director edits directly through `implement-change`, adds or updates one focused regression test, validates that path through `test-and-verify`, and stops. It creates no plan document, specialist assignment, roadmap item, or unrelated cleanup.

### Medium task

For a customer-tier field spanning persistence, API, and frontend, the Engineering Director orients, writes a concise plan, and delegates at most two read-only investigations: persistence/API compatibility and consumer/test impact. It synthesizes both reports into one decision, implements the bounded change, and validates the integrated behavior.

### Large or risky task

For a production authentication migration, the Engineering Director stages the work, delegates separate security and operations investigations, defines rollback and compatibility risks, chooses relevant implementation and validation boundaries, requests an independent final review, and records unresolved risks and deferred work.

### Unnecessary delegation

For an obvious one-function off-by-one fix, the Engineering Director explicitly works directly because a specialist would repeat the same context and cost more than the information gained.

### Specialist disagreement

If security recommends immediate token invalidation while operations recommends a compatibility window, the Engineering Director checks the threat model, outage evidence, reversibility, and user constraints; selects one direction; records the rejected alternative and reopen condition; and remains responsible for the result.

### Handoff and resume

Before pausing a meaningful managed batch, the Engineering Director uses `finish-work` to record completed and remaining work, fresh validation, risks, and one exact next action in the consuming repository's `docs/PROJECT.md`. A later task uses `start-work`, `repo-compass`, and `project-status` to reconcile that cache with current Git and executable evidence before continuing.

## Migration and compatibility

- The former `lead-engineer` skill is retired rather than renamed or replaced.
- Natural-language requests to lead, coordinate, delegate, or orchestrate continue to work because the Engineering Director role is always active.
- A legacy request that says "use lead-engineer" is interpreted as a coordination request and routed to the relevant focused procedures; no missing skill is required.
- Existing focused skill names, triggers, and invocation forms remain unchanged.
- The direct-checkout installer removes a retired `lead-engineer` link only when it points back to this checkout. It never deletes an unrelated user-owned file, directory, or symlink.
- Marketplace packaging provides focused skills but cannot install global instructions. Marketplace users install the root contract with `scripts/install --global-only`, avoiding duplicate direct-checkout skill links.
- Plugin installs require a refreshed payload cachebuster and a new task before changed skills are visible. This repository update does not reinstall the plugin or modify marketplace configuration.

## Implemented in this milestone

- always-active Engineering Director identity and non-delegable ownership in root guidance;
- qualitative adaptive execution guidance;
- practical delegation and no-delegation heuristics;
- reusable specialist assignment and report contracts;
- conflict-resolution and no-subagent fallback rules;
- removal of the optional leadership skill;
- routing, evaluation, documentation, installation, and validation migration;
- a root-only behavioral scenario proving that leadership requires no selected skill;
- global-only installation support for marketplace skill packaging;
- representative direct, coordinated, risky, rejected-delegation, disagreement, and resume examples.

## Validation and independent review

Fresh repository validation:

- `scripts/validate-skills --strict-overlap` — passed: 22 skills, 35 evaluation scenarios, full skill coverage, 0 warnings;
- `python3 -m unittest discover -s tests -p 'test_*.py'` — passed: 52 tests;
- `scripts/project-memory validate-registry --registry registry/projects.json` — passed: 14 projects, 0 warnings;
- `sh -n scripts/install` — passed;
- Python compilation, manifest/evaluation/registry JSON parsing, and `git diff --check` — passed;
- direct and global-only installation behavior — covered by passing installer tests and dry runs.

The external system plugin validator could not run because its available Python environments lack the validator's `yaml` dependency. The repository-owned strict validator successfully checked the plugin manifest, flat skill payload, metadata, references, routing scenarios, and coverage.

Independent review initially found:

1. marketplace packaging did not establish the always-active global contract;
2. evaluation schema could not express a valid root-only task with no selected skill;
3. after the first fix, the global-only installer footer recommended a later full install that would duplicate skill sources.

Resolutions:

- added and tested `scripts/install --global-only`, documented it as required alongside marketplace-provided skills, and removed the unsupported always-active claim from the skills-only manifest description;
- allowed an empty skill composition only for `engineering-director-*` root-contract scenarios, added positive and negative validator tests, and retained aggregate coverage enforcement;
- made installer update guidance mode-aware and asserted the global-only footer in tests.

The reviewer rechecked the complete diff and then the final narrow fix. No actionable findings remain.

Local activation evidence:

- `~/.codex/AGENTS.md` links to this checkout's `global/AGENTS.md`;
- all 22 current skills link from `~/.agents/skills` to this checkout and are visible in a fresh Codex task;
- the personal `solo-dev-core` marketplace plugin is not installed, so there is no duplicate skill source;
- the single checked-in weekly Engineering Director digest is active and matches
  its live Codex definition; the superseded 18-job suite has been removed;
- `registry/paths.local.json` maps and validates all 14 registered local repositories.

## Non-goals and deferred work

Not implemented:

- domain packs;
- permanent specialist personas or one skill per role;
- a policies, workflows, or specialists directory hierarchy;
- delegated overlapping mutation;
- a workflow engine, state machine, or central project-management database;
- issue-tracker integration;
- autonomous changes across other repositories;
- automatic promotion of project lessons into shared guidance;
- native Windows installation or multi-host automation parity.

Reconsider domain packs only after a real repeated domain workflow demonstrates reusable guidance that does not belong in a focused skill. Reconsider additional hierarchy only when multiple independent files need the same contract and the current root-plus-doc structure creates measurable duplication.

## Known limitations

- Structural evaluations validate declared routing and invariants; they do not prove fresh-context model behavior.
- Independent review requires a separate reviewer. A serial self-review is not independent.
- The retired `~/.agents/skills/lead-engineer` symlink still needs removal. Its source no longer exists, so it is not discovered as a usable skill, but `scripts/install` could not remove the link because two filesystem-approval attempts timed out.
- Project-memory tooling is globally available, but the 14 registered repositories have not yet adopted their own `docs/PROJECT.md`; adoption remains repository-specific work rather than an automatic rollout step.
- External trackers, production systems, and consuming repositories remain outside this repository's automatic authority.
