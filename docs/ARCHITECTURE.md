# Architecture v1

Status: DAY-1 FOUNDATION BASELINE

## Purpose
This document defines the shared architecture for the C3S seasonal forecast verification and calibration study. It separates scientific evidence, approved decisions, technical implementation, execution evidence, legacy history, and AI-assistant controls so no chat, script, old configuration, bootstrap assumption, or unsupported assistant claim can silently redefine the study.

Implementation should stay lightweight: Markdown, YAML/CSV/JSON registries, Python modules, tests, Git, and run manifests unless later scale justifies more tooling.

## Current manuscript v0.1 scope
- Study window: target/verifying years 2000-2025.
- Target month: December (`target_month = 12`) for manuscript v0.1.
- Scientific horizons H1-H6: one through six calendar months before target.
- For December, those calendar months are November, October, September, August, July, June.
- This calendar definition does not define a native C3S lead index.
- Centres: ECMWF, UKMO, DWD, CMCC, Meteo-France, NCEP.
- Variables: z500, t850, z950, t2m, total precipitation, 10 m wind speed.
- Domain set for manuscript v0.1: NH, ROI, ROI_X4. Exact geometries, masks, grids, and weighting must be verified from current approved evidence/configuration, not legacy assumptions.
- Required result modes: maximum-valid centre/system analysis and fair common-case cross-centre analysis.
- Direct raw-versus-calibrated comparisons use the same verification implementation and the same eligible evaluation cases.

Years, months, centres, domains, variables, and horizons are configuration inputs, not hard-coded scientific-core constants.

## Study-window semantics
`study_window` is defined on target/verifying time, not initialization time. Initialization dates required by a horizon may fall outside the target-year window. Example: January 2000 may require 1999 initializations.

## Truth-state model
- `main`: approved current project truth.
- `task/*`: candidate/proposed state under review.
- tracked `runs/*`: evidence of what actually ran.
- historical/superseded material: valid history, not current policy.
- chat memory: temporary reasoning only.

## AI collaboration safety layer
AI assistants are fallible reasoning/execution agents, not sources of project truth. `docs/AI_COLLABORATION_SAFETY.md` is an active Architecture v1 control and is mandatory for ChatGPT/Codex-assisted project work.

The architecture explicitly guards against hallucination/unsupported claims, stale context, silent omission of user constraints, hidden assumptions, wrong workflow/tool selection, false completion claims, scope contamination, unsafe interactive command sequences, invented artifacts/paths, partial control-file updates, diff/state blindness, and premature scientific decisions.

High-impact assistant work must use a fail-closed control loop: risk classification -> authority loading -> constraint ledger -> evidence discipline -> bounded execution -> post-action verification -> contradiction/omission scan -> completion gate.

For Architecture closure, merge review/decisions, production, QC milestones, scientific-method/data-selection decisions, policy/guardrail changes, destructive work, recovery/cleanup, or stale/confused/uncertain state:
- DEEP AUDIT is mandatory;
- fresh remote GitHub branch/main evidence is mandatory for repository state claims;
- a second adversarial review pass is mandatory;
- COMPLETE/PASS/READY/FIXED/VERIFIED/MERGE-READY language is prohibited until required evidence supports it.

Every material assistant-caused failure must be promoted from a one-off incident to a durable repository control: incident -> root cause -> impact -> immediate correction -> generalized preventive rule -> guardrail/control update -> post-fix remote audit -> re-entry/handoff update where relevant.

A new failure mode that can corrupt scientific truth, repository state, reproducibility, or milestone decisions fails closed for the affected high-impact action until understood and controlled.

## Evidence, decisions, implementation, history
1. Evidence: literature, official documentation, retrieved metadata, QC and repository execution evidence.
2. Scientific decisions: explicit, reviewed, cited, human-approved choices.
3. Technical implementation: configs, registries, scripts, tests, manifests, pipelines.
4. Legacy material: prior bootstrap code, runs, assumptions, decisions retained for audit.
5. AI-assistant control evidence: constraint coverage, tool/workflow selection, post-write verification, contradiction scans, and incident/guardrail records required by `docs/AI_COLLABORATION_SAFETY.md`.

Evidence is not a decision. A script is not a decision. Historical policy is not current policy. An assistant statement is not project truth without the required evidence.

