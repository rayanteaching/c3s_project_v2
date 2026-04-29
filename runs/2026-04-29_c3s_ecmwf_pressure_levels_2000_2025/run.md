# ECMWF seasonal monthly pressure-level download start

## Run ID
2026-04-29_c3s_ecmwf_pressure_levels_2000_2025

## Branch
task/ecmwf-pressure-levels

## Dataset
seasonal-monthly-pressure-levels

## Centre and system
- originating_centre: ecmwf
- system: 51

## Product
- product_type: monthly_mean
- data_format: grib
- download_format: unarchived

## Target blocks
- hindcast: 2000-2016
- forecast: 2017-2025

## Target variables and levels
- z500: geopotential at 500 hPa
- t850: temperature at 850 hPa
- z925: geopotential at 925 hPa

## Domain and grid
- area: 90,-180,0,180
- grid: 1.0,1.0

## Leadtime months
1,2,3,4,5,6

## Start months
01,02,03,04,05,06,07,08,09,10,11,12

## Important policy note
This branch starts preliminary ECMWF seasonal pressure-level downloads only.
Do not merge this branch into main and do not begin seasonal pressure-level verification until the ERA5 monthly z925 baseline is completed and merged into main.

## Command file
runs/2026-04-29_c3s_ecmwf_pressure_levels_2000_2025/command.txt
