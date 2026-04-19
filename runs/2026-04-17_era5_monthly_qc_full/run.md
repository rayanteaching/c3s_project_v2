# Run: 2026-04-17_era5_monthly_qc_full

## Objective
Perform a full tracked QC pass for the completed ERA5 monthly Northern Hemisphere collection for 2000-2025.

## Scope
This QC milestone covers the following tracked ERA5 monthly datasets:
- tp
- t2m
- ws10m
- z500
- t850
- z950

The QC scope includes two layers:
1. Structural QC
2. Scientific sanity QC

## Structural QC goals
- Confirm that each dataset contains exactly 312 monthly GRIB files for 2000-01 through 2025-12
- Confirm that each GRIB file has a matching request JSON file
- Confirm that each GRIB file has a matching SHA256 file
- Confirm that no monthly gaps exist
- Confirm that no duplicate month keys exist
- Confirm that no orphan request or SHA256 files exist
- Confirm that file naming is valid for the official workflow

## Scientific sanity QC goals
- Confirm full monthly temporal coverage from 2000-01 through 2025-12
- Confirm finite domain mean, domain minimum, and domain maximum for every monthly field
- Confirm positive seasonal-cycle amplitude in the domain-mean monthly climatology
- Confirm nonnegative domain-mean values for tp, ws10m, z500, and z950
- Confirm plausible domain-mean range for t2m and t850 using the 180 K to 330 K sanity bounds
- Generate tracked tables, JSON outputs, and diagnostic plots for later audit and review

## Inputs
- Tracked inventories under `data/inventory/`
- Raw ERA5 monthly GRIB files under `/mnt/e/last-aticol/data/raw/era5/`
- QC scripts:
  - `scripts/qc/20_check_era5_collection_structure.py`
  - `scripts/qc/21_build_era5_monthly_sanity_summary.py`

## Outputs
- `runs/2026-04-17_era5_monthly_qc_full/structure_qc_summary.csv`
- `runs/2026-04-17_era5_monthly_qc_full/structure_qc_details.json`
- `runs/2026-04-17_era5_monthly_qc_full/sanity_qc_dataset_summary.csv`
- `runs/2026-04-17_era5_monthly_qc_full/sanity_qc_timeseries.csv`
- `runs/2026-04-17_era5_monthly_qc_full/sanity_qc_details.json`
- `runs/2026-04-17_era5_monthly_qc_full/plots/`
- `docs/qc/ERA5_MONTHLY_QC_REPORT.md`

## Result summary
- Structural QC passed for tp, t2m, ws10m, z500, t850, and z950
- Scientific sanity QC passed for tp, t2m, ws10m, z500, t850, and z950
- Tracked summary tables, tracked JSON outputs, tracked plots, and a tracked QC report were generated successfully
- The ERA5 monthly collection is structurally complete and scientifically plausible for workflow continuation

## Follow-up
- Review the tracked QC outputs during merge review
- Merge the completed ERA5 monthly phase from `dev` into `main`
- Start the seasonal forecast collection phase on top of the validated ERA5 baseline







# ERA5 Monthly QC Run

## Purpose
Perform a tracked structural and scientific sanity QC for the completed ERA5 monthly collection.

## Scope
Datasets covered:
- tp
- t2m
- ws10m
- z500
- t850
- z950

## QC layers
1. Structural QC
2. Scientific sanity QC

## Structural QC pass criteria
- Each dataset must contain exactly 312 `.grib` files for 2000-2025.
- Each `.grib` file must have one matching `.request.json`.
- Each `.grib` file must have one matching `.sha256`.
- The final tracked inventory snapshot must match the on-disk collection.
- No orphan sidecar files are allowed.
- No missing monthly files are allowed.

## Scientific sanity QC pass criteria
- Sanity checks must be computed from the official raw files.
- Results must be written to tracked outputs.
- At minimum, the QC must produce summary tables and annual-cycle plots.

### Variable-specific rules
- `tp`: no negative values; raw monthly product only; no silent scientific conversion
- `t2m`: interpreted in Kelvin unless a documented conversion is applied
- `ws10m`: must remain non-negative
- `z500`: raw geopotential field, not geopotential height unless explicitly documented
- `t850`: interpreted in Kelvin unless a documented conversion is applied
- `z950`: raw geopotential field, not geopotential height unless explicitly documented

## Expected outputs
- Structural QC summary
- Scientific sanity summary CSV
- Tracked annual-cycle plots
- Markdown QC report

## Rule
This QC milestone must be formally closed in Git before merging the ERA5 monthly collection milestone into main.












# ERA5 Monthly QC Run

## Purpose
Perform a tracked structural and scientific sanity QC for the completed ERA5 monthly collection.

## Scope
Datasets covered:
- tp
- t2m
- ws10m
- z500
- t850
- z950

## QC layers
1. Structural QC
2. Scientific sanity QC

## Expected outputs
- Structural QC summary
- Combined value summary CSV
- Annual-cycle plots
- Markdown QC report

## Rule
This QC milestone must be formally closed in Git before merging the ERA5 monthly collection milestone into main.
