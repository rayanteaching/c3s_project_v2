# Status

## Current milestone
- Architecture v1 was approved by the human reviewer and fast-forward merged into `main`.
- Remote post-merge verification confirmed `main` at `077ec141f3442e8ec5abce4e11e56ce804764a89` and identical to `task/architecture-v1-handoff` at the time of verification.
- Day-1 Architecture v1 and its closure controls are integrated into `main` at `97ec49272524e05f6faea5e92068afd2273c6f75`.
- Base checkpoint before Architecture v1 work: `544a375c05d85331ff0e674a89494120d413794f`.
- WSL/runtime validation remains pinned to task SHA `c77f1709a66df1c8ecf195fe6eac359fa14a51d1`; after that validation, only reviewed documentation/control-state changes were made before the Architecture v1 merge.

## Active Architecture v1 control files
- `docs/ARCHITECTURE.md`
- `docs/AI_COLLABORATION_SAFETY.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `docs/DECISIONS.md`
- `docs/SEASONAL_DOWNLOAD_POLICY.md`
- `docs/CHATGPT_REENTRY_PROTOCOL.md`
- `docs/WORK_PROTOCOL.md`
- `configs/datasets/CURRENT_CONFIGS.md`
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `configs/datasets/system_registry_v1.yml`
- `configs/datasets/variable_registry_v1.yml`

## Current scientific scope
- Study window: target/verifying years 2000-2025.
- Manuscript v0.1 target month: December, configuration-driven.
- Scientific horizons H1-H6: one through six calendar months before target.
- Centres: ECMWF, UKMO, DWD, CMCC, Meteo-France, NCEP.
- Variables: z500, t850, z950, t2m, total precipitation, ws10m.
- Manuscript v0.1 domains: NH, ROI, ROI_X4; exact geometries/masks require current approved evidence/configuration.
- Required analysis modes: maximum-valid centre/system analysis and fair common-case cross-centre analysis.

## Current architecture rules
- No universal hindcast/forecast split.
- No global native-lead mapping.
- No global z950 -> z925 substitution.
- No cross-centre propagation of assumptions.
- Forecast/reforecast matching is system-cohort-aware.
- Availability is not scientific eligibility.
- Unknown/conflicting required facts fail closed.
- Common comparisons use canonical eligible case identities.
- Direct raw/calibrated comparisons use the same eligible evaluation cases.
- Parallel centre/metric workstreams require pinned contracts and integration gates.
- Legacy/bootstrap artifacts require revalidation before reuse.
- Major scientific decisions require decision-level evidence/citations and human approval.
- AI-assisted work must follow `docs/AI_COLLABORATION_SAFETY.md`.

## AI collaboration safety state
- Known workflow/assistant incidents WF-001 through WF-006 are recorded in `docs/AI_COLLABORATION_SAFETY.md` and integrated into `main`.
- `guardrails_v1.yml` version 7 in `main` adds an explicit action-specific approval rule for GitHub writes.
- GitHub app permissions are configured to allow read actions while requiring approval before writes.
- A blocked/failed write must be followed by a system-of-record reread before retrying or changing workflow.
- High-impact assistant work still requires constraint coverage, evidence classification, post-action verification, explicit negative-claim coverage, and a separate adversarial review before completion.
- Every chat/task now declares one primary deliverable and an INSPECT/CHANGE mode through `docs/WORK_PROTOCOL.md`.

## WSL validation result
At task SHA `c77f1709a66df1c8ecf195fe6eac359fa14a51d1`, synchronized WSL validation recorded:
- local `HEAD` equal to `origin/task/architecture-v1-handoff`;
- clean working tree;
- no defects from `git diff --check origin/main...HEAD`;
- PyYAML 6.0.3 available and all four active YAML files parsed successfully;
- Architecture scientific-scope assertions and guardrail-v6 required-control assertions satisfied;
- all six centre registry entries remained fail-closed/open;
- variable-registry and z950-policy assertions satisfied;
- all 15 required Architecture v1 control files present;
- retired `scripts/make_chatgpt_reentry_pack_v2.sh` absent from the synchronized active tree;
- checked entry-point documents referenced `docs/AI_COLLABORATION_SAFETY.md`;
- `git rev-list --left-right --count origin/main...HEAD` returned `0 46`.

This runtime evidence is pinned to that exact SHA and is not silently extended to later commits.

## Open scientific work
The controlled register is `docs/OPEN_SCIENTIFIC_QUESTIONS.md`. Items remain intentionally OPEN until the relevant centre/metric/method workstream reaches them. Architecture closure did not resolve centre-specific archive facts, member policy, lead mapping, z950 availability, calibration method, climatology, metric recipes, or common-case construction.

## Production state
- No new production seasonal download is authorized by Architecture v1 or by Day-1 closure.
- No calibration implementation is authorized before relevant scientific decisions/case contracts are approved.
- Human approval remains required for merges, production downloads, scientific-policy changes, and QC milestone decisions.

## Next safe action
1. Begin Day-2 centre-specific seasonal data evidence and availability audit.
2. For each centre/system/product, verify authoritative archive semantics before building production download requests.
3. Keep production downloads blocked until the required evidence and registry gates are approved.
