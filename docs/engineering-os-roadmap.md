# Engineering OS Architecture and Roadmap

- Date: 2026-07-27
- Status: Milestone 1 implemented; direct-link installation validated, fresh-task deduplication pending
- Owner/context: `solo-dev-core` maintainer
- Decision: Extend the existing skill system with one opt-in coordinator instead of a mandatory workflow chain
- Installation decision: Use direct-checkout skill and global-instruction links for personal machines; retain marketplace packaging as an alternative, not a simultaneous installation
- Exact next action: Remove the redundant `solo-dev-core@personal` installation, start a fresh Codex task, and confirm single-source skill discovery plus coordinator routing

## Original state

Before this milestone, `solo-dev-core` was a mature lean-workflow plugin rather than an unstructured skill collection. It already had:

- 15 focused skills with explicit mutation, evidence, output, stop, and composition contracts;
- a clear split between global guidance, repository-specific facts, and task procedures;
- behavioral routing scenarios and a standard-library validator;
- deliberate plugin cachebusting, manual global-instruction installation, and report-only automation specs;
- strong orientation, scoping, planning, implementation, review, verification, readiness, release, and Git boundaries.

It did not have one owner for cross-boundary classification, delegation economics, specialist assignment, conflict synthesis, or quality-boundary selection. Those gaps—not the existing specialist procedures—are the reason for `lead-engineer`.

A separately implemented project-memory foundation provides templates, a validator, a logical project registry, and focused adoption, status, start, and finish workflows. It remains a separate continuity capability. The coordinator may consume or prepare a payload for a repository's canonical record, but does not own its schema or silently update it.

## Target architecture

### 1. Shared Engineering OS

The shared layer owns reusable engineering behavior:

- `global/AGENTS.md`: short universal lean defaults and skill routing;
- `lead-engineer`: opt-in classification, direct or coordinated strategy, read-only delegation, synthesis, and routing to existing owners;
- existing skills: project-memory lifecycle, orientation, intent, scope, diagnosis, architecture, implementation, verification, review, documentation, readiness, release, and Git procedures;
- evaluations and validators: structural and behavioral contracts;
- plugin packaging: versioned distribution of the shared skills.

The coordinator is not a universal router. Ordinary local, ambiguity-only, scope-only, review-only, and readiness-only requests continue to trigger their existing skills directly.

### 2. Specialist perspectives

Specialists are bounded perspectives selected for a question, not permanent agents or separate skills. The common assignment contract defines the decision supported, question, read-only boundary, context, evidence, output, non-goals, and stop condition.

The initial selector groups roles into:

- structure and product;
- application and data;
- platform and operations;
- assurance;
- knowledge.

This covers architecture, backend, frontend, database, infrastructure, DevOps, machine learning, data, security, performance, QA, accessibility, UX, documentation, release, observability, developer experience, product scope, and independent review without maintaining a prompt for every title.

### 3. Repository memory

The repository that owns the work owns its durable facts:

- code, configuration, schemas, and tests own behavior;
- repository `AGENTS.md` owns commands, architecture boundaries, environment, and edit cautions;
- an existing issue, plan, or `docs/PROJECT.md` owns active objective, milestone, risks, deferred ideas, evidence freshness, and exact resume action;
- optional ADRs own durable rationale and rejected alternatives;
- Git owns historical changes.

The lead emits a compact continuity payload before a costly context break. Durable mutation requires explicit authority and the `documentation` workflow. On resume, `repo-compass` reconciles continuity records with current Git and executable evidence rather than trusting stale state.

### 4. Domain packs

Future domain packs should be separately installable plugins or packages with their own skills, evaluations, versions, and maintainers. They expose capabilities through trigger metadata and use the same assignment contract.

Core orchestration must not hard-code domain-pack names or import project assumptions. Nested domain skills are not added under this plugin because the current manifest and validator intentionally assume one flat skill root.

### 5. Cross-repository learning

Milestone 1 can produce a proposal only. A later authorized promotion workflow should:

1. identify the originating evidence;
2. separate project context from a generalized claim;
3. test whether the lesson is domain-specific;
4. compare existing shared guidance;
5. propose the narrowest core change;
6. validate it in the originating workflow and at least one contrasting workflow;
7. obtain independent review;
8. accept, revise, or reject it explicitly.

