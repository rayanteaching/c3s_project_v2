# Status   4

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly tp production download completed successfully
- ERA5 monthly t2m production download completed successfully
- ERA5 monthly ws10m production download is currently running

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
- Inventory snapshots exist for ERA5 monthly tp and ERA5 monthly t2m
- The ERA5 monthly ws10m production run is active on WSL
- Prepared but not yet executed production runs exist for ERA5 monthly z500, t850, and z950

## Current blockers
- No current WSL CDS connectivity blocker
- ERA5 monthly ws10m is still running and not yet formally closed
- ERA5 monthly z500 has not started yet
- ERA5 monthly t850 has not started yet
- ERA5 monthly z950 has not started yet

## Next action
1. Continue monitoring the running ERA5 monthly ws10m production run
2. After ws10m finishes, formally close that milestone in Git
3. Then start the prepared ERA5 monthly z500 production run
4. After z500, continue with t850 and z950

## Last verified commit
- 142574f





# Status 3

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly tp production download completed successfully
- ERA5 monthly t2m production download completed successfully

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
- Inventory snapshots exist for ERA5 monthly tp and ERA5 monthly t2m
- Prepared but not yet executed production runs exist for ERA5 monthly ws10m and ERA5 monthly z500

## Current blockers
- No current WSL CDS connectivity blocker
- ERA5 monthly ws10m has not started yet
- ERA5 monthly z500 has not started yet

## Next action
1. Formally close the completed ERA5 t2m milestone in Git
2. Start the prepared ERA5 ws10m production run
3. After ws10m is stable or completed, continue with z500

## Last verified commit
- debcfe1














# Status 2

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- First official ERA5 production download completed successfully

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
- Raw GRIB files, request sidecars, and sha256 sidecars were written under the WSL data root on drive E
- An inventory snapshot for the ERA5 monthly tp dataset has been created

## Current blockers
- No current WSL CDS connectivity blocker
- The next official ERA5 variable downloader has not been started yet

## Next action
1. Formally close the completed ERA5 tp milestone in Git
2. Start the next official ERA5 downloader
3. Continue building the ERA5 baseline dataset family

## Last verified commit
- 81db45e











# Status 1

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- First official ERA5 downloader not started yet

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- Miniforge is installed at /home/fibi/miniforge3
- Conda environment cds_env exists and works
- Core workflow packages are installed
- Official WSL CDS ERA5 netcheck succeeded
- Netcheck output file exists under /mnt/e/last-aticol/tmp/netcheck
- No official ERA5 downloader has been committed yet

## Current blockers
- No current connectivity blocker on WSL
- First official ERA5 downloader still needs to be implemented

## Next action
1. Commit the successful netcheck run metadata
2. Finalize the current status and handoff documents
3. Add the first official ERA5 downloader
4. Start the first production download with nohup

## Last verified commit
- 9cf19a7













# Status 0

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup in progress

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- Miniforge is installed at /home/fibi/miniforge3
- Conda environment cds_env exists
- Required workflow packages are not installed yet
- No official CDS netcheck has been run yet
- No official ERA5 downloader has been committed yet

## Current blockers
- cdsapi and other workflow packages are missing from cds_env
- env/cds_env.yml has not been exported yet
- CDS connectivity from WSL has not been verified yet

## Next action
1. Install workflow packages into cds_env
2. Export env/cds_env.yml
3. Commit environment state
4. Add and run the official CDS netcheck script

## Last verified commit
- b5a422d
