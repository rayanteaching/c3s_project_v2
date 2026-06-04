# Repository State Review After NCEP G8 Smoke Evidence

Generated at UTC: 2026-05-11T16:56:30Z
Repository root: /home/fibi/projects/c3s_project_v2

## 1. Git status
```text
## task/ncep-pressure-levels-smoke
?? runs/2026-05-11_repository_state_review_after_ncep_g8/
```

## 2. Branches
```text
  backup-main-before-era5-z925-merge-20260430T150259Z 5cef2ea runs: add ChatGPT re-entry pack snapshot
  backup-task-era5-z925-before-main-sync              44c6d4d runs(inventory): close ECMWF seasonal single-level grouped download milestone
  dev                                                 1f2556e docs(status): update last verified commit after NCEP caution
  integration/era5-z925-merge-20260430T150259Z        5cef2ea runs: add ChatGPT re-entry pack snapshot
  main                                                7267dc7 docs(state): clear seasonal unit blocker before NCEP smoke tests
  nch                                                 0920a10 runs(ncep): plan pressure-level smoke tests
  task/ecmwf-pressure-levels                          b4f6c90 runs(inspect): add ECMWF ensemble member inspection report
+ task/era5-z925                                      3f8d8d3 (/home/fibi/projects/c3s_project_v2_era5_z925) docs(state): close ERA5 z925 QC extension state
* task/ncep-pressure-levels-smoke                     2fc9757 docs(ncep): record G8 missing-date smoke evidence
```

## 3. Recent current-branch history
```text
* 2fc9757 (HEAD -> task/ncep-pressure-levels-smoke) docs(ncep): record G8 missing-date smoke evidence
* 8e6d936 runs(ncep): record G8 missing-date smoke evidence
* b4c7c7b scripts(ncep): record full smoke-test initialization dates
* 0f93a8a docs(status): update last verified commit after NCEP smoke success
* a95dfc1 docs(state): record initial NCEP pressure-level smoke success
*   eb05022 merge(dev): sync NCEP caution into smoke branch
|\
| * 1f2556e (dev) docs(status): update last verified commit after NCEP caution
| * 22b9e5c docs(seasonal): record NCEP May 2023 member-date caution
* | 339f254 runs(ncep): record pressure-level z500 t850 smoke success
* | 0920a10 (nch) runs(ncep): plan pressure-level smoke tests
|/
* 7267dc7 (main) docs(state): clear seasonal unit blocker before NCEP smoke tests
* 4c82f86 docs(status): update last verified commit after seasonal unit fix
* 0520078 configs(seasonal): restore official C3S total precipitation unit
* 3caf219 docs(status): update last verified commit after NCEP QA review
* 46f578e docs(seasonal): record pressure-level QA implications for NCEP
* c862ce7 docs(seasonal): add NCEP CFSv2 activation review
* 0fe6283 docs(status): update last verified commit after pressure-level scientific sanity QC
* 1a7451b runs(qc): verify ECMWF pressure-level scientific sanity
* ef6c847 docs(state): refresh next step after pressure-level openability QC
* 25c87fa docs(state): record pressure-level openability QC result
* 962c7b7 docs(state): close pressure-level openability QC state
* 7f52d8e runs(qc): verify ECMWF pressure-level canonical GRIB openability
* 8e8202a docs(status): update last verified commit after final cleanup sync
* bd51780 docs(status): update last verified commit after canonical naming cleanup
* 2d27623 docs(git): update workflow policy after pressure-level cleanup
* e92eaad runs(qc): canonicalize ECMWF pressure-level naming family
* 698e5d8 runs(qc): record ECMWF pressure-level structural QC warning
* 101c7bb docs(status): update last verified commit after pressure-level merge
* a59f5ff docs(protocol): include git workflow in pre-read
* 8a0092b docs(git): add workflow policy
```

## 4. Recent all-branch history
```text
* 2fc9757 (HEAD -> task/ncep-pressure-levels-smoke) docs(ncep): record G8 missing-date smoke evidence
* 8e6d936 runs(ncep): record G8 missing-date smoke evidence
* b4c7c7b scripts(ncep): record full smoke-test initialization dates
* 0f93a8a docs(status): update last verified commit after NCEP smoke success
* a95dfc1 docs(state): record initial NCEP pressure-level smoke success
*   eb05022 merge(dev): sync NCEP caution into smoke branch
|\
| * 1f2556e (dev) docs(status): update last verified commit after NCEP caution
| * 22b9e5c docs(seasonal): record NCEP May 2023 member-date caution
* | 339f254 runs(ncep): record pressure-level z500 t850 smoke success
* | 0920a10 (nch) runs(ncep): plan pressure-level smoke tests
|/
* 7267dc7 (main) docs(state): clear seasonal unit blocker before NCEP smoke tests
* 4c82f86 docs(status): update last verified commit after seasonal unit fix
* 0520078 configs(seasonal): restore official C3S total precipitation unit
* 3caf219 docs(status): update last verified commit after NCEP QA review
* 46f578e docs(seasonal): record pressure-level QA implications for NCEP
* c862ce7 docs(seasonal): add NCEP CFSv2 activation review
* 0fe6283 docs(status): update last verified commit after pressure-level scientific sanity QC
* 1a7451b runs(qc): verify ECMWF pressure-level scientific sanity
* ef6c847 docs(state): refresh next step after pressure-level openability QC
* 25c87fa docs(state): record pressure-level openability QC result
* 962c7b7 docs(state): close pressure-level openability QC state
* 7f52d8e runs(qc): verify ECMWF pressure-level canonical GRIB openability
* 8e8202a docs(status): update last verified commit after final cleanup sync
* bd51780 docs(status): update last verified commit after canonical naming cleanup
* 2d27623 docs(git): update workflow policy after pressure-level cleanup
* e92eaad runs(qc): canonicalize ECMWF pressure-level naming family
* 698e5d8 runs(qc): record ECMWF pressure-level structural QC warning
* 101c7bb docs(status): update last verified commit after pressure-level merge
* a59f5ff docs(protocol): include git workflow in pre-read
* 8a0092b docs(git): add workflow policy
* 41f282c runs(inventory): close ECMWF pressure-level production milestone
* e08284c runs(seasonal): mark ECMWF pressure-level production started
* 0a04792 feat(download): add ECMWF seasonal pressure-level downloader
* aa54d08 runs(smoke): record ECMWF pressure-level z925 smoke success
* 17a59c8 docs(status): update last verified commit after z925 policy alignment
* 78c7442 docs(state): align z925 policy after main reintegration
* cbc80a0 docs(state): mark z925 reintegration verified on main
*   62e7544 merge(era5): integrate z925 supplement and QC extension
|\
| * 3f8d8d3 (task/era5-z925) docs(state): close ERA5 z925 QC extension state
* | e5af98e merge(era5): integrate monthly z925 download and QC extension
|\|
| * 1a56570 qc(era5): extend monthly QC workflow to include z925
| *   d33b396 merge(dev): sync latest integration state into task/era5-z925 before z925 QC extension
| |\
| * | 2ba498c docs(decisions): register ERA5 z925 supplement and retain z950 baseline
| * | d47368a runs(inventory): close ERA5 monthly z925 download milestone
| * | 20cf616 runs(era5): mark z925 monthly download as running
| * | 5893eb9 feat(era5): add monthly z925 downloader and task metadata
| * | 44c6d4d (backup-task-era5-z925-before-main-sync) runs(inventory): close ECMWF seasonal single-level grouped download milestone
| | | * b4f6c90 (task/ecmwf-pressure-levels) runs(inspect): add ECMWF ensemble member inspection report
| | | * 211221a runs(inventory): close ECMWF pressure-level download milestone
| | | * 4698225 runs(seasonal): mark ECMWF pressure-level download running
```

## 5. Working-tree and staged diff summary
```text
===== git diff --stat =====

===== git diff --name-status =====

===== git diff --cached --stat =====

===== git diff --cached --name-status =====
```

## 6. Official mandatory pre-read files

### docs/CHATGPT_REENTRY_PROTOCOL.md
```text
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
cat docs/GIT_WORKFLOW.md
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
```

### docs/DECISIONS.md
```text
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
- ERA5 monthly z925 has been added as a parallel aligned dataset for the seasonal pressure-level substitute.
- Existing ERA5 monthly z950 data, metadata, inventory, and historical QC outputs remain intact and must not be deleted by this task.
- ERA5 z925 is added for seasonal comparison alignment with the repository seasonal pressure-level substitute z925.
- z925 is tracked as an ERA5 monthly pressure-level product in this repository
- z925 is the seasonal-aligned ERA5 supplement
- z950 baseline is retained and not deleted
- the z925 download, inventory, QC extension, and main reintegration are complete
- ERA5 monthly structural and scientific sanity QC now include z925 explicitly

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
- The matching ERA5 monthly z925 dataset has been downloaded, inventoried, QC-verified, and merged into main.
- That z925 collection is the seasonal-aligned supplement and does not replace the already tracked ERA5 z950 baseline.
- Seasonal pressure-level verification can now use the merged ERA5 monthly z925 baseline on main.

## Seasonal known-issues register rule
- Official C3S seasonal known issues must be copied into tracked repository documentation before a new centre or sensitive variable is activated.
- Each affected case must be classified in the repository as allow, warn, mask, or exclude.
- Non-ECMWF centres remain deferred until both period-specific system mapping and known-issues registration are committed.

## C3S seasonal pressure-level QA interpretation
- Seasonal monthly pressure-level products are monthly statistics derived from subdaily forecast data.
- These products are probabilistic seasonal forecast products, not deterministic weather forecasts.
- Monthly pressure-level fields may contain system-, region-, variable-, season-, and lead-dependent biases.
- Hindcasts/reforecasts are required for bias estimation, anomaly construction, and forecast skill assessment.
- Operational seasonal downloads must remain in native GRIB because complex NetCDF requests can have limited metadata and interpretation risk.
- Download success, checksum success, and openability success do not imply scientific readiness.
- NCEP CFSv2 production download is blocked until smoke tests verify system=2 coverage, member counts, nominal start handling, and leadtime metadata.
```

### docs/SEASONAL_DOWNLOAD_POLICY.md
```text
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

## ERA5 z925 dependency
- before seasonal pressure-level verification begins, the matching ERA5 monthly z925 dataset must be downloaded, tracked, QC-verified, and merged into main
- this dependency is now satisfied on main

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

## Seasonal pressure-level QA policy
- Monthly pressure-level products are monthly statistics derived from subdaily seasonal forecast data.
- Seasonal products must be interpreted probabilistically.
- Bias correction or bias-aware interpretation is required for scientific applications and derived forecast products.
- Hindcasts/reforecasts are required for model climatology, anomaly construction, and verification.
- Native GRIB remains the operational format for complex seasonal requests.
- Experimental NetCDF is not authorized for operational seasonal download workflows without a separate documented validation.
- Differences between forecast systems in grid, ensemble generation, start-date handling, leadtime metadata, and hindcast availability must be checked before a new centre is activated.
```

### docs/SEASONAL_KNOWN_ISSUES.md
```text
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

## NCEP CFSv2 activation review
- G8 caution for current workflow: NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. This is not treated as a blanket blocker for monthly_mean retrieval, but forecast May 2023 must receive explicit member/date-handling QC before any NCEP-derived product or multi-model analysis.
- Status: candidate centre under review; production download is not yet authorized.
- System: CFSv2-v20110310.
- CDS system keyword: 2.
- Operational caution: NCEP uses lagged/daily initialization; member counts and nominal start handling must be verified by smoke tests before production.
- E4.a1/E4.a2: fixed historical CDS availability issues for NCEP monthly statistics/anomalies. Repository action: allow after standard verification.
- E7/E7b: fixed missing-member issues affecting NCEP daily/subdaily datasets. Repository action: warn if daily/subdaily NCEP data are later activated; not a direct blocker for current monthly pressure-level workflow.
- E6: NCEP surface solar radiation variables were swapped for affected dates. Repository action: exclude from current workflow; re-review only if radiation variables are activated.
- G8: NCEP system=2 forecast data for 2023-05-22 are unavailable because all four members initialized on that date were not correctly transmitted. Repository action: warn; forecast May 2023 member/date handling must be checked explicitly in NCEP QC. This is not a blanket blocker for monthly_mean retrieval unless retrieval evidence or member/date counts show an impact.
```

