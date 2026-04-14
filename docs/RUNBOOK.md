# Runbook

## Purpose
This file stores reusable operational commands, standard checks, and repeatable workflow steps.
It is not a log file for a single run.
Single-run details must go under runs/<run_name>/.

## Standard session report
Always provide these before continuing work:

```bash
cd /home/fibi/projects/c3s_project_v2
git status --short --branch
git branch -vv
git log --oneline --decorate --graph -n 10
tree -L 3

If a relevant run exists, also provide:

tail -n 80 <relevant_log_file>
cat <relevant_status_json>

If environment work was done, also provide:

conda env list
Environment activation

Activate the official WSL environment:

cd /home/fibi/projects/c3s_project_v2
conda activate cds_env
python --version
CDS credential check

Verify that the CDS credential file exists and has restricted permissions:

ls -l ~/.cdsapirc

Expected permission style:

-rw-------
Official WSL CDS netcheck

Script:

scripts/netcheck/00_cds_netcheck_small_era5.py

Run command:

nohup /home/fibi/projects/c3s_project_v2/scripts/netcheck/00_cds_netcheck_small_era5.py \
  > /home/fibi/projects/c3s_project_v2/logs/wsl_cds_netcheck_era5_small.log 2>&1 &

Monitor:

ps -ef | grep 00_cds_netcheck_small_era5.py | grep -v grep
tail -n 100 -f /home/fibi/projects/c3s_project_v2/logs/wsl_cds_netcheck_era5_small.log

Run metadata path:

runs/wsl_cds_netcheck_era5_small/
Official ERA5 monthly total precipitation downloader

Script:

scripts/download/10_download_era5_tp_monthly_grib_cli.py

Raw data root:

/mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly

Production run command:

nohup /home/fibi/projects/c3s_project_v2/scripts/download/10_download_era5_tp_monthly_grib_cli.py \
  --start-year 2000 --end-year 2025 \
  > /home/fibi/projects/c3s_project_v2/logs/era5_tp_monthly_2000_2025.log 2>&1 &

Monitor:

ps -ef | grep 10_download_era5_tp_monthly_grib_cli.py | grep -v grep
tail -n 100 -f /home/fibi/projects/c3s_project_v2/logs/era5_tp_monthly_2000_2025.log

Run metadata path:

runs/2026-04-13_era5_tp_monthly_2000_2025/
Quick validation for completed ERA5 monthly tp dataset

Count GRIB files:

find /mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly -maxdepth 1 -type f -name "*.grib" | wc -l

Count request sidecars:

find /mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly -maxdepth 1 -type f -name "*.request.json" | wc -l

Count sha256 sidecars:

find /mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly -maxdepth 1 -type f -name "*.sha256" | wc -l

Check total directory size:

du -sh /mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly
Inventory snapshot generation

Inventory builder script:

scripts/inventory/10_build_inventory_csv.py

ERA5 tp monthly inventory command:

/home/fibi/projects/c3s_project_v2/scripts/inventory/10_build_inventory_csv.py \
  --root /mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly \
  --pattern "*.grib" \
  --out /home/fibi/projects/c3s_project_v2/data/inventory/era5_tp_monthly_2000_2025.csv

Quick checks:

wc -l /home/fibi/projects/c3s_project_v2/data/inventory/era5_tp_monthly_2000_2025.csv
head -n 5 /home/fibi/projects/c3s_project_v2/data/inventory/era5_tp_monthly_2000_2025.csv
tail -n 5 /home/fibi/projects/c3s_project_v2/data/inventory/era5_tp_monthly_2000_2025.csv
Milestone closure checklist

Before moving to the next meaningful step, do all applicable items below:

Confirm the run finished successfully or failed definitively
Update runs/<run_name>/status.json
Update docs/STATUS.md
Update docs/HANDOFF.md
Update docs/RUNBOOK.md if reusable commands or checks were added
Commit the changes with a precise message
Produce the standard session report
Notes
Do not rely on memory for operational details.
If a command is likely to be reused, store it here.
If a detail belongs to a single execution only, store it under runs/<run_name>/.
