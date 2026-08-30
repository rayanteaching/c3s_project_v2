# Project Status

## Current milestone
Architecture v1 and its Day-1 closure controls are integrated into `main`.

Current repository state must be read directly from Git; live branch SHAs are not copied into this document.

- Harness Patch 1 was merged via PR #3, with its status-closure follow-up merged via PR #4.
- Architecture v1 merge history and prior validation evidence remain preserved in Git and tracked run/control records.

## Current task
Audit and reduce the project Harness before resuming full scientific production.

Immediate objective:
- remove duplicated/stale current-state authority;
- introduce a short AI entry point;
- keep scientific decisions human-led and evidence-based;
- prepare for a small machine-enforced Harness pilot.

## Current blockers / open scientific work
The authoritative register is `docs/OPEN_SCIENTIFIC_QUESTIONS.md`.

No unresolved scientific question should be silently promoted to an implementation default. Questions affecting acquisition, eligibility, calibration, verification, or comparison remain blocking until supported by the required evidence and human decision.

## Current validation evidence
Historical WSL/runtime validation is pinned to commit `c77f1709a66df1c8ecf195fe6eac359fa14a51d1`; it must not be treated as validation of later commits.

Harness Patch 1 repository review is complete: the task branch was merged to `main` via PR #3. Runtime/scientific validation was not applicable because Patch 1 changed only documentation/control-layer files.

Harness Patch 2 validator logic has been challenged with isolated fixtures: the approved baseline passed, while an enabled global z950-to-z925 substitution, a missing centre registry entry, reintroduction of `docs/HANDOFF.md`, and a copied live `main` SHA in `docs/STATUS.md` each failed as intended. A minimal CI workflow is present on the task branch; GitHub has not yet reported a workflow run for the current head, so CI execution remains pending.

## Production state
- No new production seasonal download is authorized by the current recovery audit.
- No calibration implementation is authorized before the relevant scientific decisions and case contracts are approved.
- Human approval remains required for scientific-policy changes, production actions, destructive operations, milestone adoption, and merges.

## Next action
Review PR #5 and obtain actual GitHub CI execution evidence for `python scripts/validate_project.py` and `python -m unittest tests/test_validate_project.py`. Do not merge Patch 2 until that evidence is available.
