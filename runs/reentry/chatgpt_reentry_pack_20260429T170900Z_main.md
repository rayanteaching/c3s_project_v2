PROJECT RE-ENTRY PACK

Generated UTC: 20260429T170900Z


============================================================
A. PROJECT IDENTITY
============================================================

Project: C3S seasonal/ERA5 repository
Project root: /home/fibi/projects/c3s_project_v2
Current branch: main
Current commit: 49f28caed9a0fe52fa1476368313cac185df28ac

============================================================
B. REQUIRED OPENING INSTRUCTION FOR THE NEW CHATGPT PROJECT CHAT
============================================================

We are continuing the C3S seasonal/ERA5 project.

Do not rely on memory from previous chats.

The current repository state is the final source of truth.

First read the Project Re-entry Pack below, including the Git report and all official state files.

Then summarize:
1. current branch,
2. current milestone,
3. completed work,
4. blockers,
5. risks,
6. next safe step.

Do not give any execution command, download command, QC command, merge command, or new design decision until that summary is complete.

============================================================
C. HARD RULES
============================================================

Repository state is final.
Do not decide from remembered chat context.
Read official pre-read files before every continuation, design, execution, correction, download, QC step, merge, or policy decision.
Track lightweight workflow-critical text files.
Do not track raw data, processed data, logs, large binary files, credentials, or secrets.
After every milestone, update STATUS and HANDOFF.
Update DECISIONS when a new decision is made.
Update run metadata and inventory snapshots when operational state changes.
For commands and file content, ChatGPT output must be exactly one fenced code block only.

============================================================
D. CURRENT OBJECTIVE
============================================================

Start a new ChatGPT project chat from the real repository state and continue only after summarizing branch, milestone, completed work, blockers, risks, and next safe step.

============================================================
E. WHAT NOT TO DO
============================================================

Do not use old chat memory as a source of truth.
Do not assume the active branch.
Do not assume a milestone is closed unless STATUS, HANDOFF, run metadata, inventory, and Git history prove it.
Do not propose downloads before reading policy and state files.
Do not track data/raw, data/processed, logs, credentials, secrets, or large binaries.
Do not change official policy files casually.
Do not merge branches before checking status, diff, branch relation, and milestone closure.

============================================================
F. GIT STATUS SHORT BRANCH
============================================================

## main
?? runs/reentry/

============================================================
G. BRANCHES
============================================================

  backup-task-era5-z925-before-main-sync 44c6d4d runs(inventory): close ECMWF seasonal single-level grouped download milestone
  dev                                    5d450ee docs(state): refresh seasonal status handoff and runbook after ECMWF grouped bootstrap closure
* main                                   49f28ca docs: add ChatGPT re-entry protocol and pack generator
+ task/era5-z925                         44c6d4d (/home/fibi/projects/c3s_project_v2_era5_z925) runs(inventory): close ECMWF seasonal single-level grouped download milestone

============================================================
H. RECENT COMMITS ON CURRENT BRANCH
============================================================

* 49f28ca (HEAD -> main) docs: add ChatGPT re-entry protocol and pack generator
* 4c66101 docs(runbook): align main runbook with merged seasonal state and parallel z925 worktree rule
* b5bedd4 docs(status): refresh main state after seasonal merge and parallel z925 worktree split
* 9d0f068 docs(handoff): refresh project state after seasonal main merge and parallel z925 worktree split
*   0566034 merge(seasonal): close first ECMWF grouped single-level bootstrap milestone
|\  
| * 5d450ee (dev) docs(state): refresh seasonal status handoff and runbook after ECMWF grouped bootstrap closure
| * e373eb8 runs(inventory): close ECMWF seasonal single-level grouped download milestone
| * a407039 feat(download): add grouped ECMWF seasonal monthly single-level production downloader
| * 732d6a2 docs(runbook): repair malformed handoff and rebuild seasonal runbook
| * d7d41b2 docs(status): remove stale duplicated seasonal state blocks
| * 8147cb5 docs(status): refresh seasonal smoke-test state and enforce project pre-read rule
| * 1c3c905 runs(smoke): record ECMWF seasonal forecast smoke success
| * bce386c runs(smoke): record ECMWF seasonal hindcast smoke success
| * 56e87b0 feat(netcheck): add ECMWF seasonal monthly single-level smoke test
| * 944fcc4 docs(config): register ECMWF bootstrap assumption z925 substitution and seasonal issues policy
| * 626686b docs(config): restrict seasonal bootstrap to ECMWF and split hindcast forecast policy
| * e070f4d docs(config): add ECMWF-first seasonal download policy and dataset maps
| * 6c05456 docs(status): refresh project state after ERA5 merge and activate seasonal planning
|/  
*   f35ad85 merge(era5): integrate completed ERA5 monthly collection and QC phase
|\  
| * 5683fe3 docs(status): refresh last verified commit before ERA5 phase merge review
| * ecc9545 docs(handoff): refresh and clean to latest meaningfull version
| * 8aac26d docs(status): refresh and clean to latest meaningfull version
| * 6dc072f docs(status): refresh last verified commit after QC status update
| * 5506a0d docs(qc): refresh status and handoff after final QC metadata polish
| * 8ade26f runs(qc): finalize ERA5 monthly QC run metadata
| * d172e84 runs(qc): close ERA5 monthly scientific sanity QC milestone
| * 4c6cacf feat(qc): add ERA5 monthly scientific sanity summary and plot generator
| * c7e1936 runs(qc): record passing ERA5 monthly structural QC results
| * b58b1c9 feat(qc): add ERA5 monthly structure checker
| * 01ef09f runs(qc): mark ERA5 monthly QC milestone as started

