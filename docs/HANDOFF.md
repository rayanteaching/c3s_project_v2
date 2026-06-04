# Handoff

## Project identity
- Name: c3s_project_v2
- Repository root: /home/fibi/projects/c3s_project_v2
- Primary raw data root: /mnt/e/last-aticol/data/raw
- Primary processed data root: /mnt/e/last-aticol/data/processed

## Source of truth
The repository is the authoritative source of truth.
Do not rely on conversation memory when repository state, logs, or tracked files provide evidence.
Use the hybrid ChatGPT re-entry workflow. Normal mode is for low-risk continuation. Deep audit mode is required for production downloads, merges, QC pass/fail declarations, policy changes, scientific-method decisions, destructive operations, branch cleanup, and recovery after confused state.

## Repository rules
Track:
- docs/
- configs/
- scripts/
- runs/
- data/inventory/
- env/
- workflow-critical text and metadata files required for continuation, reproducibility, or audit

Do not track:
- data/raw/
- data/processed/
- logs/
- large binary datasets
- secrets and credentials

## Platform policy
- WSL Ubuntu is the primary download and validation environment.
- The remote server is used later for downstream processing after verified transfer.

## Re-entry workflow before continuation
Use the repository-maintained ChatGPT re-entry protocol and pack generator.
Normal mode is sufficient for planning, discussion, documentation edits, small script review, low-risk continuation, and non-destructive diagnosis.
Deep audit mode is required for production downloads, merge decisions, branch cleanup, policy changes, QC pass/fail declarations, scientific-method decisions, destructive file operations, and recovery after confusing or failed workflows.

Normal-mode command:

```bash
cd /home/fibi/projects/c3s_project_v2

./scripts/make_chatgpt_reentry_pack.sh normal "REPLACE_WITH_CURRENT_OBJECTIVE"
```

Deep-audit command:

```bash
cd /home/fibi/projects/c3s_project_v2

./scripts/make_chatgpt_reentry_pack.sh deep "REPLACE_WITH_CURRENT_OBJECTIVE"
```

Use only one mode per session unless escalation is needed.

Do not load unrelated literature notes, full repository trees, full tracked-file lists, all inventories, or long logs into normal chats.

Rules:
- Continue only from repository evidence included in the generated re-entry pack and the tracked project files it references.
- If a new policy or operational file becomes part of the official workflow, add it to docs/CHATGPT_REENTRY_PROTOCOL.md and scripts/make_chatgpt_reentry_pack.sh.
- If repository state conflicts with remembered chat context, repository state is final.
- Use deep audit mode before any new production run.

## Current confirmed state
- Clean repository bootstrap on WSL is complete.
- The ERA5 monthly baseline is complete, QC-verified, and merged.
- The ERA5 monthly z925 supplement for 2000-2025 is complete and merged into main.
- The ERA5 monthly z925 inventory snapshot is tracked on main.
- The ERA5 monthly QC workflow now includes z925 explicitly.
- ERA5 monthly structural and scientific sanity QC passed for tp, t2m, ws10m, z500, t850, z925, and z950.
- Seasonal work has advanced through planning, smoke-test validation, and the first grouped ECMWF bootstrap download.
- Seasonal bootstrap is intentionally restricted to ECMWF only.
- ECMWF seasonal bootstrap uses C3S system 51.
- Seasonal bootstrap starts with monthly single-level archives only.
- For project forecast years 2017-2025, the use of ECMWF system 51 is currently a working repository assumption for bootstrap execution and later validation.
- That ECMWF system-51 bootstrap assumption passed the initial single-level smoke test for the first project forecast year 2017.
- The ECMWF single-level hindcast path also passed the initial smoke test for project year 2000.
- ECMWF seasonal monthly pressure-level z925 smoke tests passed for project hindcast year 2000 and first project forecast year 2017.
- The official single-level smoke-test script is tracked at scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py.
- The official pressure-level smoke-test script is tracked at scripts/netcheck/11_c3s_seasonal_ecmwf_pressure_levels_smoke.py.
- The official grouped production downloader is tracked at scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py.
- Grouped hindcast download metadata is tracked under:
  - runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/
- Grouped forecast download metadata is tracked under:
  - runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/
- Grouped raw outputs were created successfully under:
  - /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016
  - /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025
- Each grouped block contains 12 GRIB files with matching request and SHA256 sidecars.
- Tracked inventory snapshots exist for both grouped blocks.
- The grouped ECMWF single-level bootstrap download milestone is formally closed and merged into main.
- main contains the closed ECMWF grouped single-level bootstrap milestone and re-entry protocol commits.
- main contains the ERA5 z925 supplement and z925 QC extension commits after reintegration.
- task/era5-z925 has been reintegrated into main for the ERA5 z925 supplement and QC extension.
- Seasonal pressure-level work has begun on the z925-based pressure-level track.
- The repository seasonal pressure-level substitute is z925, not z950.
- Matching ERA5 monthly z925 has been downloaded, inventoried, and included in ERA5 monthly QC before seasonal pressure-level verification begins.
- ECMWF pressure-level canonical GRIB openability QC passed for sampled st01 and st12 files using ecCodes.
- ECMWF pressure-level scientific sanity QC passed for all 72 canonical GRIB files using ecCodes sampled-message checks.
- ECMWF seasonal monthly pressure-level production completed successfully for hindcast 2000-2016 and forecast 2017-2025.
- ECMWF pressure-level inventory snapshots were created for z500, t850, and z925.
- ECMWF pressure-level structural checksum QC passed after canonical naming-family selection.
- Seasonal hindcasts and forecasts are requested separately.
- Project seasonal hindcast target is 2000-2016.
- Project seasonal forecast target is 2017-2025.
- GRIB is the operational download format.
- A tracked seasonal known-issues register is required before any non-ECMWF centre is activated.
- NCEP CFSv2 activation review has advanced through smoke-test and G8 missing-date evidence integration on task/ncep-main-integration.
- Initial NCEP CFSv2 pressure-level smoke evidence for z500 and t850 has been imported.
- Corrected NCEP G8-sensitive nominal June 2023 z500 evidence has been imported and confirms dataDate=20230522 is absent.
- Final NCEP production-download policy has been integrated after G8 smoke evidence.
- NCEP production download remains blocked until the production downloader design, inventory schema, and QC plan are reviewed and committed.

## Immediate next step
1. Review and commit docs/STATUS.md and docs/HANDOFF.md state closure for task/ncep-main-integration.
2. Keep NCEP production download blocked.
3. Review the design-only NCEP production plan as a separate milestone before writing or running any production downloader.
4. Merge task/ncep-main-integration only after state closure is committed and the branch diff is reviewed.

## Standard session report
Always provide the following before continuing work:
- git status --short --branch
- git branch -vv
- git log --oneline --decorate --graph -n 10
- tree -L 3

If a run exists, also provide:
- tail -n 80 <relevant_log_file>
- cat <relevant_status_json>

If environment work was done, also provide:
- conda env list
