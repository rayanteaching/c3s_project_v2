# NCEP CFSv2 pressure-level z500/t850 smoke tests

## Scope
This run records lightweight metadata for successful NCEP CFSv2 pressure-level smoke tests.

## Dataset
- CDS dataset: seasonal-monthly-pressure-levels
- Originating centre: ncep
- System: 2
- Forecast system: CFSv2-v20110310
- Format: GRIB
- Area: Northern Hemisphere

## Tested cases
- z500, year 2000, month 01, leadtime_month 1
- t850, year 2000, month 01, leadtime_month 1
- z500, year 2020, month 01, leadtime_month 1
- t850, year 2020, month 01, leadtime_month 1

## Result
The four smoke-test GRIB files were downloaded successfully and checksum verification passed.

## Important caution
Production download is still not authorized.

Before production:
- May 2023 member/date handling must be checked explicitly.
- NCEP forecast-year availability must be finalized from retrieval evidence.
- z925 must not be used for NCEP unless separately verified.
