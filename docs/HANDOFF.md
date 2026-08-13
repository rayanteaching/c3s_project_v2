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
- `main` = approved current project truth.
- `task/*` = candidate/proposed state.
- tracked run metadata = execution evidence.
- historical/superseded material = valid history, not current policy.
- chat memory and assistant statements = temporary reasoning only.

If current repository controls conflict, stop and resolve the conflict rather than guessing.

## AI collaboration safety
All AI-assisted work is governed by `docs/AI_COLLABORATION_SAFETY.md`.

High-impact work requires material-constraint coverage, evidence classification, post-action system-of-record verification, explicit coverage for critical negative claims, and a separate adversarial review before completion is claimed.

Known incidents WF-001 through WF-005 are encoded. New material assistant-caused failures keep the affected high-impact action open until root cause, generalized prevention, durable encoding, and post-fix audit are complete.

## Current study semantics
- Study window = target/verifying years 2000-2025.
- Manuscript v0.1 target month = December.
- H1-H6 = one through six calendar months before target.
- Native lead/init/verifying-period mapping is not global and must be verified per centre/system/product.
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

Legacy bootstrap configs remain history/evidence only and require Architecture v1 revalidation before reuse.

## Parallel work policy
Centre and later metric workstreams may proceed in parallel only from pinned work packages. Each package identifies base Git SHA, architecture/config/guardrail/decision context, scope, required evidence/outputs, and integration/QC requirements.

Workstreams may discover local evidence but may not silently change shared policy. Every AI-assisted workstream inherits the AI collaboration safety layer.

## Re-entry workflow
Re-entry is GitHub-first and protocol-driven through `docs/CHATGPT_REENTRY_PROTOCOL.md` and `docs/AI_COLLABORATION_SAFETY.md`.

Every DEEP AUDIT begins with fresh remote evidence for task-branch SHA, `main` SHA, merge base, ahead/behind, and branch diff. Local material or chat memory does not replace this evidence.

The former re-entry v2 generator is preserved in Git history only and is absent from the active tree.

## Human approval gates
Human approval is required before approved milestone adoption, merges, production downloads, destructive operations, scientific-policy/interpretation changes, and QC pass/fail milestone declarations.

## Current milestone
- Architecture v1 controls and registries are implemented on this branch.
- AI collaboration safety and generalized defense-in-depth assistant guardrails are active.
- The remote GitHub control-layer DEEP AUDIT after AI-safety integration is complete.
- WSL/runtime validation remains pending.
- The branch is not yet merge-ready.
- Base checkpoint before Architecture v1 work: `544a375c05d85331ff0e674a89494120d413794f`.
- No new production download or calibration implementation is authorized by this milestone.

## Next safe action
1. Synchronize the current remote task branch to WSL.
2. Validate active YAML/config state and repository state with short staged checks that leave the interactive shell open on failure.
3. Confirm the retired re-entry v2 generator is absent in the synchronized checkout.
4. Resolve any runtime/config defect before merge review.
5. Re-run fresh remote GitHub comparison after any validation-driven repository change.
6. Obtain explicit human approval before merging Architecture v1 to `main`.
7. After integration, create centre-specific work packages for parallel verification.

## Chat-quality safeguard
If a chat becomes long, stale, or confused enough that evidence, decisions, centre-specific facts, user constraints, or repository state may be mixed, stop before another high-impact decision and start a fresh remote-GitHub-first Architecture v1 re-entry.
