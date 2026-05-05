# Handoff

## Project identity
- Name: c3s_project_v2
- Repository root: /home/fibi/projects/c3s_project_v2
- Primary raw data root: /mnt/e/last-aticol/data/raw
- Primary processed data root: /mnt/e/last-aticol/data/processed

## Source of truth
The repository is the authoritative source of truth.
Do not rely on conversation memory when repository state, logs, or tracked files provide evidence.

## Repository rules
Track:
- docs/
- configs/
- scripts/
- runs/
- data/inventory/
- env/
- workflow-critical text and metadata files required for continuation, reproducibility, or audit

Do not track:
- data/raw/
- data/processed/
- logs/
- large binary datasets
- secrets and credentials

## Platform policy
- WSL Ubuntu is the primary download and validation environment.
- The remote server is used later for downstream processing after verified transfer.

## Mandatory pre-read before continuation
Before any continuation, design, execution, correction, download, QC, or new decision, run:

```bash
cd /home/fibi/projects/c3s_project_v2

cat docs/DECISIONS.md
cat docs/SEASONAL_DOWNLOAD_POLICY.md
cat docs/SEASONAL_KNOWN_ISSUES.md
cat docs/GIT_WORKFLOW.md
cat docs/STATUS.md
cat docs/HANDOFF.md
cat configs/datasets/c3s_seasonal_systems.yml
cat configs/datasets/c3s_seasonal_variables.yml
```

Rules:
- Continue only from the repository state read from those files.
- If a new policy or operational file becomes part of the official workflow, add it to the pre-read list.
- If repository state conflicts with remembered chat context, repository state is final.
- Do not skip this step before any new production run.

## Current confirmed state
- Clean repository bootstrap on WSL is complete.
- The ERA5 monthly baseline is complete, QC-verified, and merged.
- The ERA5 monthly z925 supplement for 2000-2025 is complete and merged into main.
- The ERA5 monthly z925 inventory snapshot is tracked on main.
- The ERA5 monthly QC workflow now includes z925 explicitly.
- ERA5 monthly structural and scientific sanity QC passed for tp, t2m, ws10m, z500, t850, z925, and z950.
- Seasonal work has advanced through planning, smoke-test validation, and the first grouped ECMWF bootstrap download.
- Seasonal bootstrap is intentionally restricted to ECMWF only.
- ECMWF seasonal bootstrap uses C3S system 51.
- Seasonal bootstrap starts with monthly single-level archives only.
- For project forecast years 2017-2025, the use of ECMWF system 51 is currently a working repository assumption for bootstrap execution and later validation.
- That ECMWF system-51 bootstrap assumption passed the initial single-level smoke test for the first project forecast year 2017.
- The ECMWF single-level hindcast path also passed the initial smoke test for project year 2000.
- ECMWF seasonal monthly pressure-level z925 smoke tests passed for project hindcast year 2000 and first project forecast year 2017.
- The official single-level smoke-test script is tracked at scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py.
- The official pressure-level smoke-test script is tracked at scripts/netcheck/11_c3s_seasonal_ecmwf_pressure_levels_smoke.py.
- The official grouped production downloader is tracked at scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py.
- Grouped hindcast download metadata is tracked under:
  - runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/
- Grouped forecast download metadata is tracked under:
  - runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/
- Grouped raw outputs were created successfully under:
  - /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016
  - /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025
- Each grouped block contains 12 GRIB files with matching request and SHA256 sidecars.
- Tracked inventory snapshots exist for both grouped blocks.
- The grouped ECMWF single-level bootstrap download milestone is formally closed and merged into main.
- main contains the closed ECMWF grouped single-level bootstrap milestone and re-entry protocol commits.
- main contains the ERA5 z925 supplement and z925 QC extension commits after reintegration.
- task/era5-z925 has been reintegrated into main for the ERA5 z925 supplement and QC extension.
- Seasonal pressure-level work has begun on the z925-based pressure-level track.
- The repository seasonal pressure-level substitute is z925, not z950.
- Matching ERA5 monthly z925 has been downloaded, inventoried, and included in ERA5 monthly QC before seasonal pressure-level verification begins.
- ECMWF pressure-level canonical GRIB openability QC passed for sampled st01 and st12 files using ecCodes.
- ECMWF seasonal monthly pressure-level production completed successfully for hindcast 2000-2016 and forecast 2017-2025.
- ECMWF pressure-level inventory snapshots were created for z500, t850, and z925.
- ECMWF pressure-level structural checksum QC passed after canonical naming-family selection.
- Seasonal hindcasts and forecasts are requested separately.
- Project seasonal hindcast target is 2000-2016.
- Project seasonal forecast target is 2017-2025.
- GRIB is the operational download format.
- A tracked seasonal known-issues register is required before any non-ECMWF centre is activated.

## Immediate next step
1. Run the next ECMWF pressure-level scientific sanity/QC step using the canonical z500, t850, and z925 files.
2. Keep main and dev synchronized after the QC milestone is closed.
3. Decide the next seasonal verification or processing step only after the pressure-level QC result is documented.

## Standard session report
Always provide the following before continuing work:
- git status --short --branch
- git branch -vv
- git log --oneline --decorate --graph -n 10
- tree -L 3

If a run exists, also provide:
- tail -n 80 <relevant_log_file>
- cat <relevant_status_json>

If environment work was done, also provide:
- conda env list