No project may silently mutate `solo-dev-core`.

## Task strategy

Classification uses the highest material driver, not estimated duration:

| Size | Typical signal | Default action |
| --- | --- | --- |
| Tiny | One local, reversible behavior with clear verification | Direct, zero specialists |
| Small | One component and a coherent low-risk file set | Direct |
| Medium | Several connected boundaries, ambiguity, or difficult validation | Coordinate only if questions are independent |
| Large | Multiple components or domains with material risk | Stage work and use bounded investigations |
| Epic | Several large outcomes, repositories, or migrations | Decompose through `solo-dev-scope` |

Risk remains separate: authentication, privacy, irreversible data change, public compatibility, production migration, difficult rollback, or broad operational impact can warrant a separate perspective and stronger evidence even when the code change is small.

Quality selection composes existing owners:

- completion claims → `test-and-verify`;
- structural decisions → `architecture-review`;
- bounded independent defect review → `review-changes`;
- named shipping boundary → `ship-check`.

The coordinator selects relevant boundaries but does not duplicate their checklists, evidence protocols, or verdicts.

## Directory model

```text
solo-dev-core/
├── .codex-plugin/plugin.json
├── global/AGENTS.md
├── skills/
│   ├── lead-engineer/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/coordination-contracts.md
│   ├── adopt-project/
│   │   ├── assets/{PROJECT.md,ADR.md}
│   │   └── scripts/project-memory
│   └── <existing focused and project-memory lifecycle skills>/
├── evals/scenarios.json
├── scripts/
│   ├── validate-skills
│   └── project-memory
├── registry/
│   ├── projects.json
│   └── paths.local.example.json
└── docs/engineering-os-roadmap.md
```

| Path | Responsibility and reason | Reader/updater | Scope and maintenance |
| --- | --- | --- | --- |
| `global/AGENTS.md` | Universal lean defaults and concise routing that must be available across repositories | Every Codex task; maintainer updates deliberately | Global, manual source |
| `skills/lead-engineer/SKILL.md` | Thin coordination workflow and authority boundaries | Codex when its narrow trigger matches | Global, manually maintained |
| `skills/lead-engineer/references/coordination-contracts.md` | Conditional detail for delegation, synthesis, continuity payloads, and proposals | Lead workflow only when needed | Global, manually maintained |
| `skills/*` | Existing task-specific procedures | Matching Codex workflows | Global, manually maintained |
| `evals/scenarios.json` | Canonical routing and behavior scenarios, including non-trigger cases | Validator, forward-testers, maintainers | Global, manually maintained |
| `skills/adopt-project/assets/*` | Canonical optional repository-memory shapes bundled with the installed workflow | `adopt-project` and repository maintainers adopting the convention | Shared skill assets; copied and then owned by each project |
| `skills/adopt-project/scripts/project-memory` | Canonical read-only validation bundled once for all project-memory lifecycle skills | Lifecycle skills, maintainers, and CI or local checks | Shared skill tool; no automatic mutation |
| `scripts/project-memory` | Source-checkout compatibility launcher for the bundled validator | Maintainers and existing commands | Global wrapper; contains no second validator implementation |
| `registry/projects.json` | Logical cross-machine identity inventory only | Maintainer and registry validator | Global metadata; no project details or paths |
| `registry/paths.local.json` | Machine-specific checkout mapping | Local operator only | Local, ignored, never committed |
| `.codex-plugin/plugin.json` | Plugin identity, skill root, and cachebuster payload identity | Codex installer and maintainer | Global, helper-refreshed |
| `docs/engineering-os-roadmap.md` | Architecture status, decisions, migration, limitations, and deferred milestones | Maintainer and reviewers | Global, manually maintained; not an operational routing source |

## Milestone 1

Implemented in this milestone:

- one narrowly triggered `lead-engineer` coordinating skill;
- qualitative size and risk classification mapped to direct, coordinate, or decompose;
- bounded read-only specialist assignment and response contracts;
- lead-owned synthesis and conflict resolution;
- honest serial fallback when subagents are unavailable;
- selection of existing quality and review owners;
- output-only continuity and proposal-only shared lessons;
- behavioral scenarios for direct work, multiple investigations, high-risk small work, conflicts, epic decomposition, no-subagent fallback, deferred ideas, and shared-lesson proposals;
- portable-versus-machine-local installation guidance.

