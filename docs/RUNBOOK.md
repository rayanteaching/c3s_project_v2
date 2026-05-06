# Runbook

## Purpose
This file stores reusable operational commands, standard checks, and repeatable workflow steps.
It is not a log file for a single run.
Single-run details must go under `runs/<run_name>/`.

## Mandatory seasonal pre-read
Before any continuation, design, execution, correction, download, QC, or new decision in the seasonal phase, run:

```bash
cd /home/fibi/projects/c3s_project_v2

cat docs/DECISIONS.md
cat docs/SEASONAL_DOWNLOAD_POLICY.md
cat docs/SEASONAL_KNOWN_ISSUES.md
cat docs/GIT_WORKFLOW.md
cat docs/STATUS.md
cat docs/HANDOFF.md
cat configs/datasets/c3s_seasonal_systems.yml
cat configs/datasets/c3s_seasonal_variables.yml
```

Pre-read rules:
- Decide only from the current repository state.
- If a new policy or operational file becomes official workflow state, add it to this pre-read list.
- If repository state conflicts with remembered chat context, repository state is final.
- Do not skip this step before any new production run.

## Standard session report
Always provide these before continuing work:

```bash
cd /home/fibi/projects/c3s_project_v2
git status --short --branch
git branch -vv
git log --oneline --decorate --graph -n 10
tree -L 3
```

If a relevant run exists, also provide:

```bash
tail -n 80 <relevant_log_file>
cat <relevant_status_json>
```

If environment work was done, also provide:

```bash
conda env list
```

## Environment activation

```bash
cd /home/fibi/projects/c3s_project_v2
conda activate cds_env
python --version
```

## CDS credential check

```bash
ls -l ~/.cdsapirc
```

Expected permission style:

```text
-rw-------
```

## Official WSL CDS ERA5 netcheck

Script:
- `scripts/netcheck/00_cds_netcheck_small_era5.py`

Run command:

```bash
nohup /home/fibi/projects/c3s_project_v2/scripts/netcheck/00_cds_netcheck_small_era5.py \
  > /home/fibi/projects/c3s_project_v2/logs/wsl_cds_netcheck_era5_small.log 2>&1 &
```

Monitor:

```bash
ps -ef | grep 00_cds_netcheck_small_era5.py | grep -v grep
tail -n 100 -f /home/fibi/projects/c3s_project_v2/logs/wsl_cds_netcheck_era5_small.log
```

Run metadata path:
- `runs/wsl_cds_netcheck_era5_small/`

## Official ERA5 monthly total precipitation downloader

Script:
- `scripts/download/10_download_era5_tp_monthly_grib_cli.py`

Raw data root:
- `/mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly`

Production run command:

```bash
nohup /home/fibi/projects/c3s_project_v2/scripts/download/10_download_era5_tp_monthly_grib_cli.py \
  --start-year 2000 --end-year 2025 \
  > /home/fibi/projects/c3s_project_v2/logs/era5_tp_monthly_2000_2025.log 2>&1 &
```

Monitor:

```bash
ps -ef | grep 10_download_era5_tp_monthly_grib_cli.py | grep -v grep
tail -n 100 -f /home/fibi/projects/c3s_project_v2/logs/era5_tp_monthly_2000_2025.log
```

Run metadata path:
- `runs/2026-04-13_era5_tp_monthly_2000_2025/`

## Inventory snapshot generation

Inventory builder script:
- `scripts/inventory/10_build_inventory_csv.py`

ERA5 tp monthly inventory command:

```bash
/home/fibi/projects/c3s_project_v2/scripts/inventory/10_build_inventory_csv.py \
  --root /mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly \
  --pattern "*.grib" \
  --out /home/fibi/projects/c3s_project_v2/data/inventory/era5_tp_monthly_2000_2025.csv
```

## ECMWF seasonal monthly single-level smoke tests

Script:
- `scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py`

Hindcast smoke test:

```bash
/home/fibi/projects/c3s_project_v2/scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py \
  --year 2000 \
  --month 01 \
  --leadtime-month 1 \
  --variable 2m_temperature \
  --out /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/smoke/cds__c3s_seasonal__monthly-single-levels__ecmwf__s51__t2m__surface__monthly_mean__2000__m01__lead1__NH0_90.grib \
  2>&1 | tee /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_hindcast_smoke.log
```

Hindcast smoke metadata:
- `runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke/`

Forecast smoke test:

```bash
/home/fibi/projects/c3s_project_v2/scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py \
  --year 2017 \
  --month 01 \
  --leadtime-month 1 \
  --variable 2m_temperature \
  --out /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/smoke/cds__c3s_seasonal__monthly-single-levels__ecmwf__s51__t2m__surface__monthly_mean__2017__m01__lead1__NH0_90.grib \
  2>&1 | tee /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_forecast_smoke.log
```

Forecast smoke metadata:
- `runs/2026-04-22_c3s_ecmwf_single_levels_forecast_smoke/`

Smoke output quick check:

```bash
ls -lh /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/smoke
```

## ECMWF grouped monthly single-level production

Script:
- `scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py`

