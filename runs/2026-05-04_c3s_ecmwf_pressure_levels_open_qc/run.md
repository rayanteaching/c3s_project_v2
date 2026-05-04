# ECMWF seasonal monthly pressure-level openability QC

## Scope
- Dataset: C3S seasonal monthly pressure-levels
- Centre: ECMWF
- System: 51
- Blocks: hindcast_2000_2016 and forecast_2017_2025
- Variables: z500, t850, z925
- Sample months: st01 and st12

## Checks
- GRIB file exists
- request sidecar exists
- sha256 sidecar exists
- sha256 checksum matches
- first GRIB message opens with ecCodes
- key metadata are readable and match the expected variable and pressure level

## Result
- Status: passed
- Summary: `runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/open_qc_summary.csv`
- Details: `runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/open_qc_details.json`
