# Run

- run: 2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke
- purpose: Validate the ECMWF system 51 hindcast path for the project seasonal monthly single-level bootstrap.
- dataset: seasonal-monthly-single-levels
- centre: ecmwf
- system: 51
- variable: 2m_temperature
- product_type: monthly_mean
- year: 2000
- month: 01
- leadtime_month: 1
- area: 90/-180/0/180
- format: grib
- output_root: /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/smoke