============================================================
I. RECENT COMMITS ACROSS ALL BRANCHES
============================================================

* 49f28ca (HEAD -> main) docs: add ChatGPT re-entry protocol and pack generator
* 4c66101 docs(runbook): align main runbook with merged seasonal state and parallel z925 worktree rule
* b5bedd4 docs(status): refresh main state after seasonal merge and parallel z925 worktree split
* 9d0f068 docs(handoff): refresh project state after seasonal main merge and parallel z925 worktree split
*   0566034 merge(seasonal): close first ECMWF grouped single-level bootstrap milestone
|\  
| * 5d450ee (dev) docs(state): refresh seasonal status handoff and runbook after ECMWF grouped bootstrap closure
| * e373eb8 runs(inventory): close ECMWF seasonal single-level grouped download milestone
| | * 44c6d4d (task/era5-z925, backup-task-era5-z925-before-main-sync) runs(inventory): close ECMWF seasonal single-level grouped download milestone
| |/  
| * a407039 feat(download): add grouped ECMWF seasonal monthly single-level production downloader
| * 732d6a2 docs(runbook): repair malformed handoff and rebuild seasonal runbook
| * d7d41b2 docs(status): remove stale duplicated seasonal state blocks
| * 8147cb5 docs(status): refresh seasonal smoke-test state and enforce project pre-read rule
| * 1c3c905 runs(smoke): record ECMWF seasonal forecast smoke success
| * bce386c runs(smoke): record ECMWF seasonal hindcast smoke success
| * 56e87b0 feat(netcheck): add ECMWF seasonal monthly single-level smoke test
| * 944fcc4 docs(config): register ECMWF bootstrap assumption z925 substitution and seasonal issues policy
| * 626686b docs(config): restrict seasonal bootstrap to ECMWF and split hindcast forecast policy
| * e070f4d docs(config): add ECMWF-first seasonal download policy and dataset maps
| * 6c05456 docs(status): refresh project state after ERA5 merge and activate seasonal planning
|/  
*   f35ad85 merge(era5): integrate completed ERA5 monthly collection and QC phase
|\  
| * 5683fe3 docs(status): refresh last verified commit before ERA5 phase merge review
| * ecc9545 docs(handoff): refresh and clean to latest meaningfull version
| * 8aac26d docs(status): refresh and clean to latest meaningfull version
| * 6dc072f docs(status): refresh last verified commit after QC status update
| * 5506a0d docs(qc): refresh status and handoff after final QC metadata polish
| * 8ade26f runs(qc): finalize ERA5 monthly QC run metadata
| * d172e84 runs(qc): close ERA5 monthly scientific sanity QC milestone
| * 4c6cacf feat(qc): add ERA5 monthly scientific sanity summary and plot generator
| * c7e1936 runs(qc): record passing ERA5 monthly structural QC results
| * b58b1c9 feat(qc): add ERA5 monthly structure checker
| * 01ef09f runs(qc): mark ERA5 monthly QC milestone as started
| * 87e29f0 docs(qc): record ERA5 monthly QC criteria and refresh env definition
| * a453993 runs(qc): prepare ERA5 monthly collection QC milestone
| * 4c74f78 docs(era5): close full monthly collection phase
| * a316050 runs(era5): close monthly z950 download milestone
| * 37f9a8e runs(z950): mark production run as started
| * b8b773c runs(era5): refresh final t850 inventory and close milestone cleanly
| * 7ae2b77 runs(era5): close monthly t850 download milestone
| * c7b7ace runs(t850): mark production run as started
| * 3f1bd7d runs(era5): close monthly z500 download milestone

============================================================
J. WORKING TREE DIFF STAT
============================================================


============================================================
K. WORKING TREE DIFF NAME-STATUS
============================================================


============================================================
L. STAGED DIFF STAT
============================================================


============================================================
M. STAGED DIFF NAME-STATUS
============================================================


============================================================
N. REPOSITORY TREE
============================================================

