# ECMWF seasonal monthly pressure-level z925 hindcast smoke test

## Purpose
Verify that the C3S seasonal monthly pressure-level archive can retrieve ECMWF system 51 z925 data for the project hindcast path.

## Dataset
- C3S dataset: seasonal-monthly-pressure-levels
- Originating centre: ecmwf
- System: 51
- Product type: monthly_mean
- Variable: geopotential
- Pressure level: 925 hPa
- Initialization year: 2000
- Initialization month: 01
- Leadtime month: 1
- Area: Northern Hemisphere, 90 to 0 latitude and -180 to 180 longitude
- Format: GRIB

## Result
- Smoke test completed successfully.
- GRIB output was created under the raw data root.
- Request JSON sidecar was created.
- SHA256 sidecar was created.
- Raw data and logs are intentionally not tracked by Git.