### docs/GIT_WORKFLOW.md
```text
REPRODUCIBLE GIT-BASED PROJECT OPERATING INSTRUCTIONS

Scope:
These instructions are intended for serious, long-running, research-oriented, data-oriented, or operational projects where reproducibility, auditability, continuation, and safe Git history matter. For small experiments, apply the same principles but scale down the number of documents and run records.

Core rule:
Repository state is the final source of truth. Do not rely on chat memory, assumptions, previous summaries, or informal notes when repository state is available. Before any continuation, design, execution, correction, download, QC, merge, cleanup, or new decision, first inspect the current repository state and official project files. If repository state conflicts with memory or previous chat summaries, repository state wins.

Start every work session by asking for or running:

cd /path/to/project
git status --short --branch
git branch -vv
git log --oneline --decorate --graph -n 16
git log --oneline --decorate --graph --all -n 24
tree -L 4

Then read the official state and policy files that exist in the project:

cat docs/DECISIONS.md
cat docs/STATUS.md
cat docs/HANDOFF.md
cat docs/RUNBOOK.md
cat docs/KNOWN_ISSUES.md
cat docs/GIT_WORKFLOW.md
cat docs/DATA_POLICY.md
cat docs/DOWNLOAD_POLICY.md
cat docs/QC_POLICY.md
cat configs/project.yml
cat configs/datasets.yml
cat configs/variables.yml
cat configs/paths.yml
cat configs/download.yml
cat configs/qc.yml

If a listed file does not exist, do not assume it is required. For a new project, create only the official files that are relevant to the project scope. For a serious data project, the minimum recommended official files are:

README.md
.gitignore
docs/DECISIONS.md
docs/STATUS.md
docs/HANDOFF.md
docs/RUNBOOK.md
docs/KNOWN_ISSUES.md
configs/project.yml
configs/paths.yml

Recommended repository structure:

README.md
.gitignore
docs/
  DECISIONS.md
  STATUS.md
  HANDOFF.md
  RUNBOOK.md
  KNOWN_ISSUES.md
  GIT_WORKFLOW.md
  DATA_POLICY.md
  DOWNLOAD_POLICY.md
  QC_POLICY.md
configs/
  project.yml
  datasets.yml
  variables.yml
  paths.yml
  download.yml
  qc.yml
scripts/
  download/
  qc/
  inventory/
  utils/
runs/
  YYYY-MM-DD_descriptive_run_name/
    command.txt
    request_template.json
    run_metadata.json
    environment.txt
    status.txt
    notes.md
data/
  raw/
  processed/
  inventory/
logs/
env/
  environment.yml
  requirements.txt

Repository structure rule:
The repository must separate source code, configuration, documentation, run metadata, inventories, logs, raw data, and processed data. The project must remain understandable by reading tracked lightweight files only.

Data path rule:
data/raw/ is for unchanged raw data.
data/processed/ is for processed, regridded, subsetted, aggregated, converted, or derived data.
data/inventory/ is for lightweight tracked CSV/JSON inventory files.

data/raw/ and data/processed/ may exist inside the project tree, but they must be ignored by Git. For large projects, raw and processed data should preferably live outside the Git repository and be referenced through configs/paths.yml or configs/project.yml. Only lightweight inventory and metadata files should be tracked.

Important paths must be read from configs/paths.yml or configs/project.yml whenever possible. Scripts should not hard-code machine-specific data paths unless there is a documented reason.

Git tracking policy:
Track lightweight workflow-critical files needed for reproduction, continuation, understanding, QC, audit, or handoff.

Track:

README.md
.gitignore
docs/
configs/
scripts/
env/
runs/ metadata
data/inventory/
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
primary data files such as *.nc, *.grib, *.grib2, *.tif, *.zip, *.tar
temporary partial files such as *.part
credentials, secrets, tokens, API keys, .env, .cdsapirc, *.key, *.token

Raw and processed data must stay outside Git tracking. Metadata, inventories, requests, checksums, configs, scripts, decisions, and run records must be tracked.

.gitignore policy:
A project-level .gitignore file is mandatory for any project with data, logs, secrets, or long-running jobs. It must prevent accidental staging of raw data, processed data, logs, partial files, large binaries, credentials, local caches, and environment directories.

Minimum recommended .gitignore content:

data/raw/
data/processed/
logs/
*.nc
*.grib
*.grib2
*.tif
*.zip
*.tar
*.part
.env
.cdsapirc
*.key
*.token
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
envs/
*.egg-info/

If the project uses local machine-specific files, add them to .gitignore unless they are safe, lightweight, and required for reproduction.

Milestone policy:
Every important stage must be formally closed. Examples include:

initializing the repository
adding or changing configs
writing or changing scripts
starting a production run
completing a download
building an inventory
running QC
fixing a known issue
merging a branch
changing project policy
changing data paths
changing variable definitions
changing dataset definitions
changing run strategy

After every milestone:

Update docs/STATUS.md.
Update docs/HANDOFF.md.
Update docs/DECISIONS.md if a new decision was made.
Update docs/KNOWN_ISSUES.md if an issue was found, fixed, accepted, or deferred.
Update docs/RUNBOOK.md if execution instructions changed.
Record run metadata under runs/ if a run was executed.
Create or update data/inventory/ if data was created, downloaded, checked, or summarized.
Commit all official lightweight files.
Do not commit raw data, processed data, logs, large binaries, credentials, or secrets.

Commit message style:
Use short, precise, auditable commit messages.

Good examples:

chore(repo): initialize project structure
docs(policy): add repository tracking policy
configs(data): add dataset definitions
configs(paths): add external data paths
scripts(download): add monthly download script
runs/download: mark production run as started
data/inventory): add raw data inventory snapshot
scripts(qc): add checksum verification workflow
docs(status): refresh status after QC
docs(handoff): refresh continuation point
merge(data): integrate completed dataset branch

Avoid vague messages such as:

update files
changes
fix stuff
latest
new version
final update

Branch strategy:
main contains stable, closed, explainable project states only.
dev is optional. Use dev only if it reduces risk by providing an integration branch before main.
task branches should be used for meaningful isolated work.

Recommended branch names:

task/add-download-script
task/run-era5-inventory
task/qc-monthly-data
task/fix-z925-policy
docs/refresh-handoff
configs/update-paths

Before merging:

git status must be clean unless the merge itself is being prepared.
docs/STATUS.md must be updated.
docs/HANDOFF.md must be updated.
docs/DECISIONS.md must be updated if the branch introduced a decision.
docs/KNOWN_ISSUES.md must be updated if the branch introduced, fixed, or documented an issue.
Relevant inventory and run metadata must be committed if the branch executed a run.

Important merges should use --no-ff when useful for audit history. Do not use --no-ff mechanically for every tiny change. Use it when preserving a visible task boundary is valuable.

After merging, inspect history:

git log --oneline --decorate --graph -n 16
git log --oneline --decorate --graph --all -n 24

End-of-milestone report:
At the end of every meaningful milestone, collect the current project state:

cd /path/to/project
git status --short --branch
git diff --stat
git diff --name-only
git log --oneline --decorate --graph -n 16
git log --oneline --decorate --graph --all -n 24

Check tracked workflow files when needed:

git ls-files docs
git ls-files configs
git ls-files scripts
git ls-files runs
git ls-files data/inventory
git ls-files env

Run management:
Every run must have its own deterministic and readable metadata directory:

runs/YYYY-MM-DD_descriptive_run_name/

Good examples:

runs/2026-05-03_era5_z925_monthly_download/
runs/2026-05-03_ecmwf_pressure_levels_hindcast_z500/
runs/2026-05-03_monthly_inventory_build/
runs/2026-05-03_era5_monthly_qc/

Avoid vague run names:

runs/run1/
runs/test/
runs/new/
runs/final/

Recommended files inside each run directory:

command.txt
request_template.json
run_metadata.json
environment.txt
status.txt
notes.md

File meanings:

command.txt:
Exact command used to start the run.

request_template.json:
Request, processing template, or API query template used by the run.

run_metadata.json:
Machine, time, script version, config version, branch, commit hash, run directory, output directory, and important runtime settings.

environment.txt:
Python version, package information, conda export or pip freeze, uname -a, and other relevant environment details.

status.txt:
One clear status value and short explanation. Recommended status values are:

planned
started
running
completed
failed
verified
abandoned

notes.md:
Human notes about errors, decisions, caveats, warnings, retries, assumptions, and continuation context.

Even if raw data is not tracked, run metadata must be tracked.

Run directory size rule:
runs/ should contain lightweight metadata and summaries, not large outputs. Do not store large raw data, processed data, or full logs in tracked run directories. Important log information must be summarized into tracked run metadata files.

Download policy:
Every download must be reproducible. For each downloaded file, create sidecar metadata:

filename.ext
filename.ext.request.json
filename.ext.sha256

The request JSON should include:

created_at_utc
dataset
request
target_path
script_path
script_git_commit
config_path
config_git_commit
notes

Every downloaded file must have a checksum for integrity checks. It must always be possible to know which dataset, request, script, config, time, and checksum produced each file.

Partial download policy:
Downloads should use a temporary partial file extension such as .part while running. A file should be renamed to its final name only after successful completion and checksum creation.

Scripts should support --skip-existing or equivalent behavior when appropriate. Scripts should not silently overwrite existing files unless overwrite behavior is explicitly requested and documented.

Inventory policy:
Create inventory snapshots for every dataset collection under data/inventory/.

Recommended columns:

dataset
source
system
variable
level
year
month
leadtime
member_count
file_path
file_size_bytes
sha256
request_json_path
created_at_utc
verified
notes

Inventory files are audit tools, not raw data, so they should be tracked when they remain lightweight and useful.

If an inventory becomes too large for practical Git tracking, track a lightweight summary inventory and document where the full inventory is stored. Do not blindly commit huge CSV or JSON files only because the extension is allowed.

QC policy:
QC must be separate from download. A downloaded file is not automatically a verified file.

Recommended QC checks:

file existence
file size
checksum
file open test with the proper library
dimensions
variables
coordinate names
time coverage
missing months
duplicates
units
metadata consistency
expected file count
recorded QC result

Track lightweight QC outputs such as:

data/inventory/qc_summary_YYYY-MM-DD.csv
runs/YYYY-MM-DD_descriptive_run_name/qc_report.json
runs/YYYY-MM-DD_descriptive_run_name/qc_notes.md

QC outputs should state clearly whether the checked collection passed, failed, partially passed, or requires manual review.

Log policy:
logs/ must not be tracked. Full logs are operational artifacts and may be large, noisy, or machine-specific.

Important log information must be summarized into tracked files:

runs/YYYY-MM-DD_descriptive_run_name/status.txt
runs/YYYY-MM-DD_descriptive_run_name/notes.md
runs/YYYY-MM-DD_descriptive_run_name/run_metadata.json
docs/KNOWN_ISSUES.md
docs/HANDOFF.md

Environment policy:
Track environment definitions, not installed environments.

Recommended commands:

conda env export --no-builds > env/environment.yml
pip freeze > env/requirements.txt

Do not commit virtual environments, conda environments, package caches, or machine-specific installation directories.

Credential policy:
Never commit real credentials. If credentials are needed, create templates only, such as:

configs/cdsapirc.template
env/env.template

Templates must not contain real secrets.

Never copy real credentials into:

docs/
configs/
runs/
logs/
env/
data/inventory/
command.txt
notes.md
run_metadata.json

Before committing, inspect staged files enough to ensure no credentials, tokens, API keys, private paths, or secret values are included.

Configuration policy:
Configuration files must be clear, minimal, and project-relevant.

Recommended config files:

configs/project.yml
configs/paths.yml
configs/datasets.yml
configs/variables.yml
configs/download.yml
configs/qc.yml

Config files should avoid hidden assumptions. Dataset names, variables, levels, date ranges, output roots, and QC expectations should be explicit.

Configuration validation policy:
When configs become important for execution, add a lightweight validation script or validation mode.

Recommended location:

scripts/utils/validate_configs.py

The validation should check, when relevant:

required keys exist
paths are defined
paths are not accidentally hard-coded in scripts
dataset names are valid
variable names are valid
levels are valid
year and month ranges are valid
download settings are complete
QC settings are complete
output directories are defined
credentials are not stored inside configs

Script policy:
Scripts must live under scripts/ and have clear names.

Recommended script directories:

scripts/download/
scripts/qc/
scripts/inventory/
scripts/utils/

Scripts should:

read inputs from CLI arguments or config files
support dry-run or check mode when possible
produce understandable logs
create request sidecars for downloads
create checksum sidecars for downloads
report failures clearly
use .part for partial files
support skip-existing or resume behavior when appropriate
print a final summary
avoid machine-specific hard-coded paths
fail loudly when required inputs are missing
write outputs to documented locations

Long-running execution pattern:

nohup python scripts/download/example_download.py \
  --config configs/download.yml \
  --run-dir runs/YYYY-MM-DD_descriptive_run_name \
  > logs/YYYY-MM-DD_descriptive_run_name.nohup.out 2>&1 &

Then record the PID with:

echo $!

Save the exact command in:

runs/YYYY-MM-DD_descriptive_run_name/command.txt

Pre-run review:
Before every new run, check:

current branch
git status
relevant configs
relevant scripts
output directory
overwrite risk
logs directory
run directory
command.txt
credentials outside Git
disk space
network access
expected file count
expected output structure
QC plan

Post-run review:
After every run, check:

tail of logs
file counts
partial file counts
failure messages
checksum files
checksum verification
inventory creation
QC results
docs/STATUS.md
docs/HANDOFF.md
docs/KNOWN_ISSUES.md if needed
git status
tracked lightweight files only
milestone commit

Local validation policy:
Before important milestone commits, run lightweight validation appropriate to the project.

Recommended checks:

python -m py_compile scripts/**/*.py
python scripts/utils/validate_configs.py
git status --short --branch
git diff --stat
git diff --name-only

Use project-specific validation commands when available. Do not let validation become a replacement for scientific QC. Code validation, config validation, inventory validation, and scientific QC are separate concerns.

STATUS.md policy:
docs/STATUS.md is the current state file. It should be factual, concise, and updated after every meaningful milestone. It must not become a long diary.

Recommended template for docs/STATUS.md:

# Status

## Last verified repository state
- Branch:
- Commit:
- Verified at UTC:
- Verified by:

## Project goal
- Short goal:

## Current phase
- Active phase:
- Phase status:

## Completed milestones
- YYYY-MM-DD:
- YYYY-MM-DD:

## Current data status
- Raw data:
- Processed data:
- Inventory:
- QC:

## Current code/config status
- Scripts:
- Configs:
- Environment:

## Known blockers
- None, or list blockers clearly.

## Known issues summary
- None, or list issue IDs/titles from docs/KNOWN_ISSUES.md.

## Next action
- Exact next step:

## Do not do next
- Explicitly list risky, forbidden, or premature actions.

## Required files to read before continuation
- docs/DECISIONS.md
- docs/STATUS.md
- docs/HANDOFF.md
- docs/RUNBOOK.md
- docs/KNOWN_ISSUES.md
- relevant configs

HANDOFF.md policy:
docs/HANDOFF.md is the continuation file. It should be short, practical, and written for a new person or a new ChatGPT session. It should answer exactly where the project stands and how to continue safely.

HANDOFF.md must not duplicate the full history. It should point to the correct official files and state the next action clearly.

Recommended template for docs/HANDOFF.md:

# Handoff

## Read this first
Before continuing, inspect repository state and read the official files listed in docs/STATUS.md.

## Current continuation point
- Branch:
- Commit:
- Current task:
- Last completed action:
- Last verified result:

## Immediate next action
- Exact next action:

## Commands to inspect state
cd /path/to/project
git status --short --branch
git branch -vv
git log --oneline --decorate --graph -n 16
git log --oneline --decorate --graph --all -n 24
tree -L 4

## Important context
- Key decision:
- Key data status:
- Key QC status:
- Key known issue:

## Files likely needed next
- docs/DECISIONS.md
- docs/STATUS.md
- docs/RUNBOOK.md
- docs/KNOWN_ISSUES.md
- relevant configs
- relevant scripts
- relevant inventory files
- relevant run metadata

## Risks and warnings
- Do not:
- Check before running:
- Verify after running:

## Expected milestone closure
After the next action succeeds, update:
- docs/STATUS.md
- docs/HANDOFF.md
- docs/DECISIONS.md if a decision changed
- docs/KNOWN_ISSUES.md if an issue changed
- docs/RUNBOOK.md if execution instructions changed
- runs/ metadata if a run was executed
- data/inventory/ if data status changed

DECISIONS.md policy:
docs/DECISIONS.md records durable project decisions. It should not include every small note. It should record decisions that affect future work, reproducibility, interpretation, data policy, branch strategy, download strategy, QC strategy, variables, datasets, paths, or assumptions.

Recommended decision entry format:

## YYYY-MM-DD - Decision title
- Decision:
- Reason:
- Alternatives considered:
- Consequences:
- Files/configs affected:
- Status:

KNOWN_ISSUES.md policy:
docs/KNOWN_ISSUES.md records accepted, active, fixed, or deferred issues.

Recommended issue format:

## ISSUE-ID - Issue title
- Status:
- Found at:
- Affected files/data/scripts:
- Description:
- Impact:
- Workaround:
- Fix:
- Verification:
- Related commits:

RUNBOOK.md policy:
docs/RUNBOOK.md contains operational instructions. It should explain how to run, verify, and continue the project. If execution instructions change, update RUNBOOK.md in the same milestone.

ChatGPT working rules:
Before technical decisions, inspect repository state or ask for the standard Git report.
Use docs/STATUS.md and docs/HANDOFF.md as the basis for continuation.
Avoid guessing about files, branches, scripts, paths, variables, configs, data status, QC status, or merge status.
Suggest documentation updates and commits after every meaningful milestone.
Never suggest committing raw data, processed data, logs, large binaries, or credentials.
Suggest committing metadata, configs, scripts, docs, inventories, and run records.
Use exact, ordered, copy-paste-friendly shell commands when commands are requested.
Use vi for file editing if an editor is needed.
Use nohup for long-running jobs.
After long-running jobs, check logs, file counts, partial files, checksums, inventory, QC, and Git status.
If something is uncertain, say it clearly and give a verification method.
If repository state is unavailable, ask for the standard Git report instead of guessing.

Response formatting rule:
When the user explicitly asks for shell commands, exact repository file content, or copy-paste-ready terminal/project instructions, output exactly one fenced code block only. Do not add explanations, bullets, warnings, introductions, or summaries outside the code block. Do not split one file across multiple code blocks. Keep paths, filenames, commands, variable names, and technical artifacts in English.

This rule applies only to copy-paste-ready commands, exact file content, or terminal procedures. It does not apply to conceptual explanations, reviews, critiques, or planning discussions unless the user explicitly requests copy-paste-ready output.

File naming policy:
Use deterministic, readable, parseable names.

Good examples:

era5_t2m_monthly_2000_2025.grib
era5_t2m_monthly_2000_2025.request.json
era5_t2m_monthly_2000_2025.sha256
c3s_ecmwf_hindcast_z500_2000_2016.grib
inventory_era5_monthly_2000_2025.csv
qc_summary_era5_monthly_YYYY-MM-DD.csv

Avoid vague names:

data.grib
new.nc
final.csv
test2.json
output_latest.txt

Trustworthiness goal:
The repository must be self-explanatory enough that a new person or ChatGPT in a new chat can understand the project goal, required datasets, collected datasets, incomplete work, scripts, commands used for runs, data provenance, QC status, known issues, branch state, and exact continuation point by reading the repository only.


```

