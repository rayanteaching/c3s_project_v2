# Seasonal Download Policy

## Scope
This policy governs seasonal forecast data collection from the Copernicus Climate Change Service (C3S) monthly seasonal archives.

## Official source datasets
- seasonal-monthly-single-levels
- seasonal-monthly-pressure-levels

## Phase order
1. ECMWF-only bootstrap
2. Other centres after ECMWF workflow is verified

## Time policy
- Hindcasts: 1993-2016
- Forecasts: 2017-2025
- Full-year collection is allowed at the download stage
- December-target analysis is a later analysis layer, not a download restriction

## ECMWF bootstrap policy
- originating_centre: ecmwf
- system: 51

## Variable policy
### Single levels
- t2m -> 2m_temperature
- ws10m -> 10m_wind_speed
- tp -> total_precipitation

### Pressure levels
- z500 -> geopotential at 500 hPa
- t850 -> temperature at 850 hPa
- z950 -> geopotential at 950 hPa

## Raw-data semantics
- Raw seasonal files must be stored exactly as delivered by CDS.
- Any scientific unit conversion or anomaly calculation belongs to later analysis stages.
- tp must not be silently converted during download.
- z500 and z950 are raw geopotential fields, not geopotential height.

## Request policy
- data_format: grib
- product_type: monthly_mean
- requests must record the exact API payload in tracked run metadata or raw sidecars
- valid month must be derived programmatically from start month and leadtime month
- lagged-system handling must be implemented explicitly when non-ECMWF centres are introduced

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
