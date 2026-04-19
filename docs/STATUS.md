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
- ERA5 monthly collection is ready for merge review
- Seasonal forecast collection has not started yet

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- Miniforge is installed at /home/fibi/miniforge3
- Conda environment cds_env exists and works
- Core workflow packages are installed
- Official WSL CDS ERA5 netcheck succeeded
- Official ERA5 monthly total precipitation download completed successfully for 2000-2025
- Official ERA5 monthly 2m temperature download completed successfully for 2000-2025
- Official ERA5 monthly 10m wind speed download completed successfully for 2000-2025
- Official ERA5 monthly geopotential at 500 hPa download completed successfully for 2000-2025
- Official ERA5 monthly temperature at 850 hPa download completed successfully for 2000-2025
- Official ERA5 monthly geopotential at 950 hPa download completed successfully for 2000-2025
- Inventory snapshots exist for ERA5 monthly tp, t2m, ws10m, z500, t850, and z950
- Run metadata exists for all ERA5 monthly production runs
- ERA5 monthly collection milestone is formally closed in Git
- ERA5 monthly structural QC passed with tracked summary and details outputs
- ERA5 monthly scientific sanity QC passed with tracked CSV outputs, plots, and report

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 monthly download blocker
- Seasonal forecast download phase has not started yet
- No current ERA5 monthly QC blocker
- Merge to main has not been performed yet

## Next action
1. Review the tracked ERA5 monthly QC report and plots
2. Prepare and perform the dev-to-main merge for the completed ERA5 monthly phase
3. Start the next seasonal-data phase on top of the closed ERA5 monthly baseline
4. Define the first seasonal forecast collection target and dataset order
5. Prepare the first official seasonal downloader and run metadata
6. Start the first seasonal production run on WSL
7. After WSL validation, plan transfer and downstream server use

## Last verified commit
- 5506a0d


