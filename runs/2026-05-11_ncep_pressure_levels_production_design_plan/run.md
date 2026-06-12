# NCEP pressure-level production design plan

## Purpose
Design the NCEP CFSv2 system=2 pressure-level production workflow after smoke-test and G8 evidence closure.

## Status
planned

## Production execution status
Not authorized in this plan.

## Candidate dataset
- dataset: seasonal-monthly-pressure-levels
- originating_centre: ncep
- system: 2
- forecast_system: CFSv2-v20110310
- data_format: grib
- product_type: monthly_mean

## Candidate pressure-level variables
- z500: geopotential at 500 hPa
- t850: temperature at 850 hPa
- z925: geopotential at 925 hPa, pending explicit NCEP availability smoke test before production inclusion

## Required production split
- hindcast block: 2000-2016
- forecast block: 2017-2025

## Required inventory fields
- dataset
- originating_centre
- system
- variable_key
- pressure_level
- year
- month
- leadtime_month
- file_path
- file_size_bytes
- sha256
- request_json_path
- message_count
- unique_data_date_count
- expected_message_count
- observed_missing_message_count
- contains_20230522
- messages_for_20230522
- completeness_status
- notes

## Required QC before derived products
- file existence
- request sidecar existence
- sha256 sidecar existence
- checksum verification
- GRIB openability with ecCodes
- shortName and pressure-level validation
- message_count validation
- initialization date/time completeness validation
- explicit G8 handling for affected nominal months

## G8 handling rule
NCEP nominal windows that include dataDate=20230522 must be flagged. They must not be treated as complete 31-date lagged windows unless future official data availability changes and is verified by repository evidence.

## Next required review
Review this plan before writing or running any NCEP production downloader.
