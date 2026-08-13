# Handoff

## Current project-control layer
Architecture v1 is the approved shared design baseline on `main`.

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

## Architecture v1 integration state
- Human approval for the Architecture v1 merge was given explicitly.
- Architecture v1 was fast-forward merged into `main`.
- Remote verification confirmed `main` at `077ec141f3442e8ec5abce4e11e56ce804764a89` and identical to `task/architecture-v1-handoff` at the time of verification.
- `task/day1-closure` exists only to correct post-merge state documentation and durably encode the newly discovered GitHub-write approval workflow failure before final Day-1 closure integration.
- No scientific archive fact, production policy, calibration method, variable substitution, lead mapping, or centre-specific availability decision is being changed by this closure patch.

## AI collaboration safety
All AI-assisted work is governed by `docs/AI_COLLABORATION_SAFETY.md`.

High-impact work requires material-constraint coverage, evidence classification, post-action system-of-record verification, explicit coverage for critical negative claims, and a separate adversarial review before completion is claimed.

Known incidents WF-001 through WF-006 are encoded on the closure branch. WF-006 records the failure to preserve action-specific approval behavior for GitHub writes. The generalized prevention is: use read-without-prompt/write-with-approval permissions where available; describe the exact intended mutation; obtain approval immediately before the write; treat that approval as scoped to that action; and re-read remote state after blocked, failed, or ambiguous writes before retrying.

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

## Human approval gates
Human approval is required before approved milestone adoption, merges, production downloads, destructive operations, scientific-policy/interpretation changes, and QC pass/fail milestone declarations.

GitHub repository writes should use action-specific approval immediately before the mutation when the connected-app permission model supports it. A prior broad approval must not be silently stretched to later unrelated writes.

## Current milestone
- Architecture v1 controls and registries are integrated into `main`.
- The Architecture v1 merge itself has been remotely verified.
- WSL/runtime validation remains pinned to `c77f1709a66df1c8ecf195fe6eac359fa14a51d1`; later documentation/control-state commits are not falsely described as runtime-validated at that SHA.
- The focused `task/day1-closure` patch is updating stale post-merge state text and encoding WF-006/guardrail v7.
- Day-1 is not declared durably closed until this closure patch is remotely audited and, after explicit human approval, integrated into `main`.
- No new production download or calibration implementation is authorized by this milestone.

## Next safe action
1. Re-read all four files changed by `task/day1-closure` from remote GitHub.
2. Compare `task/day1-closure` against `main` and confirm the changed-file set is exactly the intended closure controls.
3. Perform the adversarial pass for contradiction, unsupported completion claims, accidental scientific-policy drift, stale authority paths, and unintended files.
4. Present the focused closure patch for human merge approval.
5. After approved integration, verify `main` remotely and only then declare Day-1 durably closed.
6. Begin Day-2 centre-specific seasonal data evidence and availability audit; production downloads remain blocked.

## Chat-quality safeguard
If a chat becomes long, stale, or confused enough that evidence, decisions, centre-specific facts, user constraints, or repository state may be mixed, stop before another high-impact decision and start a fresh remote-GitHub-first Architecture v1 re-entry.