.
├── .gitignore
├── README.md
├── configs
│   ├── datasets
│   │   ├── c3s_seasonal_systems.yml
│   │   └── c3s_seasonal_variables.yml
│   └── paths
│       └── paths.example.yml
├── data
│   ├── inventory
│   │   ├── c3s_ecmwf_single_levels_forecast_2017_2025.csv
│   │   ├── c3s_ecmwf_single_levels_hindcast_2000_2016.csv
│   │   ├── era5_t2m_monthly_2000_2025.csv
│   │   ├── era5_t850_monthly_2000_2025.csv
│   │   ├── era5_tp_monthly_2000_2025.csv
│   │   ├── era5_ws10m_monthly_2000_2025.csv
│   │   ├── era5_z500_monthly_2000_2025.csv
│   │   └── era5_z950_monthly_2000_2025.csv
│   ├── processed
│   └── raw
├── docs
│   ├── CHATGPT_REENTRY_PROTOCOL.md
│   ├── DECISIONS.md
│   ├── ERA5_MONTHLY_COLLECTION_SUMMARY.md
│   ├── HANDOFF.md
│   ├── RUNBOOK.md
│   ├── SCOPE.md
│   ├── SEASONAL_DOWNLOAD_POLICY.md
│   ├── SEASONAL_KNOWN_ISSUES.md
│   ├── STATUS.md
│   └── qc
│       └── ERA5_MONTHLY_QC_REPORT.md
├── env
│   └── cds_env.yml
├── runs
│   ├── 2026-04-13_era5_tp_monthly_2000_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-14_era5_t2m_monthly_2000_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-14_era5_ws10m_monthly_2000_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-14_era5_z500_monthly_2000_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-15_era5_t850_monthly_2000_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-15_era5_z950_monthly_2000_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-17_era5_monthly_qc_full
│   │   ├── command.txt
│   │   ├── plots
│   │   │   ├── t2m_domain_mean_timeseries.png
│   │   │   ├── t2m_monthly_climatology.png
│   │   │   ├── t850_domain_mean_timeseries.png
│   │   │   ├── t850_monthly_climatology.png
│   │   │   ├── tp_domain_mean_timeseries.png
│   │   │   ├── tp_monthly_climatology.png
│   │   │   ├── ws10m_domain_mean_timeseries.png
│   │   │   ├── ws10m_monthly_climatology.png
│   │   │   ├── z500_domain_mean_timeseries.png
│   │   │   ├── z500_monthly_climatology.png
│   │   │   ├── z950_domain_mean_timeseries.png
│   │   │   └── z950_monthly_climatology.png
│   │   ├── run.md
│   │   ├── sanity_qc_dataset_summary.csv
│   │   ├── sanity_qc_details.json
│   │   ├── sanity_qc_timeseries.csv
│   │   ├── status.json
│   │   ├── structure_qc_details.json
│   │   └── structure_qc_summary.csv
│   ├── 2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-22_c3s_ecmwf_single_levels_forecast_smoke
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── README.md
│   ├── reentry
│   │   └── chatgpt_reentry_pack_20260429T170900Z_main.md
│   └── wsl_cds_netcheck_era5_small
│       ├── command.txt
│       ├── run.md
│       └── status.json
└── scripts
    ├── download
    │   ├── 10_download_era5_tp_monthly_grib_cli.py
    │   ├── 11_download_era5_t2m_monthly_grib_cli.py
    │   ├── 12_download_era5_ws10m_monthly_grib_cli.py
    │   ├── 13_download_era5_z500_monthly_grib_cli.py
    │   ├── 14_download_era5_t850_monthly_grib_cli.py
    │   ├── 15_download_era5_z950_monthly_grib_cli.py
    │   └── 20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py
    ├── inventory
    │   └── 10_build_inventory_csv.py
    ├── make_chatgpt_reentry_pack.sh
    ├── netcheck
    │   ├── 00_cds_netcheck_small_era5.py
    │   └── 10_c3s_seasonal_ecmwf_single_levels_smoke.py
    ├── qc
    │   ├── 20_check_era5_collection_structure.py
    │   └── 21_build_era5_monthly_sanity_summary.py
    └── transfer

32 directories, 92 files

============================================================
O. TRACKED FILES
============================================================

