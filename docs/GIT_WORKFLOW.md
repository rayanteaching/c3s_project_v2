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
docs/refresh-status
configs/update-paths

Before merging:

git status must be clean unless the merge itself is being prepared.
docs/STATUS.md must be updated.
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
Use `AGENTS.md` as the project entry point, then read `docs/STATUS.md` and only the decision/config/run/QC material relevant to the current task.

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
Use AGENTS.md and docs/STATUS.md as the basis for continuation.
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


