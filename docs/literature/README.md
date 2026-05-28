# Literature and Scientific Evidence Notes

This directory stores lightweight, tracked notes from scientific papers, books, official documentation, and technical references that may affect project methods, coding decisions, QC design, or interpretation.

These files are evidence notes, not operational decisions by themselves.

A scientific source becomes an official project decision only when it is summarized in `docs/DECISIONS.md` with:
- the decision,
- the evidence used,
- the reason,
- alternatives considered when relevant,
- consequences for scripts/configs/QC/data handling,
- affected files,
- current status.

Use this directory for:
- C3S seasonal forecast methodology notes,
- ERA5 reference-data notes,
- verification and validation methods,
- ensemble forecast handling,
- missing-data handling,
- GRIB/cfgrib/ecCodes technical notes,
- LLM workflow engineering notes when they affect project operating procedure.

Do not store copyrighted full papers, book chapters, or large source documents here.
Store only short notes, citations, summaries, and links or identifiers.

Recommended note format:

## Source
- Title:
- Authors:
- Year:
- Type: paper / book / official documentation / technical documentation / other
- URL or DOI:
- Accessed date:

## Relevance to this project
- Why this source matters:

## Key points
- Point 1:
- Point 2:
- Point 3:

## What this supports
- Supported project method or decision:

## What this does not support
- Limits, caveats, or things not justified by this source:

## Possible project action
- None / update DECISIONS / update config / update script / update QC / update RUNBOOK

## Status
- background / under review / used in decision / superseded
