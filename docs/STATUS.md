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
- Grouped ECMWF monthly single-level hindcast download for 2000-2016 completed successfully
- Grouped ECMWF monthly single-level forecast download for 2017-2025 completed successfully
- Tracked inventory snapshots were created for both ECMWF grouped single-level blocks
- The first ECMWF seasonal monthly single-level bootstrap download milestone was merged into main
- A separate linked worktree exists for parallel ERA5 monthly z925 work
- Seasonal pressure-level work on the stable main branch remains deferred until the z925 branch workflow is completed and merged
- A matching ERA5 monthly z925 dataset must be downloaded later before seasonal pressure-level verification begins
- Hindcast and forecast requests are handled separately operationally

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main, dev, task/era5-z925, and backup-task-era5-z925-before-main-sync exist
- main is the current stable branch baseline
- The grouped ECMWF bootstrap milestone was merged into main at commit 0566034
- The grouped-download milestone closure commit on dev is e373eb8
- The post-closure document refresh commit on dev is 5d450ee
- The current dev tip is already contained in main through merge commit 0566034
- A linked worktree exists at /home/fibi/projects/c3s_project_v2_era5_z925 on branch task/era5-z925
- The linked task/era5-z925 branch currently points to commit 44c6d4d and is behind main
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

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 monthly blocker on main
- No current ECMWF grouped single-level download blocker
- Seasonal pressure-level verification on main remains blocked until ERA5 monthly z925 is downloaded, tracked, and later merged from the parallel branch workflow

## Next action
1. Keep main as the stable project-state branch
2. Continue ERA5 monthly z925 work only in the linked worktree /home/fibi/projects/c3s_project_v2_era5_z925 on branch task/era5-z925
3. Before final reintegration, handle the fact that task/era5-z925 is behind main explicitly
4. Formally close the ERA5 monthly z925 milestone in Git on that branch
5. Merge the z925 branch back into main after milestone closure
6. Begin seasonal pressure-level verification only after the ERA5 monthly z925 baseline is available in repository state on main
7. Re-read repository state before any new production run or any new merge decision

## Last verified commit
- 0566034


## ECMWF seasonal pressure-level task branch started
- Updated at UTC: 2026-04-29T17:33:23Z
- Branch: task/ecmwf-pressure-levels
- Dataset: seasonal-monthly-pressure-levels
- Centre: ECMWF
- System: 51
- Targets: z500, t850, z925
- Hindcast target: 2000-2016
- Forecast target: 2017-2025
- This is a task-branch download start only.
- Do not merge this pressure-level branch into main and do not begin pressure-level verification until ERA5 monthly z925 is completed and merged into main.