### docs/STATUS.md
```text
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
- ERA5 monthly z925 supplement for 2000-2025 completed successfully on task/era5-z925
- ERA5 monthly z925 inventory snapshot is tracked
- ERA5 monthly QC workflow was extended to include z925 explicitly
- ERA5 monthly structural QC passed for tp, t2m, ws10m, z500, t850, z925, and z950
- ERA5 monthly scientific sanity QC passed for tp, t2m, ws10m, z500, t850, z925, and z950
- Seasonal forecast planning is active
- Seasonal bootstrap is restricted to ECMWF only
- Seasonal bootstrap starts with monthly single-level archives
- ECMWF seasonal monthly single-level smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
- ECMWF seasonal monthly pressure-level z925 smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
- The repository bootstrap assumption using ECMWF system 51 for forecast years 2017-2025 has passed initial smoke validation
- Grouped ECMWF monthly single-level hindcast download for 2000-2016 completed successfully
- Grouped ECMWF monthly single-level forecast download for 2017-2025 completed successfully
- Tracked inventory snapshots were created for both ECMWF grouped single-level blocks
- The first ECMWF seasonal monthly single-level bootstrap download milestone is formally closed and merged into main
- Seasonal pressure-level work has begun on the z925-based pressure-level track
- A matching ERA5 monthly z925 dataset has been downloaded, inventoried, and included in the ERA5 monthly QC workflow before seasonal pressure-level verification
- Hindcast and forecast requests are handled separately operationally
- ECMWF seasonal monthly pressure-level production completed successfully for hindcast 2000-2016 and forecast 2017-2025
- ECMWF pressure-level inventory snapshots were created for z500, t850, and z925
- ECMWF pressure-level structural checksum QC passed after canonical naming-family selection

## Confirmed facts
- Repository root: /home/fibi/projects/c3s_project_v2
- Raw data root: /mnt/e/last-aticol/data/raw
- Processed data root: /mnt/e/last-aticol/data/processed
- Git branches main and dev exist
- main contains the closed ECMWF grouped single-level bootstrap milestone and re-entry protocol commits
- ECMWF seasonal bootstrap target is system 51
- Documented ECMWF hindcast coverage for system 51 reaches 2016
- Project seasonal hindcast target is 2000-2016
- Project seasonal forecast target is 2017-2025
- Seasonal bootstrap product type is monthly_mean
- Seasonal bootstrap format is GRIB
- Seasonal known-issues registration is part of repository policy
- Official ECMWF seasonal monthly single-level smoke-test script is tracked
- Official ECMWF seasonal monthly pressure-level smoke-test script is tracked
- Official grouped ECMWF seasonal monthly single-level production downloader is tracked
- Hindcast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- Forecast grouped download produced 12 GRIB files, 12 request sidecars, and 12 SHA256 sidecars
- No `.part` files remain in the grouped forecast directory
- Inventory snapshots exist at:
  - data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
  - data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
- The grouped-download milestone closure commit on dev is e373eb8
- main contains the ERA5 z925 supplement and z925 QC extension commits after reintegration
- task/era5-z925 has been reintegrated into main for the ERA5 z925 supplement and QC extension

## Current blockers
- No current WSL CDS connectivity blocker
- No open ERA5 blocker
- No current ECMWF grouped download blocker
- No blocker remains for the completed ECMWF single-level bootstrap download milestone
- No blocker remains for the completed ECMWF pressure-level production download milestone
- Pressure-level duplicate naming-family warning was handled by moving the noncanonical duplicate family out of active raw directories without deletion
- ECMWF pressure-level canonical GRIB openability QC passed for sampled st01 and st12 files using ecCodes
- ECMWF pressure-level scientific sanity QC passed for all 72 canonical GRIB files using ecCodes sampled-message checks
- NCEP CFSv2 activation review has started; production download is blocked until smoke tests verify system=2 coverage and member handling
- C3S seasonal pressure-level QA review is documented; NCEP production remains blocked until smoke tests verify system=2 coverage, member handling, and metadata semantics
- NCEP May 2023 forecast requires explicit member/date-handling QC because documented system=2 data initialized on 2023-05-22 are unavailable.
- Initial NCEP CFSv2 pressure-level smoke tests passed for z500 and t850 for hindcast year 2000 and forecast year 2020; production download remains blocked.
- Corrected NCEP G8-sensitive smoke test for nominal June 2023 z500 confirmed that dataDate=20230522 is absent; message_count=120 instead of the expected 124 for a complete 31-date lagged window.

## Next action
1. Decide and document final NCEP production-download policy using the committed initial smoke-test metadata and G8 missing-date evidence
2. Keep production NCEP download blocked until the final policy is committed
3. Do not use NCEP May/June 2023 blindly in any derived product without explicit missing-date handling

## Last verified commit
- a95dfc1
```

### docs/HANDOFF.md
```text
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
cat docs/GIT_WORKFLOW.md
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
- NCEP CFSv2 activation review has started; production download is blocked until smoke tests verify system=2 coverage and member handling.
- C3S seasonal pressure-level QA review is documented; NCEP production remains blocked until smoke tests verify system=2 coverage, member handling, and metadata semantics.
- NCEP May 2023 forecast requires explicit member/date-handling QC because documented system=2 data initialized on 2023-05-22 are unavailable.
- Initial NCEP CFSv2 pressure-level smoke tests passed for z500 and t850 for hindcast year 2000 and forecast year 2020; production download remains blocked.
- Corrected NCEP G8-sensitive smoke test for nominal June 2023 z500 confirmed that dataDate=20230522 is absent; message_count=120 instead of the expected 124 for a complete 31-date lagged window.

## Immediate next step
1. Decide and document final NCEP production-download policy using the committed initial smoke-test metadata and G8 missing-date evidence.
2. Keep production NCEP download blocked until the final policy is committed.
3. Do not use NCEP May/June 2023 blindly in any derived product without explicit missing-date handling.

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
```

### configs/datasets/c3s_seasonal_systems.yml
```text
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
```

### configs/datasets/c3s_seasonal_variables.yml
```text
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
    note: official CDS seasonal monthly single-level unit for total_precipitation; raw monthly archive quantity only; conversion to accumulated depth belongs to analysis stage

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
    note: seasonal pressure-level substitute for the supervisor wording z950; matching ERA5 monthly z925 has been downloaded, tracked, QC-verified, and merged into main

external_requirement_note:
  supervisor_original_pressure_level_wording: z950
  repository_operational_pressure_level_substitute: z925
  reason: seasonal-monthly-pressure-levels documentation spans 925 hPa to 10 hPa, not 950 hPa
```

## 7. Seasonal review documents

### docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md
```text
# C3S seasonal monthly pressure-level quality-assurance review

## Scope
This document records repository-relevant quality-assurance implications from the CDS quality tab for `seasonal-monthly-pressure-levels`.

This review applies before activating NCEP CFSv2 production downloads and before any multi-model seasonal verification or product generation.

## Reviewed source
- CDS dataset: `seasonal-monthly-pressure-levels`
- CDS tab: Quality
- Fitness-for-purpose evaluation date shown by CDS: 2026-04-29
- Dataset update date shown by CDS: 2026-05-05

## Core interpretation
Seasonal monthly pressure-level data are monthly statistics derived from subdaily seasonal forecast data.

The monthly products are appropriate when the application does not require daily or subdaily information.

The data must not be interpreted as deterministic weather forecasts. Seasonal forecasts are probabilistic and are intended to provide information about potential deviations from normal climate conditions at monthly to seasonal timescales.

## Bias and hindcast dependency
The CDS quality information states that monthly statistics contain systematic deviations from the true climate.

Repository implications:
- Raw forecast fields must not be used as final scientific products without bias assessment.
- Bias correction or at minimum bias-aware interpretation is required for forecast applications.
- Hindcasts/reforecasts are required to estimate model climatology, systematic error, and forecast skill.
- Any anomaly or bias-corrected product must document the reference period, method, system, lead time, and variable.

## Forecast skill
Forecast skill is case-specific.

Skill depends on:
- variable
- lead time
- region
- season
- climate state
- forecast system
- predictable phenomena and teleconnections

Repository implications:
- Skill must not be assumed from download success.
- Northern Hemisphere verification must be performed explicitly against ERA5 or another documented reference.
- Skill may be stronger for large-scale features and shorter lead times.
- Skill may be stronger in the tropics than in mid-latitudes.
- Temperature may generally be more skillful than precipitation, but this must not be generalized without project-specific verification.

## Multi-system and NCEP caution
The CDS quality information stresses that this is a complex multi-system forecast dataset with start-date and lead-time dimensions.

Forecast systems can differ in:
- spatial grid
- ensemble generation method
- burst versus lagged ensemble design
- available hindcast/reforecast periods
- metadata representation in CDS
- system-version transitions

Repository implications for NCEP:
- May 2023 NCEP forecast data require explicit member/date-handling QC because the documented G8 issue states that NCEP system=2 data initialized on 2023-05-22 are unavailable.
- NCEP CFSv2 must not be treated as operationally identical to ECMWF.
- NCEP member counts, nominal start dates, initialization-date handling, and lead-time metadata must be verified by smoke tests before production.
- NCEP production download remains blocked until smoke tests confirm correct request semantics and metadata interpretation.

## Format decision
The CDS quality information warns that experimental NetCDF files may have limited metadata and can create interpretation problems for complex requests.

Repository decision:
- Operational seasonal downloads must use native GRIB.
- NetCDF must not be used for operational seasonal download workflows unless a separate documented validation justifies it.
- GRIB metadata must be inspected with ecCodes/cfgrib-aware tools during QC.

## Dataset usability implications
Download completion does not imply scientific readiness.

Required workflow layers:
1. raw download
2. sidecar request capture
3. checksum verification
4. inventory snapshot
5. structural QC
6. openability QC
7. metadata sanity QC
8. scientific sanity QC
9. hindcast-based verification
10. bias/anomaly strategy before derived products

## NCEP activation rule
Before NCEP production download, the repository must complete and commit:
- NCEP smoke-test script
- representative hindcast smoke tests
- representative forecast smoke tests
- member-count inspection
- nominal start-date and leadtime interpretation notes
- relevant known-issue registration
- run metadata and status updates

Recommended NCEP smoke-test years:
- hindcast: 2000
- hindcast: 2010
- hindcast: 2011
- hindcast: 2016
- forecast: 2017
- forecast: 2023
- forecast: 2025

## Current decision
NCEP is still a candidate centre under activation review.

Production download is not authorized until smoke tests and metadata checks pass.
```

### docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md
```text
# NCEP CFSv2 activation review

## Scope
This document records the repository activation review for NCEP CFSv2 before any NCEP seasonal download is started.

## Reviewed official sources
- CDS dataset: seasonal-monthly-pressure-levels
- C3S Knowledge Base: Description of the C3S seasonal multi-system
- C3S Knowledge Base: NCEP Forecast System
- C3S Knowledge Base: Description of CFSv2-v20110310 C3S contribution
- C3S Knowledge Base: C3S Seasonal Forecast known issues
- C3S Knowledge Base: Summary of available data
- C3S Knowledge Base: Detailed list of parameters
- C3S Knowledge Base: Recommendations and efficiency tips for C3S seasonal forecast datasets

## Dataset relevance
The CDS pressure-level monthly dataset is relevant to the project pressure-level targets:
- z500: geopotential at 500 hPa
- t850: temperature at 850 hPa
- z925: geopotential at 925 hPa

The dataset is monthly, global, regular latitude-longitude, 1 degree by 1 degree, and delivered in GRIB format.

## NCEP system mapping
- Provider: NCEP
- Forecast system: CFSv2-v20110310
- CDS system keyword: 2
- C3S multi-system provider code shown in documentation: kwbc
- Forecast model: NCEP Global Forecast System coupled to GFDL MOM4 ocean model
- Atmosphere resolution: T128, approximately 1 degree latitude-longitude
- Atmosphere vertical resolution: 64 hybrid sigma-pressure levels
- Ocean model: GFDL MOM4
- Ocean vertical resolution: 40 layers

## Operational differences from ECMWF
NCEP must not be treated as operationally identical to ECMWF.

Documented NCEP characteristics:
- Forecast initial conditions are available every day of the month.
- Forecast members are initialized every 6 hours at 00, 06, 12, and 18 UTC.
- Forecast ensemble construction is therefore lagged/daily.
- Hindcast initial conditions are available every 5 days.
- Hindcast members are initialized every 6 hours at 00, 06, 12, and 18 UTC.
- Hindcast production is fixed.

Implication:
NCEP smoke tests and QC must explicitly inspect member counts, initialization dates, nominal start month handling, and leadtime metadata.

## Time-period caution
The CDS dataset overview states:
- hindcasts: 1993-2016
- forecasts: 2017 to present

The CFSv2 system-description page states:
- hindcast years: 1981-2010

Repository action:
Before production download, run NCEP smoke tests for representative project years and do not assume complete 2000-2016 coverage without CDS retrieval evidence.

Required smoke-test years:
- hindcast: 2000
- hindcast: 2010
- hindcast: 2011
- hindcast: 2016
- forecast: 2017
- forecast: 2023
- forecast: 2025

## Known issues relevant to NCEP
- G8 caution: NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. Repository interpretation: this is not a blanket blocker for monthly_mean retrieval, but May 2023 forecast member/date handling must be explicitly checked during NCEP QC before using NCEP in derived products or multi-model analysis.
### E4.a1 and E4.a2
Monthly statistics and anomalies for some NCEP CFSv2 hindcast and forecast dates were temporarily unavailable in 2019.
Official status: fixed in the archive.
Repository action: allow, but keep note in known-issues register.

### E7 and E7b
Missing members affected NCEP CFSv2 high-frequency daily/subdaily datasets.
Official status: fixed.
Repository action: not a blocker for monthly pressure-level downloads, but warn if daily/subdaily NCEP data are later activated.

### E6
NCEP CFSv2 surface solar radiation variables were swapped for affected start dates.
Repository action: not relevant to current z500, t850, z925 workflow. Exclude or re-review if radiation variables are later activated.

### G8
NCEP system=2 forecast data for 2023-05-22 are unavailable because all four members initialized on that date were not correctly transmitted.
Repository action: warn. Forecast May 2023 member counts must be explicitly checked during NCEP QC.

Repository smoke-test evidence: corrected nominal June 2023 z500 monthly_mean retrieval recorded dataDate=20230522 as absent, messages_for_20230522=0, message_count=120, and observed_missing_message_count=4. This confirms the G8 missing initialization-date issue in retrieved monthly_mean GRIB metadata. Production download remains blocked until final NCEP production policy is documented.

## Pressure-level variable decision
The repository pressure-level substitute remains z925, not z950.

NCEP activation should use:
- z500
- t850
- z925

Do not introduce z950 for C3S seasonal pressure-level downloads.

## Format and retrieval policy
- Use native GRIB.
- Do not use experimental NetCDF conversion for operational workflow.
- Do not silently interpolate or convert units during download.
- Record exact request payloads and sidecars.
- Use checksum sidecars.
- Keep raw data outside Git.
- Track only lightweight run metadata and inventories.

## Activation status
NCEP is not yet activated for production download.

Allowed next step:
- create NCEP smoke-test script and run smoke tests for representative hindcast and forecast years.

Blocked until smoke tests pass:
- grouped NCEP production download
- NCEP inclusion in multi-model analysis
- NCEP-derived products

## CDS quality-assurance implications for NCEP
The CDS quality information for seasonal monthly pressure-levels reinforces that NCEP must be activated cautiously.

Repository implications:
- Do not proceed directly to NCEP production download.
- Verify NCEP system=2 request semantics using smoke tests first.
- Verify member-count behaviour explicitly because NCEP uses lagged/daily ensemble generation.
- Verify nominal start-month and leadtime metadata before grouped downloads.
- Keep native GRIB as the operational format.
- Do not use experimental NetCDF for operational NCEP downloads.
- Do not create NCEP anomaly, bias-corrected, or multi-model products until hindcast-based verification and bias strategy are documented.
```

## 8. NCEP smoke-test run metadata

### runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json
```text
{
  "status": "planned",
  "dataset": "seasonal-monthly-pressure-levels",
  "originating_centre": "ncep",
  "system": "2",
  "forecast_system": "CFSv2-v20110310",
  "purpose": "pre-production NCEP pressure-level smoke-test planning",
  "production_download_authorized": false,
  "safe_first_variables": ["z500", "t850"],
  "unsafe_first_targets": ["z925", "pressure_level=925", "year=2017 as first forecast smoke-test year"],
  "required_checks": [
    "system=2 request semantics",
    "hindcast availability",
    "forecast availability",
    "pressure-level availability",
    "nominal start-month handling",
    "leadtime_month metadata",
    "member/date handling",
    "May 2023 G8 caution handling",
    "GRIB metadata readability"
  ],
  "may_2023_g8_caution": "NCEP system=2 data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. This is not a blanket blocker for monthly_mean retrieval, but May 2023 must receive explicit member/date-handling QC."
}
```

### runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md
```text
# NCEP CFSv2 pressure-level smoke-test plan

## Scope
This run metadata records the safe pre-production smoke-test plan for NCEP CFSv2 pressure-level data.

## Centre and system
- Originating centre: ncep
- MARS origin: kwbc
- Forecast system: CFSv2-v20110310
- CDS system: 2
- Dataset: seasonal-monthly-pressure-levels
- Operational format: GRIB

## Current repository decision
NCEP production download is not authorized yet.

## Safe variables for first smoke tests
- z500: variable=geopotential, pressure_level=500
- t850: variable=temperature, pressure_level=850

## Do not use for NCEP pressure-level activation smoke tests
- z925
- pressure_level=925
- year=2017 as the first forecast smoke-test year

## Smoke-test purpose
The smoke tests must verify:
- system=2 request semantics
- available hindcast years and forecast years
- safe pressure-level availability
- nominal start-month handling
- leadtime_month metadata
- member/date handling
- May 2023 G8 caution handling
- GRIB metadata readability

## May 2023 G8 caution
The documented G8 issue states that NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted.

Repository interpretation:
- This is not a blanket blocker for monthly_mean retrieval.
- Forecast May 2023 requires explicit member/date-handling QC.
- NCEP-derived products and multi-model analysis must not use May 2023 blindly.

## First smoke-test candidates
Use small requests only.

Recommended first hindcast smoke tests:
- year=2000, month=01, leadtime_month=1, z500
- year=2000, month=01, leadtime_month=1, t850

Recommended first forecast smoke tests:
- year=2020 or 2021, month=01, leadtime_month=1, z500
- year=2020 or 2021, month=01, leadtime_month=1, t850

Recommended caution-specific smoke test after basic availability succeeds:
- year=2023, month=05, leadtime_month=1, z500
- year=2023, month=05, leadtime_month=1, t850

## Blocked until smoke tests pass
- grouped NCEP production download
- NCEP inclusion in multi-model analysis
- NCEP-derived products
```

### runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/status.json
```text
{
  "dataset": "seasonal-monthly-pressure-levels",
  "details_json": "runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json",
  "grib_count": 4,
  "leadtime_month": "1",
  "metadata_json_count": 4,
  "month": "01",
  "originating_centre": "ncep",
  "part_count": 0,
  "production_download_authorized": false,
  "request_json_count": 4,
  "result": "Initial NCEP z500/t850 smoke tests passed for hindcast year 2000 and forecast year 2020. Production download remains blocked pending May 2023 member/date QC and final NCEP production policy.",
  "sha256_count": 4,
  "status": "passed",
  "summary_csv": "runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_summary.csv",
  "system": "2",
  "variables": [
    "z500",
    "t850"
  ],
  "years_checked": [
    "2000",
    "2020"
  ]
}```

### runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_summary.csv
```text
metadata_file,status,variable_key,year,month,leadtime_month,message_count,first_shortName,first_level,first_typeOfLevel,first_forecastMonth,first_stepRange,first_dataDate,first_dataTime,first_number
cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.metadata.json,downloaded,t850,2000,01,1,28,t,850,isobaricInhPa,1,744,20000101,0,0
cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.metadata.json,downloaded,t850,2020,01,1,124,t,850,isobaricInhPa,1,744,20200101,0,0
cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.metadata.json,downloaded,z500,2000,01,1,28,z,500,isobaricInhPa,1,744,20000101,0,0
cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.metadata.json,downloaded,z500,2020,01,1,124,z,500,isobaricInhPa,1,744,20200101,0,0
```

### runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json
```text
{
  "contains_20230522": false,
  "dataset": "seasonal-monthly-pressure-levels",
  "expected_full_window_message_count_if_31_dates": 124,
  "forecast_system": "CFSv2-v20110310",
  "interpretation": "Corrected nominal June 2023 NCEP z500 smoke test confirms that dataDate=20230522 is absent from the retrieved monthly_mean GRIB metadata. Production download remains blocked until final NCEP production policy is documented.",
  "leadtime_month": "1",
  "message_count": 120,
  "messages_for_20230522": 0,
  "month": "06",
  "observed_missing_message_count": 4,
  "originating_centre": "ncep",
  "production_download_authorized": false,
  "raw_smoke_root": "/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202306",
  "source_metadata_json": "/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202306/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__NH0_90.grib.metadata.json",
  "status": "passed",
  "system": "2",
  "unique_data_date_count": 30,
  "variable_key": "z500",
  "year": "2023"
}
```

### runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_summary.csv
```text
status,dataset,originating_centre,system,variable_key,year,month,leadtime_month,message_count,contains_20230522,messages_for_20230522,unique_data_date_count,expected_full_window_message_count_if_31_dates,observed_missing_message_count,production_download_authorized
passed,seasonal-monthly-pressure-levels,ncep,2,z500,2023,06,1,120,False,0,30,124,4,False
```

### runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md
```text
# NCEP CFSv2 G8-sensitive smoke test

## Scope
- Dataset: seasonal-monthly-pressure-levels
- Originating centre: ncep
- System: 2
- Forecast system: CFSv2-v20110310
- Variable: z500
- Pressure level: 500 hPa
- Year: 2023
- Nominal start month: 06
- Leadtime month: 1

## Result
- Status: passed
- GRIB metadata was readable with ecCodes.
- dataDate=20230522 was not present.
- messages_for_20230522 = 0.
- Total message_count = 120.
- The observed metadata is consistent with the documented G8 missing initialization-date issue.

## Repository interpretation
- This confirms the G8 caution for the corrected nominal June 2023 test case.
- This is not a production download.
- This does not authorize NCEP production download.
- Final NCEP production policy still needs to be documented before production.
```

