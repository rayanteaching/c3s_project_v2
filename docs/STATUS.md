# Project Status

## Current milestone
Architecture v1 and its Day-1 closure controls are integrated into `main`.

Current repository baseline for this recovery audit:
- `main`: `a399db9550d085a30a9e5cbb34aedcc04993b0fa`
- Harness Patch 1 was merged via PR #3.
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

## Production state
- No new production seasonal download is authorized by the current recovery audit.
- No calibration implementation is authorized before the relevant scientific decisions and case contracts are approved.
- Human approval remains required for scientific-policy changes, production actions, destructive operations, milestone adoption, and merges.

## Next action
Proceed to Harness Patch 2: identify the smallest set of high-value prose rules that should become tests, validators, or CI gates before the pilot.
