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
- Git branches main and dev exist and are currently aligned at the ERA5 merge commit.
- Large datasets are stored under /mnt/e/last-aticol.
- Miniforge is installed under /home/fibi/miniforge3.
- Conda environment cds_env exists and is functional.
- Required workflow packages are installed.
- Official WSL CDS ERA5 netcheck script has been committed and succeeded.
- Official ERA5 monthly collection is complete for all required variables for 2000-2025.
- Structural QC for the full ERA5 monthly collection passed and is tracked.
- Scientific sanity QC for the full ERA5 monthly collection passed and is tracked.
- The ERA5 monthly collection and QC phase has been merged into main.
- Seasonal forecast work has not started yet.
- The next active phase is seasonal forecast collection planning from the merged ERA5 baseline.
- The first seasonal target is ECMWF on the C3S monthly seasonal archives.

## Immediate next step
1. Add tracked seasonal planning and configuration files.
2. Define the ECMWF-first seasonal download policy explicitly in Git.
3. Add an official ECMWF seasonal smoke test.
4. Add the first official ECMWF seasonal downloader.
5. Create run metadata before execution.
6. Start the first seasonal workflow on WSL.
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

