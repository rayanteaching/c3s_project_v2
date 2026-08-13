# ChatGPT Re-entry Protocol

## Purpose
This protocol starts or restarts ChatGPT/Codex-assisted work without relying on stale chat memory.

The repository is the durable project system of record. ChatGPT/Codex are temporary reasoning/execution assistants, not the project-state database.

## Truth-state model
- `main` = approved current project truth.
- `task/*` = candidate/proposed state under review.
- tracked `runs/*` = evidence of what actually ran.
- historical/superseded material = valid history, not current policy.
- chat memory = temporary reasoning only.

If chat memory conflicts with repository evidence, repository evidence wins. If current repository files conflict internally, stop and resolve the conflict; do not guess.

## Repository-change workflow safety
For repository work performed with ChatGPT/Codex, use the shared GitHub task branch as the default collaboration write target. The WSL checkout is normally the synchronized runtime/validation workspace, not an independent project-truth source.

Before a repository change:
- read the current GitHub task-branch state;
- confirm the intended branch and base SHA;
- read Architecture v1 control files relevant to the change.

After a repository change:
- audit the remote branch state and changed-file diff before declaring the work complete;
- then synchronize WSL from that GitHub branch for runtime or syntax validation when local execution is required.

Local-first repository editing is an exception, not the default. It requires an explicit reason such as runtime-only tooling, local-only generated artifacts, or connector limitations. If local-first work is necessary, the reason and synchronization path must be stated before making the change.

Interactive validation commands given to the user must not intentionally enable shell behavior that can terminate the user's interactive terminal on the first failed check. Validation should be short, staged, and failure-reporting rather than terminal-exiting.

## Mandatory Architecture v1 control files
Every project re-entry must load these before using legacy bootstrap files as context:
- `docs/ARCHITECTURE.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `docs/STATUS.md`
- `docs/HANDOFF.md`
- `docs/DECISIONS.md`

These files define current shared design, open questions, guardrails, study semantics, and state.

## Evidence priority
Use evidence in this order:
1. current repository files and current command output;
2. generated repository re-entry pack;
3. user-provided current terminal/runtime output;
4. user statements about intended decisions/scope;
5. earlier chat memory only as weak context.

Scientific evidence uses the project classes:
- VERIFIED — REPOSITORY
- VERIFIED — AUTHORITATIVE SOURCE
- INFERENCE
- UNKNOWN / NEEDS VERIFICATION

Required unknowns fail closed.

## Re-entry modes
### Normal mode
Use for planning, discussion, documentation, low-risk review, and non-destructive diagnosis.

Normal mode should include:
- objective;
- branch/SHA/status;
- Architecture v1 control files;
- recent branch commits;
- relevant configs/scripts/evidence only for the current objective.

Do not load unrelated literature, all inventories, long logs, or the full repository tree merely for completeness.

### Deep-audit mode
Required for:
- production downloads;
- merge decisions;
- branch cleanup/recovery;
- QC pass/fail declarations;
- scientific-method/data-selection decisions;
- policy/guardrail changes;
- destructive operations;
- confused or stale state;
- any case where scientific interpretation or repository/data state is uncertain.

Deep audit adds, as relevant:
- full branch graph and diffs;
- current policies/configs/scripts;
- run metadata/inventories/checksums;
- relevant logs;
- authoritative scientific references;
- centre/system/product registry/case evidence;
- artifact-lineage/staleness evidence.

## Mandatory opening behavior
At a new chat or after migration, first summarize:
1. current branch and SHA;
2. current objective;
3. current milestone;
4. architecture/config/guardrail versions;
5. completed work;
6. blockers/open questions relevant to the objective;
7. risks;
8. next safe step;
9. missing evidence.

Do not issue production/download/merge/destructive commands or adopt a scientific decision before this re-entry summary is complete.

## Legacy quarantine on re-entry
Legacy scripts, configs, runs, and historical decisions may be useful evidence, but they must not override Architecture v1 merely because they are older or already implemented.

Do not automatically inherit:
- universal 2000-2016 hindcast / 2017-2025 forecast split;
- global z950 -> z925 substitution;
- fixed native lead 1-6 as H1-H6;
- ECMWF assumptions for other centres;
- any centre-specific assumption for another centre.

## Task-specific evidence checklists
### Documentation-only change
- branch/status/SHA;
- target document;
- Architecture v1 relevance;
- current objective;
- diff before milestone closure.

### Script/config change
- branch/status/SHA;
- Architecture v1/guardrails;
- target script/config;
- relevant scientific decision/evidence;
- expected behavior;
- validation/test command;
- diff.

### Production acquisition
- deep audit;
- centre/system/product work package;
- verified system cohort/availability;
- horizon/native-lead/init semantics;
- variable/level semantic eligibility;
- known issues;
- target script/plan;
- paths/storage;
- request/run metadata;
- expected outputs;
- inventory/QC plan;
- explicit human approval.

### QC pass/fail declaration
- QC layer/criteria;
- QC implementation;
- outputs/inventory/log evidence;
- exact pass/fail thresholds;
- known issues/exclusions;
- explicit human approval for milestone declaration.

### Scientific decision
- open-question ID/scope;
- current architecture/guardrails/config;
- relevant official documentation and peer-reviewed evidence;
- repository/retrieval evidence where applicable;
- alternatives;
- consequences;
- uncertainty/limitations;
- decision-level citations;
- human approval;
- consistent updates to decisions/configs/registries/QC.

Use `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`.

## Parallel workstream rule
Centre and metric chats/workstreams may run in parallel only from pinned work packages. They may discover local evidence but may not silently alter shared Architecture/guardrails/method policy. Shared conflicts return to CONTROL for review and integration.

A work package should identify:
- base Git SHA;
- architecture/config/guardrail/decision versions;
- scope;
- required evidence/outputs;
- forbidden shared-policy changes;
- integration/QC requirements.

## Scientific evidence layer
Scientific papers and official documentation are evidence, not decisions. Store/retrieve relevant evidence under `docs/literature/` and cite authoritative online sources where appropriate.

A scientific decision becomes current policy only after the adoption process defined in `docs/DECISIONS.md` and `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`.

## Human approval gates
Human approval is required before:
- milestone commits intended to establish approved state;
- merges;
- production downloads;
- destructive operations;
- scientific policy/interpretation changes;
- QC pass/fail milestone declarations.

## Tracking policy
Track lightweight workflow-critical docs, configs, scripts, run metadata, inventories, environment definitions, registries, case manifests, and other text metadata required for audit/reproduction.

Do not track large raw/processed data, bulky logs, primary GRIB/NetCDF datasets, secrets, or credentials.

## Milestone closure
Before closing a meaningful milestone:
1. update `docs/STATUS.md`;
2. update `docs/HANDOFF.md`;
3. update `docs/DECISIONS.md` when a decision changed;
4. update Architecture/open questions/guardrails/configs when relevant;
5. update run metadata/inventories/QC evidence when runtime state changed;
6. review Git diff and forbidden files;
7. validate config/script syntax/tests as relevant;
8. obtain human approval before merge/milestone adoption.

## Chat migration quality rule
If the active chat becomes long/confused enough that evidence, decisions, centre-specific facts, or repository state may be mixed or hallucinated, stop before making another high-impact decision. Close or checkpoint the current milestone in Git where appropriate, generate a fresh re-entry pack, and migrate to a new chat.

Do not continue a degraded chat merely to avoid migration.

## Output rule
Keep repository artifacts, paths, filenames, commands, configs, and technical identifiers in English. Discussion/review with the user may be in Persian.
