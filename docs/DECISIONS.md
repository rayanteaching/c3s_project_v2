# Decisions

## Architecture v1 decision baseline
Architecture v1 and its Day-1 closure controls are the approved shared design baseline on `main`.

Required control files:
- `docs/ARCHITECTURE.md`
- `docs/AI_COLLABORATION_SAFETY.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`

## Current approved architecture-level decisions
- The repository is the durable project system of record; chat is temporary reasoning context.
- `main` is approved current truth; task branches are candidate state; run metadata is execution evidence; historical/superseded material is not current policy.
- AI assistants are fallible reasoning/execution agents, not sources of project truth; AI-assisted work is governed by `docs/AI_COLLABORATION_SAFETY.md`.
- High-impact AI-assisted work requires risk classification, current authority loading, material constraint coverage, evidence classification, bounded execution, post-action verification, a separate adversarial contradiction/omission audit, and a completion gate.
- Material assistant-caused failures must be promoted from incidents to generalized durable guardrails; conversational promises alone do not close a failure mode.
- High-impact re-entry requires a fresh remote GitHub comparison of the task branch and `main`; local generated packs or local refs are supporting evidence only.
- The former `scripts/make_chatgpt_reentry_pack_v2.sh` is preserved in Git history only and is not an Architecture v1 approval gate.
- Study window semantics are target/verifying years 2000-2025.
- Manuscript v0.1 target month is December and must be configuration-driven.
- Scientific horizons H1-H6 mean one through six calendar months before the target month.
- The calendar horizon definition does not globally determine native C3S lead indices.
- Native lead, nominal initialization, actual member initialization, and verifying-period mapping must be verified per centre/system/product.
- No centre-specific assumption may be propagated to another centre without verification.
- Six centres are in scope: ECMWF, UKMO, DWD, CMCC, Meteo-France, NCEP.
- Current target variables are z500, t850, z950, t2m, total precipitation, and ws10m.
- There is no global z950 -> z925 substitution.
- Manuscript v0.1 domains are NH, ROI, ROI_X4; exact geometries/masks must be verified from current approved evidence/configuration.
- Two result modes are required: maximum-valid centre/system analysis and fair common-case cross-centre analysis.
- Common comparisons use actual intersections of eligible canonical cases, not only nominal year ranges.
- Forecast calibration must use scientifically matching reforecast/hindcast system cohorts.
- Availability is not equivalent to scientific eligibility.
- Unknown/conflicting required scientific facts fail closed.
- Raw and calibrated direct comparisons must use the same eligible evaluation cases and shared verification implementation.
- Parallel centre and metric workstreams are allowed only under pinned work-package contracts and integration gates and inherit the AI collaboration safety controls.
- Major scientific decisions require traceable evidence, inline citations, alternatives, rationale, consequences, human approval, and Git adoption reference.
- New guardrails may be added later when new failure modes are discovered; changes must be reviewed/versioned and may not rewrite prior execution history silently.

## Assistant/workflow incident governance
The current incident register and prevention rules are maintained in `docs/AI_COLLABORATION_SAFETY.md`.

Known encoded incidents include:
- WF-001 — wrong repository workflow;
- WF-002 — interactive terminal closed by inappropriate fail-fast behavior;
- WF-003 — wrong re-entry mode;
- WF-004 — re-entry branch-diff blind spot and machine-specific generator path;
- WF-005 — piecemeal assistant-error controls without a generalized safety layer;
- WF-006 — GitHub write approval mismatch.

A material new assistant-caused incident keeps the affected Architecture/milestone state open until root cause, generalized prevention, durable encoding, and post-fix audit are complete.

## Intentionally open scientific decisions
The following remain `OPEN — VERIFY WHEN REACHED` and must not be inferred from old code/configuration or chat memory:
- centre/system/version cohorts and valid forecast/reforecast periods;
- native lead and initialization semantics;
- lagged-ensemble horizon attribution;
- member-set policy and unequal ensemble handling;
- exact variable semantic recipes;
- z950 centre/system exceptions if needed;
- below-orography mask handling;
- grid/regridding/area weighting;
- common calibration training-case policy;
- calibration algorithm;
- CV/leakage design;
- climatology/event/reference definitions;
- metric estimator/formulation details;
- multi-model construction;
- uncertainty/significance/sensitivity methods.

