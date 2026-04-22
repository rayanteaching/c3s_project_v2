# Status

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly collection completed successfully for all required variables
- ERA5 monthly structural QC passed
- ERA5 monthly scientific sanity QC passed
- ERA5 monthly collection was merged into main
- Seasonal forecast planning is active
- Seasonal bootstrap is restricted to ECMWF only
- Seasonal bootstrap starts with monthly single-level archives
- ECMWF seasonal monthly single-level smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
- The repository bootstrap assumption using ECMWF system 51 for forecast years 2017-2025 has passed initial smoke validation
- Seasonal pressure-level work is deferred until the repository begins the z925-based pressure-level branch
- A matching ERA5 monthly z925 dataset must be downloaded later before seasonal pressure-level verification begins
- Hindcast and forecast requests will be separated operationally
- No seasonal production downloader has been committed yet
- No seasonal grouped production run has started yet

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- Branch dev is ahead of main with seasonal planning and ECMWF smoke-test commits
- ECMWF seasonal bootstrap target is system 51
- Documented ECMWF hindcast coverage for system 51 reaches 2016
- Project seasonal hindcast target is 2000-2016
- Project seasonal forecast target is 2017-2025
- Seasonal bootstrap product type is monthly_mean
- Seasonal bootstrap format is GRIB
- Seasonal known-issues registration is now part of repository policy
- Official ECMWF seasonal monthly single-level smoke-test script has been committed
- ECMWF system 51 hindcast smoke test succeeded for year 2000, month 01, leadtime_month 1, variable 2m_temperature
- ECMWF system 51 forecast smoke test succeeded for year 2017, month 01, leadtime_month 1, variable 2m_temperature
- Smoke-test GRIB, request sidecar, and SHA256 sidecar were created successfully under the seasonal raw-data tree

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 blocker
- No current ECMWF smoke-test blocker
- The first grouped ECMWF monthly single-level production downloader is not yet committed
- Separate hindcast and forecast production run metadata are not yet prepared
- The ECMWF system-51 full forecast-period assumption has passed smoke validation but still awaits broader grouped production validation

## Next action
1. Repair and commit the tracked project documents after smoke-test success
2. Add the first official grouped ECMWF monthly single-level production downloader
3. Create separate hindcast and forecast production run metadata
4. Start the grouped hindcast bootstrap workflow on WSL
5. Start the grouped forecast bootstrap workflow on WSL
6. Track inventory snapshots for produced files
7. Close the first ECMWF seasonal monthly single-level milestone formally in Git

## Last verified commit
- 1c3c905








# Status

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly collection completed successfully for all required variables
- ERA5 monthly structural QC passed
- ERA5 monthly scientific sanity QC passed
- ERA5 monthly collection was merged into main
- Seasonal forecast planning is active
- Seasonal bootstrap is restricted to ECMWF only
- Seasonal bootstrap starts with monthly single-level archives
- Seasonal ECMWF forecast years 2017-2025 are currently handled with a working repository assumption of system 51
- Seasonal pressure-level work is deferred until the repository begins the z925-based pressure-level branch
- A matching ERA5 monthly z925 dataset must be downloaded later before seasonal pressure-level verification begins
- Hindcast and forecast requests will be separated operationally

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- ECMWF seasonal bootstrap target is system 51
- Documented ECMWF hindcast coverage for system 51 reaches 2016
- Project seasonal hindcast target is 2000-2016
- Project seasonal forecast target is 2017-2025
- Seasonal bootstrap product type is monthly_mean
- Seasonal bootstrap format is GRIB
- Seasonal work has not started yet
- No seasonal smoke test has been committed yet
- No seasonal downloader has been committed yet
- Seasonal known-issues registration is now part of repository policy

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 blocker
- Seasonal smoke test and first downloader are not yet committed
- The ECMWF system-51 full forecast-period assumption still requires empirical validation during bootstrap

## Next action
1. Commit the seasonal known-issues register and seasonal assumption wording
2. Add an official ECMWF seasonal smoke test
3. Add the first official ECMWF monthly single-level downloader
4. Create separate run metadata for hindcast and forecast execution
5. Start the hindcast bootstrap run
6. Start the forecast bootstrap run
7. Track inventory and close the milestone formally in Git

## Last verified commit
- 626686b
