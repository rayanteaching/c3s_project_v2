# Seasonal Download Policy

## Scope
This policy governs future C3S seasonal data acquisition under Architecture v1.

Official source datasets may include:
- `seasonal-monthly-single-levels`
- `seasonal-monthly-pressure-levels`

This policy does not authorize any production download by itself.

## Architecture precedence
Before any new production seasonal acquisition, read:
- `docs/ARCHITECTURE.md`
- `docs/AI_COLLABORATION_SAFETY.md`
- `docs/CHATGPT_REENTRY_PROTOCOL.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- relevant current centre/system evidence and known-issue records.

Older ECMWF/NCEP bootstrap acquisition choices remain in Git history, runs, inventories, and scripts as historical execution evidence. They do not automatically define current six-centre scientific policy.

## Required pre-acquisition verification
For the requested centre/system/product/variable/level/horizon/time range, production remains blocked until the relevant items are resolved sufficiently for acquisition:
- system/version cohort identity;
- actual valid forecast and reforecast/hindcast availability;
- scientifically matching forecast-reforecast cohort;
- scientific-horizon to archive-native-lead mapping;
- nominal initialization semantics;
- actual member initialization semantics where relevant/observable;
- verifying period;
- member-set structure and completeness requirements;
- variable/level availability and semantic recipe;
- known issues and gaps;
- output path and storage plan;
- request metadata/sidecar plan;
- inventory/QC plan.

Unknown or conflicting required facts fail closed.

## No universal period split
Architecture v1 study window is target/verifying years 2000-2025. There is no universal project-wide hindcast 2000-2016 / forecast 2017-2025 split. Each centre/system cohort must use its scientifically verified valid periods.

Initialization dates required by a scientific horizon may fall outside the target/verifying-year window.

## Scientific horizons and native leads
H1-H6 are calendar distances before the target month. No global native C3S lead formula is assumed. Mapping must be verified per centre/system/product using authoritative documentation and retrieved metadata.

## System-cohort matching
Forecast and reforecast/hindcast acquisition must preserve the matching system/version relationship required for later calibration and verification. Centre name alone is insufficient.

## Variable and pressure-level policy
Current manuscript v0.1 targets:
- t2m
- total precipitation
- ws10m
- z500
- t850
- z950

There is no global z950 -> z925 substitution. If a target variable/level is unavailable or scientifically unsuitable for a specific centre/system/product, production for that target remains blocked pending a centre/system-specific Scientific Exception Review.

Any previously downloaded z925 data remain valid historical/technical assets and may be reused only if a later approved scientific decision calls for them.

## Raw-data policy
- Preserve raw seasonal files as delivered by the source archive.
- Record exact request payloads/metadata and integrity sidecars according to the active run schema.
- Do not perform silent scientific conversions during acquisition.
- Download success, checksum success, and openability do not imply scientific eligibility.
- Operational file format choices must be justified by current metadata/QC requirements; legacy GRIB choices are evidence, not an immutable architecture rule.

## Lagged systems
Lagged-system behavior must be represented explicitly. Nominal start, actual member initialization, member-set completeness, and horizon attribution may require centre/system-specific handling. No burst-system shortcut may be applied globally.

## Known issues
Known issues and retrieval-discovered gaps must be registered and connected to eligibility. Handling must be explicit: allow, warn, mask, exclude, or unresolved/block. Known issues are not passive notes.

## Parallel centre acquisition design
Centre workstreams may prepare acquisition plans in parallel after receiving pinned work packages. A centre workstream may not modify shared horizon, calibration, common-case, or other project-wide scientific policy. Shared conflicts return to CONTROL.

## Required acquisition provenance
Each production acquisition plan/run must be traceable to, as applicable:
- base Git SHA;
- architecture/config/guardrail versions;
- centre/system cohort record;
- availability/known-issue evidence;
- request payload;
- output location;
- checksums/inventory;
- QC plan/results;
- run manifest.

## Human approval gate
Production execution requires separate explicit human approval after deep audit of the relevant policy, config, script/plan, paths, expected outputs, known issues, and QC criteria.

AI-assisted production work must also satisfy `docs/AI_COLLABORATION_SAFETY.md` before readiness or completion is claimed.

## Legacy note
Earlier policies that fixed ECMWF system 51, 2000-2016/2017-2025 blocks, z925 substitution, or NCEP-specific production rules are retained in Git history and related evidence. They may inform new work but do not override Architecture v1.
