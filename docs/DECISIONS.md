# Decisions

## Repository rules
Track:
- docs/
- configs/
- scripts/
- runs/
- data/inventory/

Do not track:
- data/raw/
- data/processed/
- logs/
- large binary datasets

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
