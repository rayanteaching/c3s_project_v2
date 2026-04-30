# Decisions

## Pre-read rule:
Before any continuation step, always read the current project decision, policy, handoff, status, known-issues, and active dataset-config files from the repository. Continuation must rely on repository state, not chat memory.

## Repository tracking policy
Track all lightweight, text-based, workflow-critical files that are needed to understand, reproduce, verify, continue, or audit the project.

This includes:
- README.md
- all files under docs/
- all files under configs/
- all files under scripts/
- all run metadata under runs/
- all inventory snapshots under data/inventory/
- all environment definition files under env/
- other lightweight workflow files inside the repository, including:
  - *.md
  - *.txt
  - *.json
  - *.yml
  - *.yaml
  - *.csv
when they are part of the official workflow.

Do not track:
- data/raw/
- data/processed/
- logs/
- large binary datasets
- secrets and credentials

## Platform
- Primary download environment: WSL Ubuntu
- The server will be used after verified transfer

## Branch policy
- main: stable history
- dev: active integration
- task/*: focused work branches when needed

## Storage policy
- The Git repository stays inside the WSL Linux filesystem.
- Large raw and processed datasets are stored on /mnt/e/last-aticol due to limited space on the system drive.

## Milestone closure rule
- Every meaningful milestone must be formally closed in Git before moving on.
- Closure includes, when applicable:
  - run metadata under runs/
  - updated docs/STATUS.md
  - updated docs/HANDOFF.md
  - updated docs/RUNBOOK.md if reusable commands or checks were added
  - a precise commit message
- Continuation must rely on repository state, not chat memory.

## ERA5 monthly total precipitation semantics
- The current ERA5 monthly total precipitation workflow downloads the official raw monthly product as delivered by CDS.
- For this monthly product, total_precipitation must be interpreted carefully during analysis.
- A dedicated conversion rule may be required later when deriving analysis-ready monthly precipitation quantities.
- The downloader itself is responsible only for retrieving and verifying the official raw files, not for scientific conversion.



## ERA5 monthly z500 semantics
- The workflow label z500 refers to ERA5 monthly geopotential at the 500 hPa pressure level.
- The downloader retrieves the official raw geopotential field from the ERA5 monthly pressure-level dataset.
- If geopotential height is needed later, that conversion belongs to the analysis stage, not to the downloader.


## ERA5 monthly pressure-level workflow semantics
- The workflow labels t850, z500, z925, and z950 refer to official ERA5 monthly pressure-level products tracked in this repository.
- The downloader retrieves the official raw ERA5 pressure-level fields exactly as delivered by CDS.
- t850 refers to temperature at the 850 hPa pressure level.
- z500 refers to geopotential at the 500 hPa pressure level.
- z925 refers to geopotential at the 925 hPa pressure level.
- z950 refers to geopotential at the 950 hPa pressure level.
- The z925 collection is the seasonal-aligned ERA5 supplement introduced because the monthly C3S seasonal pressure-level archive does not provide 950 hPa.
- The pre-existing z950 ERA5 collection is retained and not deleted.
- If any later scientific conversion is needed, that conversion belongs to the analysis stage, not to the downloader.

## ERA5 monthly QC policy

### QC layers
- ERA5 monthly collection QC must be performed in two layers:
  1. Structural QC
  2. Scientific sanity QC

### Structural QC pass criteria
- Each completed ERA5 monthly dataset must contain exactly 312 `.grib` files for 2000-2025.
- Each `.grib` file must have a matching `.request.json` sidecar.
- Each `.grib` file must have a matching `.sha256` sidecar.
- The tracked inventory snapshot must match the final file collection on disk.
- No orphan sidecar files are allowed.
- No missing months are allowed.

### Scientific sanity QC pass criteria
- Scientific sanity QC must be documented and tracked before merging the full ERA5 monthly collection milestone.
- The sanity check must use the official raw files only.
- The sanity check must not silently convert scientific units without documenting the rule.

#### tp
- `tp` must be treated as the official raw monthly product delivered by CDS.
- No negative values are acceptable in the sanity summary.
- Any later conversion into analysis-ready monthly precipitation quantities must be documented separately.

#### t2m
- `t2m` must be interpreted in Kelvin unless an explicit documented conversion is applied.
- The monthly series and annual cycle must be physically plausible over the Northern Hemisphere.

#### ws10m
- `ws10m` must remain non-negative.
- The monthly series and annual cycle must be physically plausible over the Northern Hemisphere.

#### z500
- `z500` in this workflow is the raw ERA5 geopotential field, not geopotential height.
- Any conversion from geopotential to geopotential height must be documented explicitly.
- The monthly series and annual cycle must be physically plausible over the Northern Hemisphere.

#### t850
- `t850` must be interpreted in Kelvin unless an explicit documented conversion is applied.
- The monthly series and annual cycle must be physically plausible over the Northern Hemisphere.

## ERA5 monthly z925 alignment rule
- The task branch `task/era5-z925` adds ERA5 monthly z925 as a parallel aligned dataset for the seasonal pressure-level substitute.
- Existing ERA5 monthly z950 data, metadata, inventory, and historical QC outputs remain intact and must not be deleted by this task.
- ERA5 z925 is added for seasonal comparison alignment with the repository seasonal pressure-level substitute z925.
- z925 is tracked as an ERA5 monthly pressure-level product in this repository
- z925 is the seasonal-aligned ERA5 supplement
- z950 baseline is retained and not deleted
- the z925 download/inventory is complete on task/era5-z925
- QC still needs to be extended explicitly for z925 before reintegration

#### z950
- `z950` in this workflow is the raw ERA5 geopotential field, not geopotential height.
- Any conversion from geopotential to geopotential height must be documented explicitly.
- The monthly series and annual cycle must be physically plausible over the Northern Hemisphere.

### Merge rule
- The ERA5 monthly collection must not be merged before QC outputs, QC report, tracked plots, and updated run metadata are committed.

## Seasonal ECMWF bootstrap assumption
- The seasonal bootstrap phase currently proceeds with ECMWF only.
- The repository will request ECMWF monthly seasonal data using system=51 for both project hindcasts (2000-2016) and project forecasts (2017-2025).
- For forecast years 2017-2025, this is a working repository assumption adopted for bootstrap execution and later validation; it is not yet a fully validated period-specific system manifest for scientific evaluation.
- The assumption must be revisited after smoke tests and first production retrievals.

## Seasonal pressure-level substitution
- The supervisor wording includes z950, but the monthly C3S pressure-level archive spans 925 hPa to 10 hPa.
- Therefore the repository seasonal pressure-level substitute is z925, not z950.
- The matching ERA5 monthly z925 dataset has now been downloaded and inventoried on the dedicated task/era5-z925 branch.
- That z925 collection is the seasonal-aligned supplement and does not replace the already tracked ERA5 z950 baseline.
- Before seasonal pressure-level verification begins on the main integration branch, the z925 task branch changes must be merged and the ERA5 QC workflow must be extended to include z925 explicitly.

## Seasonal known-issues register rule
- Official C3S seasonal known issues must be copied into tracked repository documentation before a new centre or sensitive variable is activated.
- Each affected case must be classified in the repository as allow, warn, mask, or exclude.
- Non-ECMWF centres remain deferred until both period-specific system mapping and known-issues registration are committed.
