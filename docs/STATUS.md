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
- Seasonal bootstrap will start with monthly single-level archives
- Seasonal pressure-level work is deferred until the 925-vs-supervisor-level decision is documented
- Hindcast and forecast requests will be separated operationally

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- ECMWF seasonal bootstrap target is system 51
- Project seasonal hindcast target is 2000-2016
- Project seasonal forecast target is 2017-2025
- Seasonal bootstrap product type is monthly_mean
- Seasonal bootstrap format is GRIB
- Seasonal work has not started yet
- No seasonal smoke test has been committed yet
- No seasonal downloader has been committed yet

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 blocker
- Seasonal operational files still need correction before execution
- Seasonal smoke test and first downloader are not yet committed

## Next action
1. Correct and commit the seasonal policy/config files
2. Add an official ECMWF seasonal smoke test
3. Add the first official ECMWF monthly single-level downloader
4. Commit hindcast and forecast run metadata separately before execution
5. Start the hindcast bootstrap run
6. Start the forecast bootstrap run
7. Track inventory and close the milestone formally in Git

## Last verified commit
- e070f4d
