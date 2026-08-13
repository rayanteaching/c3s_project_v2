# ChatGPT Re-entry Protocol

## Purpose
Start or restart ChatGPT/Codex-assisted work from current repository truth without relying on stale chat memory.

The repository is the durable project system of record. ChatGPT/Codex are temporary reasoning/execution assistants, not the project-state database.

## Truth-state model
- `main` = approved current project truth.
- `task/*` = candidate/proposed state under review.
- tracked `runs/*` = evidence of what actually ran.
- historical/superseded material = valid history, not current policy.
- chat memory = temporary reasoning only.

If chat memory conflicts with repository evidence, repository evidence wins. If current repository controls conflict internally, stop and resolve the conflict; do not guess.

## Mandatory control files
Load the current controls relevant to the task before using legacy material as authority:
- `docs/ARCHITECTURE.md`
- `docs/AI_COLLABORATION_SAFETY.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `docs/DECISIONS.md`
- `docs/STATUS.md`
- `docs/HANDOFF.md`
- `docs/SEASONAL_DOWNLOAD_POLICY.md`
- `docs/CHATGPT_REENTRY_PROTOCOL.md`
- `docs/WORK_PROTOCOL.md`
- `configs/datasets/CURRENT_CONFIGS.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `configs/datasets/system_registry_v1.yml`
- `configs/datasets/variable_registry_v1.yml`

Do not load unrelated files merely for completeness.

## Mandatory opening behavior
Every new chat begins with repository verification, but verification depth is proportional to risk under `docs/WORK_PROTOCOL.md`.

The first response must establish enough current authority for the intended deliverable and state:
1. mode: `INSPECT` or `CHANGE`;
2. risk: `LOW`, `MEDIUM`, or `HIGH`;
3. one concrete, bounded, verifiable primary deliverable;
4. current remote authority/SHA required by that risk;
5. relevant blockers/TBD/contradictions;
6. allowed scope and forbidden adjacent work;
7. next safe action.

This opening verification is not a separate bureaucratic milestone for LOW work. It may be a compact header when a minimal remote check is sufficient.

If verification reveals stale/confused state, a control contradiction, unexpected branch divergence, sensitive scope, or material uncertainty, escalate the risk level before changing state.

## Risk-based re-entry
### LOW
For typo fixes, ordinary documentation edits, narrow non-destructive maintenance, simple planning, and low-risk read-only diagnosis where authority is clear.

Minimum evidence:
- fresh remote `main` or target-branch SHA relevant to the task;
- target file/state;
- bounded scope;
- proportional post-change diff/state check if writing.

Do not run a Deep Audit solely because the task touches GitHub.

### MEDIUM
For normal code/config/control-document changes with meaningful repository impact but no architecture, security/permission, production, deploy, destructive, or scientific-policy decision.

Required path:
- fresh remote branch/base state;
- exact scope/preflight;
- task branch;
- bounded implementation;
- tests/validation appropriate to the change;
- remote diff/state audit;
- PR/review before becoming `main` truth.

### HIGH
For architecture/governance/guardrail changes, security or permissions, scientific-method/data-selection decisions, production actions, deploys, merge decisions for high-impact work, destructive operations, QC milestone decisions, recovery/cleanup, or stale/confused/uncertain state.

HIGH invokes Deep Audit. Obtain fresh remote evidence for:
1. task-branch SHA;
2. `main` SHA;
3. merge base;
4. ahead/behind;
5. changed-file list/diff relative to `main`.

Then load all relevant controls/configs/evidence, preserve a constraint ledger, keep required TBDs fail-closed, perform proportional tests/runtime verification, and execute the mandatory adversarial second pass.

A local checkout, local remote-tracking ref, generated pack, or remembered handoff does not substitute for fresh remote evidence in HIGH work.

## Repository-change workflow
Use the shared GitHub task branch as the default write target for MEDIUM/HIGH repository work. The WSL checkout is normally a synchronized runtime/validation workspace, not an independent truth source.

