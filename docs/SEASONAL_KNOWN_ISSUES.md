# Seasonal Known Issues Register

## Scope
This register tracks official C3S seasonal data issues that affect repository download and evaluation decisions.

## Active bootstrap scope
- Centre: ECMWF
- System: 51
- Datasets: seasonal-monthly-single-levels, later seasonal-monthly-pressure-levels
- Active bootstrap variables: t2m, ws10m, tp
- Deferred pressure-level variables: z500, t850, z925

## ECMWF system 51
- In the reviewed official known-issues page, the explicit ECMWF system 51 issue identified for now concerns volumetric soil moisture GRIB2 packing.
- That issue is outside the current ECMWF monthly single-level bootstrap variables.
- No explicit official known issue affecting the current bootstrap variables t2m, ws10m, and tp was identified in the reviewed pages for this repository step.
- This is not a blanket guarantee for later variables or later centres; each activation step must re-check the official known-issues page.

## Non-ECMWF centres
- UK Met Office, DWD, CMCC, Météo-France, and NCEP remain deferred.
- Before any of them is activated, the repository must record:
  - period-specific system mapping
  - relevant official known issues for the selected years, variables, and product types
  - operational action for each issue: allow, warn, mask, or exclude

## Lagged-system decoding rule
- For lagged monthly systems, nominal start date and real initialization date handling must be documented before scientific evaluation begins.
- Tools based on ecCodes and cfgrib must be used when that phase is activated.

## Operational rules
- Known issues must be checked before each new centre or variable is activated.
- Issues stating that archived wrong data will not be overwritten must be treated as hard warnings.
- Data gaps must be recorded explicitly in run metadata and inventories.
- Deferred centres must not be operationally downloaded until their issue registration is committed.

## NCEP CFSv2 activation review
- G8 caution for current workflow: NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. This is not treated as a blanket blocker for monthly_mean retrieval, but forecast May 2023 must receive explicit member/date-handling QC before any NCEP-derived product or multi-model analysis.
- Status: candidate centre under review; production download is not yet authorized.
- System: CFSv2-v20110310.
- CDS system keyword: 2.
- Operational caution: NCEP uses lagged/daily initialization; member counts and nominal start handling must be verified by smoke tests before production.
- E4.a1/E4.a2: fixed historical CDS availability issues for NCEP monthly statistics/anomalies. Repository action: allow after standard verification.
- E7/E7b: fixed missing-member issues affecting NCEP daily/subdaily datasets. Repository action: warn if daily/subdaily NCEP data are later activated; not a direct blocker for current monthly pressure-level workflow.
- E6: NCEP surface solar radiation variables were swapped for affected dates. Repository action: exclude from current workflow; re-review only if radiation variables are activated.
- G8: NCEP system=2 forecast data for 2023-05-22 are unavailable because all four members initialized on that date were not correctly transmitted. Repository action: warn; forecast May 2023 member/date handling must be checked explicitly in NCEP QC. This is not a blanket blocker for monthly_mean retrieval unless retrieval evidence or member/date counts show an impact.