.gitignore
README.md
configs/datasets/c3s_seasonal_systems.yml
configs/datasets/c3s_seasonal_variables.yml
configs/paths/paths.example.yml
data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
data/inventory/era5_t2m_monthly_2000_2025.csv
data/inventory/era5_t850_monthly_2000_2025.csv
data/inventory/era5_tp_monthly_2000_2025.csv
data/inventory/era5_ws10m_monthly_2000_2025.csv
data/inventory/era5_z500_monthly_2000_2025.csv
data/inventory/era5_z950_monthly_2000_2025.csv
docs/CHATGPT_REENTRY_PROTOCOL.md
docs/DECISIONS.md
docs/ERA5_MONTHLY_COLLECTION_SUMMARY.md
docs/HANDOFF.md
docs/RUNBOOK.md
docs/SCOPE.md
docs/SEASONAL_DOWNLOAD_POLICY.md
docs/SEASONAL_KNOWN_ISSUES.md
docs/STATUS.md
docs/qc/ERA5_MONTHLY_QC_REPORT.md
env/cds_env.yml
runs/2026-04-13_era5_tp_monthly_2000_2025/command.txt
runs/2026-04-13_era5_tp_monthly_2000_2025/run.md
runs/2026-04-13_era5_tp_monthly_2000_2025/status.json
runs/2026-04-14_era5_t2m_monthly_2000_2025/command.txt
runs/2026-04-14_era5_t2m_monthly_2000_2025/run.md
runs/2026-04-14_era5_t2m_monthly_2000_2025/status.json
runs/2026-04-14_era5_ws10m_monthly_2000_2025/command.txt
runs/2026-04-14_era5_ws10m_monthly_2000_2025/run.md
runs/2026-04-14_era5_ws10m_monthly_2000_2025/status.json
runs/2026-04-14_era5_z500_monthly_2000_2025/command.txt
runs/2026-04-14_era5_z500_monthly_2000_2025/run.md
runs/2026-04-14_era5_z500_monthly_2000_2025/status.json
runs/2026-04-15_era5_t850_monthly_2000_2025/command.txt
runs/2026-04-15_era5_t850_monthly_2000_2025/run.md
runs/2026-04-15_era5_t850_monthly_2000_2025/status.json
runs/2026-04-15_era5_z950_monthly_2000_2025/command.txt
runs/2026-04-15_era5_z950_monthly_2000_2025/run.md
runs/2026-04-15_era5_z950_monthly_2000_2025/status.json
runs/2026-04-17_era5_monthly_qc_full/command.txt
runs/2026-04-17_era5_monthly_qc_full/plots/t2m_domain_mean_timeseries.png
runs/2026-04-17_era5_monthly_qc_full/plots/t2m_monthly_climatology.png
runs/2026-04-17_era5_monthly_qc_full/plots/t850_domain_mean_timeseries.png
runs/2026-04-17_era5_monthly_qc_full/plots/t850_monthly_climatology.png
runs/2026-04-17_era5_monthly_qc_full/plots/tp_domain_mean_timeseries.png
runs/2026-04-17_era5_monthly_qc_full/plots/tp_monthly_climatology.png
runs/2026-04-17_era5_monthly_qc_full/plots/ws10m_domain_mean_timeseries.png
runs/2026-04-17_era5_monthly_qc_full/plots/ws10m_monthly_climatology.png
runs/2026-04-17_era5_monthly_qc_full/plots/z500_domain_mean_timeseries.png
runs/2026-04-17_era5_monthly_qc_full/plots/z500_monthly_climatology.png
runs/2026-04-17_era5_monthly_qc_full/plots/z950_domain_mean_timeseries.png
runs/2026-04-17_era5_monthly_qc_full/plots/z950_monthly_climatology.png
runs/2026-04-17_era5_monthly_qc_full/run.md
runs/2026-04-17_era5_monthly_qc_full/sanity_qc_dataset_summary.csv
runs/2026-04-17_era5_monthly_qc_full/sanity_qc_details.json
runs/2026-04-17_era5_monthly_qc_full/sanity_qc_timeseries.csv
runs/2026-04-17_era5_monthly_qc_full/status.json
runs/2026-04-17_era5_monthly_qc_full/structure_qc_details.json
runs/2026-04-17_era5_monthly_qc_full/structure_qc_summary.csv
runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/command.txt
runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/run.md
runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/status.json
runs/2026-04-22_c3s_ecmwf_single_levels_forecast_smoke/command.txt
runs/2026-04-22_c3s_ecmwf_single_levels_forecast_smoke/run.md
runs/2026-04-22_c3s_ecmwf_single_levels_forecast_smoke/status.json
runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/command.txt
runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/run.md
runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/status.json
runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke/command.txt
runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke/run.md
runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke/status.json
runs/README.md
runs/wsl_cds_netcheck_era5_small/command.txt
runs/wsl_cds_netcheck_era5_small/run.md
runs/wsl_cds_netcheck_era5_small/status.json
scripts/download/10_download_era5_tp_monthly_grib_cli.py
scripts/download/11_download_era5_t2m_monthly_grib_cli.py
scripts/download/12_download_era5_ws10m_monthly_grib_cli.py
scripts/download/13_download_era5_z500_monthly_grib_cli.py
scripts/download/14_download_era5_t850_monthly_grib_cli.py
scripts/download/15_download_era5_z950_monthly_grib_cli.py
scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py
scripts/inventory/10_build_inventory_csv.py
scripts/make_chatgpt_reentry_pack.sh
scripts/netcheck/00_cds_netcheck_small_era5.py
scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py
scripts/qc/20_check_era5_collection_structure.py
scripts/qc/21_build_era5_monthly_sanity_summary.py

============================================================
P. STATUS INCLUDING IGNORED FILES
============================================================

?? runs/reentry/
!! logs/

============================================================
Q. OFFICIAL STATE FILE: docs/CHATGPT_REENTRY_PROTOCOL.md
============================================================

# ChatGPT Re-entry Protocol

## Purpose

This document defines the official procedure for starting or restarting any ChatGPT-assisted work on this repository.

The goal is to prevent decisions based on stale conversation memory and to force every new continuation to start from the current repository state.

