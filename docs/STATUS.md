# Project Status

## Current milestone
Architecture v1 and its Day-1 closure controls are integrated into `main`.

Current repository baseline for this recovery audit:
- `main`: `c8527705e7ac36dba8bd6264e84ff3d8a9550674`
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

Patch-specific validation for the current Harness cleanup is still pending until the task branch changes are reviewed.

## Production state
- No new production seasonal download is authorized by the current recovery audit.
- No calibration implementation is authorized before the relevant scientific decisions and case contracts are approved.
- Human approval remains required for scientific-policy changes, production actions, destructive operations, milestone adoption, and merges.

## Next action
1. Complete and review Harness Patch 1 on `task/harness-patch-1`.
2. Verify there are no active stale references to retired current-state artifacts.
3. Confirm that Patch 1 changes no scientific policy.
4. After human review, proceed to Patch 2: identify the smallest set of prose rules that should become tests/validators/CI gates.
