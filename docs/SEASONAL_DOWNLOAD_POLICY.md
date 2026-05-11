# Seasonal Download Policy

## Scope
This policy governs seasonal forecast data collection from the Copernicus Climate Change Service (C3S) monthly seasonal archives.

## Official source datasets
- seasonal-monthly-single-levels
- seasonal-monthly-pressure-levels

## Bootstrap phase order
1. ECMWF-only bootstrap
2. ECMWF monthly single-levels workflow verification
3. ECMWF pressure-level introduction after documented level decision
4. Other centres after period-specific system mapping and issue registration are validated and committed

## Project target period
- Project hindcast target: 2000-2016
- Project forecast target: 2017-2025
- Year 2026 is out of scope for the current project target

## ECMWF bootstrap policy
- originating_centre: ecmwf
- system: 51
- same system must be used when pairing hindcasts and forecasts
- use of system=51 for forecast years 2017-2025 is currently a working repository assumption for bootstrap, not a final scientific manifest

## Bootstrap variable policy
### Active bootstrap variables
- t2m -> 2m_temperature
- ws10m -> 10m_wind_speed
- tp -> total_precipitation

### Deferred pressure-level variables
- z500 -> geopotential at 500 hPa
- t850 -> temperature at 850 hPa
- z925 -> geopotential at 925 hPa
- the supervisor wording z950 is retained as an external requirement note, but the operational monthly C3S implementation in this repository uses z925 instead

## Request split policy
For operational collection in this repository, hindcasts and forecasts must be requested separately.

### Hindcast request block
- project years: 2000-2016

### Forecast request block
- project years: 2017-2025

## Product policy
- bootstrap product_type: monthly_mean
- bootstrap data_format: grib
- native GRIB is the operational format
- netCDF conversion is not part of the operational download workflow

## Raw-data semantics
- Raw seasonal files must be stored exactly as delivered by CDS.
- Any scientific unit conversion or anomaly calculation belongs to later analysis stages.
- tp must not be silently converted during download.
- z500 and z925 are raw geopotential fields, not geopotential height.

## Operational request policy
- exact API payloads must be recorded in run metadata and raw sidecars
- target valid month must be derived programmatically from start month and leadtime month
- lagged-system handling must be implemented explicitly before any non-ECMWF centre is activated
- form-generated API snippets are helper outputs, not repository source-of-truth configuration

## Known-issues policy
- official C3S seasonal known issues must be registered in tracked repository documentation before a new centre is activated
- each issue must be classified as allow, warn, mask, or exclude
- issues stating that archived wrong data will not be overwritten must be treated as hard warnings

## ERA5 z925 dependency
- before seasonal pressure-level verification begins, the matching ERA5 monthly z925 dataset must be downloaded, tracked, QC-verified, and merged into main
- this dependency is now satisfied on main

## NCEP CFSv2 pressure-level production policy
- NCEP CFSv2 uses originating_centre=ncep and system=2.
- NCEP production download is not authorized until the committed policy, downloader design, inventory schema, and QC checks explicitly handle lagged initialization dates and missing-date completeness.
- Initial NCEP pressure-level smoke tests passed for z500 and t850 for hindcast year 2000 and forecast year 2020.
- Corrected G8-sensitive smoke evidence confirms that nominal June 2023 z500 monthly_mean retrieval is missing dataDate=20230522: contains_20230522=false, messages_for_20230522=0, message_count=120, expected complete 31-date window message_count=124.
- G8 is not a blanket blocker for all NCEP monthly_mean retrievals, but affected nominal months must be flagged and handled explicitly.
- NCEP production inventories and QC summaries must include member/date completeness fields before any NCEP-derived product or multi-model analysis.
- Native GRIB remains required for NCEP production.

## Tracking policy
The following must be tracked in Git:
- docs/
- configs/
- scripts/
- runs/
- data/inventory/
- env/
- workflow-critical text and metadata files

The following must not be tracked:
- data/raw/
- data/processed/
- logs/
- large binary datasets
- secrets and credentials

## Milestone closure policy
No seasonal milestone is considered complete until:
- run metadata is updated
- inventory snapshot is tracked if files were produced
- docs/STATUS.md is updated
- docs/HANDOFF.md is updated
- any reusable operational command is added to docs/RUNBOOK.md when needed
- a precise closing commit is created

## Seasonal pressure-level QA policy
- Monthly pressure-level products are monthly statistics derived from subdaily seasonal forecast data.
- Seasonal products must be interpreted probabilistically.
- Bias correction or bias-aware interpretation is required for scientific applications and derived forecast products.
- Hindcasts/reforecasts are required for model climatology, anomaly construction, and verification.
- Native GRIB remains the operational format for complex seasonal requests.
- Experimental NetCDF is not authorized for operational seasonal download workflows without a separate documented validation.
- Differences between forecast systems in grid, ensemble generation, start-date handling, leadtime metadata, and hindcast availability must be checked before a new centre is activated.