Hindcast grouped production command:

```bash
nohup /home/fibi/projects/c3s_project_v2/scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py \
  --start-year 2000 \
  --end-year 2016 \
  --out-root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 \
  --skip-existing \
  > /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_hindcast_2000_2016.log 2>&1 &
```

Forecast grouped production command:

```bash
nohup /home/fibi/projects/c3s_project_v2/scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py \
  --start-year 2017 \
  --end-year 2025 \
  --out-root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 \
  --skip-existing \
  > /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_forecast_2017_2025.log 2>&1 &
```

Monitor:

```bash
ps -ef | grep 20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py | grep -v grep
tail -n 80 /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_hindcast_2000_2016.log
tail -n 80 /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_forecast_2017_2025.log
```

Expected grouped-file counts after successful completion:
- Hindcast block: 12 `.grib`, 12 `.request.json`, 12 `.sha256`
- Forecast block: 12 `.grib`, 12 `.request.json`, 12 `.sha256`
- No `.part` files should remain

Quick grouped completion checks:

```bash
find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 -maxdepth 1 -type f -name "*.grib" | wc -l
find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 -maxdepth 1 -type f -name "*.request.json" | wc -l
find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 -maxdepth 1 -type f -name "*.sha256" | wc -l

find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.grib" | wc -l
find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.request.json" | wc -l
find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.sha256" | wc -l
find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.part" | wc -l
```

Grouped inventory commands:

```bash
/home/fibi/projects/c3s_project_v2/scripts/inventory/10_build_inventory_csv.py \
  --root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 \
  --pattern "*.grib" \
  --out /home/fibi/projects/c3s_project_v2/data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv

/home/fibi/projects/c3s_project_v2/scripts/inventory/10_build_inventory_csv.py \
  --root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 \
  --pattern "*.grib" \
  --out /home/fibi/projects/c3s_project_v2/data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
```

Grouped run metadata paths:
- `runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/`
- `runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/`

## ECMWF seasonal monthly pressure-level z925 smoke tests

Script:
- `scripts/netcheck/11_c3s_seasonal_ecmwf_pressure_levels_smoke.py`

Hindcast z925 smoke metadata:
- `runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_z925_smoke/`

Forecast z925 smoke metadata:
- `runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_z925_smoke/`

The raw GRIB smoke outputs, request sidecars, SHA256 sidecars, and logs are not tracked by Git.

## ECMWF seasonal monthly pressure-level production

Script:
- scripts/download/21_download_c3s_ecmwf_pressure_levels_monthly_grib_cli.py

Completed production blocks:
- Hindcast: 2000-2016
- Forecast: 2017-2025

Variables:
- z500
- t850
- z925

Expected completion counts per block:
- 72 GRIB files
- 72 request JSON sidecars
- 72 SHA256 sidecars
- 0 part files

Inventory snapshots:
- data/inventory/c3s_ecmwf_pressure_levels_hindcast_2000_2016.csv
- data/inventory/c3s_ecmwf_pressure_levels_forecast_2017_2025.csv

Run metadata:
- runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_2000_2016/
- runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_2017_2025/

## Seasonal bootstrap production rules
- ECMWF-only bootstrap is the active seasonal production scope.
- Hindcast and forecast production requests must remain separated operationally.
- Native GRIB is the operational seasonal download format.
- Exact API payloads must be recorded in run metadata and raw sidecars.
- The ERA5 monthly z925 dataset for 2000-2025 has been downloaded, inventoried, included in structural and scientific sanity QC, and merged into main.
- Seasonal pressure-level verification may proceed only after the standard pre-read confirms the clean merged main state.

## Milestone closure checklist
Before moving to the next meaningful step, do all applicable items below:
- Confirm the run finished successfully or failed definitively.
- Update `runs/<run_name>/status.json`.
- Update `docs/STATUS.md`.
- Update `docs/HANDOFF.md`.
- Update `docs/RUNBOOK.md` if reusable commands or checks were added.
- Commit the changes with a precise message.
- Produce the standard session report.

## Notes
- Do not rely on memory for operational details.
- If a command is likely to be reused, store it here.
- If a detail belongs to a single execution only, store it under `runs/<run_name>/`.

## ECMWF seasonal pressure-level openability QC

Script:
- `scripts/qc/22_check_c3s_ecmwf_pressure_levels_openability.py`

Run command:
- `/home/fibi/projects/c3s_project_v2/scripts/qc/22_check_c3s_ecmwf_pressure_levels_openability.py`

Expected tracked outputs:
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/command.txt`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/run.md`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/status.json`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/open_qc_summary.csv`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/open_qc_details.json`

## ECMWF seasonal pressure-level scientific sanity QC

Script:
- `scripts/qc/23_check_c3s_ecmwf_pressure_levels_scientific_sanity.py`

Run command:
- `/home/fibi/projects/c3s_project_v2/scripts/qc/23_check_c3s_ecmwf_pressure_levels_scientific_sanity.py`

Expected tracked outputs:
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/command.txt`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/run.md`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/status.json`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/scientific_sanity_summary.csv`
- `runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/scientific_sanity_details.json`
