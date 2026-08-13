# Status

## Current milestone
- Day-1 Architecture v1 foundation and the AI collaboration safety layer are implemented on `task/architecture-v1-handoff`.
- WSL/runtime validation completed against task SHA `c77f1709a66df1c8ecf195fe6eac359fa14a51d1` after synchronizing the task branch.
- Current gate: human merge review. Merge remains blocked until explicit human approval.
- Base checkpoint before Architecture v1 work: `544a375c05d85331ff0e674a89494120d413794f`.
- NCEP integration commit `b574f26702163c424a5b605e414c1d992435642b` is already an ancestor of `main`; older instructions to merge NCEP next are historical.

## Active Architecture v1 control files
- `docs/ARCHITECTURE.md`
- `docs/AI_COLLABORATION_SAFETY.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- `docs/DECISIONS.md`
- `docs/SEASONAL_DOWNLOAD_POLICY.md`
- `docs/CHATGPT_REENTRY_PROTOCOL.md`
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
- Known workflow/assistant incidents WF-001 through WF-005 are recorded in `docs/AI_COLLABORATION_SAFETY.md`.
- `guardrails_v1.yml` version 6 contains generalized assistant-safety and defense-in-depth controls.
- High-impact assistant work requires constraint coverage, evidence classification, post-action verification, explicit negative-claim coverage, and a separate adversarial review before completion.
- The assistant's self-assessment is not sufficient evidence for a high-impact milestone claim.
- A new material assistant-caused failure keeps the affected high-impact milestone open until a durable preventive control is encoded and audited.

## Remote audit result
The current remote control layer was re-read after the AI-safety integration. Architecture, AI safety, re-entry, decisions, status, handoff, guardrails, README entry guidance, and seasonal production policy are aligned on the AI collaboration safety requirements. The retired re-entry v2 generator is absent from the active branch tree and remains history only.

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

This runtime evidence is pinned to the exact remote task SHA above. Any later task-branch change requires fresh comparison and validation appropriate to that change.

## Open scientific work
The controlled register is `docs/OPEN_SCIENTIFIC_QUESTIONS.md`. Items remain intentionally `OPEN — VERIFY WHEN REACHED` until the relevant centre/metric/method workstream reaches them.

## Legacy state
Earlier ERA5/ECMWF/NCEP bootstrap work remains preserved in Git history, runs, inventories, scripts, and literature notes. Legacy configs `c3s_seasonal_systems.yml` and `c3s_seasonal_variables.yml` are classified as historical/bootstrap by `configs/datasets/CURRENT_CONFIGS.md` and are not current Architecture v1 configuration.

## Re-entry state
Architecture v1 re-entry is GitHub-first and protocol-driven through `docs/CHATGPT_REENTRY_PROTOCOL.md` and `docs/AI_COLLABORATION_SAFETY.md`.

The former `scripts/make_chatgpt_reentry_pack_v2.sh` generator is preserved in Git history only and is absent from the current Architecture v1 tree. It is not authoritative for NORMAL or DEEP re-entry.

Before every DEEP AUDIT, fresh remote GitHub evidence must establish the task-branch SHA, `main` SHA, merge base, ahead/behind state, and changed-file diff. Local generated material does not replace that evidence.

## Production state
- No new production seasonal download is authorized by Architecture v1 itself.
- No calibration implementation is authorized before relevant scientific decisions/case contracts are approved.
- No merge to `main` without explicit human review/approval.

## Next safe action
1. Re-read the resulting remote `STATUS/HANDOFF` after this validation-state update.
2. Re-run a fresh remote GitHub task-vs-main comparison.
3. Perform the mandatory adversarial second pass for omissions, contradictions, stale authority paths, unintended files, unsupported claims, and scientific-policy drift.
4. Present the Architecture v1 human merge review if the evidence supports proceeding to that gate.
5. Obtain explicit human approval before merging Architecture v1 into `main`.
6. After an approved merge, verify `main` remotely before closing Day-1.
7. After integration, create centre-specific work packages and begin parallel centre verification.
