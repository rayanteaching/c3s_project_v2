# ECMWF seasonal monthly pressure-level scientific sanity QC

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

## Method
The QC script checked all 72 canonical GRIB files using ecCodes.

Checks included:
- GRIB existence
- request sidecar existence
- SHA256 sidecar existence
- checksum verification
- ecCodes scan/open test
- sampled message statistics
- pressure-level metadata
- grid metadata
- physical sanity range checks

## Result
Canonical ECMWF pressure-level files passed sampled scientific sanity checks.
