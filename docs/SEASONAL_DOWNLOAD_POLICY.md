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

## Future ERA5 dependency
- before seasonal pressure-level verification begins, the matching ERA5 monthly z925 dataset must be downloaded and tracked

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
