# Run

- run: 2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025
- purpose: Grouped ECMWF monthly single-level forecast bootstrap for project years 2017-2025
- dataset: seasonal-monthly-single-levels
- centre: ecmwf
- system: 51
- variables:
  - 2m_temperature
  - 10m_wind_speed
  - total_precipitation
- product_type: monthly_mean
- years: 2017-2025
- initialization_months: 01-12
- leadtime_months: 1-6
- area: 90/-180/0/180
- format: grib
- grouping_rule: one request per initialization month, all years in the forecast block
- output_root: /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025
