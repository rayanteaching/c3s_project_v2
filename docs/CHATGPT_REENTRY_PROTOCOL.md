# High-Impact Re-entry Protocol

## Purpose
Use this document only for high-impact ChatGPT/Codex work. Normal work should start from `AGENTS.md` and `docs/STATUS.md` and load additional material only as needed.

High-impact work includes:
- merge review or milestone adoption;
- production downloads;
- QC pass/fail milestone declarations;
- scientific-method or data-selection decisions;
- policy/guardrail changes;
- destructive operations;
- recovery/cleanup when repository or scientific state is uncertain.

## Fresh repository-state check
Before a high-impact repository decision, obtain fresh remote evidence for the relevant task branch and `main`:
1. task-branch SHA;
2. `main` SHA;
3. merge base;
4. ahead/behind counts;
5. changed-file list/diff.

Do not substitute remembered chat state, stale local refs, or generated re-entry packs for current repository evidence.

## Evidence discipline
Load only the authority needed for the task:
- current repository state for repository claims;
- runtime/run evidence for execution claims;
- current configs/registries for machine-readable project state;
- authoritative scientific sources plus approved decision records for scientific claims.

If required evidence is missing or conflicting, mark the point UNKNOWN / NEEDS VERIFICATION and block the affected high-impact decision.

## Repository-change workflow
Before a material write:
- identify the exact target branch and file scope;
- confirm the intended base;
- obtain the required human approval.

After the write:
- re-read the resulting remote state;
- inspect the changed-file diff;
- confirm no unintended files changed;
- run the relevant validation/tests where available.

An attempted write is not proof of a successful write.

## Task-specific checks

### Script/config change
Check the target script/config, relevant scientific decision/evidence, expected behavior, validation command, remote diff, and post-write state.

### Production acquisition
Require verified centre/system/product semantics, availability/eligibility evidence, horizon/init mapping, variable/level semantics, known issues, expected outputs, inventory/QC plan, and explicit human approval.

### QC milestone
Require explicit criteria, QC implementation, output/inventory/runtime evidence, known issues/exclusions, and human approval before declaring PASS/FAIL as a milestone.

### Scientific decision
Use the relevant open-question ID and `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`. Require authoritative evidence, alternatives, consequences, uncertainty, explicit human approval, and consistent updates to affected configs/registries/docs.

## Completion gate
For high-impact work, do not claim COMPLETE / PASS / READY / FIXED / VERIFIED / MERGE-READY until:
- required evidence is present;
- relevant tests/validators have run where available;
- changed repository state has been re-read;
- contradictions and omissions have been checked;
- required human approval has been obtained.

## Chat migration
If the active chat becomes stale or confused enough that project state, evidence, scientific facts, or user constraints may be mixed, stop high-impact decisions and restart from fresh repository evidence.

Repository artifacts and technical identifiers remain in English; discussion with the user may be in Persian.
