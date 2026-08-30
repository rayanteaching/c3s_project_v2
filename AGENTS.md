# AGENTS.md

This repository, not chat history, is the durable project state.

## Start here
1. Read `docs/STATUS.md`.
2. Identify the current task and blockers.
3. Read only the scientific, config, code, and evidence relevant to that task.
4. For high-impact repository work, use `docs/CHATGPT_REENTRY_PROTOCOL.md`.
5. For scientific decisions, use `docs/OPEN_SCIENTIFIC_QUESTIONS.md`, `docs/DECISIONS.md`, and `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`.

## Core rules
- Never invent project state, scientific facts, files, results, validation outcomes, or tool success.
- If required evidence is missing or conflicting, mark it UNKNOWN / NEEDS VERIFICATION and stop the affected downstream decision.
- Major scientific decisions require traceable evidence and explicit human approval.
- Do not propagate assumptions across centres, systems, or products without verification.
- Availability is not scientific eligibility.
- Legacy code, configs, runs, and old chat are not current policy unless revalidated.
- Do not modify raw data.
- Do not silently change scientific definitions, conventions, or policy.
- Do not claim completion without the required tests, validators, runtime/repository evidence, and human approval where required.
- Keep changes bounded to the declared task.

## Authority map
- Current state and next task: `docs/STATUS.md`
- Stable scientific/project architecture: `docs/ARCHITECTURE.md`
- AI high-impact safety controls: `docs/AI_COLLABORATION_SAFETY.md`
- Open scientific questions: `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- Approved durable decisions: `docs/DECISIONS.md`
- Scientific decision record format: `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`
- Active dataset/config index: `configs/datasets/CURRENT_CONFIGS.md`
- Study scope: `configs/datasets/study_v0_1.yml`
- System facts/state: `configs/datasets/system_registry_v1.yml`
- Variable semantics/state: `configs/datasets/variable_registry_v1.yml`
- Execution evidence: `runs/`
- Data inventories: `data/inventory/`

## Progressive disclosure
Do not load the full repository or every control document by default. Read deeper material only when the current task requires it.

Scientific truth, implementation truth, and current data/repository state have different authorities:
- scientific definitions/rationale -> approved scientific decisions and authoritative sources;
- intended computational behavior -> configs/contracts/tests;
- current repository/data/runtime state -> Git/filesystem/runtime/validators.

If current authoritative sources conflict, stop and resolve the conflict rather than guessing.
