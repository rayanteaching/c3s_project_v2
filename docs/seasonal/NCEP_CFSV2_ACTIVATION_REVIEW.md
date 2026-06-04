# NCEP CFSv2 activation review

## Scope
This document records the repository activation review for NCEP CFSv2 before any NCEP seasonal download is started.

## Reviewed official sources
- CDS dataset: seasonal-monthly-pressure-levels
- C3S Knowledge Base: Description of the C3S seasonal multi-system
- C3S Knowledge Base: NCEP Forecast System
- C3S Knowledge Base: Description of CFSv2-v20110310 C3S contribution
- C3S Knowledge Base: C3S Seasonal Forecast known issues
- C3S Knowledge Base: Summary of available data
- C3S Knowledge Base: Detailed list of parameters
- C3S Knowledge Base: Recommendations and efficiency tips for C3S seasonal forecast datasets

## Dataset relevance
The CDS pressure-level monthly dataset is relevant to the project pressure-level targets:
- z500: geopotential at 500 hPa
- t850: temperature at 850 hPa
- z925: geopotential at 925 hPa

The dataset is monthly, global, regular latitude-longitude, 1 degree by 1 degree, and delivered in GRIB format.

## NCEP system mapping
- Provider: NCEP
- Forecast system: CFSv2-v20110310
- CDS system keyword: 2
- C3S multi-system provider code shown in documentation: kwbc
- Forecast model: NCEP Global Forecast System coupled to GFDL MOM4 ocean model
- Atmosphere resolution: T128, approximately 1 degree latitude-longitude
- Atmosphere vertical resolution: 64 hybrid sigma-pressure levels
- Ocean model: GFDL MOM4
- Ocean vertical resolution: 40 layers

## Operational differences from ECMWF
NCEP must not be treated as operationally identical to ECMWF.

Documented NCEP characteristics:
- Forecast initial conditions are available every day of the month.
- Forecast members are initialized every 6 hours at 00, 06, 12, and 18 UTC.
- Forecast ensemble construction is therefore lagged/daily.
- Hindcast initial conditions are available every 5 days.
- Hindcast members are initialized every 6 hours at 00, 06, 12, and 18 UTC.
- Hindcast production is fixed.

Implication:
NCEP smoke tests and QC must explicitly inspect member counts, initialization dates, nominal start month handling, and leadtime metadata.

## Time-period caution
The CDS dataset overview states:
- hindcasts: 1993-2016
- forecasts: 2017 to present

The CFSv2 system-description page states:
- hindcast years: 1981-2010

Repository action:
Before production download, run NCEP smoke tests for representative project years and do not assume complete 2000-2016 coverage without CDS retrieval evidence.

Required smoke-test years:
- hindcast: 2000
- hindcast: 2010
- hindcast: 2011
- hindcast: 2016
- forecast: 2017
- forecast: 2023
- forecast: 2025

## Known issues relevant to NCEP
- G8 caution: NCEP system=2 forecast data initialized on 2023-05-22 are unavailable because all four members for that date were not correctly transmitted. Repository interpretation: this is not a blanket blocker for monthly_mean retrieval, but May 2023 forecast member/date handling must be explicitly checked during NCEP QC before using NCEP in derived products or multi-model analysis.
### E4.a1 and E4.a2
Monthly statistics and anomalies for some NCEP CFSv2 hindcast and forecast dates were temporarily unavailable in 2019.
Official status: fixed in the archive.
Repository action: allow, but keep note in known-issues register.

### E7 and E7b
Missing members affected NCEP CFSv2 high-frequency daily/subdaily datasets.
Official status: fixed.
Repository action: not a blocker for monthly pressure-level downloads, but warn if daily/subdaily NCEP data are later activated.

### E6
NCEP CFSv2 surface solar radiation variables were swapped for affected start dates.
Repository action: not relevant to current z500, t850, z925 workflow. Exclude or re-review if radiation variables are later activated.

### G8
NCEP system=2 forecast data for 2023-05-22 are unavailable because all four members initialized on that date were not correctly transmitted.
Repository action: warn. Forecast May 2023 member counts must be explicitly checked during NCEP QC.

Repository smoke-test evidence: corrected nominal June 2023 z500 monthly_mean retrieval recorded dataDate=20230522 as absent, messages_for_20230522=0, message_count=120, and observed_missing_message_count=4. This confirms the G8 missing initialization-date issue in retrieved monthly_mean GRIB metadata. Production download remains blocked until final NCEP production policy is documented.

## Pressure-level variable decision
The repository pressure-level substitute remains z925, not z950.

NCEP activation should use:
- z500
- t850
- z925

Do not introduce z950 for C3S seasonal pressure-level downloads.

## Format and retrieval policy
- Use native GRIB.
- Do not use experimental NetCDF conversion for operational workflow.
- Do not silently interpolate or convert units during download.
- Record exact request payloads and sidecars.
- Use checksum sidecars.
- Keep raw data outside Git.
- Track only lightweight run metadata and inventories.

## Activation status
NCEP is not yet activated for production download.

Allowed next step:
- create NCEP smoke-test script and run smoke tests for representative hindcast and forecast years.

Blocked until smoke tests pass:
- grouped NCEP production download
- NCEP inclusion in multi-model analysis
- NCEP-derived products

## CDS quality-assurance implications for NCEP
The CDS quality information for seasonal monthly pressure-levels reinforces that NCEP must be activated cautiously.

Repository implications:
- Do not proceed directly to NCEP production download.
- Verify NCEP system=2 request semantics using smoke tests first.
- Verify member-count behaviour explicitly because NCEP uses lagged/daily ensemble generation.
- Verify nominal start-month and leadtime metadata before grouped downloads.
- Keep native GRIB as the operational format.
- Do not use experimental NetCDF for operational NCEP downloads.
- Do not create NCEP anomaly, bias-corrected, or multi-model products until hindcast-based verification and bias strategy are documented.
