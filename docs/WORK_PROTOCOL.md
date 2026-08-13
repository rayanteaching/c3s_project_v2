# Work Protocol

Status: ACTIVE OPERATIONAL CONTROL

Principle: **Fast by default, strict when risky.** Verification, review, and approval depth must be proportional to risk; low-risk work must not inherit production-level ceremony, while uncertainty or high blast radius escalates the workflow.

Use this short header for every ChatGPT/Codex task.

```text
Mode: INSPECT | CHANGE
Risk: LOW | MEDIUM | HIGH
Primary deliverable: <one concrete, bounded, verifiable output>
Authority: <fresh remote GitHub SHA appropriate to the risk>
Preconditions: <facts that must be verified first>
Allowed scope: <exact files, systems, centre, or data range>
Forbidden: <adjacent work explicitly excluded>
Evidence status: VERIFIED | INFERENCE | TBD
Validation: <proportional checks for this change>
Next action: <one action only>
```

## Risk levels

### LOW
Use for typo fixes, ordinary documentation edits, narrow non-destructive maintenance, and simple read-only inspection where project truth is clear.

Workflow: minimal fresh verification -> bounded change/inspection -> proportional validation -> diff/state check.

Do not run a Deep Audit merely because GitHub is involved. If a contradiction, unclear authority, sensitive target, unexpected diff, or material uncertainty appears, escalate to MEDIUM or HIGH.

### MEDIUM
Use for normal code/config/document-control changes with meaningful repository impact but no production, architecture, security, destructive, or scientific-policy decision.

Workflow: fresh verification -> scope/preflight -> task branch -> bounded change -> tests/validation -> remote diff -> PR/review.

A PR is required before MEDIUM changes become `main` truth.

### HIGH
Use for architecture or governance changes, guardrails/security/permissions, scientific-method or data-selection decisions, production actions, deploys, merges of high-impact work, destructive operations, QC milestone decisions, recovery/cleanup, or stale/confused/uncertain state.

Workflow: fresh remote/live verification -> full preflight and constraint ledger -> Deep Audit -> TBD/fail-closed gate -> ADR when architecture changes -> bounded implementation -> tests/runtime evidence as applicable -> adversarial second pass -> PR/review -> independent sensitive-operation approval.

A PR is required before HIGH repository changes become `main` truth.

## Rules

- `INSPECT` is read-only. It may investigate and report; it may not write, download production data, merge, deploy, alter configuration, or adopt a decision.
- `CHANGE` requires verified preconditions, exact allowed scope, proposed diff or equivalent precise change description, a validation plan, and explicit human approval appropriate to the risk.
- Declare exactly one primary deliverable. It must be concrete, bounded, and independently verifiable. Everything else is out of scope unless separately approved.
- Do not perform adjacent improvements.
- Do not refactor unrelated code.
- Do not create infrastructure the human did not request.
- Classify load-bearing statements as VERIFIED, INFERENCE, or TBD. A required TBD blocks the affected action.
- Verification depth is proportional to risk. LOW uses the smallest check that establishes the needed authority; HIGH requires the full remote/deep-audit evidence path.
- One explicit approval may cover one predeclared bounded change-set when target branch, file/system scope, intended changes, and validation are already stated. That approval may cover the in-scope branch writes, commits, validation, and PR creation/preparation while the scope and method remain unchanged.
- A scope expansion, materially different fallback workflow, changed target, or changed mutation method requires fresh approval.
- **Merge, deploy, delete/destructive operations, and production writes/downloads always require their own independent approval immediately before that sensitive operation.** They are never implied by approval of the implementation change-set.
- Architecture changes require an Architecture Decision Record (ADR) before adoption. Ordinary typo/documentation maintenance and centre-specific evidence collection do not require an ADR. Scientific decisions continue to use `docs/SCIENTIFIC_DECISION_TRACEABILITY.md`; an ADR does not replace that process.
- When project tools are available, ChatGPT/Codex is responsible for performing repository inspection, branch work, bounded edits, diffs, applicable tests/validation, and PR preparation/creation. Do not transfer routine executable work to the human merely for assistant convenience. Human involvement is reserved for decisions, approvals, credentials/access, or actions the available tools genuinely cannot perform.
- This protocol adds operational clarity; it does not replace existing evidence requirements, fail-closed scientific rules, or independent sensitive-operation gates.
