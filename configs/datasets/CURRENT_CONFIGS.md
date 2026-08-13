# Current Architecture v1 Dataset Configuration

## Authoritative current files
For Architecture v1 scientific planning and future production design, use:
- `configs/datasets/study_v0_1.yml`
- `configs/datasets/guardrails_v1.yml`
- `configs/datasets/system_registry_v1.yml`
- `configs/datasets/variable_registry_v1.yml`

These files are read together with:
- `docs/ARCHITECTURE.md`
- `docs/OPEN_SCIENTIFIC_QUESTIONS.md`
- `docs/DECISIONS.md`

## Legacy/bootstrap files
The following files are preserved because they document earlier bootstrap implementation, but they are not Architecture v1 scientific source-of-truth configuration:
- `configs/datasets/c3s_seasonal_systems.yml`
- `configs/datasets/c3s_seasonal_variables.yml`

They may contain earlier ECMWF system-51 assumptions, fixed 2000-2016/2017-2025 blocks, z925 substitution, or other bootstrap choices. Reuse requires explicit revalidation under Architecture v1.

## Conflict rule
If a legacy/bootstrap config conflicts with the current Architecture v1 files, the legacy config does not override current policy. If two current Architecture v1 sources conflict, stop and resolve the conflict before production or scientific analysis.
