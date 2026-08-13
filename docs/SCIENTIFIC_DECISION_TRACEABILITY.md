# Scientific Decision Traceability

## Purpose

Major scientific decisions must be inspectable by the supervisor and reproducible from
repository evidence.

A citation only in the final bibliography is insufficient. Each important decision must
carry its own traceable evidence.

## Decision record template

### Decision ID
Stable identifier, for example `SD-001`.

### Title
Short scientific decision title.

### Status
One of:
- OPEN
- UNDER REVIEW
- APPROVED
- SUPERSEDED
- REJECTED

### Scope
Centre/system/product/variable/horizon/domain/metric or project-wide scope.

### Scientific question
The question that required a decision.

### Decision
The adopted choice. Leave blank while OPEN.

### Alternatives considered
List serious alternatives and why they remain viable or were rejected.

### Evidence
For every load-bearing source record:
- evidence class;
- source type;
- authors/organization;
- title;
- year/version;
- DOI where available;
- official URL where applicable;
- access date for online documentation;
- exact claim supported by the source;
- repository evidence path/run ID where applicable.

Evidence classes:
- VERIFIED — REPOSITORY
- VERIFIED — AUTHORITATIVE SOURCE
- INFERENCE
- UNKNOWN / NEEDS VERIFICATION

### Rationale
Why the evidence supports the adopted decision.

### Consequences
Record consequences for:
- acquisition;
- eligibility;
- system selection;
- forecast/reforecast periods;
- member handling;
- calibration;
- verification;
- common-case comparison;
- multi-model analysis;
- QC;
- manuscript interpretation.

### Limitations / uncertainty
What is still uncertain after the decision.

### Sensitivity analysis required
Yes/no/pending and why.

### Human approval
Approval identity/date or explicit approval record.

### Git adoption commit
Commit in which the approved decision became current project truth.

### Manuscript relevance
Methods/results/supplement/none.

### Advisor-report inclusion
Yes/no and proposed section.

## Citation rule

Every major scientific decision shown in the advisor-facing report must include inline
citations beside the decision/rationale and must also appear in the consolidated
References section.

For official web documentation, retain the canonical source URL and access date.
For peer-reviewed literature, retain complete bibliographic metadata and DOI where
available.

## Advisor-facing report

The project will later generate an English report provisionally titled:

`Scientific Method and Data Selection Decision Report`

Suggested sections:
1. Study design decisions
2. Centre/system data decisions
3. Variable/level decisions
4. Calibration decisions
5. Verification decisions
6. Multi-model decisions
7. Explicit decision table
8. References

The report is a derived communication artifact. The authoritative decision/evidence
records remain in the version-controlled repository.