## 9. Leadtime, nominal start, G8, NCEP, and production-block references in tracked docs
```text
docs/GIT_WORKFLOW.md:229:task/fix-z925-policy
docs/GIT_WORKFLOW.md:275:runs/2026-05-03_era5_z925_monthly_download/
docs/GIT_WORKFLOW.md:276:runs/2026-05-03_ecmwf_pressure_levels_hindcast_z500/
docs/GIT_WORKFLOW.md:367:leadtime
docs/GIT_WORKFLOW.md:752:c3s_ecmwf_hindcast_z500_2000_2016.grib
docs/DECISIONS.md:71:- The workflow labels t850, z500, z925, and z950 refer to official ERA5 monthly pressure-level products tracked in this repository.
docs/DECISIONS.md:75:- z925 refers to geopotential at the 925 hPa pressure level.
docs/DECISIONS.md:76:- z950 refers to geopotential at the 950 hPa pressure level.
docs/DECISIONS.md:77:- The z925 collection is the seasonal-aligned ERA5 supplement introduced because the monthly C3S seasonal pressure-level archive does not provide 950 hPa.
docs/DECISIONS.md:78:- The pre-existing z950 ERA5 collection is retained and not deleted.
docs/DECISIONS.md:123:## ERA5 monthly z925 alignment rule
docs/DECISIONS.md:124:- ERA5 monthly z925 has been added as a parallel aligned dataset for the seasonal pressure-level substitute.
docs/DECISIONS.md:125:- Existing ERA5 monthly z950 data, metadata, inventory, and historical QC outputs remain intact and must not be deleted by this task.
docs/DECISIONS.md:126:- ERA5 z925 is added for seasonal comparison alignment with the repository seasonal pressure-level substitute z925.
docs/DECISIONS.md:127:- z925 is tracked as an ERA5 monthly pressure-level product in this repository
docs/DECISIONS.md:128:- z925 is the seasonal-aligned ERA5 supplement
docs/DECISIONS.md:129:- z950 baseline is retained and not deleted
docs/DECISIONS.md:130:- the z925 download, inventory, QC extension, and main reintegration are complete
docs/DECISIONS.md:131:- ERA5 monthly structural and scientific sanity QC now include z925 explicitly
docs/DECISIONS.md:133:#### z950
docs/DECISIONS.md:134:- `z950` in this workflow is the raw ERA5 geopotential field, not geopotential height.
docs/DECISIONS.md:143:- The repository will request ECMWF monthly seasonal data using system=51 for both project hindcasts (2000-2016) and project forecasts (2017-2025).
docs/DECISIONS.md:144:- For forecast years 2017-2025, this is a working repository assumption adopted for bootstrap execution and later validation; it is not yet a fully validated period-specific system manifest for scientific evaluation.
docs/DECISIONS.md:148:- The supervisor wording includes z950, but the monthly C3S pressure-level archive spans 925 hPa to 10 hPa.
docs/DECISIONS.md:149:- Therefore the repository seasonal pressure-level substitute is z925, not z950.
docs/DECISIONS.md:150:- The matching ERA5 monthly z925 dataset has been downloaded, inventoried, QC-verified, and merged into main.
docs/DECISIONS.md:151:- That z925 collection is the seasonal-aligned supplement and does not replace the already tracked ERA5 z950 baseline.
docs/DECISIONS.md:152:- Seasonal pressure-level verification can now use the merged ERA5 monthly z925 baseline on main.
docs/DECISIONS.md:160:- Seasonal monthly pressure-level products are monthly statistics derived from subdaily forecast data.
docs/DECISIONS.md:161:- These products are probabilistic seasonal forecast products, not deterministic weather forecasts.
docs/DECISIONS.md:163:- Hindcasts/reforecasts are required for bias estimation, anomaly construction, and forecast skill assessment.
docs/DECISIONS.md:166:- NCEP CFSv2 production download is blocked until smoke tests verify system=2 coverage, member counts, nominal start handling, and leadtime metadata.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:1:# NCEP CFSv2 activation review
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:4:This document records the repository activation review for NCEP CFSv2 before any NCEP seasonal download is started.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:9:- C3S Knowledge Base: NCEP Forecast System
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:10:- C3S Knowledge Base: Description of CFSv2-v20110310 C3S contribution
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:14:- C3S Knowledge Base: Recommendations and efficiency tips for C3S seasonal forecast datasets
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:20:- z925: geopotential at 925 hPa
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:24:## NCEP system mapping
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:25:- Provider: NCEP
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:26:- Forecast system: CFSv2-v20110310
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:29:- Forecast model: NCEP Global Forecast System coupled to GFDL MOM4 ocean model
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:36:NCEP must not be treated as operationally identical to ECMWF.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:38:Documented NCEP characteristics:
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:47:NCEP smoke tests and QC must explicitly inspect member counts, initialization dates, nominal start month handling, and leadtime metadata.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:51:- hindcasts: 1993-2016
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:52:- forecasts: 2017 to present
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:54:The CFSv2 system-description page states:
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:55:- hindcast years: 1981-2010
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:58:Before production download, run NCEP smoke tests for representative project years and do not assume complete 2000-2016 coverage without CDS retrieval evidence.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:61:- hindcast: 2000
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:62:- hindcast: 2010
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:63:- hindcast: 2011
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:64:- hindcast: 2016
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:65:- forecast: 2017
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:66:- forecast: 2023
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:67:- forecast: 2025
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:69:## Known issues relevant to NCEP
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:70:- G8 caution: NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. Repository interpretation: this is not a blanket blocker for monthly_mean retrieval, but May 2023 forecast member/date handling must be explicitly checked during NCEP QC before using NCEP in derived products or multi-model analysis.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:72:Monthly statistics and anomalies for some NCEP CFSv2 hindcast and forecast dates were temporarily unavailable in 2019.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:77:Missing members affected NCEP CFSv2 high-frequency daily/subdaily datasets.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:79:Repository action: not a blocker for monthly pressure-level downloads, but warn if daily/subdaily NCEP data are later activated.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:82:NCEP CFSv2 surface solar radiation variables were swapped for affected start dates.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:83:Repository action: not relevant to current z500, t850, z925 workflow. Exclude or re-review if radiation variables are later activated.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:85:### G8
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:86:NCEP system=2 forecast data for 2023-05-22 are unavailable because all four members initialized on that date were not correctly transmitted.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:87:Repository action: warn. Forecast May 2023 member counts must be explicitly checked during NCEP QC.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:89:Repository smoke-test evidence: corrected nominal June 2023 z500 monthly_mean retrieval recorded dataDate=20230522 as absent, messages_for_20230522=0, message_count=120, and observed_missing_message_count=4. This confirms the G8 missing initialization-date issue in retrieved monthly_mean GRIB metadata. Production download remains blocked until final NCEP production policy is documented.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:92:The repository pressure-level substitute remains z925, not z950.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:94:NCEP activation should use:
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:97:- z925
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:99:Do not introduce z950 for C3S seasonal pressure-level downloads.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:111:NCEP is not yet activated for production download.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:114:- create NCEP smoke-test script and run smoke tests for representative hindcast and forecast years.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:117:- grouped NCEP production download
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:118:- NCEP inclusion in multi-model analysis
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:119:- NCEP-derived products
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:121:## CDS quality-assurance implications for NCEP
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:122:The CDS quality information for seasonal monthly pressure-levels reinforces that NCEP must be activated cautiously.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:125:- Do not proceed directly to NCEP production download.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:126:- Verify NCEP system=2 request semantics using smoke tests first.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:127:- Verify member-count behaviour explicitly because NCEP uses lagged/daily ensemble generation.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:128:- Verify nominal start-month and leadtime metadata before grouped downloads.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:130:- Do not use experimental NetCDF for operational NCEP downloads.
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md:131:- Do not create NCEP anomaly, bias-corrected, or multi-model products until hindcast-based verification and bias strategy are documented.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:6:This review applies before activating NCEP CFSv2 production downloads and before any multi-model seasonal verification or product generation.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:15:Seasonal monthly pressure-level data are monthly statistics derived from subdaily seasonal forecast data.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:19:The data must not be interpreted as deterministic weather forecasts. Seasonal forecasts are probabilistic and are intended to provide information about potential deviations from normal climate conditions at monthly to seasonal timescales.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:21:## Bias and hindcast dependency
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:25:- Raw forecast fields must not be used as final scientific products without bias assessment.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:26:- Bias correction or at minimum bias-aware interpretation is required for forecast applications.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:27:- Hindcasts/reforecasts are required to estimate model climatology, systematic error, and forecast skill.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:39:- forecast system
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:49:## Multi-system and NCEP caution
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:50:The CDS quality information stresses that this is a complex multi-system forecast dataset with start-date and lead-time dimensions.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:56:- available hindcast/reforecast periods
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:60:Repository implications for NCEP:
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:61:- May 2023 NCEP forecast data require explicit member/date-handling QC because the documented G8 issue states that NCEP system=2 data initialized on 2023-05-22 are unavailable.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:62:- NCEP CFSv2 must not be treated as operationally identical to ECMWF.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:63:- NCEP member counts, nominal start dates, initialization-date handling, and lead-time metadata must be verified by smoke tests before production.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:64:- NCEP production download remains blocked until smoke tests confirm correct request semantics and metadata interpretation.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:86:9. hindcast-based verification
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:89:## NCEP activation rule
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:90:Before NCEP production download, the repository must complete and commit:
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:91:- NCEP smoke-test script
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:92:- representative hindcast smoke tests
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:93:- representative forecast smoke tests
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:95:- nominal start-date and leadtime interpretation notes
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:99:Recommended NCEP smoke-test years:
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:100:- hindcast: 2000
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:101:- hindcast: 2010
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:102:- hindcast: 2011
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:103:- hindcast: 2016
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:104:- forecast: 2017
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:105:- forecast: 2023
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:106:- forecast: 2025
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:109:NCEP is still a candidate centre under activation review.
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md:111:Production download is not authorized until smoke tests and metadata checks pass.
docs/RUNBOOK.md:147:  --leadtime-month 1 \
docs/RUNBOOK.md:150:  2>&1 | tee /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_hindcast_smoke.log
docs/RUNBOOK.md:154:- `runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_smoke/`
docs/RUNBOOK.md:162:  --leadtime-month 1 \
docs/RUNBOOK.md:165:  2>&1 | tee /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_forecast_smoke.log
docs/RUNBOOK.md:169:- `runs/2026-04-22_c3s_ecmwf_single_levels_forecast_smoke/`
docs/RUNBOOK.md:188:  --out-root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 \
docs/RUNBOOK.md:190:  > /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_hindcast_2000_2016.log 2>&1 &
docs/RUNBOOK.md:199:  --out-root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 \
docs/RUNBOOK.md:201:  > /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_forecast_2017_2025.log 2>&1 &
docs/RUNBOOK.md:208:tail -n 80 /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_hindcast_2000_2016.log
docs/RUNBOOK.md:209:tail -n 80 /home/fibi/projects/c3s_project_v2/logs/c3s_ecmwf_single_levels_forecast_2017_2025.log
docs/RUNBOOK.md:220:find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 -maxdepth 1 -type f -name "*.grib" | wc -l
docs/RUNBOOK.md:221:find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 -maxdepth 1 -type f -name "*.request.json" | wc -l
docs/RUNBOOK.md:222:find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 -maxdepth 1 -type f -name "*.sha256" | wc -l
docs/RUNBOOK.md:224:find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.grib" | wc -l
docs/RUNBOOK.md:225:find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.request.json" | wc -l
docs/RUNBOOK.md:226:find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.sha256" | wc -l
docs/RUNBOOK.md:227:find /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 -maxdepth 1 -type f -name "*.part" | wc -l
docs/RUNBOOK.md:234:  --root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016 \
docs/RUNBOOK.md:236:  --out /home/fibi/projects/c3s_project_v2/data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
docs/RUNBOOK.md:239:  --root /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025 \
docs/RUNBOOK.md:241:  --out /home/fibi/projects/c3s_project_v2/data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
docs/RUNBOOK.md:245:- `runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/`
docs/RUNBOOK.md:246:- `runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/`
docs/RUNBOOK.md:248:## ECMWF seasonal monthly pressure-level z925 smoke tests
docs/RUNBOOK.md:253:Hindcast z925 smoke metadata:
docs/RUNBOOK.md:254:- `runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_z925_smoke/`
docs/RUNBOOK.md:256:Forecast z925 smoke metadata:
docs/RUNBOOK.md:257:- `runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_z925_smoke/`
docs/RUNBOOK.md:273:- z925
docs/RUNBOOK.md:282:- data/inventory/c3s_ecmwf_pressure_levels_hindcast_2000_2016.csv
docs/RUNBOOK.md:283:- data/inventory/c3s_ecmwf_pressure_levels_forecast_2017_2025.csv
docs/RUNBOOK.md:286:- runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_2000_2016/
docs/RUNBOOK.md:287:- runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_2017_2025/
docs/RUNBOOK.md:291:- Hindcast and forecast production requests must remain separated operationally.
docs/RUNBOOK.md:294:- The ERA5 monthly z925 dataset for 2000-2025 has been downloaded, inventoried, included in structural and scientific sanity QC, and merged into main.
docs/HANDOFF.md:59:- The ERA5 monthly z925 supplement for 2000-2025 is complete and merged into main.
docs/HANDOFF.md:60:- The ERA5 monthly z925 inventory snapshot is tracked on main.
docs/HANDOFF.md:61:- The ERA5 monthly QC workflow now includes z925 explicitly.
docs/HANDOFF.md:62:- ERA5 monthly structural and scientific sanity QC passed for tp, t2m, ws10m, z500, t850, z925, and z950.
docs/HANDOFF.md:67:- For project forecast years 2017-2025, the use of ECMWF system 51 is currently a working repository assumption for bootstrap execution and later validation.
docs/HANDOFF.md:68:- That ECMWF system-51 bootstrap assumption passed the initial single-level smoke test for the first project forecast year 2017.
docs/HANDOFF.md:69:- The ECMWF single-level hindcast path also passed the initial smoke test for project year 2000.
docs/HANDOFF.md:70:- ECMWF seasonal monthly pressure-level z925 smoke tests passed for project hindcast year 2000 and first project forecast year 2017.
docs/HANDOFF.md:73:- The official grouped production downloader is tracked at scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py.
docs/HANDOFF.md:74:- Grouped hindcast download metadata is tracked under:
docs/HANDOFF.md:75:  - runs/2026-04-22_c3s_ecmwf_single_levels_hindcast_2000_2016/
docs/HANDOFF.md:76:- Grouped forecast download metadata is tracked under:
docs/HANDOFF.md:77:  - runs/2026-04-22_c3s_ecmwf_single_levels_forecast_2017_2025/
docs/HANDOFF.md:79:  - /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/hindcast_2000_2016
docs/HANDOFF.md:80:  - /mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51/forecast_2017_2025
docs/HANDOFF.md:85:- main contains the ERA5 z925 supplement and z925 QC extension commits after reintegration.
docs/HANDOFF.md:86:- task/era5-z925 has been reintegrated into main for the ERA5 z925 supplement and QC extension.
docs/HANDOFF.md:87:- Seasonal pressure-level work has begun on the z925-based pressure-level track.
docs/HANDOFF.md:88:- The repository seasonal pressure-level substitute is z925, not z950.
docs/HANDOFF.md:89:- Matching ERA5 monthly z925 has been downloaded, inventoried, and included in ERA5 monthly QC before seasonal pressure-level verification begins.
docs/HANDOFF.md:92:- ECMWF seasonal monthly pressure-level production completed successfully for hindcast 2000-2016 and forecast 2017-2025.
docs/HANDOFF.md:93:- ECMWF pressure-level inventory snapshots were created for z500, t850, and z925.
docs/HANDOFF.md:95:- Seasonal hindcasts and forecasts are requested separately.
docs/HANDOFF.md:96:- Project seasonal hindcast target is 2000-2016.
docs/HANDOFF.md:97:- Project seasonal forecast target is 2017-2025.
docs/HANDOFF.md:100:- NCEP CFSv2 activation review has started; production download is blocked until smoke tests verify system=2 coverage and member handling.
docs/HANDOFF.md:101:- C3S seasonal pressure-level QA review is documented; NCEP production remains blocked until smoke tests verify system=2 coverage, member handling, and metadata semantics.
docs/HANDOFF.md:102:- NCEP May 2023 forecast requires explicit member/date-handling QC because documented system=2 data initialized on 2023-05-22 are unavailable.
docs/HANDOFF.md:103:- Initial NCEP CFSv2 pressure-level smoke tests passed for z500 and t850 for hindcast year 2000 and forecast year 2020; production download remains blocked.
docs/HANDOFF.md:104:- Corrected NCEP G8-sensitive smoke test for nominal June 2023 z500 confirmed that dataDate=20230522 is absent; message_count=120 instead of the expected 124 for a complete 31-date lagged window.
docs/HANDOFF.md:107:1. Decide and document final NCEP production-download policy using the committed initial smoke-test metadata and G8 missing-date evidence.
docs/HANDOFF.md:108:2. Keep production NCEP download blocked until the final policy is committed.
docs/HANDOFF.md:109:3. Do not use NCEP May/June 2023 blindly in any derived product without explicit missing-date handling.
docs/ERA5_MONTHLY_COLLECTION_SUMMARY.md:22:- geopotential at 950 hPa (z950)
docs/ERA5_MONTHLY_COLLECTION_SUMMARY.md:40:- data/inventory/era5_z950_monthly_2000_2025.csv
docs/ERA5_MONTHLY_COLLECTION_SUMMARY.md:65:The next project phase is the seasonal forecast collection workflow.
docs/STATUS.md:14:- ERA5 monthly z925 supplement for 2000-2025 completed successfully on task/era5-z925
docs/STATUS.md:15:- ERA5 monthly z925 inventory snapshot is tracked
docs/STATUS.md:16:- ERA5 monthly QC workflow was extended to include z925 explicitly
docs/STATUS.md:17:- ERA5 monthly structural QC passed for tp, t2m, ws10m, z500, t850, z925, and z950
docs/STATUS.md:18:- ERA5 monthly scientific sanity QC passed for tp, t2m, ws10m, z500, t850, z925, and z950
docs/STATUS.md:19:- Seasonal forecast planning is active
docs/STATUS.md:22:- ECMWF seasonal monthly single-level smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
docs/STATUS.md:23:- ECMWF seasonal monthly pressure-level z925 smoke tests succeeded for project hindcast year 2000 and first project forecast year 2017
docs/STATUS.md:24:- The repository bootstrap assumption using ECMWF system 51 for forecast years 2017-2025 has passed initial smoke validation
docs/STATUS.md:25:- Grouped ECMWF monthly single-level hindcast download for 2000-2016 completed successfully
docs/STATUS.md:26:- Grouped ECMWF monthly single-level forecast download for 2017-2025 completed successfully
docs/STATUS.md:29:- Seasonal pressure-level work has begun on the z925-based pressure-level track
docs/STATUS.md:30:- A matching ERA5 monthly z925 dataset has been downloaded, inventoried, and included in the ERA5 monthly QC workflow before seasonal pressure-level verification
docs/STATUS.md:31:- Hindcast and forecast requests are handled separately operationally
docs/STATUS.md:32:- ECMWF seasonal monthly pressure-level production completed successfully for hindcast 2000-2016 and forecast 2017-2025
docs/STATUS.md:33:- ECMWF pressure-level inventory snapshots were created for z500, t850, and z925
docs/STATUS.md:43:- Documented ECMWF hindcast coverage for system 51 reaches 2016
docs/STATUS.md:44:- Project seasonal hindcast target is 2000-2016
docs/STATUS.md:45:- Project seasonal forecast target is 2017-2025
docs/STATUS.md:51:- Official grouped ECMWF seasonal monthly single-level production downloader is tracked
docs/STATUS.md:54:- No `.part` files remain in the grouped forecast directory
docs/STATUS.md:56:  - data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
docs/STATUS.md:57:  - data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
docs/STATUS.md:59:- main contains the ERA5 z925 supplement and z925 QC extension commits after reintegration
docs/STATUS.md:60:- task/era5-z925 has been reintegrated into main for the ERA5 z925 supplement and QC extension
docs/STATUS.md:67:- No blocker remains for the completed ECMWF pressure-level production download milestone
docs/STATUS.md:71:- NCEP CFSv2 activation review has started; production download is blocked until smoke tests verify system=2 coverage and member handling
docs/STATUS.md:72:- C3S seasonal pressure-level QA review is documented; NCEP production remains blocked until smoke tests verify system=2 coverage, member handling, and metadata semantics
docs/STATUS.md:73:- NCEP May 2023 forecast requires explicit member/date-handling QC because documented system=2 data initialized on 2023-05-22 are unavailable.
docs/STATUS.md:74:- Initial NCEP CFSv2 pressure-level smoke tests passed for z500 and t850 for hindcast year 2000 and forecast year 2020; production download remains blocked.
docs/STATUS.md:75:- Corrected NCEP G8-sensitive smoke test for nominal June 2023 z500 confirmed that dataDate=20230522 is absent; message_count=120 instead of the expected 124 for a complete 31-date lagged window.
docs/STATUS.md:78:1. Decide and document final NCEP production-download policy using the committed initial smoke-test metadata and G8 missing-date evidence
docs/STATUS.md:79:2. Keep production NCEP download blocked until the final policy is committed
docs/STATUS.md:80:3. Do not use NCEP May/June 2023 blindly in any derived product without explicit missing-date handling
docs/SEASONAL_KNOWN_ISSUES.md:11:- Deferred pressure-level variables: z500, t850, z925
docs/SEASONAL_KNOWN_ISSUES.md:20:- UK Met Office, DWD, CMCC, Météo-France, and NCEP remain deferred.
docs/SEASONAL_KNOWN_ISSUES.md:27:- For lagged monthly systems, nominal start date and real initialization date handling must be documented before scientific evaluation begins.
docs/SEASONAL_KNOWN_ISSUES.md:36:## NCEP CFSv2 activation review
docs/SEASONAL_KNOWN_ISSUES.md:37:- G8 caution for current workflow: NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. This is not treated as a blanket blocker for monthly_mean retrieval, but forecast May 2023 must receive explicit member/date-handling QC before any NCEP-derived product or multi-model analysis.
docs/SEASONAL_KNOWN_ISSUES.md:38:- Status: candidate centre under review; production download is not yet authorized.
docs/SEASONAL_KNOWN_ISSUES.md:39:- System: CFSv2-v20110310.
docs/SEASONAL_KNOWN_ISSUES.md:41:- Operational caution: NCEP uses lagged/daily initialization; member counts and nominal start handling must be verified by smoke tests before production.
docs/SEASONAL_KNOWN_ISSUES.md:42:- E4.a1/E4.a2: fixed historical CDS availability issues for NCEP monthly statistics/anomalies. Repository action: allow after standard verification.
docs/SEASONAL_KNOWN_ISSUES.md:43:- E7/E7b: fixed missing-member issues affecting NCEP daily/subdaily datasets. Repository action: warn if daily/subdaily NCEP data are later activated; not a direct blocker for current monthly pressure-level workflow.
docs/SEASONAL_KNOWN_ISSUES.md:44:- E6: NCEP surface solar radiation variables were swapped for affected dates. Repository action: exclude from current workflow; re-review only if radiation variables are activated.
docs/SEASONAL_KNOWN_ISSUES.md:45:- G8: NCEP system=2 forecast data for 2023-05-22 are unavailable because all four members initialized on that date were not correctly transmitted. Repository action: warn; forecast May 2023 member/date handling must be checked explicitly in NCEP QC. This is not a blanket blocker for monthly_mean retrieval unless retrieval evidence or member/date counts show an impact.
docs/SCOPE.md:6:- C3S seasonal forecast systems
docs/SCOPE.md:17:- z950
docs/SEASONAL_DOWNLOAD_POLICY.md:4:This policy governs seasonal forecast data collection from the Copernicus Climate Change Service (C3S) monthly seasonal archives.
docs/SEASONAL_DOWNLOAD_POLICY.md:17:- Project hindcast target: 2000-2016
docs/SEASONAL_DOWNLOAD_POLICY.md:18:- Project forecast target: 2017-2025
docs/SEASONAL_DOWNLOAD_POLICY.md:24:- same system must be used when pairing hindcasts and forecasts
docs/SEASONAL_DOWNLOAD_POLICY.md:25:- use of system=51 for forecast years 2017-2025 is currently a working repository assumption for bootstrap, not a final scientific manifest
docs/SEASONAL_DOWNLOAD_POLICY.md:36:- z925 -> geopotential at 925 hPa
docs/SEASONAL_DOWNLOAD_POLICY.md:37:- the supervisor wording z950 is retained as an external requirement note, but the operational monthly C3S implementation in this repository uses z925 instead
docs/SEASONAL_DOWNLOAD_POLICY.md:40:For operational collection in this repository, hindcasts and forecasts must be requested separately.
docs/SEASONAL_DOWNLOAD_POLICY.md:58:- z500 and z925 are raw geopotential fields, not geopotential height.
docs/SEASONAL_DOWNLOAD_POLICY.md:62:- target valid month must be derived programmatically from start month and leadtime month
docs/SEASONAL_DOWNLOAD_POLICY.md:71:## ERA5 z925 dependency
docs/SEASONAL_DOWNLOAD_POLICY.md:72:- before seasonal pressure-level verification begins, the matching ERA5 monthly z925 dataset must be downloaded, tracked, QC-verified, and merged into main
docs/SEASONAL_DOWNLOAD_POLICY.md:102:- Monthly pressure-level products are monthly statistics derived from subdaily seasonal forecast data.
docs/SEASONAL_DOWNLOAD_POLICY.md:104:- Bias correction or bias-aware interpretation is required for scientific applications and derived forecast products.
docs/SEASONAL_DOWNLOAD_POLICY.md:105:- Hindcasts/reforecasts are required for model climatology, anomaly construction, and verification.
docs/SEASONAL_DOWNLOAD_POLICY.md:107:- Experimental NetCDF is not authorized for operational seasonal download workflows without a separate documented validation.
docs/SEASONAL_DOWNLOAD_POLICY.md:108:- Differences between forecast systems in grid, ensemble generation, start-date handling, leadtime metadata, and hindcast availability must be checked before a new centre is activated.
docs/qc/ERA5_MONTHLY_QC_REPORT.md:5:- Datasets: tp, t2m, ws10m, z500, t850, z925, z950
docs/qc/ERA5_MONTHLY_QC_REPORT.md:12:- Nonnegative domain-mean values for tp, ws10m, z500, z925, and z950
docs/qc/ERA5_MONTHLY_QC_REPORT.md:25:| z925 | m**2 s**-2 | 312 | 2000-01 | 2025-12 | 7574.433809 | 7470.136535 | 7656.007272 | 4344.480469 | 9217.265625 | 70.294097 | True |
docs/qc/ERA5_MONTHLY_QC_REPORT.md:26:| z950 | m**2 s**-2 | 312 | 2000-01 | 2025-12 | 5373.445341 | 5274.677740 | 5461.156339 | 2271.658447 | 7248.177734 | 69.884742 | True |
docs/qc/ERA5_MONTHLY_QC_REPORT.md:50:### z925
docs/qc/ERA5_MONTHLY_QC_REPORT.md:51:- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/z925_domain_mean_timeseries.png`
docs/qc/ERA5_MONTHLY_QC_REPORT.md:52:- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/z925_monthly_climatology.png`
docs/qc/ERA5_MONTHLY_QC_REPORT.md:54:### z950
docs/qc/ERA5_MONTHLY_QC_REPORT.md:55:- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/z950_domain_mean_timeseries.png`
docs/qc/ERA5_MONTHLY_QC_REPORT.md:56:- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/z950_monthly_climatology.png`
configs/datasets/c3s_seasonal_variables.yml:37:  z925:
configs/datasets/c3s_seasonal_variables.yml:43:    note: seasonal pressure-level substitute for the supervisor wording z950; matching ERA5 monthly z925 has been downloaded, tracked, QC-verified, and merged into main
configs/datasets/c3s_seasonal_variables.yml:46:  supervisor_original_pressure_level_wording: z950
configs/datasets/c3s_seasonal_variables.yml:47:  repository_operational_pressure_level_substitute: z925
configs/datasets/c3s_seasonal_systems.yml:8:    hindcast_production: fixed
configs/datasets/c3s_seasonal_systems.yml:9:    documented_hindcast_year_start: 1981
configs/datasets/c3s_seasonal_systems.yml:10:    documented_hindcast_year_end: 2016
configs/datasets/c3s_seasonal_systems.yml:11:    project_hindcast_year_start: 2000
configs/datasets/c3s_seasonal_systems.yml:12:    project_hindcast_year_end: 2016
configs/datasets/c3s_seasonal_systems.yml:13:    project_forecast_year_start: 2017
configs/datasets/c3s_seasonal_systems.yml:14:    project_forecast_year_end: 2025
configs/datasets/c3s_seasonal_systems.yml:15:    hindcast_member_count: 25
configs/datasets/c3s_seasonal_systems.yml:16:    forecast_member_count: 51
configs/datasets/c3s_seasonal_systems.yml:17:    bootstrap_assumption_forecast_system_2017_2025: true
configs/datasets/c3s_seasonal_systems.yml:18:    bootstrap_assumption_note: "Repository bootstrap proceeds by requesting ECMWF system 51 for forecast years 2017-2025. This is a working repository assumption to be checked by smoke tests and first production retrievals. A period-specific forecast-system manifest may still be required later for scientific evaluation."
runs/2026-05-08_ncep_pressure_levels_smoke_plan/command.txt:2:Next operational step is to write or revise the NCEP smoke-test script so that it tests z500 and t850 first, not z925.
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:1:# NCEP CFSv2 pressure-level smoke-test plan
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:4:This run metadata records the safe pre-production smoke-test plan for NCEP CFSv2 pressure-level data.
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:9:- Forecast system: CFSv2-v20110310
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:15:NCEP production download is not authorized yet.
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:21:## Do not use for NCEP pressure-level activation smoke tests
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:22:- z925
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:24:- year=2017 as the first forecast smoke-test year
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:28:- system=2 request semantics
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:29:- available hindcast years and forecast years
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:31:- nominal start-month handling
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:32:- leadtime_month metadata
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:34:- May 2023 G8 caution handling
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:37:## May 2023 G8 caution
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:38:The documented G8 issue states that NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted.
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:43:- NCEP-derived products and multi-model analysis must not use May 2023 blindly.
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:48:Recommended first hindcast smoke tests:
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:49:- year=2000, month=01, leadtime_month=1, z500
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:50:- year=2000, month=01, leadtime_month=1, t850
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:52:Recommended first forecast smoke tests:
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:53:- year=2020 or 2021, month=01, leadtime_month=1, z500
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:54:- year=2020 or 2021, month=01, leadtime_month=1, t850
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:57:- year=2023, month=05, leadtime_month=1, z500
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:58:- year=2023, month=05, leadtime_month=1, t850
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:61:- grouped NCEP production download
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:62:- NCEP inclusion in multi-model analysis
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md:63:- NCEP-derived products
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:6:  "forecast_system": "CFSv2-v20110310",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:7:  "purpose": "pre-production NCEP pressure-level smoke-test planning",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:8:  "production_download_authorized": false,
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:10:  "unsafe_first_targets": ["z925", "pressure_level=925", "year=2017 as first forecast smoke-test year"],
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:12:    "system=2 request semantics",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:13:    "hindcast availability",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:14:    "forecast availability",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:16:    "nominal start-month handling",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:17:    "leadtime_month metadata",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:19:    "May 2023 G8 caution handling",
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json:22:  "may_2023_g8_caution": "NCEP system=2 data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. This is not a blanket blocker for monthly_mean retrieval, but May 2023 must receive explicit member/date-handling QC."
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_summary.csv:1:metadata_file,status,variable_key,year,month,leadtime_month,message_count,first_shortName,first_level,first_typeOfLevel,first_forecastMonth,first_stepRange,first_dataDate,first_dataTime,first_number
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:16:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:30:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:44:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:58:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:72:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:86:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:100:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:114:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:128:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:142:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:156:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:170:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:184:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:198:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:212:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:226:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:240:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:254:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:268:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:282:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:296:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:310:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:324:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:338:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:352:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:366:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:380:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:394:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:404:    "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:431:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:445:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:459:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:473:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:487:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:501:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:515:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:529:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:543:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:557:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:571:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:585:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:599:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:613:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:627:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:641:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:655:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:669:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:683:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:697:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:711:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:725:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:739:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:753:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:767:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:781:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:795:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:809:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:823:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:837:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:847:    "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:874:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:888:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:902:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:916:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:930:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:944:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:958:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:972:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:986:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1000:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1014:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1028:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1042:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1056:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1070:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1084:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1098:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1112:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1126:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1140:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1154:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1168:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1182:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1196:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1210:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1224:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1238:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1252:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1262:    "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1289:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1303:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1317:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1331:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1345:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1359:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1373:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1387:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1401:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1415:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1429:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1443:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1457:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1471:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1485:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1499:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1513:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1527:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1541:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1555:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1569:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1583:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1597:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1611:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1625:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1639:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1653:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1667:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1681:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1695:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json:1705:    "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/command.txt:1:NCEP z500/t850 smoke tests were run from:
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:1:# NCEP CFSv2 pressure-level z500/t850 smoke tests
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:4:This run records lightweight metadata for successful NCEP CFSv2 pressure-level smoke tests.
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:10:- Forecast system: CFSv2-v20110310
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:15:- z500, year 2000, month 01, leadtime_month 1
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:16:- t850, year 2000, month 01, leadtime_month 1
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:17:- z500, year 2020, month 01, leadtime_month 1
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:18:- t850, year 2020, month 01, leadtime_month 1
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:24:Production download is still not authorized.
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:28:- NCEP forecast-year availability must be finalized from retrieval evidence.
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md:29:- z925 must not be used for NCEP unless separately verified.
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/status.json:5:  "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/status.json:10:  "production_download_authorized": false,
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/status.json:12:  "result": "Initial NCEP z500/t850 smoke tests passed for hindcast year 2000 and forecast year 2020. Production download remains blocked pending May 2023 member/date QC and final NCEP production policy.",
runs/2026-05-11_ncep_pressure_levels_g8_202306/command.txt:7:No production download was started by this metadata-recording step.
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_summary.csv:1:status,dataset,originating_centre,system,variable_key,year,month,leadtime_month,message_count,contains_20230522,messages_for_20230522,unique_data_date_count,expected_full_window_message_count_if_31_dates,observed_missing_message_count,production_download_authorized
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:1:# NCEP CFSv2 G8-sensitive smoke test
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:7:- Forecast system: CFSv2-v20110310
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:17:- dataDate=20230522 was not present.
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:18:- messages_for_20230522 = 0.
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:20:- The observed metadata is consistent with the documented G8 missing initialization-date issue.
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:23:- This confirms the G8 caution for the corrected nominal June 2023 test case.
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:24:- This is not a production download.
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:25:- This does not authorize NCEP production download.
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md:26:- Final NCEP production policy still needs to be documented before production.
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:160:      "contains_20230522": false,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:318:      "messages_for_20230522": 0,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:326:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:340:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:354:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:368:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:382:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:396:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:410:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:424:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:438:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:452:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:466:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:480:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:494:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:508:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:522:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:536:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:550:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:564:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:578:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:592:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:606:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:620:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:634:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:648:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:662:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:676:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:690:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:704:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:718:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:732:          "forecastMonth": 1,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:896:    "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:910:    "contains_20230522": false,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:913:    "forecast_system": "CFSv2-v20110310",
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:914:    "interpretation": "Corrected nominal June 2023 NCEP z500 smoke test confirms that dataDate=20230522 is absent from the retrieved monthly_mean GRIB metadata. Production download remains blocked until final NCEP production policy is documented.",
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:915:    "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:917:    "messages_for_20230522": 0,
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json:921:    "production_download_authorized": false,
runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json:2:  "contains_20230522": false,
runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json:5:  "forecast_system": "CFSv2-v20110310",
runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json:6:  "interpretation": "Corrected nominal June 2023 NCEP z500 smoke test confirms that dataDate=20230522 is absent from the retrieved monthly_mean GRIB metadata. Production download remains blocked until final NCEP production policy is documented.",
runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json:7:  "leadtime_month": "1",
runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json:9:  "messages_for_20230522": 0,
runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json:13:  "production_download_authorized": false,
```

