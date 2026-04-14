# Decisions

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
