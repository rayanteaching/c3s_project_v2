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

## Current confirmed state
- Clean repository bootstrap on WSL is complete.
- Git branches main and dev exist.
- Large datasets are stored under /mnt/e/last-aticol.
- Miniforge is installed under /home/fibi/miniforge3.
- Conda environment cds_env exists and is functional.
- Required workflow packages are installed.
- Official WSL CDS ERA5 netcheck script has been committed and succeeded.
- Official ERA5 monthly collection is complete for all required variables for 2000-2025.
- Completed ERA5 monthly variables:
  - tp
  - t2m
  - ws10m
  - z500
  - t850
  - z950
- Inventory snapshots exist for all completed ERA5 monthly variables.
- Run metadata exists for all completed ERA5 monthly runs.
- The ERA5 monthly collection milestone is formally closed in Git.
- Structural QC for the full ERA5 monthly collection passed and is tracked under runs/2026-04-17_era5_monthly_qc_full/.
- Scientific sanity QC for the full ERA5 monthly collection passed and produced tracked tables, plots, and a report.
- The ERA5 monthly collection is ready for merge review before seasonal work starts.
- The next project phase has not started yet.

## Immediate next step

1. Review the tracked ERA5 monthly QC outputs.
2. Perform the formal merge workflow for the completed ERA5 monthly phase.
3. Begin the seasonal-data phase from the clean, QC-verified baseline.
4. Choose the first seasonal forecast dataset/system to collect.
5. Prepare the corresponding downloader, run metadata, and inventory plan.
6. Start the first seasonal production workflow on WSL.
7. Continue using the same milestone-closure discipline in Git.

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