## Repository-first rule

The current repository state is the final source of truth.

If remembered chat context conflicts with tracked repository files, the repository files win.

No new design, execution, correction, download, QC step, merge, branch decision, or policy change should be made before reading the official pre-read files.

## Official project root

/home/fibi/projects/c3s_project_v2

## Mandatory pre-read files

Every new ChatGPT project chat must start by reading these files:

docs/CHATGPT_REENTRY_PROTOCOL.md
docs/DECISIONS.md
docs/SEASONAL_DOWNLOAD_POLICY.md
docs/SEASONAL_KNOWN_ISSUES.md
docs/STATUS.md
docs/HANDOFF.md
configs/datasets/c3s_seasonal_systems.yml
configs/datasets/c3s_seasonal_variables.yml

If another policy, runbook, checklist, or operational file becomes official workflow state, it must be added to this list.

## Mandatory pre-read command

cd /home/fibi/projects/c3s_project_v2

cat docs/CHATGPT_REENTRY_PROTOCOL.md
cat docs/DECISIONS.md
cat docs/SEASONAL_DOWNLOAD_POLICY.md
cat docs/SEASONAL_KNOWN_ISSUES.md
cat docs/STATUS.md
cat docs/HANDOFF.md
cat configs/datasets/c3s_seasonal_systems.yml
cat configs/datasets/c3s_seasonal_variables.yml

## Mandatory Git report

Every new ChatGPT project chat must include a fresh Git report generated from the repository root.

Minimum required commands:

git status --short --branch
git branch -vv
git log --oneline --decorate --graph -n 30
git log --oneline --decorate --graph --all -n 40
git diff --stat
git diff --name-status
git diff --cached --stat
git diff --cached --name-status
git ls-files
git status --short --ignored
tree -a -L 4 -I '.git|__pycache__|*.pyc|data/raw|data/processed|logs'

## Required re-entry pack sections

Every Project Re-entry Pack must contain these sections:

1. Project identity
2. Hard rules
3. Current objective
4. What not to do
5. Git report
6. Official state files
7. Current repository tree
8. Tracked workflow files
9. Modified and untracked files
10. Next requested assistant action

## Required opening instruction for a new ChatGPT project chat

Use this instruction at the top of every new project chat:

We are continuing the C3S seasonal/ERA5 project.

Do not rely on memory from previous chats.

The current repository state is the final source of truth.

First read the Project Re-entry Pack below, including the Git report and all official state files.

Then summarize:
1. current branch,
2. current milestone,
3. completed work,
4. blockers,
5. risks,
6. next safe step.

Do not give any execution command, download command, QC command, merge command, or new design decision until that summary is complete.

## Tracking policy reminder

Track lightweight text-based workflow files required for reproduction, continuation, understanding, or audit.

Track:

README.md
docs/
configs/
scripts/
runs/ metadata
data/inventory/
env/
*.md
*.txt
*.json
*.yml
*.yaml
*.csv

Do not track:

data/raw/
data/processed/
logs/
large binary files
credentials
secrets

## Milestone close rule

After every important milestone:

1. Update docs/STATUS.md.
2. Update docs/HANDOFF.md.
3. Update docs/DECISIONS.md if a new project decision was made.
4. Update run metadata under runs/ if a run was started, completed, failed, resumed, or verified.
5. Update inventory snapshots under data/inventory/ if data state changed.
6. Commit the workflow state to Git.

## Output formatting rule for ChatGPT

For repository file content, shell command blocks, or copy-paste instructions, ChatGPT must return exactly one fenced code block and nothing outside it.

Do not split one file across multiple code blocks.

Do not add explanations before or after the code block.

Keep paths, filenames, commands, and technical text in English.

============================================================
R. OFFICIAL STATE FILE: docs/DECISIONS.md
============================================================

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
- The workflow labels t850, z500, and z950 refer to official ERA5 monthly pressure-level products.
- The downloader retrieves the official raw ERA5 pressure-level fields exactly as delivered by CDS.
- t850 refers to temperature at the 850 hPa pressure level.
- z500 refers to geopotential at the 500 hPa pressure level.
- z950 refers to geopotential at the 950 hPa pressure level.
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
- Before seasonal pressure-level verification begins, the matching ERA5 monthly z925 dataset must also be downloaded and tracked through the normal run and inventory workflow.

## Seasonal known-issues register rule
- Official C3S seasonal known issues must be copied into tracked repository documentation before a new centre or sensitive variable is activated.
- Each affected case must be classified in the repository as allow, warn, mask, or exclude.
- Non-ECMWF centres remain deferred until both period-specific system mapping and known-issues registration are committed.

============================================================
S. OFFICIAL STATE FILE: docs/SEASONAL_DOWNLOAD_POLICY.md
============================================================

# Seasonal Download Policy

## Scope
This policy governs seasonal forecast data collection from the Copernicus Climate Change Service (C3S) monthly seasonal archives.

## Official source datasets
- seasonal-monthly-single-levels
- seasonal-monthly-pressure-levels