## 10. Tracked files
```text
.gitignore
README.md
configs/datasets/c3s_seasonal_systems.yml
configs/datasets/c3s_seasonal_variables.yml
configs/paths/paths.example.yml
data/inventory/c3s_ecmwf_pressure_levels_forecast_2017_2025.csv
data/inventory/c3s_ecmwf_pressure_levels_hindcast_2000_2016.csv
data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv
data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv
data/inventory/era5_t2m_monthly_2000_2025.csv
data/inventory/era5_t850_monthly_2000_2025.csv
data/inventory/era5_tp_monthly_2000_2025.csv
data/inventory/era5_ws10m_monthly_2000_2025.csv
data/inventory/era5_z500_monthly_2000_2025.csv
data/inventory/era5_z925_monthly_2000_2025.csv
data/inventory/era5_z950_monthly_2000_2025.csv
docs/CHATGPT_REENTRY_PROTOCOL.md
docs/DECISIONS.md
docs/ERA5_MONTHLY_COLLECTION_SUMMARY.md
docs/GIT_WORKFLOW.md
docs/HANDOFF.md
docs/RUNBOOK.md
docs/SCOPE.md
docs/SEASONAL_DOWNLOAD_POLICY.md
docs/SEASONAL_KNOWN_ISSUES.md
docs/STATUS.md
docs/qc/ERA5_MONTHLY_QC_REPORT.md
docs/seasonal/C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md
docs/seasonal/NCEP_CFSV2_ACTIVATION_REVIEW.md
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
runs/2026-04-17_era5_monthly_qc_full/plots/z925_domain_mean_timeseries.png
runs/2026-04-17_era5_monthly_qc_full/plots/z925_monthly_climatology.png
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
runs/2026-04-28_era5_z925_monthly_2000_2025/command.txt
runs/2026-04-28_era5_z925_monthly_2000_2025/run.md
runs/2026-04-28_era5_z925_monthly_2000_2025/status.json
runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_2017_2025/command.txt
runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_2017_2025/run.md
runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_2017_2025/status.json
runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_z925_smoke/command.txt
runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_z925_smoke/run.md
runs/2026-05-01_c3s_ecmwf_pressure_levels_forecast_z925_smoke/status.json
runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_2000_2016/command.txt
runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_2000_2016/run.md
runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_2000_2016/status.json
runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_z925_smoke/command.txt
runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_z925_smoke/run.md
runs/2026-05-01_c3s_ecmwf_pressure_levels_hindcast_z925_smoke/status.json
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/before_all_pressure_level_files.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/canonical_grib_files_after.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/canonical_grib_files_before.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/moved_noncanonical_files.tsv
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/noncanonical_files_to_move.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/quarantined_noncanonical_files.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/run.md
runs/2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming/status.json
runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/command.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/open_qc_details.json
runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/open_qc_summary.csv
runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/run.md
runs/2026-05-04_c3s_ecmwf_pressure_levels_open_qc/status.json
runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/command.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/run.md
runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/scientific_sanity_details.json
runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/scientific_sanity_summary.csv
runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc/status.json
runs/2026-05-04_c3s_ecmwf_pressure_levels_structure_qc/forecast_grib_files.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_structure_qc/forecast_relative_grib_files.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_structure_qc/hindcast_grib_files.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_structure_qc/hindcast_relative_grib_files.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_structure_qc/qc_report.txt
runs/2026-05-04_c3s_ecmwf_pressure_levels_structure_qc/run.md
runs/2026-05-04_c3s_ecmwf_pressure_levels_structure_qc/status.json
runs/2026-05-08_ncep_pressure_levels_smoke_plan/command.txt
runs/2026-05-08_ncep_pressure_levels_smoke_plan/run.md
runs/2026-05-08_ncep_pressure_levels_smoke_plan/status.json
runs/2026-05-11_ncep_pressure_levels_g8_202306/command.txt
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_details.json
runs/2026-05-11_ncep_pressure_levels_g8_202306/g8_summary.csv
runs/2026-05-11_ncep_pressure_levels_g8_202306/run.md
runs/2026-05-11_ncep_pressure_levels_g8_202306/status.json
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/command.txt
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/run.md
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_details.json
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/smoke_summary.csv
runs/2026-05-11_ncep_pressure_levels_smoke_z500_t850/status.json
runs/README.md
runs/reentry/chatgpt_reentry_pack_20260429T170900Z_main.md
runs/reentry/chatgpt_reentry_pack_20260429T170900Z_main.md.sha256
runs/reentry/chatgpt_reentry_pack_20260429T171018Z_main.md
runs/reentry/chatgpt_reentry_pack_20260429T171018Z_main.md.sha256
runs/wsl_cds_netcheck_era5_small/command.txt
runs/wsl_cds_netcheck_era5_small/run.md
runs/wsl_cds_netcheck_era5_small/status.json
scripts/download/10_download_era5_tp_monthly_grib_cli.py
scripts/download/11_download_era5_t2m_monthly_grib_cli.py
scripts/download/12_download_era5_ws10m_monthly_grib_cli.py
scripts/download/13_download_era5_z500_monthly_grib_cli.py
scripts/download/14_download_era5_t850_monthly_grib_cli.py
scripts/download/15_download_era5_z950_monthly_grib_cli.py
scripts/download/16_download_era5_z925_monthly_grib_cli.py
scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py
scripts/download/21_download_c3s_ecmwf_pressure_levels_monthly_grib_cli.py
scripts/inventory/10_build_inventory_csv.py
scripts/make_chatgpt_reentry_pack.sh
scripts/netcheck/00_cds_netcheck_small_era5.py
scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py
scripts/netcheck/11_c3s_seasonal_ecmwf_pressure_levels_smoke.py
scripts/netcheck/12_c3s_seasonal_ncep_pressure_levels_smoke.py
scripts/qc/20_check_era5_collection_structure.py
scripts/qc/21_build_era5_monthly_sanity_summary.py
scripts/qc/22_check_c3s_ecmwf_pressure_levels_openability.py
scripts/qc/23_check_c3s_ecmwf_pressure_levels_scientific_sanity.py
```

