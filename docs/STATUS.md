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
- a316050






# Status

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly tp production download completed successfully
- ERA5 monthly t2m production download completed successfully
- ERA5 monthly ws10m production download completed successfully
- ERA5 monthly z500 production download completed successfully
- ERA5 monthly t850 production download completed successfully
- ERA5 monthly z950 production download completed successfully

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
- Official ERA5 monthly z500 download completed successfully for 2000-2025
- Official ERA5 monthly t850 download completed successfully for 2000-2025
- Official ERA5 monthly z950 download completed successfully for 2000-2025
- Inventory snapshots exist for ERA5 monthly tp, t2m, ws10m, z500, t850, and z950

## Current blockers
- No current WSL CDS connectivity blocker
- No active ERA5 monthly downloader is required for the current six-variable target set
- Seasonal forecast collection has not started yet

## Next action
1. Formally confirm the full ERA5 monthly collection state across all required variables
2. Review repository documents and run metadata for consistency
3. Prepare the next phase for seasonal forecast data collection
4. Keep transfer-to-server work separate until the local WSL dataset state is fully validated

## Last verified commit
- b8b773c







# Status

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly tp production download completed successfully
- ERA5 monthly t2m production download completed successfully
- ERA5 monthly ws10m production download completed successfully
- ERA5 monthly z500 production download completed successfully
- ERA5 monthly t850 production download completed successfully

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- Miniforge is installed at /home/fibi/miniforge3
- Conda environment cds_env exists and works
- Core workflow packages are installed
- Official WSL CDS ERA5 netcheck succeeded
- Official ERA5 monthly total precipitation download succeeded for 2000-2025
- Official ERA5 monthly 2m temperature download succeeded for 2000-2025
- Official ERA5 monthly 10m wind speed download succeeded for 2000-2025
- Official ERA5 monthly z500 download succeeded for 2000-2025
- Official ERA5 monthly t850 download succeeded for 2000-2025
- Inventory snapshots exist for ERA5 monthly tp, t2m, ws10m, z500, and t850
- A prepared but not yet executed production run exists for ERA5 monthly z950

## Current blockers
- No current WSL CDS connectivity blocker
- ERA5 monthly z950 has not started yet

## Next action
1. Formally close the ERA5 monthly t850 milestone in Git with the final inventory snapshot
2. Start the prepared ERA5 monthly z950 production run
3. After z950 finishes, build the final inventory snapshot and close that milestone in Git

## Last verified commit
- 7ae2b77







# Status

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly tp production download completed successfully
- ERA5 monthly t2m production download completed successfully
- ERA5 monthly ws10m production download completed successfully
- ERA5 monthly z500 production download completed successfully

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- Miniforge is installed at /home/fibi/miniforge3
- Conda environment cds_env exists and works
- Core workflow packages are installed
- Official WSL CDS ERA5 netcheck succeeded
- Official ERA5 monthly total precipitation download succeeded for 2000-2025
- Official ERA5 monthly 2m temperature download succeeded for 2000-2025
- Official ERA5 monthly 10m wind speed download succeeded for 2000-2025
- Official ERA5 monthly z500 download succeeded for 2000-2025
- Inventory snapshots exist for ERA5 monthly tp, t2m, ws10m, and z500
- Prepared but not yet executed production runs exist for ERA5 monthly t850 and z950

## Current blockers
- No current WSL CDS connectivity blocker
- ERA5 monthly t850 has not started yet
- ERA5 monthly z950 has not started yet

## Next action
1. Start the prepared ERA5 monthly t850 production run
2. After t850 is complete and formally closed, continue with the prepared ERA5 monthly z950 run

## Last verified commit
- b9e1d15


