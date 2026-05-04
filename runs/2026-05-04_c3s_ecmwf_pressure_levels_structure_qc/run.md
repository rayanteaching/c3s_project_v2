# ECMWF seasonal monthly pressure-level structural QC

## Scope
- Dataset: C3S seasonal monthly pressure-levels
- Centre: ECMWF
- System: 51
- Hindcast block: 2000-2016
- Forecast block: 2017-2025
- Variables: z500, t850, z925
- Start months: 01-12
- Leadtime months: 1-6

## Result
- Hindcast block contains 72 GRIB files, 72 request JSON sidecars, and 72 SHA256 sidecars.
- Forecast block contains 72 GRIB files, 72 request JSON sidecars, and 72 SHA256 sidecars.
- No `.part` files remain.
- SHA256 verification returned OK for all checked files.
- Inventory files contain 73 lines each: 1 header line plus 72 data rows.

## Important note
Each variable currently has 24 GRIB files per block, not 12. This means the raw pressure-level directories contain two naming families for the same variable/month coverage. Nothing was deleted. The current QC confirms file integrity and sidecar consistency, but the duplicate naming-family situation must be handled explicitly before scientific analysis or derived products.

## Tracked outputs
- qc_report.txt
- hindcast_grib_files.txt
- forecast_grib_files.txt
- hindcast_relative_grib_files.txt
- forecast_relative_grib_files.txt
- status.json
