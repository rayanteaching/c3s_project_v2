# Open Scientific Questions

Status: ACTIVE REGISTER
Rule: OPEN questions remain unresolved until the relevant workstream reaches them.
Default behavior: if an unresolved item affects scientific eligibility or a downstream
method, the relevant gate fails closed.

## OQ-001 — Native lead mapping by centre/system/product
Status: OPEN — VERIFY WHEN REACHED

Question:
How does each relevant centre/system/product map the study's calendar scientific horizon
(H1-H6) to nominal initialization, native archive lead, and verifying month?

Required evidence:
- authoritative centre/C3S documentation;
- retrieval request metadata;
- retrieved GRIB metadata;
- verifying-period checks.

Scope:
Per centre, system cohort, product, target month, and horizon.

## OQ-002 — Lagged-ensemble horizon attribution
Status: OPEN — VERIFY WHEN REACHED

Question:
For lagged systems, how should the scientific phrase "one/two/... months before target" be
attributed when the nominal monthly bundle contains members with different actual
initialization dates?

Required evidence:
- supervisor definition;
- centre/C3S documentation;
- actual member-start evidence where available;
- literature if methodological interpretation is needed.

No global burst or lagged shortcut is assumed.

## OQ-003 — Centre/system cohort map and valid periods
Status: OPEN — VERIFY WHEN REACHED

Question:
Which exact system/version cohorts and valid forecast/reforecast periods are scientifically
eligible for each centre during the 2000-2025 target/verifying study window?

No universal hindcast/forecast split is assumed.

## OQ-004 — Matching forecast/reforecast cohort
Status: OPEN — VERIFY WHEN REACHED

Question:
For each forecast cohort, which reforecast/hindcast cohort is the scientifically matching
training/reference set?

Pooling across cohorts is blocked unless explicitly justified and approved.

## OQ-005 — Ensemble member selection and unequal ensemble size
Status: OPEN — VERIFY WHEN REACHED

Questions:
- Which members are scientifically eligible for each centre/system/product?
- How are lagged-member sets represented?
- How are missing members handled?
- Is any subsampling/matching required?
- How should unequal ensemble size affect probability construction, diagnostics, or score
  estimators?

## OQ-006 — Variable semantic recipes
Status: OPEN — VERIFY WHEN REACHED

Questions:
What exact archive semantics, temporal aggregation, units, transformations, and ERA5
counterparts apply to t2m, total precipitation, ws10m, z500, t850, and z950?

This includes special sensitivity to:
- accumulated precipitation semantics;
- wind-speed construction/aggregation;
- geopotential versus geopotential height.

## OQ-007 — z950 availability and scientific exception handling
Status: OPEN — VERIFY WHEN REACHED

Question:
Is z950 available and scientifically usable for each centre/system/product?

No global z925 substitution is allowed. Any exception requires a centre/system-specific
Scientific Exception Review.

## OQ-008 — Pressure-level mask / below-orography handling
Status: OPEN — VERIFY WHEN REACHED

Question:
What common spatial-support/mask rule is required for pressure-level fields, especially
near-surface levels such as z950?

## OQ-009 — Known issues and data gaps
Status: OPEN — VERIFY WHEN REACHED

Question:
How should each documented or retrieval-discovered centre/system/date/member issue affect
eligibility: allow, warn, mask, exclude, or block?

## OQ-010 — Regridding, grid alignment, and area weighting
Status: OPEN — VERIFY WHEN REACHED

Questions:
- What grid is used for verification?
- How is ERA5 aligned?
- What interpolation is appropriate per variable?
- What spatial weighting is used?
- How are masks propagated?

## OQ-011 — Common calibration training cases
Status: OPEN — VERIFY WHEN REACHED

Question:
For cross-centre comparison, should calibration use:
- system-specific maximum-valid training cases and then common evaluation cases;
- common training cases across compared systems with separate fits;
- another literature-supported policy?

The user has not approved a final option.

## OQ-012 — Calibration algorithm
Status: OPEN — VERIFY WHEN REACHED

Question:
Which calibration family/method is scientifically appropriate for each variable/event
representation and study objective?

No EMOS, quantile mapping, regression, logistic, Bayesian, or other method is preselected.

## OQ-013 — Cross-validation and leakage-control design
Status: OPEN — VERIFY WHEN REACHED

Question:
Which cross-validation strategy is appropriate for the reforecast sample?

Candidate LOYO is not selected.

The chosen design must control leakage in:
- calibration;
- climatology;
- event thresholds;
- reference probabilities;
- multi-model fitted weights.

## OQ-014 — Climatology, events, thresholds, and reference forecasts
Status: OPEN — VERIFY WHEN REACHED

Questions:
- What climatology/reference period is used?
- How are terciles/quantiles/events defined?
- How are probabilistic event forecasts constructed?
- What is the BSS/CRPSS reference?
- What reliability-bin definition is used?

## OQ-015 — Metric estimator/formulation
Status: OPEN — VERIFY WHEN REACHED

Question:
For BS/BSS, CRPS/CRPSS, reliability, ROC/AUC, and ensemble diagnostics, what exact
formulation/estimator/member-size handling is used?

Metric code may not silently choose these methodological details.

## OQ-016 — Multi-model construction
Status: OPEN — VERIFY WHEN REACHED

Question:
Which multi-model construction is scientifically justified?

Candidate classes to review include:
- equal model weighting;
- member pooling;
- probability/distribution mixtures;
- skill-based weighting;
- calibrated combinations.

No strategy is approved yet.

## OQ-017 — Uncertainty, significance, and sensitivity
Status: OPEN — VERIFY WHEN REACHED

Question:
What confidence-interval, bootstrap/significance, and sensitivity procedures are required
for manuscript claims?

## OQ-018 — Exact manuscript v0.1 domain geometries
Status: OPEN — VERIFY FROM CURRENT APPROVED CONFIG/EVIDENCE

The domain set NH, ROI, and ROI_X4 is approved for manuscript v0.1, but exact current
geometry/masks must be verified from approved project evidence rather than copied from
legacy assumptions.

## Registry rule

Each open question must eventually record:
- decision status;
- scope;
- evidence;
- alternatives;
- rationale;
- consequences;
- approval;
- implementation references;
- Git adoption commit.

Questions may be split into centre-specific or metric-specific subquestions without
changing the shared architecture.
