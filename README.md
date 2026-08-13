# c3s_project_v2

C3S seasonal forecast verification and calibration project with ERA5 reference data.

## Start here
For current project work, read Architecture v1 before legacy/bootstrap scripts or configs:
- `docs/ARCHITECTURE.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `docs/STATUS.md`
- `docs/HANDOFF.md`
- `docs/DECISIONS.md`
- `configs/datasets/CURRENT_CONFIGS.md`

## Current Architecture v1 configuration
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `configs/datasets/system_registry_v1.yml`
- `configs/datasets/variable_registry_v1.yml`

Legacy/bootstrap configs and scripts are preserved for audit/history but do not automatically define current scientific policy.

## Re-entry for ChatGPT/Codex work
Architecture v1 re-entry is GitHub-first and protocol-driven. Before high-impact work, verify the current remote task-branch SHA, `main` SHA, merge base, ahead/behind counts, and changed-file diff directly from GitHub, then read `docs/CHATGPT_REENTRY_PROTOCOL.md` and the current control files.

`scripts/make_chatgpt_reentry_pack_v2.sh` is retained as historical tooling but is not authoritative for current Architecture v1 re-entry or DEEP AUDIT because it does not prove the committed branch diff relative to current remote `main` and contains a machine-specific project path.

Do not use a generated local pack as a substitute for fresh remote GitHub state.

## Core principles
- Repository state is the durable system of record; chat memory is not project truth.
- `main` is approved current truth; task branches are candidate state.
- Unknown/conflicting required scientific facts fail closed.
- Do not propagate assumptions across centres without verification.
- Availability is not equivalent to scientific eligibility.
- Major scientific decisions require traceable evidence and human approval.
- Independent centre/metric workstreams may proceed in parallel only under pinned contracts and integration gates.
- Raw and processed large datasets are not tracked in Git.

## Main paths
- Project root: `~/projects/c3s_project_v2`
- Raw/processed data: external/local storage according to current path configuration
- Scripts: `scripts/`
- Configs: `configs/`
- Inventory: `data/inventory/`
- Runs: `runs/`
- Documentation: `docs/`