See `docs/OPEN_SCIENTIFIC_QUESTIONS.md` for the controlled register.

## Legacy/superseded global assumptions
The following earlier repository choices remain preserved in Git history as bootstrap/history but are superseded as GLOBAL Architecture v1 policy:
- universal project hindcast 2000-2016 / forecast 2017-2025 split;
- global seasonal z950 -> z925 substitution;
- ECMWF system-51 bootstrap assumptions as six-centre study policy;
- hard-coded native lead 1-6 interpreted as H1-H6;
- any assumption that an old downloader/config defines current scientific truth merely because it exists.

Historical ERA5 z925 downloads/QC and earlier ECMWF/NCEP runs remain valid evidence of what was executed. They are not deleted and may be reused only when a current approved decision makes them scientifically relevant.

## Evidence classification
Important claims use:
- VERIFIED — REPOSITORY
- VERIFIED — AUTHORITATIVE SOURCE
- VERIFIED — RUNTIME/EXECUTION EVIDENCE
- INFERENCE
- UNKNOWN / NEEDS VERIFICATION

Scientific/data/method and high-impact workflow unknowns that affect eligibility or milestone truth fail closed.

## Scientific decision adoption rule
A new scientific-method or data-selection decision becomes current project policy only after:
1. the question/scope is explicit;
2. authoritative/repository evidence is recorded;
3. alternatives and consequences are documented;
4. unresolved uncertainty is stated;
5. human approval is explicit;
6. affected configs/registries/QC/docs are updated consistently;
7. the adoption is version-controlled.

Use `docs/SCIENTIFIC_DECISION_TRACEABILITY.md` for the decision record structure.

## Work protocol decision
Candidate workflow hardening adopts **Fast by default, strict when risky**.

Every chat/task declares one concrete, bounded, verifiable primary deliverable using `docs/WORK_PROTOCOL.md`, together with `INSPECT`/`CHANGE` and a `LOW`/`MEDIUM`/`HIGH` risk classification.

- LOW uses minimal fresh verification and proportional validation.
- MEDIUM uses scope/preflight, task branch, validation/tests, remote diff, and PR/review.
- HIGH invokes Deep Audit, required-TBD fail-closed behavior, stronger verification, and the adversarial second pass.

One explicit approval may cover one predeclared bounded change-set while target, scope, method, and validation remain unchanged. Scope expansion or a materially different fallback requires fresh approval.

Merge, deploy, delete/destructive operations, and production writes/downloads always require independent approval immediately before the sensitive operation.

Architecture changes require an ADR before adoption. Ordinary typo/documentation maintenance and centre-specific evidence collection do not require ADRs. Scientific decisions continue to use `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`.

When tools are available, ChatGPT/Codex performs repository inspection, branch work, bounded edits, diffs, applicable validation/tests, and PR preparation/creation. Routine executable work is not transferred to the human merely for assistant convenience.

Do not perform adjacent improvements. Do not refactor unrelated code. Do not create unrequested infrastructure.

## Repository and workflow policy
Track lightweight workflow-critical files needed for understanding, reproduction, verification, continuation, or audit, including docs, configs, scripts, run metadata, inventories, AI-assistant incident/control records, and environment definitions.

Do not track raw/processed large datasets, large logs, secrets, or credentials.

## Human approval gates
Independent human approval is required before:
- merges;
- deploys;
- production writes/downloads;
- destructive/delete operations;
- scientific policy/interpretation changes;
- QC pass/fail milestone declarations;
- milestone adoption intended as approved shared state where applicable.

## Milestone closure
A meaningful milestone must update the relevant current state, decisions, AI collaboration safety controls when affected, run metadata, inventories/QC, and reusable workflow documentation before merge. Continuation relies on repository state, not chat memory.
