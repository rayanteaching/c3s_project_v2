# Handoff 2

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
- The first official ERA5 production downloader has been committed.
- Official ERA5 monthly total precipitation download completed successfully for 2000-2025.
- Run metadata exists under runs/2026-04-13_era5_tp_monthly_2000_2025/.
- The ERA5 monthly tp raw files, request sidecars, and sha256 sidecars exist under the configured raw data root.
- An inventory snapshot exists at data/inventory/era5_tp_monthly_2000_2025.csv.

## Immediate next step
1. Commit the completed ERA5 tp milestone closure.
2. Start the next official ERA5 variable downloader.
3. Continue building the ERA5 baseline dataset family.

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












# Handoff 1

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
- Large datasets are planned to live under /mnt/e/last-aticol.
- Miniforge is installed under /home/fibi/miniforge3.
- Conda environment cds_env exists and is functional.
- Required workflow packages are installed.
- Official WSL CDS ERA5 netcheck script has been committed.
- Official WSL CDS ERA5 netcheck completed successfully.
- Netcheck run metadata exists under runs/wsl_cds_netcheck_era5_small/.
- No official production ERA5 downloader has been committed yet.

## Immediate next step
1. Commit the successful netcheck run metadata if not already committed.
2. Finalize status and handoff tracking.
3. Add the first official ERA5 downloader.
4. Start the first production download with nohup.
5. Record the run metadata and inventory snapshot.

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
















# Handoff 0

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
- Large datasets are planned to live under /mnt/e/last-aticol.
- Miniforge is installed under /home/fibi/miniforge3.
- Conda environment cds_env has been created.
- Required Python packages for the workflow are not fully installed yet.
- No official netcheck script has been committed yet.
- No official downloader script has been committed yet.

## Immediate next step
1. Install workflow packages into cds_env.
2. Export env/cds_env.yml and commit it.
3. Add the official WSL CDS netcheck script.
4. Run the netcheck and record the run metadata.

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
