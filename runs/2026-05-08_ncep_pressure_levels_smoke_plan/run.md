# NCEP CFSv2 pressure-level smoke-test plan

## Scope
This run metadata records the safe pre-production smoke-test plan for NCEP CFSv2 pressure-level data.

## Centre and system
- Originating centre: ncep
- MARS origin: kwbc
- Forecast system: CFSv2-v20110310
- CDS system: 2
- Dataset: seasonal-monthly-pressure-levels
- Operational format: GRIB

## Current repository decision
NCEP production download is not authorized yet.

## Safe variables for first smoke tests
- z500: variable=geopotential, pressure_level=500
- t850: variable=temperature, pressure_level=850

## Do not use for NCEP pressure-level activation smoke tests
- z925
- pressure_level=925
- year=2017 as the first forecast smoke-test year

## Smoke-test purpose
The smoke tests must verify:
- system=2 request semantics
- available hindcast years and forecast years
- safe pressure-level availability
- nominal start-month handling
- leadtime_month metadata
- member/date handling
- May 2023 G8 caution handling
- GRIB metadata readability

## May 2023 G8 caution
The documented G8 issue states that NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted.

Repository interpretation:
- This is not a blanket blocker for monthly_mean retrieval.
- Forecast May 2023 requires explicit member/date-handling QC.
- NCEP-derived products and multi-model analysis must not use May 2023 blindly.

## First smoke-test candidates
Use small requests only.

Recommended first hindcast smoke tests:
- year=2000, month=01, leadtime_month=1, z500
- year=2000, month=01, leadtime_month=1, t850

Recommended first forecast smoke tests:
- year=2020 or 2021, month=01, leadtime_month=1, z500
- year=2020 or 2021, month=01, leadtime_month=1, t850

Recommended caution-specific smoke test after basic availability succeeds:
- year=2023, month=05, leadtime_month=1, z500
- year=2023, month=05, leadtime_month=1, t850

## Blocked until smoke tests pass
- grouped NCEP production download
- NCEP inclusion in multi-model analysis
- NCEP-derived products