## Bootstrap phase order
1. ECMWF-only bootstrap
2. ECMWF monthly single-levels workflow verification
3. ECMWF pressure-level introduction after documented level decision
4. Other centres after period-specific system mapping and issue registration are validated and committed

## Project target period
- Project hindcast target: 2000-2016
- Project forecast target: 2017-2025
- Year 2026 is out of scope for the current project target

## ECMWF bootstrap policy
- originating_centre: ecmwf
- system: 51
- same system must be used when pairing hindcasts and forecasts
- use of system=51 for forecast years 2017-2025 is currently a working repository assumption for bootstrap, not a final scientific manifest

## Bootstrap variable policy
### Active bootstrap variables
- t2m -> 2m_temperature
- ws10m -> 10m_wind_speed
- tp -> total_precipitation

### Deferred pressure-level variables
- z500 -> geopotential at 500 hPa
- t850 -> temperature at 850 hPa
- z925 -> geopotential at 925 hPa
- the supervisor wording z950 is retained as an external requirement note, but the operational monthly C3S implementation in this repository uses z925 instead

## Request split policy
For operational collection in this repository, hindcasts and forecasts must be requested separately.

### Hindcast request block
- project years: 2000-2016

### Forecast request block
- project years: 2017-2025

## Product policy
- bootstrap product_type: monthly_mean
- bootstrap data_format: grib
- native GRIB is the operational format
- netCDF conversion is not part of the operational download workflow

## Raw-data semantics
- Raw seasonal files must be stored exactly as delivered by CDS.
- Any scientific unit conversion or anomaly calculation belongs to later analysis stages.
- tp must not be silently converted during download.
- z500 and z925 are raw geopotential fields, not geopotential height.

## Operational request policy
- exact API payloads must be recorded in run metadata and raw sidecars
- target valid month must be derived programmatically from start month and leadtime month
- lagged-system handling must be implemented explicitly before any non-ECMWF centre is activated
- form-generated API snippets are helper outputs, not repository source-of-truth configuration

## Known-issues policy
- official C3S seasonal known issues must be registered in tracked repository documentation before a new centre is activated
- each issue must be classified as allow, warn, mask, or exclude
- issues stating that archived wrong data will not be overwritten must be treated as hard warnings

## Future ERA5 dependency
- before seasonal pressure-level verification begins, the matching ERA5 monthly z925 dataset must be downloaded and tracked

## Tracking policy
The following must be tracked in Git:
- docs/
- configs/
- scripts/
- runs/
- data/inventory/
- env/
- workflow-critical text and metadata files

The following must not be tracked:
- data/raw/
- data/processed/
- logs/
- large binary datasets
- secrets and credentials

## Milestone closure policy
No seasonal milestone is considered complete until:
- run metadata is updated
- inventory snapshot is tracked if files were produced
- docs/STATUS.md is updated
- docs/HANDOFF.md is updated
- any reusable operational command is added to docs/RUNBOOK.md when needed
- a precise closing commit is created

============================================================
T. OFFICIAL STATE FILE: docs/SEASONAL_KNOWN_ISSUES.md
============================================================

# Seasonal Known Issues Register

## Scope
This register tracks official C3S seasonal data issues that affect repository download and evaluation decisions.

## Active bootstrap scope
- Centre: ECMWF
- System: 51
- Datasets: seasonal-monthly-single-levels, later seasonal-monthly-pressure-levels
- Active bootstrap variables: t2m, ws10m, tp
- Deferred pressure-level variables: z500, t850, z925

## ECMWF system 51
- In the reviewed official known-issues page, the explicit ECMWF system 51 issue identified for now concerns volumetric soil moisture GRIB2 packing.
- That issue is outside the current ECMWF monthly single-level bootstrap variables.
- No explicit official known issue affecting the current bootstrap variables t2m, ws10m, and tp was identified in the reviewed pages for this repository step.
- This is not a blanket guarantee for later variables or later centres; each activation step must re-check the official known-issues page.

## Non-ECMWF centres
- UK Met Office, DWD, CMCC, Météo-France, and NCEP remain deferred.
- Before any of them is activated, the repository must record:
  - period-specific system mapping
  - relevant official known issues for the selected years, variables, and product types
  - operational action for each issue: allow, warn, mask, or exclude

## Lagged-system decoding rule
- For lagged monthly systems, nominal start date and real initialization date handling must be documented before scientific evaluation begins.
- Tools based on ecCodes and cfgrib must be used when that phase is activated.

## Operational rules
- Known issues must be checked before each new centre or variable is activated.
- Issues stating that archived wrong data will not be overwritten must be treated as hard warnings.
- Data gaps must be recorded explicitly in run metadata and inventories.
- Deferred centres must not be operationally downloaded until their issue registration is committed.

============================================================
U. OFFICIAL STATE FILE: docs/STATUS.md
============================================================

# Status

## Current platform
- WSL Ubuntu 24.04.1 LTS

