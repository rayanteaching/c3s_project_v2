# Handoff

## Current project-control layer
Architecture v1 is the active shared design baseline on `task/architecture-v1-handoff`.

Required first reads for continuation:
- `docs/ARCHITECTURE.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `configs/datasets/CURRENT_CONFIGS.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `configs/datasets/system_registry_v1.yml`
- `configs/datasets/variable_registry_v1.yml`
- `docs/STATUS.md`
- `docs/DECISIONS.md`
- `docs/CHATGPT_REENTRY_PROTOCOL.md`
- `docs/SEASONAL_DOWNLOAD_POLICY.md`

## Source of truth
The repository is the durable system of record, with truth state:
- `main` = approved current project truth;
- `task/*` = proposed/candidate state;
- tracked `runs/*` = evidence of what actually ran;
- historical/superseded material = valid history, not current policy;
- chat memory = temporary reasoning only.

If remembered chat context conflicts with repository evidence, use repository evidence. If current repository files conflict internally, stop and resolve the conflict rather than guessing.

## Current study semantics
- Study window = target/verifying years 2000-2025.
- Manuscript v0.1 target month = December.
- H1-H6 = one through six calendar months before target.
- Native C3S lead mapping is not global; verify per centre/system/product.
- Nominal/actual initialization and lagged-ensemble horizon attribution remain centre/system/product questions until verified.
- No universal hindcast/forecast split is current policy.
- No global z950 -> z925 substitution is current policy.
- Centres: ECMWF, UKMO, DWD, CMCC, Meteo-France, NCEP.
- Manuscript v0.1 domains: NH, ROI, ROI_X4; exact geometries/masks require current approved evidence/configuration.
- Maximum-valid and common-case analyses are distinct required result modes.

## Config precedence
Use `configs/datasets/CURRENT_CONFIGS.md`.

Current Architecture v1 configs/registries:
- `study_v0_1.yml`
- `guardrails_v1.yml`
- `system_registry_v1.yml`
- `variable_registry_v1.yml`

Legacy/bootstrap configs:
- `c3s_seasonal_systems.yml`
- `c3s_seasonal_variables.yml`

Legacy files remain evidence/history only and require revalidation before reuse.

## Parallel-work policy
Centre workstreams and later metric workstreams may proceed in parallel only from pinned work packages. Each work package must identify base Git SHA, architecture/config/guardrail/decision context, allowed scope, required outputs, and QC. Workstreams may discover local evidence but may not silently change shared policy. Shared-policy issues return to CONTROL and pass an integration gate.

## Open scientific questions
Do not solve unresolved questions from memory or legacy code. Use `docs/OPEN_SCIENTIFIC_QUESTIONS.md`. Questions remain `OPEN — VERIFY WHEN REACHED` until the relevant centre/metric/method workstream has enough evidence and human approval.

## Re-entry workflow
Architecture v1 re-entry is GitHub-first and protocol-driven. Use `docs/CHATGPT_REENTRY_PROTOCOL.md`.

For every DEEP-AUDIT objective, the first evidence must come from the current remote GitHub repository and establish:
- task-branch SHA;
- `main` SHA;
- merge base;
- ahead/behind counts;
- changed-file list and branch diff relative to `main`.

A local checkout, local remote-tracking branch, generated pack, or chat memory does not replace this fresh remote comparison.

`scripts/make_chatgpt_reentry_pack_v2.sh` is retained only as historical tooling and is not an active Architecture v1 re-entry authority. Do not use it to gate merge, production, QC milestones, policy/guardrail changes, scientific-method decisions, destructive work, or other DEEP-AUDIT objectives.

Deep audit is required for Architecture closure, production downloads, merges, QC pass/fail declarations, policy/guardrail or scientific-method changes, destructive work, and confused/stale/uncertain state.

## Human approval gates
Human approval is required before:
- milestone commits intended as approved project state;
- merges;
- production downloads;
- destructive operations;
- scientific-policy or interpretation changes;
- QC pass/fail milestone declarations.

## Current milestone
- Architecture v1 control documents/configs/registries are implemented on this branch.
- Re-entry authority is now protocol-driven and remote-GitHub-first; the v2 generator is historical/non-authoritative.
- Base checkpoint before Architecture v1 work: `544a375c05d85331ff0e674a89494120d413794f`.
- NCEP integration commit `b574f26702163c424a5b605e414c1d992435642b` is already in main history; old instructions to merge NCEP are stale history.
- No new production download or calibration implementation is authorized by this milestone.

## Next safe action
1. Audit the complete current remote branch diff against `main` after the re-entry safety corrections.
2. Confirm there is no remaining current-control reference that treats re-entry v2 as authoritative.
3. Sync this branch to WSL only after the remote audit is clean.
4. Validate YAML and current scripts with short staged commands that leave the interactive shell open on failure.
5. Fix any audit/validation defect before merge.
6. Obtain explicit human approval before merging Architecture v1 to `main`.
7. After integration, create centre-specific work packages for parallel verification.

## Standard session report
Before high-impact continuation provide fresh remote GitHub evidence for the relevant branch/main comparison. After WSL synchronization, also provide as needed:
- `git status --short --branch`
- `git branch -vv`
- `git log --oneline --decorate --graph -n 10`
- targeted local runtime/diff/status evidence relevant to the task.

For production/QC/runtime work, also provide relevant logs, run metadata, inventory/checksum evidence, and environment state as required by the re-entry protocol.

## Chat-quality safeguard
If a chat becomes long/confused enough that evidence, decisions, centre-specific facts, or repository state may be mixed, stop before another high-impact decision, checkpoint in Git where appropriate, and start a fresh remote-GitHub-first Architecture v1 re-entry in a new chat.
