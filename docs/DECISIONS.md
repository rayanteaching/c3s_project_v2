# Decisions

## Architecture v1 decision baseline
Architecture v1 is the current shared design baseline on `task/architecture-v1-handoff` pending final human review and merge to `main`.

Required control files:
- `docs/ARCHITECTURE.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`

## Current approved architecture-level decisions
- The repository is the durable project system of record; chat is temporary reasoning context.
- `main` is approved current truth; task branches are candidate state; run metadata is execution evidence; historical/superseded material is not current policy.
- High-impact re-entry requires a fresh remote GitHub comparison of the task branch and `main`; local generated packs or local refs are supporting evidence only.
- `scripts/make_chatgpt_reentry_pack_v2.sh` is historical/non-authoritative tooling and is not an Architecture v1 approval gate.
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
- Parallel centre and metric workstreams are allowed only under pinned work-package contracts and integration gates.
- Major scientific decisions require traceable evidence, inline citations, alternatives, rationale, consequences, human approval, and Git adoption reference.
- New guardrails may be added later when new failure modes are discovered; changes must be reviewed/versioned and may not rewrite prior execution history silently.

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
- INFERENCE
- UNKNOWN / NEEDS VERIFICATION

Scientific/data/method unknowns that affect eligibility fail closed.

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

## Repository and workflow policy
Track lightweight workflow-critical files needed for understanding, reproduction, verification, continuation, or audit, including docs, configs, scripts, run metadata, inventories, and environment definitions.

Do not track raw/processed large datasets, large logs, secrets, or credentials.

## Human approval gates
Human approval is required before:
- milestone commits/closure intended as approved state;
- merges;
- production downloads;
- destructive operations;
- scientific policy/interpretation changes;
- QC pass/fail milestone declarations.

## Milestone closure
A meaningful milestone must update the relevant current state, decisions, run metadata, inventories/QC, and reusable workflow documentation before merge. Continuation relies on repository state, not chat memory.
