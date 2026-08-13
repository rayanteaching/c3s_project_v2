# Status

## Current milestone
- Day-1 Architecture v1 foundation is being closed on `task/architecture-v1-handoff`.
- Architecture v1, the open-scientific-question register, scientific-decision traceability, study v0.1 config, and guardrails v1 are tracked on this branch.
- The architecture checkpoint before this work was `544a375c05d85331ff0e674a89494120d413794f`.
- At that checkpoint, local/remote `main`, `task/literature-note-workflow`, and `task/architecture-v1-handoff` were aligned.
- NCEP integration commit `b574f26702163c424a5b605e414c1d992435642b` is already an ancestor of `main`; older instructions to merge NCEP next are historical and no longer current.

## Current scientific scope
- Study window semantics: target/verifying years 2000-2025.
- Manuscript v0.1 target month: December, configuration-driven.
- Scientific horizons H1-H6: one through six calendar months before target.
- Centres: ECMWF, UKMO, DWD, CMCC, Meteo-France, NCEP.
- Variables: z500, t850, z950, t2m, total precipitation, ws10m.
- Manuscript v0.1 domains: NH, ROI, ROI_X4; exact geometries/masks must be verified from current approved evidence/configuration.
- Required analysis modes: maximum-valid centre/system analysis and fair common-case cross-centre analysis.

## Current architecture rules
- No universal hindcast/forecast split is current scientific policy.
- No global native-lead mapping is assumed.
- No global z950 -> z925 substitution is current scientific policy.
- Centre/system/product facts require independent verification.
- Forecast/reforecast matching is system-cohort-aware.
- Availability is not scientific eligibility.
- Unknown/conflicting required facts fail closed.
- Common comparisons use canonical eligible case identities, not loose year ranges.
- Raw/calibrated direct comparisons use the same eligible evaluation cases.
- Parallel centre and later metric workstreams are allowed only under pinned work-package contracts and integration gates.
- Legacy/bootstrap artifacts are historical evidence and require revalidation before reuse.

## Open scientific work
The following remain intentionally OPEN — VERIFY WHEN REACHED:
- centre/system/version cohorts and valid periods;
- native lead and nominal/actual initialization mapping;
- lagged-ensemble horizon attribution;
- member-set policy and unequal ensemble handling;
- variable semantic recipes and z950 exception handling;
- masks/orography, regridding, weighting;
- calibration training policy and algorithm;
- CV/leakage design;
- climatology/events/reference definitions;
- metric estimators;
- multi-model method;
- uncertainty/significance/sensitivity.

See `docs/OPEN_SCIENTIFIC_QUESTIONS.md` for the controlled register.

## Legacy evidence state
Earlier ERA5, ECMWF bootstrap, and NCEP smoke/download/QC work remains preserved in Git history, runs, inventories, scripts, and literature notes. It is not automatically promoted into Architecture v1 scientific policy.

## Production state
- No new production seasonal download is authorized by the Architecture v1 milestone.
- No calibration implementation is authorized before the relevant scientific decisions and case contracts are approved.
- No merge to `main` is authorized without explicit human review/approval.

## Next safe action
1. Complete migration of current control/re-entry files to Architecture v1.
2. Audit the full branch diff against `main`.
3. Validate re-entry behavior and configuration syntax.
4. Request explicit approval before merging Architecture v1 into `main`.
5. After integration, create centre-specific work packages and begin centre-level verification in parallel.