## 11. Repository tree
```text
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
│   │   ├── c3s_ecmwf_pressure_levels_forecast_2017_2025.csv
│   │   ├── c3s_ecmwf_pressure_levels_hindcast_2000_2016.csv
│   │   ├── c3s_ecmwf_single_levels_forecast_2017_2025.csv
│   │   ├── c3s_ecmwf_single_levels_hindcast_2000_2016.csv
│   │   ├── era5_t2m_monthly_2000_2025.csv
│   │   ├── era5_t850_monthly_2000_2025.csv
│   │   ├── era5_tp_monthly_2000_2025.csv
│   │   ├── era5_ws10m_monthly_2000_2025.csv
│   │   ├── era5_z500_monthly_2000_2025.csv
│   │   ├── era5_z925_monthly_2000_2025.csv
│   │   └── era5_z950_monthly_2000_2025.csv
│   ├── processed
│   └── raw
├── docs
│   ├── CHATGPT_REENTRY_PROTOCOL.md
│   ├── DECISIONS.md
│   ├── ERA5_MONTHLY_COLLECTION_SUMMARY.md
│   ├── GIT_WORKFLOW.md
│   ├── HANDOFF.md
│   ├── RUNBOOK.md
│   ├── SCOPE.md
│   ├── SEASONAL_DOWNLOAD_POLICY.md
│   ├── SEASONAL_KNOWN_ISSUES.md
│   ├── STATUS.md
│   ├── qc
│   │   └── ERA5_MONTHLY_QC_REPORT.md
│   └── seasonal
│       ├── C3S_SEASONAL_PRESSURE_LEVELS_QA_REVIEW.md
│       └── NCEP_CFSV2_ACTIVATION_REVIEW.md
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
│   │   │   ├── z925_domain_mean_timeseries.png
│   │   │   ├── z925_monthly_climatology.png
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
│   ├── 2026-04-28_era5_z925_monthly_2000_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-01_c3s_ecmwf_pressure_levels_forecast_2017_2025
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-01_c3s_ecmwf_pressure_levels_forecast_z925_smoke
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-01_c3s_ecmwf_pressure_levels_hindcast_2000_2016
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-01_c3s_ecmwf_pressure_levels_hindcast_z925_smoke
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-04_c3s_ecmwf_pressure_levels_canonicalize_naming
│   │   ├── before_all_pressure_level_files.txt
│   │   ├── canonical_grib_files_after.txt
│   │   ├── canonical_grib_files_before.txt
│   │   ├── moved_noncanonical_files.tsv
│   │   ├── noncanonical_files_to_move.txt
│   │   ├── quarantined_noncanonical_files.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-04_c3s_ecmwf_pressure_levels_open_qc
│   │   ├── command.txt
│   │   ├── open_qc_details.json
│   │   ├── open_qc_summary.csv
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc
│   │   ├── command.txt
│   │   ├── run.md
│   │   ├── scientific_sanity_details.json
│   │   ├── scientific_sanity_summary.csv
│   │   └── status.json
│   ├── 2026-05-04_c3s_ecmwf_pressure_levels_structure_qc
│   │   ├── forecast_grib_files.txt
│   │   ├── forecast_relative_grib_files.txt
│   │   ├── hindcast_grib_files.txt
│   │   ├── hindcast_relative_grib_files.txt
│   │   ├── qc_report.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-08_ncep_pressure_levels_smoke_plan
│   │   ├── command.txt
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-11_ncep_pressure_levels_g8_202306
│   │   ├── command.txt
│   │   ├── g8_details.json
│   │   ├── g8_summary.csv
│   │   ├── run.md
│   │   └── status.json
│   ├── 2026-05-11_ncep_pressure_levels_smoke_z500_t850
│   │   ├── command.txt
│   │   ├── run.md
│   │   ├── smoke_details.json
│   │   ├── smoke_summary.csv
│   │   └── status.json
│   ├── 2026-05-11_repository_state_review_after_ncep_g8
│   │   └── report.md
│   ├── README.md
│   ├── reentry
│   │   ├── chatgpt_reentry_pack_20260429T170900Z_main.md
│   │   ├── chatgpt_reentry_pack_20260429T170900Z_main.md.sha256
│   │   ├── chatgpt_reentry_pack_20260429T171018Z_main.md
│   │   └── chatgpt_reentry_pack_20260429T171018Z_main.md.sha256
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
    │   ├── 16_download_era5_z925_monthly_grib_cli.py
    │   ├── 20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py
    │   └── 21_download_c3s_ecmwf_pressure_levels_monthly_grib_cli.py
    ├── inspect
    ├── inventory
    │   └── 10_build_inventory_csv.py
    ├── make_chatgpt_reentry_pack.sh
    ├── netcheck
    │   ├── 00_cds_netcheck_small_era5.py
    │   ├── 10_c3s_seasonal_ecmwf_single_levels_smoke.py
    │   ├── 11_c3s_seasonal_ecmwf_pressure_levels_smoke.py
    │   └── 12_c3s_seasonal_ncep_pressure_levels_smoke.py
    ├── qc
    │   ├── 20_check_era5_collection_structure.py
    │   ├── 21_build_era5_monthly_sanity_summary.py
    │   ├── 22_check_c3s_ecmwf_pressure_levels_openability.py
    │   └── 23_check_c3s_ecmwf_pressure_levels_scientific_sanity.py
    └── transfer

47 directories, 163 files
```

