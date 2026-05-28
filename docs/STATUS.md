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
- ECMWF seasonal monthly pressure-level z925 smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
- The repository bootstrap assumption using ECMWF system 51 for forecast years 2017-2025 has passed initial smoke validation
- Grouped ECMWF monthly single-level hindcast download for 2000-2016 completed successfully
- Grouped ECMWF monthly single-level forecast download for 2017-2025 completed successfully
- Tracked inventory snapshots were created for both ECMWF grouped single-level blocks
- The first ECMWF seasonal monthly single-level bootstrap download milestone is formally closed and merged into main
- Seasonal pressure-level work has begun on the z925-based pressure-level track
- A matching ERA5 monthly z925 dataset has been downloaded, inventoried, and included in the ERA5 monthly QC workflow before seasonal pressure-level verification
- Hindcast and forecast requests are handled separately operationally
- ECMWF seasonal monthly pressure-level production completed successfully for hindcast 2000-2016 and forecast 2017-2025
- ECMWF pressure-level inventory snapshots were created for z500, t850, and z925
- ECMWF pressure-level structural checksum QC passed after canonical naming-family selection
- Hybrid ChatGPT re-entry architecture was added on branch task/llm-workflow-os
- Re-entry workflow now supports normal and deep audit modes
- Scientific evidence notes are now stored under docs/literature/ as evidence notes, not official decisions
- Hybrid re-entry pack generation was syntax-checked and smoke-tested in both normal and deep modes

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
- Official ECMWF seasonal monthly pressure-level smoke-test script is tracked
- Official grouped ECMWF seasonal monthly single-level production downloader is tracked
- Hindcast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- Forecast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- No `.part` files remain in the grouped forecast directory
- Inventory snapshots exist at:
  - data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
  - data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
- The grouped-download milestone closure commit on dev is e373eb8
- main contains the ERA5 z925 supplement and z925 QC extension commits after reintegration
- task/era5-z925 has been reintegrated into main for the ERA5 z925 supplement and QC extension
- Hybrid ChatGPT re-entry feature commit on task/llm-workflow-os is 89ceb1a
- Normal re-entry mode is intended for low-risk planning, documentation, small script review, and non-destructive diagnosis
- Deep audit re-entry mode is required for production downloads, merges, QC pass/fail declarations, policy changes, scientific-method decisions, destructive operations, branch cleanup, or recovery after confused state
- Generated test re-entry packs are treated as ephemeral validation artifacts unless explicitly archived for audit or recovery

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 blocker
- No current ECMWF grouped download blocker
- No blocker remains for the completed ECMWF single-level bootstrap download milestone
- No blocker remains for the completed ECMWF pressure-level production download milestone
- No blocker remains for the hybrid LLM workflow architecture.
- Pressure-level duplicate naming-family warning was handled by moving the noncanonical duplicate family out of active raw directories without deletion
- ECMWF pressure-level canonical GRIB openability QC passed for sampled st01 and st12 files using ecCodes
- ECMWF pressure-level scientific sanity QC passed for all 72 canonical GRIB files using ecCodes sampled-message checks
- NCEP CFSv2 activation review has started; production download is blocked until smoke tests verify system=2 coverage and member handling
- C3S seasonal pressure-level QA review is documented; NCEP production remains blocked until smoke tests verify system=2 coverage, member handling, and metadata semantics
- An unrelated untracked NCEP design-only run metadata directory exists at runs/2026-05-11_ncep_pressure_levels_production_design_plan/ and must be handled in a separate NCEP milestone

## Next action
1. Review the hybrid LLM workflow closure commit on task/llm-workflow-os
2. Decide whether to merge or reintegrate task/llm-workflow-os according to repository branch policy
3. Keep the unrelated NCEP design-only run metadata out of the workflow closure commit
4. Handle runs/2026-05-11_ncep_pressure_levels_production_design_plan/ in a dedicated NCEP milestone

## Last verified milestone commit
- fd60190
