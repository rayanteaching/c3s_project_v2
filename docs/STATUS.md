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