Acceptance criteria:

- existing simple tasks do not require the coordinator;
- direct handling explicitly avoids delegation;
- coordinated work uses only independent read-only assignments;
- conflicting recommendations produce one evidence-backed lead decision or explicit blocker;
- epic work stops at one milestone;
- self-review is never called independent review;
- continuity and shared guidance are never silently mutated;
- existing routing, skill structure, unit tests, project-memory validation, and Markdown diffs pass;
- fresh-context forward tests exercise direct, coordinated, conflicting, and no-subagent paths.

Independent review initially blocked the milestone on installed-payload resource availability, incomplete global routing, and overlap between project-status reconciliation and ordinary closeout. The resolution:

- bundled the canonical project-memory templates and validator under `adopt-project`;
- retained the root validator command as a compatibility launcher;
- added a deterministic skills-only payload smoke test;
- made portfolio registration conditional on an explicit writable registry;
- routed all project-memory lifecycle skills globally;
- kept ordinary batch closeout with `finish-work` and broader reconciliation with `project-status`.

The reviewer rechecked these changes and returned `APPROVE`.

## Migration and portability

Adoption is gradual:

1. Existing repositories can continue with the plugin and global defaults only.
2. Use `repo-compass` on the next serious task.
3. Add or tighten repository `AGENTS.md` only when stable project facts are missing.
4. Adopt project memory only when losing context is costly.
5. Invoke `lead-engineer` only for explicit coordination or materially risky multi-boundary work.

This Git checkout is the portable source. Marketplace registration, installed caches, live global instructions, local paths, credentials, and enabled automations remain machine-local. New machines should prefer a marketplace source that points directly at a reviewed checkout. Legacy machines may retain a separate source copy, but must reconcile it deliberately before reinstalling.

The core must work without automations, subagents, a project registry, or project-memory adoption. No Windows or multi-host automation parity is claimed without testing.

## Roadmap

### Next milestone

- Remove the redundant local marketplace plugin now that direct-checkout links are active.
- Confirm single-source skill discovery and forward-test the coordinator in a fresh Codex task.
- Use the results to tighten triggers or examples before adding capability.

Completed activation work:

- Added and tested an idempotent macOS/Linux installer for 23 direct skill links and global instructions.
- Validated the live links, complete test suite, strict skill checks, project registry, and installed global guidance.
- Documented direct links and marketplace plugins as alternative installation modes.

### Later milestones

- Validate gradual project-memory adoption in real repositories and reduce schema friction if evidence warrants it.
- Add a deliberate cross-repository lesson-promotion workflow.
- Define domain-pack packaging after one real domain pack exists.
- Improve repository health, debt review, release, and maintenance workflows only where current automations or skills leave demonstrated gaps.
- Consider issue-tracker integration, multi-repository coordination, and reusable project bootstrap separately.

### Experiments

- Compare direct-checkout marketplace sources with the legacy two-copy promotion flow.
- Evaluate whether one or two additional specialist perspective examples improve behavior without creating a role catalogue.
- Test the coordinator with and without subagents on equivalent prompts.

### Rejected for now

- A mandatory end-to-end workflow chain.
- Separate task-classification and delegation skills.
- Permanent agents or one skill per specialist role.
- Delegated mutation or overlapping writers.
- A workflow engine, state machine, or central project-management database.
- Silent project-memory updates or automatic shared-lesson promotion.
- Nested domain packs inside the current flat skill root.
- A sync daemon or cross-platform installer.

### Open design questions

- Should the personal marketplace point directly at the Git checkout on every machine, or is a validated promotion command needed for legacy layouts?
- Which project-memory fields prove useful after several real handoffs, and which are ceremony?
- What evidence should justify a first domain pack and its packaging boundary?
- Is a manifest-to-Git revision field needed, or is a committed cachebuster plus source revision sufficient?

## Known limitations

- Structural evaluation validates schemas and routing declarations; it does not prove model behavior.
- No live plugin pickup occurs until the configured source is reconciled, reinstalled, and loaded in a new task.
- The current installation may differ from this Git source and must not be treated as parity evidence.
- Specialist independence is unavailable when only one agent can run.
- Domain packs, automatic promotion, multi-repository execution, and issue-tracker integration are not implemented.
