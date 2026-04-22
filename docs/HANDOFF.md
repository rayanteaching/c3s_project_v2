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
cat docs/STATUS.md
cat docs/HANDOFF.md
cat configs/datasets/c3s_seasonal_systems.yml
cat configs/datasets/c3s_seasonal_variables.yml

Rules:

Continue only from the repository state read from those files.
If a new policy or operational file becomes part of the official workflow, add it to the pre-read list.
If repository state conflicts with remembered chat context, repository state is final.
Do not skip this step before any new production run.
Current confirmed state
Clean repository bootstrap on WSL is complete.
The ERA5 monthly baseline is complete, QC-verified, and merged.
Seasonal work has started at the planning and smoke-test stage.
Seasonal bootstrap is intentionally restricted to ECMWF only.
ECMWF seasonal bootstrap uses C3S system 51.
Seasonal bootstrap starts with monthly single-level archives only.
For project forecast years 2017-2025, the use of ECMWF system 51 is currently a working repository assumption for bootstrap execution and later validation.
That ECMWF system-51 bootstrap assumption has passed the initial smoke test for the first project forecast year 2017.
The ECMWF hindcast path has also passed the initial smoke test for project year 2000.
The official smoke-test script is tracked at scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py.
Smoke-test run metadata is tracked under:
runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke/
runs/2026-04-22_c3s_ecmwf_single_levels_forecast_smoke/
Smoke-test raw outputs were created successfully under:
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/smoke
Seasonal pressure-level work is deferred until the pressure-level requirement is documented cleanly against CDS monthly availability.
The repository seasonal pressure-level substitute is z925, not z950.
Matching ERA5 monthly z925 must be downloaded later before seasonal pressure-level verification begins.
Seasonal hindcasts and forecasts will be requested separately.
Project seasonal hindcast target is 2000-2016.
Project seasonal forecast target is 2017-2025.
GRIB is the operational download format.
A tracked seasonal known-issues register is required before any non-ECMWF centre is activated.
The branch dev is ahead of main with seasonal planning and smoke-test commits.
Immediate next step
Refresh the tracked project documents after smoke-test success.
Add the first official grouped ECMWF monthly single-level production downloader.
Create separate hindcast and forecast production run metadata.
Start the grouped hindcast bootstrap workflow on WSL.
Start the grouped forecast bootstrap workflow on WSL.
Track inventory snapshots for produced files.
Continue with the same Git milestone-closure discipline.
Standard session report

Always provide the following before continuing work:

git status --short --branch
git branch -vv
git log --oneline --decorate --graph -n 10
tree -L 3

If a run exists, also provide:

tail -n 80 <relevant_log_file>
cat <relevant_status_json>

If environment work was done, also provide:

conda env list









# Handoff

## Pre-read rule:
Before any continuation step, always read the current project decision, policy, handoff, status, known-issues, and active dataset-config files from the repository. Continuation must rely on repository state, not chat memory.

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

## Current confirmed state
- Clean repository bootstrap on WSL is complete.
- The ERA5 monthly baseline is complete, QC-verified, and merged.
- Seasonal work has not started yet.
- Seasonal bootstrap is intentionally restricted to ECMWF only.
- ECMWF seasonal bootstrap uses C3S system 51.
- Seasonal bootstrap starts with monthly single-level archives only.
- For project forecast years 2017-2025, the use of ECMWF system 51 is currently a working repository assumption for bootstrap execution and later validation.
- Seasonal pressure-level work is deferred until the pressure-level requirement is documented cleanly against CDS monthly availability.
- The repository seasonal pressure-level substitute is z925, not z950.
- Matching ERA5 monthly z925 must be downloaded later before seasonal pressure-level verification begins.
- Seasonal hindcasts and forecasts will be requested separately.
- Project seasonal hindcast target is 2000-2016.
- Project seasonal forecast target is 2017-2025.
- GRIB is the operational download format.
- A tracked seasonal known-issues register is required before any non-ECMWF centre is activated.

## Immediate next step
1. Add an official ECMWF seasonal smoke test.
2. Add the first official ECMWF monthly single-level downloader.
3. Create separate run metadata for hindcast and forecast execution.
4. Start the hindcast bootstrap workflow on WSL.
5. Start the forecast bootstrap workflow on WSL.
6. Continue with the same Git milestone-closure discipline.

## Standard session report
Always provide the following before continuing work:
- git status --short --branch
- git branch -vv
- git log --oneline --decorate --graph -n 10
- tree -L 3

If a run exists, also provide:
- tail -n 80 <relevant_log_file>

If environment work was done, also provide:
- conda env list
