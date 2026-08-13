# Status

## Current milestone
- Day-1 Architecture v1 foundation is implemented on `task/architecture-v1-handoff` and remains under final deep audit before any merge to `main`.
- Base checkpoint before Architecture v1 work: `544a375c05d85331ff0e674a89494120d413794f`.
- NCEP integration commit `b574f26702163c424a5b605e414c1d992435642b` is already an ancestor of `main`; older instructions to merge NCEP next are historical.

## Active Architecture v1 control files
- `docs/ARCHITECTURE.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `docs/DECISIONS.md`
- `docs/SEASONAL_DOWNLOAD_POLICY.md`
- `docs/CHATGPT_REENTRY_PROTOCOL.md`
- `configs/datasets/CURRENT_CONFIGS.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `configs/datasets/system_registry_v1.yml`
- `configs/datasets/variable_registry_v1.yml`

## Current scientific scope
- Study window: target/verifying years 2000-2025.
- Manuscript v0.1 target month: December, configuration-driven.
- Scientific horizons H1-H6: one through six calendar months before target.
- Centres: ECMWF, UKMO, DWD, CMCC, Meteo-France, NCEP.
- Variables: z500, t850, z950, t2m, total precipitation, ws10m.
- Manuscript v0.1 domains: NH, ROI, ROI_X4; exact geometries/masks require current approved evidence/configuration.
- Required analysis modes: maximum-valid centre/system analysis and fair common-case cross-centre analysis.

## Current architecture rules
- No universal hindcast/forecast split.
- No global native-lead mapping.
- No global z950 -> z925 substitution.
- No cross-centre propagation of assumptions.
- Forecast/reforecast matching is system-cohort-aware.
- Availability is not scientific eligibility.
- Unknown/conflicting required facts fail closed.
- Common comparisons use canonical eligible case identities.
- Direct raw/calibrated comparisons use the same eligible evaluation cases.
- Parallel centre/metric workstreams require pinned contracts and integration gates.
- Legacy/bootstrap artifacts require revalidation before reuse.
- Major scientific decisions require decision-level evidence/citations and human approval.

## Open scientific work
The controlled register is `docs/OPEN_SCIENTIFIC_QUESTIONS.md`. Items remain intentionally `OPEN — VERIFY WHEN REACHED` until the relevant centre/metric/method workstream reaches them.

## Legacy state
Earlier ERA5/ECMWF/NCEP bootstrap work remains preserved in Git history, runs, inventories, scripts, and literature notes. Legacy configs `c3s_seasonal_systems.yml` and `c3s_seasonal_variables.yml` are classified as historical/bootstrap by `configs/datasets/CURRENT_CONFIGS.md` and are not current Architecture v1 configuration.

## Re-entry state
Architecture v1 re-entry is currently GitHub-first and protocol-driven through `docs/CHATGPT_REENTRY_PROTOCOL.md`.

`scripts/make_chatgpt_reentry_pack_v2.sh` is retained as historical tooling but is not an active control file and is not authoritative for NORMAL or DEEP re-entry. It must not be used as the basis for merge, production, QC milestone, policy/guardrail, scientific-method, destructive, or uncertain-state decisions.

Before every DEEP AUDIT, fresh remote GitHub evidence must establish the task-branch SHA, `main` SHA, merge base, ahead/behind state, and changed-file diff. Local generated packs do not replace that evidence.

## Production state
- No new production seasonal download is authorized by Architecture v1 itself.
- No calibration implementation is authorized before relevant scientific decisions/case contracts are approved.
- No merge to `main` without explicit human review/approval.

## Next safe action
1. Audit the complete current remote branch diff against `main` after the re-entry safety corrections.
2. Confirm all active Architecture v1 control files are internally consistent and that v2 has no current-authority path.
3. Only after the remote audit is clean, sync the task branch to WSL and validate YAML/current scripts with short staged commands.
4. Resolve any runtime validation defect before merge.
5. Obtain explicit human approval before merging Architecture v1 into `main`.
6. After integration, create centre-specific work packages and begin parallel centre verification.
