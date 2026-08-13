# Handoff

## Current project-control layer
Architecture v1 is the active shared design baseline on `task/architecture-v1-handoff`.

Required first reads for continuation:
- `docs/ARCHITECTURE.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `docs/STATUS.md`
- `docs/DECISIONS.md`

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
- Nominal/actual initialization and lagged-ensemble horizon attribution are centre/system/product questions and remain open until verified.
- No universal hindcast/forecast split is current policy.
- No global z950 -> z925 substitution is current policy.
- Six centres are in scope: ECMWF, UKMO, DWD, CMCC, Meteo-France, NCEP.
- Manuscript v0.1 domains are NH, ROI, ROI_X4; exact geometries/masks require current approved evidence/configuration.
- Maximum-valid and common-case analyses are distinct required result modes.

## Legacy quarantine
Earlier ERA5/ECMWF/NCEP bootstrap work remains preserved in Git history, runs, inventories, scripts, and evidence notes. It may contain useful execution evidence or reusable code, but its scientific assumptions are not automatically current Architecture v1 policy.

In particular, do not inherit without revalidation:
- a universal 2000-2016 hindcast / 2017-2025 forecast split;
- a global z950 -> z925 substitution;
- fixed native lead 1-6 as H1-H6;
- ECMWF-specific bootstrap assumptions for other centres.

## Parallel-work policy
Centre workstreams and later metric workstreams may proceed in parallel only from pinned work packages. Each work package must identify base Git SHA, architecture/config/guardrail/decision context, allowed scope, required outputs, and QC. Workstreams may discover local evidence but may not silently change shared policy. Shared-policy issues return to CONTROL and pass an integration gate.

## Open scientific questions
Do not solve unresolved questions from memory or legacy code. Use `docs/OPEN_SCIENTIFIC_QUESTIONS.md`. Questions remain `OPEN — VERIFY WHEN REACHED` until the relevant centre/metric/method workstream has enough evidence and human approval.

## Human approval gates
Human approval is required before:
- commits intended as approved milestone closure;
- merges;
- production downloads;
- destructive operations;
- scientific-policy or interpretation changes;
- QC pass/fail milestone declarations.

## Re-entry workflow
Use the repository re-entry protocol and pack generator. Architecture v1 control files must be loaded before centre/system production or scientific-method decisions.

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

Deep audit is required for production downloads, merges, QC pass/fail declarations, policy/scientific-method changes, destructive work, or confused/stale state.

## Current milestone
- Architecture v1 core documents/configs are being integrated on `task/architecture-v1-handoff`.
- Base checkpoint before Architecture v1 work: `544a375c05d85331ff0e674a89494120d413794f`.
- NCEP integration commit `b574f26702163c424a5b605e414c1d992435642b` is already in main history; old instructions to merge NCEP are stale history.
- No new production download or calibration implementation is authorized by this milestone.

## Next safe action
1. Complete Architecture v1 migration of DECISIONS, seasonal policy, re-entry protocol, and generator.
2. Audit branch diff against `main`.
3. Validate re-entry/config syntax.
4. Obtain explicit human approval before merging Architecture v1 to `main`.
5. After integration, create centre-specific work packages for parallel verification.

## Standard session report
Before high-impact continuation provide:
- `git status --short --branch`
- `git branch -vv`
- `git log --oneline --decorate --graph -n 10`
- targeted diff/status evidence relevant to the task.

For production/QC/runtime work, also provide relevant logs, run metadata, inventory/checksum evidence, and environment state as required by the re-entry protocol.