## Evidence classes
Important claims use:
- VERIFIED — REPOSITORY
- VERIFIED — AUTHORITATIVE SOURCE
- VERIFIED — RUNTIME/EXECUTION EVIDENCE
- INFERENCE
- UNKNOWN / NEEDS VERIFICATION

Unknowns fail closed when they affect scientific eligibility, production, calibration, verification, common comparison, multi-model work, repository milestone state, or other high-impact decisions.

## Legacy quarantine
Legacy artifacts are retained but never trusted automatically. Before reuse they must be revalidated against Architecture v1.

The following legacy/bootstrap assumptions are not global scientific rules:
- universal 2000-2016 hindcast / 2017-2025 forecast split;
- global z950 -> z925 substitution;
- ECMWF bootstrap assumptions as six-centre policy;
- hard-coded native lead 1-6 as H1-H6;
- any centre-specific result propagated to another centre without verification.

## No cross-centre propagation of assumptions
A fact verified for one centre/system/product is not automatically true for another. Each centre/system/product must independently verify relevant system/version cohort, forecast/reforecast periods, matching identity, native lead semantics, nominal/actual initialization semantics, verifying period, member structure, variable/level availability, known issues and gaps.

## Scientific horizons and archive mapping
H1-H6 are calendar distances before target. Mapping them to nominal initialization, issue/release context, actual member initialization, native archive lead, and verifying month is not globally assumed. It must be verified per centre/system/product from authoritative documentation and retrieved metadata. Burst and lagged systems are both subject to this rule. Lagged-ensemble horizon attribution remains open until resolved for the relevant workstream.

## System-cohort-aware matching
Forecasts must be calibrated only against scientifically matching reforecast/hindcast systems or versions. The system registry must be time-aware. Centre name alone is not a calibration identity. Pooling across cohorts requires an explicit approved decision.

## Availability is not eligibility
Distinguish documented availability, retrieval-verified availability, metadata-verified availability, QC-passed availability, and scientific eligibility. States may include available, unavailable, conditional, partially available, documented-but-not-retrieval-verified, conflicting-sources, and unknown. Conflicting or unknown required facts fail closed.

## Canonical case identity
Scientific comparisons use canonical cases, not loose year ranges. At minimum track centre, system cohort, forecast/reforecast type, product, nominal initialization, target/verifying period, scientific horizon, native lead, variable/level, domain, grid/mask identity, eligibility/QC status. Where relevant also track member ID, actual initialization, visibility/status, inclusion/exclusion, member-set identity, and verifying period. Observation/reference identity must be traceable.

## Eligibility gates
Use deterministic fail-closed gates such as eligible_for_acquisition, eligible_for_harmonization, eligible_for_calibration, eligible_for_raw_verification, eligible_for_calibrated_verification, eligible_for_common_comparison, and eligible_for_multimodel. Downstream stages may not override unresolved upstream gates.

## Variable semantic recipes
A variable name is insufficient. Each variable requires an approved semantic recipe covering source variable(s), physical definition, units, level, temporal aggregation, transformations, accumulation handling, ERA5 counterpart, missing behavior, and mask/orography behavior as relevant. No silent conversion or substitution is permitted. z950 is the supervisor target; any exception requires a centre/system/product Scientific Exception Review. There is no global z950 -> z925 replacement.

## Known issues feed eligibility
Known issues, date gaps, missing members, metadata defects, and archive problems must be registered and connected to eligibility. Handling may be allow, warn, mask, exclude, or unresolved/block, but must be explicit and traceable.

## Harmonization
Harmonization is explicit and versioned: units, temporal aggregation, grid/regridding, domain extraction, area weighting, masks, below-orography handling, ERA5 alignment. Scientifically consequential defaults may not be hidden in utilities.

## Analysis case construction
Maximum-valid selector uses the maximum scientifically valid cases for a selected centre/system analysis. Common-case selector builds the actual intersection of eligible evaluation cases for the requested centres/systems, variable, target month, horizon, metric/analysis type, domain, and other dimensions. Common comparison uses canonical eligible case IDs, not merely overlapping years.

## Training/evaluation/CV planner
Training/evaluation selection is separate from calibration implementation. The planner controls any fitted/estimated component that could leak evaluation information, including calibration fitting, climatology, event thresholds, reference probabilities, and multi-model weights. Exact CV remains open. Any common training policy must be represented by explicit training-case manifests, not only nominal year ranges.