## Current phase
- Repository bootstrap completed
- Environment setup completed
- CDS netcheck completed successfully
- ERA5 monthly collection completed successfully for all required variables
- ERA5 monthly structural QC passed
- ERA5 monthly scientific sanity QC passed
- ERA5 monthly collection was merged into main
- Seasonal forecast planning is active
- Seasonal bootstrap is restricted to ECMWF only
- Seasonal bootstrap starts with monthly single-level archives
- ECMWF seasonal monthly single-level smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
- The repository bootstrap assumption using ECMWF system 51 for forecast years 2017-2025 has passed initial smoke validation
- Grouped ECMWF monthly single-level hindcast download for 2000-2016 completed successfully
- Grouped ECMWF monthly single-level forecast download for 2017-2025 completed successfully
- Tracked inventory snapshots were created for both ECMWF grouped single-level blocks
- The first ECMWF seasonal monthly single-level bootstrap download milestone was merged into main
- A separate linked worktree exists for parallel ERA5 monthly z925 work
- Seasonal pressure-level work on the stable main branch remains deferred until the z925 branch workflow is completed and merged
- A matching ERA5 monthly z925 dataset must be downloaded later before seasonal pressure-level verification begins
- Hindcast and forecast requests are handled separately operationally

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main, dev, task/era5-z925, and backup-task-era5-z925-before-main-sync exist
- main is the current stable branch baseline
- The grouped ECMWF bootstrap milestone was merged into main at commit 0566034
- The grouped-download milestone closure commit on dev is e373eb8
- The post-closure document refresh commit on dev is 5d450ee
- The current dev tip is already contained in main through merge commit 0566034
- A linked worktree exists at /home/fibi/projects/c3s_project_v2_era5_z925 on branch task/era5-z925
- The linked task/era5-z925 branch currently points to commit 44c6d4d and is behind main
- ECMWF seasonal bootstrap target is system 51
- Documented ECMWF hindcast coverage for system 51 reaches 2016
- Project seasonal hindcast target is 2000-2016
- Project seasonal forecast target is 2017-2025
- Seasonal bootstrap product type is monthly_mean
- Seasonal bootstrap format is GRIB
- Seasonal known-issues registration is part of repository policy
- Official ECMWF seasonal monthly single-level smoke-test script is tracked
- Official grouped ECMWF seasonal monthly single-level production downloader is tracked
- Hindcast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- Forecast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- No `.part` files remain in the grouped forecast directory
- Inventory snapshots exist at:
  - data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
  - data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 monthly blocker on main
- No current ECMWF grouped single-level download blocker
- Seasonal pressure-level verification on main remains blocked until ERA5 monthly z925 is downloaded, tracked, and later merged from the parallel branch workflow

## Next action
1. Keep main as the stable project-state branch
2. Continue ERA5 monthly z925 work only in the linked worktree /home/fibi/projects/c3s_project_v2_era5_z925 on branch task/era5-z925
3. Before final reintegration, handle the fact that task/era5-z925 is behind main explicitly
4. Formally close the ERA5 monthly z925 milestone in Git on that branch
5. Merge the z925 branch back into main after milestone closure
6. Begin seasonal pressure-level verification only after the ERA5 monthly z925 baseline is available in repository state on main
7. Re-read repository state before any new production run or any new merge decision

## Last verified commit
- 0566034

============================================================
V. OFFICIAL STATE FILE: docs/HANDOFF.md
============================================================

# Handoff

## Project identity
- Name: c3s_project_v2
- Repository root: /home/fibi/projects/c3s_project_v2
- Primary raw data root: /mnt/e/last-aticol/data/raw
- Primary processed data root: /mnt/e/last-aticol/data/processed

## Source of truth
The repository is the authoritative source of truth.
Do not rely on conversation memory when repository state, logs, or tracked files provide evidence.

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

## Mandatory pre-read before continuation
Before any continuation, design, execution, correction, download, QC, or new decision, run:

```bash
cd /home/fibi/projects/c3s_project_v2

cat docs/DECISIONS.md
cat docs/SEASONAL_DOWNLOAD_POLICY.md
cat docs/SEASONAL_KNOWN_ISSUES.md
cat docs/STATUS.md
cat docs/HANDOFF.md
cat configs/datasets/c3s_seasonal_systems.yml
cat configs/datasets/c3s_seasonal_variables.yml
```

Rules:
- Continue only from the repository state read from those files.
- If a new policy or operational file becomes part of the official workflow, add it to the pre-read list.
- If repository state conflicts with remembered chat context, repository state is final.
- Do not skip this step before any new production run.

