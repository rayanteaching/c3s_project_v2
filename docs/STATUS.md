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
- ERA5 monthly z925 supplement for 2000-2025 completed successfully on task/era5-z925
- ERA5 monthly z925 inventory snapshot is tracked
- ERA5 monthly QC workflow was extended to include z925 explicitly
- ERA5 monthly structural QC passed for tp, t2m, ws10m, z500, t850, z925, and z950
- ERA5 monthly scientific sanity QC passed for tp, t2m, ws10m, z500, t850, z925, and z950
- Seasonal forecast planning is active
- Seasonal bootstrap is restricted to ECMWF only
- Seasonal bootstrap starts with monthly single-level archives
- ECMWF seasonal monthly single-level smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
- The repository bootstrap assumption using ECMWF system 51 for forecast years 2017-2025 has passed initial smoke validation
- Grouped ECMWF monthly single-level hindcast download for 2000-2016 completed successfully
- Grouped ECMWF monthly single-level forecast download for 2017-2025 completed successfully
- Tracked inventory snapshots were created for both ECMWF grouped single-level blocks
- The first ECMWF seasonal monthly single-level bootstrap download milestone is formally closed in Git on dev
- Seasonal pressure-level work has begun on the z925-based pressure-level track
- A matching ERA5 monthly z925 dataset has been downloaded, inventoried, and included in the ERA5 monthly QC workflow before seasonal pressure-level verification
- Hindcast and forecast requests are handled separately operationally

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- main contains the closed ECMWF grouped single-level bootstrap milestone and re-entry protocol commits
- ECMWF seasonal bootstrap target is system 51
- Documented ECMWF hindcast coverage for system 51 reaches 2016
- Project seasonal hindcast target is 2000-2016
- Project seasonal forecast target is 2017-2025
- Seasonal bootstrap product type is monthly_mean
- Seasonal bootstrap format is GRIB
- Seasonal known-issues registration is part of repository policy
- Official ECMWF seasonal monthly single-level smoke-test script is tracked
- Official grouped ECMWF seasonal monthly single-level production downloader is tracked
- Hindcast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- Forecast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- No `.part` files remain in the grouped forecast directory
- Inventory snapshots exist at:
  - data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
  - data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
- The grouped-download milestone closure commit on dev is e373eb8
- main does not yet contain the ERA5 z925 supplement and z925 QC extension commits
- task/era5-z925 has been synchronized with the latest seasonal integration state and is now the active ERA5 z925 supplement branch

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 blocker
- No current ECMWF grouped download blocker
- No blocker remains for the completed ECMWF single-level bootstrap download milestone

## Next action
1. Refresh STATUS, HANDOFF, and RUNBOOK to reflect the completed ERA5 z925 download and QC extension
2. Commit the refreshed z925 project state on task/era5-z925
3. Resolve or abort the stale integration merge-conflict state in /home/fibi/projects/c3s_project_v2 before reintegration
4. Merge task/era5-z925 into main only after the main worktree is clean
5. Decide the next seasonal pressure-level verification step only after z925 reintegration is closed

## Last verified commit
- 1a56570