## Climatology, events, references
Climatology, terciles/quantiles, event definitions, thresholds, and reference forecasts are explicit scientific components and may not be hidden in metric/plotting code. Exact definitions remain open until literature review and approval.

## Calibration
Architecture v1 preselects no calibration algorithm. Calibration includes fit, apply, leakage guard, and provenance of fitted parameters/training cases. Calibration is not assumed to improve every metric.

## Verification
Raw and calibrated forecasts use a shared verification implementation. Target families include reliability, Brier Score/BSS, CRPS/CRPSS, ROC/AUC, and scientifically justified ensemble diagnostics. A metric name alone is insufficient: formulation/estimator, reference definition, ensemble-size handling, and case manifest must be versioned and traceable. Metric-specific choices remain open until implementation.

## Multi-model
Multi-model analysis is in scope but construction remains open. Naive member pooling is not assumed. Candidate methods require literature review and approval. Common-case eligibility and approved member/model handling are mandatory.

## Uncertainty and sensitivity
Confidence intervals, bootstrap/significance procedures, and sensitivity analyses remain open method choices but are supported as a separate layer.

## Parallel workstream orchestration
Independent work may proceed in parallel after shared contracts are pinned. Centre workstreams may run in parallel for all six centres. Metric workstreams may later run in parallel once shared prerequisites are satisfied. Each work package pins base Git SHA, architecture version, study-config snapshot, guardrail version, decision snapshot, relevant schema/registry versions, scope, forbidden shared-policy changes, required outputs, and QC. Workstreams may discover local evidence/problems but may not silently change shared policy; shared-policy conflicts return to CONTROL.

Every parallel AI-assisted workstream also inherits `docs/AI_COLLABORATION_SAFETY.md`; local workstream convenience cannot weaken shared assistant-safety controls.

## Fan-out / fan-in integration
Parallel work follows shared contract -> fan-out -> isolated work -> integration gate -> shared validation -> human-reviewed integration. Parallel outputs are not shared truth before integration.

## QC architecture
Six layers:
1. DATA_QC — integrity, checksums, openability, expected objects.
2. SEMANTIC_QC — dates, variables, units, leads, verifying time, members, aggregation semantics.
3. METHOD_QC — case identity, leakage, references, estimator correctness, masks/weights.
4. SCIENCE_QC — plausibility, known issues, exclusions, interpretation/sensitivity.
5. REPRO_QC — Git/config/registry/input/environment/run provenance.
6. ASSISTANT_QC — constraint coverage, evidence classification, post-action verification, contradiction/omission scan, false-completion prevention, and incident-to-guardrail promotion for AI-assisted high-impact work.

Download success, file openability, or assistant confidence never implies scientific or milestone readiness.

## Artifact lineage and invalidation
Important artifacts/results trace Git SHA, architecture version, study config, decision/registry snapshots, case manifest, input checksums, environment, random seeds, QC as applicable. If a dependency capable of changing a result changes, affected downstream results become stale and must not be treated as current.

## Extensibility
The architecture supports changes through config/registries rather than core rewrites where scientifically possible: adding 1999, variables, domains, target months, all months, and later extreme/special cases. Configurability never bypasses availability, semantic, QC, case, lineage, or assistant-safety checks.

## Future scope
Inactive for manuscript v0.1 but preserved as extension points: all target months; extreme/special cases requested by the supervisor; additional years/variables/domains after review.

## Scientific decision traceability
Every major scientific decision must carry traceable evidence at the decision itself, including inline citations, official URLs, DOI where available, access dates for web sources, alternatives, rationale, consequences, approval state, and Git adoption commit. A separate English advisor-facing Scientific Method and Data Selection Decision Report will later be generated from approved records with inline references and a consolidated References section.

## Human approval gates
Human approval is required before commits intended as approved milestone state, merges, production downloads, destructive operations, scientific-policy/interpretation changes, and QC pass/fail milestone declarations. Assistant completion language does not substitute for human approval.

## Open-question and new-failure policy
Architecture v1 intentionally leaves scientific questions open as `OPEN — VERIFY WHEN REACHED`. The project must know that a question is unresolved, when it becomes blocking, and what evidence is required.

New guardrails may be added when new scientific, workflow, or assistant failure modes are discovered. A material new assistant-caused incident must follow the incident-to-guardrail promotion process in `docs/AI_COLLABORATION_SAFETY.md`; it may not be closed by conversational reassurance alone. Changes must be reviewed/versioned and must not silently rewrite prior execution history.
