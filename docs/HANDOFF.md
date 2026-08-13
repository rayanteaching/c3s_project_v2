# Handoff

## Current project-control layer
Architecture v1 is the active shared design baseline on `task/architecture-v1-handoff`.

Required first reads for continuation:
- `docs/ARCHITECTURE.md`
- `docs/AI_COLLABORATION_SAFETY.md`
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

## AI collaboration safety
AI assistants are fallible agents, not project-truth sources. All AI-assisted work inherits `docs/AI_COLLABORATION_SAFETY.md`.

For high-impact work the assistant must preserve material user constraints, classify load-bearing claims by evidence state, verify important writes/results from the relevant system of record, and perform a separate contradiction/omission/unsupported-claim/authority-path review before claiming completion.

Known assistant/workflow incidents WF-001 through WF-005 are recorded in the safety layer. A newly discovered material assistant-caused failure keeps the affected high-impact action open until root cause, generalized prevention, durable repository encoding, and post-fix audit are complete.

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

Every AI-assisted workstream inherits the AI collaboration safety layer; local workstream convenience cannot weaken it.

## Open scientific questions
Do not solve unresolved questions from memory or legacy code. Use `docs/OPEN_SCIENTIFIC_QUESTIONS.md`. Questions remain `OPEN — VERIFY WHEN REACHED` until the relevant centre/metric/method workstream has enough evidence and human approval.

## Re-entry workflow
Architecture v1 re-entry is GitHub-first and protocol-driven. Use `docs/CHATGPT_REENTRY_PROTOCOL.md` and `docs/AI_COLLABORATION_SAFETY.md`.

For every DEEP-AUDIT objective, the first evidence must come from the current remote GitHub repository and establish:
- task-branch SHA;
- `main` SHA;
- merge base;
- ahead/behind counts;
- changed-file list and branch diff relative to `main`.

A local checkout, local remote-tracking branch, generated pack, or chat memory does not replace this fresh remote comparison.

The former `scripts/make_chatgpt_reentry_pack_v2.sh` is preserved in Git history only and is absent from the active tree. It is not an active Architecture v1 re-entry authority.

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
- The AI collaboration safety layer and generalized assistant guardrails are active on this branch.
- Re-entry authority is protocol-driven and remote-GitHub-first; the former v2 generator is historical/non-authoritative.
- Base checkpoint before Architecture v1 work: `544a375c05d85331ff0e674a89494120d413794f`.
- NCEP integration commit `b574f26702163c424a5b605e414c1d992435642b` is already in main history; old instructions to merge NCEP are stale history.
- No new production download or calibration implementation is authorized by this milestone.

## Next safe action
1. Audit the complete current remote branch diff against `main` after the AI collaboration safety integration.
2. Perform the mandatory adversarial second pass across all active control files.
3. Confirm no current authority path bypasses `docs/AI_COLLABORATION_SAFETY.md` and no active path treats re-entry v2 as authoritative.
4. Sync this branch to WSL only after the remote audit is clean.
5. Validate YAML and current scripts with short staged commands that leave the interactive shell open on failure.
6. Fix any audit/validation defect before merge.
7. Obtain explicit human approval before merging Architecture v1 to `main`.
8. After integration, create centre-specific work packages for parallel verification.

## Standard session report
Before high-impact continuation provide fresh remote GitHub evidence for the relevant branch/main comparison. After WSL synchronization, also provide as needed:
- `git status --short --branch`
- `git branch -vv`
- `git log --oneline --decorate --graph -n 10`
- targeted local runtime/diff/status evidence relevant to the task.

For production/QC/runtime work, also provide relevant logs, run metadata, inventory/checksum evidence, environment state, and assistant-safety constraint/evidence coverage as required by the re-entry protocol.

## Chat-quality safeguard
If a chat becomes long/confused enough that evidence, decisions, centre-specific facts, user constraints, or repository state may be mixed, stop before another high-impact decision, checkpoint in Git where appropriate, and start a fresh remote-GitHub-first Architecture v1 re-entry in a new chat.
