# NCEP CFSv2 G8-sensitive smoke test

## Scope
- Dataset: seasonal-monthly-pressure-levels
- Originating centre: ncep
- System: 2
- Forecast system: CFSv2-v20110310
- Variable: z500
- Pressure level: 500 hPa
- Year: 2023
- Nominal start month: 06
- Leadtime month: 1

## Result
- Status: passed
- GRIB metadata was readable with ecCodes.
- dataDate=20230522 was not present.
- messages_for_20230522 = 0.
- Total message_count = 120.
- The observed metadata is consistent with the documented G8 missing initialization-date issue.

## Repository interpretation
- This confirms the G8 caution for the corrected nominal June 2023 test case.
- This is not a production download.
- This does not authorize NCEP production download.
- Final NCEP production policy still needs to be documented before production.
