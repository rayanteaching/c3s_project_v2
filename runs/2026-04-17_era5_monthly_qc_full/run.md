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