## 12. Inventory snapshots
```text
data/inventory/c3s_ecmwf_pressure_levels_forecast_2017_2025.csv  17779 bytes
data/inventory/c3s_ecmwf_pressure_levels_hindcast_2000_2016.csv  17779 bytes
data/inventory/c3s_ecmwf_single_levels_forecast_2017_2025.csv  6031 bytes
data/inventory/c3s_ecmwf_single_levels_hindcast_2000_2016.csv  6031 bytes
data/inventory/era5_t2m_monthly_2000_2025.csv  118939 bytes
data/inventory/era5_t850_monthly_2000_2025.csv  122683 bytes
data/inventory/era5_tp_monthly_2000_2025.csv  121435 bytes
data/inventory/era5_ws10m_monthly_2000_2025.csv  120187 bytes
data/inventory/era5_z500_monthly_2000_2025.csv  123307 bytes
data/inventory/era5_z925_monthly_2000_2025.csv  123307 bytes
data/inventory/era5_z950_monthly_2000_2025.csv  123307 bytes
```

## 13. Scripts overview
```text
scripts/download/10_download_era5_tp_monthly_grib_cli.py  7017 bytes
scripts/download/11_download_era5_t2m_monthly_grib_cli.py  7008 bytes
scripts/download/12_download_era5_ws10m_monthly_grib_cli.py  7010 bytes
scripts/download/13_download_era5_z500_monthly_grib_cli.py  7082 bytes
scripts/download/14_download_era5_t850_monthly_grib_cli.py  7080 bytes
scripts/download/15_download_era5_z950_monthly_grib_cli.py  7082 bytes
scripts/download/16_download_era5_z925_monthly_grib_cli.py  7161 bytes
scripts/download/20_download_c3s_ecmwf_single_levels_monthly_grib_cli.py  5245 bytes
scripts/download/21_download_c3s_ecmwf_pressure_levels_monthly_grib_cli.py  6215 bytes
scripts/download/__pycache__/21_download_c3s_ecmwf_pressure_levels_monthly_grib_cli.cpython-311.pyc  10667 bytes
scripts/inspect/__pycache__/30_report_c3s_ensemble_members.cpython-311.pyc  21464 bytes
scripts/inventory/10_build_inventory_csv.py  1713 bytes
scripts/make_chatgpt_reentry_pack.sh  5259 bytes
scripts/netcheck/00_cds_netcheck_small_era5.py  4127 bytes
scripts/netcheck/10_c3s_seasonal_ecmwf_single_levels_smoke.py  2255 bytes
scripts/netcheck/11_c3s_seasonal_ecmwf_pressure_levels_smoke.py  2413 bytes
scripts/netcheck/12_c3s_seasonal_ncep_pressure_levels_smoke.py  6801 bytes
scripts/netcheck/__pycache__/11_c3s_seasonal_ecmwf_pressure_levels_smoke.cpython-311.pyc  4687 bytes
scripts/netcheck/__pycache__/12_c3s_seasonal_ncep_pressure_levels_smoke.cpython-311.pyc  9881 bytes
scripts/netcheck/__pycache__/12_c3s_seasonal_ncep_pressure_levels_smoke.cpython-313.pyc  7751 bytes
scripts/qc/20_check_era5_collection_structure.py  8877 bytes
scripts/qc/21_build_era5_monthly_sanity_summary.py  15622 bytes
scripts/qc/22_check_c3s_ecmwf_pressure_levels_openability.py  10456 bytes
scripts/qc/23_check_c3s_ecmwf_pressure_levels_scientific_sanity.py  13290 bytes
scripts/qc/__pycache__/22_check_c3s_ecmwf_pressure_levels_openability.cpython-311.pyc  14317 bytes
scripts/qc/__pycache__/23_check_c3s_ecmwf_pressure_levels_scientific_sanity.cpython-311.pyc  17287 bytes
```

## 14. Raw-data count checks outside Git
```text
PATH=/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2
GRIB=7
REQUEST_JSON=9
SHA256=7
METADATA_JSON=7
PART=0
42M	/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2

PATH=/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ecmwf/system_51
GRIB=146
REQUEST_JSON=146
SHA256=146
METADATA_JSON=0
PART=0
24G	/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ecmwf/system_51

PATH=/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51
GRIB=26
REQUEST_JSON=26
SHA256=26
METADATA_JSON=0
PART=0
12G	/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-single-levels/ecmwf/system_51

PATH=/mnt/e/last-aticol/data/raw/era5
GRIB=2184
REQUEST_JSON=2184
SHA256=2184
METADATA_JSON=0
PART=0
154M	/mnt/e/last-aticol/data/raw/era5

```

## 15. NCEP raw smoke files outside Git
```text
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z925__925hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.request.json  671 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z925__925hPa__monthly_mean__2017__st01__lead1__NH0_90.grib.request.json  671 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202305/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st05__lead1__NH0_90.grib  7797120 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202305/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st05__lead1__NH0_90.grib.metadata.json  18469 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202305/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st05__lead1__NH0_90.grib.request.json  979 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202305/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st05__lead1__NH0_90.grib.sha256  179 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202306/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__NH0_90.grib  7797120 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202306/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__NH0_90.grib.metadata.json  18469 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202306/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__NH0_90.grib.request.json  979 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_202306/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__NH0_90.grib.sha256  179 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_20260511/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__G8_check__NH0_90.grib  7797120 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_20260511/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__G8_check__NH0_90.grib.metadata.json  11273 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_20260511/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__G8_check__NH0_90.grib.request.json  991 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_g8_20260511/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2023__st06__lead1__G8_check__NH0_90.grib.sha256  189 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2000__st01__lead1__NH0_90.grib  1819328 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.metadata.json  10622 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.request.json  987 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.sha256  179 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2020__st01__lead1__NH0_90.grib  8057024 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.metadata.json  11261 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.request.json  987 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__t850__850hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.sha256  179 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2000__st01__lead1__NH0_90.grib  1819328 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.metadata.json  10622 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.request.json  988 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2000__st01__lead1__NH0_90.grib.sha256  179 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2020__st01__lead1__NH0_90.grib  8057024 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.metadata.json  11261 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.request.json  988 bytes
/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ncep/system_2/smoke_z500_t850_20260510/cds__c3s_seasonal__monthly-pressure-levels__ncep__s2__z500__500hPa__monthly_mean__2020__st01__lead1__NH0_90.grib.sha256  179 bytes
```

## 16. Git ignored files summary
```text
?? runs/2026-05-11_repository_state_review_after_ncep_g8/
!! logs/
!! scripts/download/__pycache__/
!! scripts/inspect/
!! scripts/netcheck/__pycache__/
!! scripts/qc/__pycache__/
```

## 17. Immediate analysis questions to answer after reading this report
```text
1. Is the working tree clean after this report file is created?
2. Is task/ncep-pressure-levels-smoke ready for a final NCEP policy decision, or is another smoke test needed?
3. Should NCEP production include z500 and t850 only, or also another available pressure-level target?
4. How should the confirmed 20230522 missing initialization date be handled in production inventory and downstream QC?
5. Should production requests avoid May/June 2023 until explicit masking/exclusion rules are implemented?
6. Should final production be grouped by month/year/variable or kept in smaller request batches because NCEP is lagged-start?
7. What exact repository files must be updated before production is authorized?
```
