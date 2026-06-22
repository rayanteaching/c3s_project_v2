# C3S NCEP Nominal Start Dates and Pressure-Level Notes

## Source

- Source: ECMWF / C3S Knowledge Base
- Page: Seasonal monthly pressure-level data and detailed parameter/system documentation
- URL: https://confluence.ecmwf.int/display/CKB/Detailed+list+of+parameters
- Type: official documentation
- Status: evidence note

## Why this source matters

This source affects NCEP CFSv2 production design because NCEP uses lagged ensembles and nominal start months that represent multiple initialization dates, not a single forecast start date.

## Key findings

- The pressure-level dataset covers monthly aggregated pressure-level seasonal forecast data.
- The documented vertical coverage is from 1000 hPa to 10 hPa.
- Main pressure-level variables include geopotential, temperature, specific humidity, u-component wind, and v-component wind.
- NCEP CFSv2 uses `system=2`.
- NCEP forecasts for nominal month M include members initialized on the 1st of month M and available members back to the 2nd of month M-1.
- NCEP hindcasts for nominal month M include multiple initialization dates from month M-1, not a single start date.
- This confirms that NCEP nominal-month metadata must be interpreted through lagged-ensemble semantics.

## Repository impact

- NCEP production inventory must track initialization-date completeness.
- NCEP QC must validate member/date completeness, not only file existence or GRIB openability.
- `message_count`, `unique_data_date_count`, `expected_message_count`, `observed_missing_message_count`, `contains_20230522`, and `messages_for_20230522` are required evidence fields, not optional metadata.
- G8 missing-date handling is consistent with documented NCEP lagged-ensemble behaviour.
- z500 and t850 have initial repository smoke evidence.
- z925 remains a project target but still needs explicit NCEP smoke/availability evidence before production inclusion.

## What this supports

- Keeping NCEP production download blocked until downloader design, inventory schema, and QC plan explicitly handle lagged initialization dates.
- Designing NCEP inventory and QC differently from ECMWF.
- Treating nominal start month as a grouped forecast construct rather than a single initialization date.

## What this does not support

- It does not authorize NCEP production download.
- It does not prove that z925 has passed repository smoke testing.
- It does not complete the representative NCEP smoke matrix.
- It does not define the final downloader implementation.

## Open questions

- Should z925 be included in production v1 or deferred until a dedicated NCEP z925 smoke test passes?
- What is the exact expected message-count model for each nominal month, year, variable, and leadtime?
- How should `completeness_status` classify G8-affected months: warning, incomplete, or usable-with-flag?

## Decision status

Not a policy decision by itself. This note should inform:
- `NCEP_PRODUCTION_READINESS_PLAN.md`
- `NCEP_DOWNLOADER_DESIGN.md`
- `NCEP_INVENTORY_SCHEMA.md`
- `NCEP_PRODUCTION_QC_PLAN.md`