Local-first editing is an exception and requires an explicit reason and synchronization path before mutation.

After a meaningful repository write, verify the resulting remote state rather than relying on attempted action memory.

A failed/blocked/ambiguous write requires a system-of-record re-read before retry or fallback.

## Approval model
One explicit approval may cover one predeclared bounded change-set while its target, scope, method, and validation remain unchanged. This may include the scoped branch writes, commits, validation, and PR preparation/creation.

Fresh approval is required for scope expansion or a materially different fallback/target/mutation method.

The following always require their own independent approval immediately before execution:
- merge;
- deploy;
- delete/destructive operation;
- production write/download.

## Assistant execution responsibility
When connected tools can perform the work, ChatGPT/Codex should execute repository inspection, branch work, edits, diffs, applicable tests/validation, and PR preparation/creation rather than transferring routine steps to the user.

User action should be requested only for decisions, required approvals, credentials/access, or operations genuinely unavailable to the tools.

## ADR rule
Architecture changes require an ADR before adoption. Ordinary typo/documentation maintenance and centre-specific evidence work do not.

Scientific decisions use `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`; ADR does not replace scientific traceability.

## Evidence priority
Use evidence in this order:
1. fresh remote GitHub state and current repository controls;
2. current command/runtime output and tracked run evidence;
3. generated local material only as supporting context;
4. user-provided current terminal/runtime output;
5. explicit user decisions/scope;
6. earlier chat memory only as weak context.

Important claims use:
- VERIFIED — REPOSITORY
- VERIFIED — AUTHORITATIVE SOURCE
- VERIFIED — RUNTIME/EXECUTION EVIDENCE
- INFERENCE
- UNKNOWN / NEEDS VERIFICATION

Required unknowns fail closed.

## Legacy quarantine
Legacy scripts, configs, runs, and historical decisions may be useful evidence but do not override Architecture v1 without revalidation.

Do not automatically inherit:
- universal 2000-2016 hindcast / 2017-2025 forecast split;
- global z950 -> z925 substitution;
- fixed native lead 1-6 as H1-H6;
- ECMWF assumptions for other centres;
- any centre-specific assumption for another centre.

## High-impact evidence requirements
### Production acquisition
- HIGH / Deep Audit;
- fresh remote comparison;
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
- independent production approval.

### QC pass/fail declaration
- HIGH / Deep Audit;
- QC layer/criteria and implementation;
- outputs/inventory/log evidence;
- exact thresholds;
- known issues/exclusions;
- explicit milestone approval.

### Scientific decision
- HIGH / Deep Audit;
- open-question ID/scope;
- current architecture/guardrails/config;
- authoritative documentation and peer-reviewed evidence as relevant;
- repository/retrieval evidence where applicable;
- alternatives and consequences;
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

## Tracking policy
Track lightweight workflow-critical docs, configs, scripts, run metadata, inventories, environment definitions, registries, case manifests, AI-assistant incident/control records, and other text metadata required for audit/reproduction.

Do not track large raw/processed data, bulky logs, primary GRIB/NetCDF datasets, secrets, or credentials.

## Milestone closure
Before closing a meaningful HIGH milestone:
1. update current state/control files that are actually affected;
2. review fresh remote branch-vs-main state and changed files;
3. validate syntax/tests/runtime evidence as relevant;
4. perform the adversarial contradiction/omission/unsupported-claim/authority-path second pass;
5. obtain the required independent approval before merge or other sensitive adoption action.

## Chat migration quality rule
If a chat becomes long, stale, or confused enough that evidence, decisions, centre-specific facts, user constraints, or repository state may be mixed, stop before another HIGH decision and start a fresh GitHub-first re-entry.

Do not continue a degraded chat merely to avoid migration.

## Output rule
Keep repository artifacts, paths, filenames, commands, configs, and technical identifiers in English. Discussion/review with the user may be in Persian.