## Current confirmed state
- Clean repository bootstrap on WSL is complete.
- The ERA5 monthly baseline is complete, QC-verified, and merged into main.
- Seasonal work has advanced through planning, smoke-test validation, grouped ECMWF bootstrap download, tracked inventory creation, document refresh, and stable-branch merge closure.
- Seasonal bootstrap is intentionally restricted to ECMWF only.
- ECMWF seasonal bootstrap uses C3S system 51.
- Seasonal bootstrap starts with monthly single-level archives only.
- For project forecast years 2017-2025, the use of ECMWF system 51 is currently a working repository assumption for bootstrap execution and later validation.
- That ECMWF system-51 bootstrap assumption passed the initial smoke test for the first project forecast year 2017.
- The ECMWF hindcast path also passed the initial smoke test for project year 2000.
- The official smoke-test script is tracked at scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py.
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
- The first ECMWF seasonal monthly single-level bootstrap milestone is present on main through merge commit 0566034.
- Branch dev remains available as the integration branch and its latest document-refresh tip is 5d450ee.
- A separate linked worktree exists at /home/fibi/projects/c3s_project_v2_era5_z925 on branch task/era5-z925 for parallel ERA5 monthly z925 work.
- The linked task/era5-z925 branch currently points to commit 44c6d4d and is behind main.
- The backup branch backup-task-era5-z925-before-main-sync exists and currently points to 44c6d4d.
- The repository seasonal pressure-level substitute is z925, not z950.
- Matching ERA5 monthly z925 must be downloaded, tracked, and later merged before seasonal pressure-level verification begins.
- Seasonal hindcasts and forecasts are requested separately.
- Project seasonal hindcast target is 2000-2016.
- Project seasonal forecast target is 2017-2025.
- GRIB is the operational download format.
- A tracked seasonal known-issues register is required before any non-ECMWF centre is activated.

## Immediate next step
1. Keep main as the stable project-state branch.
2. Continue ERA5 monthly z925 work only in the linked worktree /home/fibi/projects/c3s_project_v2_era5_z925 on branch task/era5-z925.
3. Explicitly handle the fact that task/era5-z925 is behind main before final reintegration.
4. Formally close the ERA5 monthly z925 milestone in Git on that branch.
5. Merge the z925 branch back into main after milestone closure.
6. Begin seasonal pressure-level verification only after the ERA5 monthly z925 baseline is available in repository state on main.

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

============================================================
W. OFFICIAL CONFIG FILE: configs/datasets/c3s_seasonal_systems.yml
============================================================

seasonal_systems:
  ecmwf:
    originating_centre: ecmwf
    system: "51"
    label: "ECMWF SEAS5.1"
    status: active_bootstrap_target
    is_lagged: false
    hindcast_production: fixed
    documented_hindcast_year_start: 1981
    documented_hindcast_year_end: 2016
    project_hindcast_year_start: 2000
    project_hindcast_year_end: 2016
    project_forecast_year_start: 2017
    project_forecast_year_end: 2025
    hindcast_member_count: 25
    forecast_member_count: 51
    bootstrap_assumption_forecast_system_2017_2025: true
    bootstrap_assumption_note: "Repository bootstrap proceeds by requesting ECMWF system 51 for forecast years 2017-2025. This is a working repository assumption to be checked by smoke tests and first production retrievals. A period-specific forecast-system manifest may still be required later for scientific evaluation."
    datasets:
      single_levels: seasonal-monthly-single-levels
      pressure_levels: seasonal-monthly-pressure-levels

deferred_other_centres:
  note: "Other centres remain deferred until period-specific system mapping and issue registration are validated and committed."

============================================================
X. OFFICIAL CONFIG FILE: configs/datasets/c3s_seasonal_variables.yml
============================================================

bootstrap_single_levels:
  t2m:
    cds_variable: 2m_temperature
    dataset: seasonal-monthly-single-levels
    level_label: surface
    units: K

  ws10m:
    cds_variable: 10m_wind_speed
    dataset: seasonal-monthly-single-levels
    level_label: surface
    units: m s-1

  tp:
    cds_variable: total_precipitation
    dataset: seasonal-monthly-single-levels
    level_label: surface
    units: m s-1
    note: raw monthly archive quantity only; conversion belongs to analysis stage

deferred_pressure_levels:
  z500:
    cds_variable: geopotential
    dataset: seasonal-monthly-pressure-levels
    pressure_level: "500"
    level_label: 500hPa
    units: m2 s-2
    note: raw geopotential, not geopotential height

  t850:
    cds_variable: temperature
    dataset: seasonal-monthly-pressure-levels
    pressure_level: "850"
    level_label: 850hPa
    units: K

  z925:
    cds_variable: geopotential
    dataset: seasonal-monthly-pressure-levels
    pressure_level: "925"
    level_label: 925hPa
    units: m2 s-2
    note: seasonal pressure-level substitute for the supervisor wording z950; matching ERA5 monthly z925 must be downloaded later before seasonal pressure-level verification

external_requirement_note:
  supervisor_original_pressure_level_wording: z950
  repository_operational_pressure_level_substitute: z925
  reason: seasonal-monthly-pressure-levels documentation spans 925 hPa to 10 hPa, not 950 hPa

============================================================
Y. NEXT REQUESTED ASSISTANT ACTION
============================================================

Read this pack first.
Summarize the real repository state.
Identify the next safe step for the objective.
Do not provide operational commands until the state summary is complete.
