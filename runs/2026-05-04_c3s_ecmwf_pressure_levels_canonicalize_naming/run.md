# ECMWF seasonal monthly pressure-level naming canonicalization

## Scope
- Dataset: C3S seasonal monthly pressure-levels
- Centre: ECMWF
- System: 51
- Blocks:
  - hindcast_2000_2016
  - forecast_2017_2025
- Variables:
  - z500
  - t850
  - z925

## Canonical naming rule
The canonical naming family is the one aligned with the completed single-level workflow:

`cds__c3s_seasonal__monthly-pressure-levels__ecmwf__s51__...__stXX__lead1-6__NH0_90`

The noncanonical duplicate naming family is:

`cds__seasonal-monthly-pressure-levels__ecmwf__system_51__...__mXX__lt01-06__NH0_90__grid_1p0`

## Action
Noncanonical duplicate files were moved out of the active raw hindcast and forecast directories into:

`/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ecmwf/system_51/noncanonical_duplicate_naming_family_20260504`

No raw files were deleted.

## Result
The active pressure-level raw directories now retain only the canonical naming family aligned with the single-level workflow.
