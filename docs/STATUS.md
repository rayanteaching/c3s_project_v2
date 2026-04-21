# Status

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly collection completed successfully for all required variables (tp, t2m, ws10m, z500, t850, and z950)
- ERA5 monthly structural QC passed
- ERA5 monthly scientific sanity QC passed
- ERA5 monthly collection was merged into main
- Seasonal forecast collection planning is now the active phase
- First seasonal target: ECMWF monthly seasonal archives on C3S

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist and currently point to the same merge commit
- Miniforge is installed at /home/fibi/miniforge3
- Conda environment cds_env exists and works
- Core workflow packages are installed
- Official WSL CDS ERA5 netcheck succeeded
- Official ERA5 monthly collection and QC baseline is closed and merged
- Seasonal monthly download phase has not started yet
- Seasonal work will begin from the merged ERA5 baseline

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 blocker
- No current seasonal download blocker identified yet
- Seasonal ECMWF smoke test and downloader bootstrap have not yet been created

## Next action
1. Refresh tracked project state after the ERA5 merge
2. Add tracked seasonal planning/config files for ECMWF
3. Add an official ECMWF seasonal smoke test on C3S monthly single levels
4. Add the first official ECMWF seasonal downloader
5. Commit run metadata before execution
6. Start the first seasonal production workflow on WSL

## Last verified commit
- f35ad85
