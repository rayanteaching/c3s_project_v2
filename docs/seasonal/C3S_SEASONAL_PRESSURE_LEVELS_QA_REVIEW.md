# C3S seasonal monthly pressure-level quality-assurance review

## Scope
This document records repository-relevant quality-assurance implications from the CDS quality tab for `seasonal-monthly-pressure-levels`.

This review applies before activating NCEP CFSv2 production downloads and before any multi-model seasonal verification or product generation.

## Reviewed source
- CDS dataset: `seasonal-monthly-pressure-levels`
- CDS tab: Quality
- Fitness-for-purpose evaluation date shown by CDS: 2026-04-29
- Dataset update date shown by CDS: 2026-05-05

## Core interpretation
Seasonal monthly pressure-level data are monthly statistics derived from subdaily seasonal forecast data.

The monthly products are appropriate when the application does not require daily or subdaily information.

The data must not be interpreted as deterministic weather forecasts. Seasonal forecasts are probabilistic and are intended to provide information about potential deviations from normal climate conditions at monthly to seasonal timescales.

## Bias and hindcast dependency
The CDS quality information states that monthly statistics contain systematic deviations from the true climate.

Repository implications:
- Raw forecast fields must not be used as final scientific products without bias assessment.
- Bias correction or at minimum bias-aware interpretation is required for forecast applications.
- Hindcasts/reforecasts are required to estimate model climatology, systematic error, and forecast skill.
- Any anomaly or bias-corrected product must document the reference period, method, system, lead time, and variable.

## Forecast skill
Forecast skill is case-specific.

Skill depends on:
- variable
- lead time
- region
- season
- climate state
- forecast system
- predictable phenomena and teleconnections

Repository implications:
- Skill must not be assumed from download success.
- Northern Hemisphere verification must be performed explicitly against ERA5 or another documented reference.
- Skill may be stronger for large-scale features and shorter lead times.
- Skill may be stronger in the tropics than in mid-latitudes.
- Temperature may generally be more skillful than precipitation, but this must not be generalized without project-specific verification.

## Multi-system and NCEP caution
The CDS quality information stresses that this is a complex multi-system forecast dataset with start-date and lead-time dimensions.

Forecast systems can differ in:
- spatial grid
- ensemble generation method
- burst versus lagged ensemble design
- available hindcast/reforecast periods
- metadata representation in CDS
- system-version transitions

Repository implications for NCEP:
- May 2023 NCEP forecast data require explicit member/date-handling QC because the documented G8 issue states that NCEP system=2 data initialized on 2023-05-22 are unavailable.
- NCEP CFSv2 must not be treated as operationally identical to ECMWF.
- NCEP member counts, nominal start dates, initialization-date handling, and lead-time metadata must be verified by smoke tests before production.
- NCEP production download remains blocked until smoke tests confirm correct request semantics and metadata interpretation.

## Format decision
The CDS quality information warns that experimental NetCDF files may have limited metadata and can create interpretation problems for complex requests.

Repository decision:
- Operational seasonal downloads must use native GRIB.
- NetCDF must not be used for operational seasonal download workflows unless a separate documented validation justifies it.
- GRIB metadata must be inspected with ecCodes/cfgrib-aware tools during QC.

## Dataset usability implications
Download completion does not imply scientific readiness.

Required workflow layers:
1. raw download
2. sidecar request capture
3. checksum verification
4. inventory snapshot
5. structural QC
6. openability QC
7. metadata sanity QC
8. scientific sanity QC
9. hindcast-based verification
10. bias/anomaly strategy before derived products

## NCEP activation rule
Before NCEP production download, the repository must complete and commit:
- NCEP smoke-test script
- representative hindcast smoke tests
- representative forecast smoke tests
- member-count inspection
- nominal start-date and leadtime interpretation notes
- relevant known-issue registration
- run metadata and status updates

Recommended NCEP smoke-test years:
- hindcast: 2000
- hindcast: 2010
- hindcast: 2011
- hindcast: 2016
- forecast: 2017
- forecast: 2023
- forecast: 2025

## Current decision
NCEP is still a candidate centre under activation review.

Production download is not authorized until smoke tests and metadata checks pass.
