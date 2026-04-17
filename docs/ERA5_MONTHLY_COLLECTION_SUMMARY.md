# ERA5 Monthly Collection Summary

## Scope
This milestone covers the official ERA5 monthly collection on WSL for the Northern Hemisphere domain and the project time range 2000-2025.

## Platform
- Execution platform: WSL Ubuntu 24.04.1 LTS
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Inventory root: /home/fibi/projects/c3s_project_v2/data/inventory

## Completed variables

### Single-level variables
- total_precipitation (tp)
- 2m_temperature (t2m)
- 10m_wind_speed (ws10m)

### Pressure-level variables
- geopotential at 500 hPa (z500)
- temperature at 850 hPa (t850)
- geopotential at 950 hPa (z950)

## Completion status
All six ERA5 monthly variables were downloaded successfully for 2000-2025 on WSL.

For each variable, the workflow produced:
- raw GRIB files
- request JSON sidecars
- SHA256 sidecars
- run metadata under runs/
- inventory CSV snapshots under data/inventory/

## Inventory snapshots
- data/inventory/era5_tp_monthly_2000_2025.csv
- data/inventory/era5_t2m_monthly_2000_2025.csv
- data/inventory/era5_ws10m_monthly_2000_2025.csv
- data/inventory/era5_z500_monthly_2000_2025.csv
- data/inventory/era5_t850_monthly_2000_2025.csv
- data/inventory/era5_z950_monthly_2000_2025.csv

## Expected monthly count
For the 2000-2025 range:
- 26 years
- 12 months per year
- expected GRIB count per variable: 312

## Verified final counts
Each completed variable has:
- 312 GRIB files
- 312 request JSON files
- 312 SHA256 files
- 1 tracked inventory CSV snapshot

## Notes
- The repository tracks workflow-critical text/configuration/metadata files.
- Raw and processed datasets remain outside Git.
- Logs remain outside Git.
- The ERA5 monthly total precipitation product is stored as the official raw CDS monthly product and may require a later documented conversion rule for analysis-ready interpretation.

## Outcome
The ERA5 monthly collection milestone is complete and formally documented in Git.

## Next phase
The next project phase is the seasonal forecast collection workflow.
