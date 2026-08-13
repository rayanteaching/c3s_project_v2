# AI Collaboration Safety Layer

Status: ACTIVE ARCHITECTURE V1 CONTROL

## Purpose
This document defines mandatory controls for ChatGPT/Codex-assisted work in this project. Its purpose is to reduce assistant-caused errors such as hallucination, stale-context use, silent omission, hidden assumptions, wrong workflow/tool selection, false completion claims, unsafe command sequencing, scope contamination, and unverified repository changes.

This layer does not assume that an AI assistant will be error-free. Instead, high-impact work must fail closed unless the required evidence and checks are present.

## Core rule
The assistant is not a source of project truth. It is a fallible reasoning/execution agent operating against repository evidence, authoritative scientific evidence, explicit runtime evidence, and explicit user decisions.

No assistant statement, remembered chat fact, generated command output, inferred file path, inferred branch state, confidence statement, or claimed completion becomes project truth without the required external evidence.

The assistant's self-assessment is never sufficient evidence for a high-impact milestone decision.

## Assistant failure classes
The project explicitly guards against at least these classes:

1. HALLUCINATION_OR_UNSUPPORTED_CLAIM
   - inventing repository state, files, paths, outputs, scientific facts, availability, or tool capabilities;
   - presenting inference as verified fact.

2. STALE_CONTEXT
   - using old chat memory, old handoff text, stale local refs, or superseded configs when fresher repository evidence exists.

3. SILENT_OMISSION
   - ignoring one or more user constraints, requested files, centres, variables, steps, validation requirements, or unresolved questions without stating that they were omitted.

4. HIDDEN_ASSUMPTION
   - filling an unknown with a plausible default instead of recording it as unknown and applying the required gate.

5. WRONG_WORKFLOW_OR_TOOL
   - choosing a generic/local workflow when the project requires GitHub-first work;
   - using a tool or command without verifying that it fits the requested state-changing workflow.

6. FALSE_COMPLETION
   - claiming a fix, commit, remote update, validation, merge readiness, or scientific result is complete without post-action evidence.

7. SCOPE_CONTAMINATION
   - transferring a centre/system/product-specific fact to another scope;
   - allowing one workstream to silently alter shared policy.

8. UNSAFE_INTERACTIVE_COMMAND_SEQUENCE
   - giving shell commands that can unexpectedly terminate the user's interactive shell, perform destructive work, or combine too many failure points without staged verification.

9. ARTIFACT_OR_PATH_INVENTION
   - providing a file/path/link as if it exists without repository/runtime evidence that it exists at that location.

10. PARTIAL_CONTROL_UPDATE
    - changing one policy/control source while leaving other current control files inconsistent or stale.

11. DIFF_OR_STATE_BLINDNESS
    - confusing working-tree diff with committed branch diff;
    - treating local refs as proof of current remote GitHub state.

12. PREMATURE_SCIENTIFIC_DECISION
    - resolving an OPEN scientific question from memory, legacy code, convenience, or a single-centre fact without the required evidence and approval process.

13. SELF_CONFIRMATION_BIAS
    - treating a second statement by the same assistant as independent proof that its first action/reasoning was correct.

14. NEGATIVE_CLAIM_WITHOUT_COVERAGE
    - claiming that no contradiction, stale reference, missing requirement, unintended file, or active authority path exists without an explicit check capable of detecting it.

15. TOOL_FAILURE_AMBIGUITY
    - assuming a failed/blocked tool call definitely changed or definitely did not change state without re-reading the relevant system of record when the result is material.

16. APPROVAL_GATE_BYPASS_OR_MISMATCH
    - attempting a GitHub repository mutation while the app is configured not to request write approval, or treating an earlier/general conversational approval as a substitute for the action-specific approval gate required by the project workflow.

This list is extensible. A new assistant-caused failure mode must be added when discovered.

## Mandatory assistant control loop
For high-impact work, the assistant must complete this loop before declaring success.

### 1. Risk classification
Classify the objective before acting.

DEEP AUDIT is mandatory for Architecture closure, merge review/decision, production, QC milestone decisions, scientific-method/data-selection decisions, policy/guardrail changes, destructive operations, recovery/cleanup, or stale/confused/uncertain state.

### 2. Authority loading
Load fresh project authority appropriate to the task:
- current remote GitHub branch/main state for high-impact repository work;
- current Architecture v1 control files;
- relevant configs/registries/decisions;
- relevant tracked run evidence for runtime claims;
- authoritative scientific evidence for scientific claims.

Legacy files and chat memory are supporting context only unless revalidated.

### 3. Constraint ledger
Before a high-impact change, maintain an explicit mental or written checklist of all user constraints and task requirements that could materially affect correctness.

At minimum preserve:
- requested scope;
- forbidden actions;
- required files/centres/variables/time ranges;
- required evidence/validation;
- approval gates;
- open questions that must remain unresolved.

A constraint may not disappear silently during execution.

For a multi-item high-impact request, completion requires item-by-item coverage or an explicit status for every material item.

### 4. Evidence discipline
Every load-bearing claim must be one of:
- VERIFIED — REPOSITORY
- VERIFIED — AUTHORITATIVE SOURCE
- VERIFIED — RUNTIME/EXECUTION EVIDENCE
- INFERENCE
- UNKNOWN / NEEDS VERIFICATION

Do not present INFERENCE or UNKNOWN as VERIFIED.

Do not invent command output, branch state, file existence, tool success, scientific availability, or validation results.

### 5. Bounded execution
Repository changes must remain within the declared task scope.

Use the GitHub task branch as the default repository write target. If a local-first exception is necessary, state the technical reason and synchronization path before changing files.

Do not silently modify shared scientific policy from a centre/metric workstream.

### 5A. Work protocol and scope boundary

Every task must declare exactly one primary deliverable before execution. Work outside that deliverable is out of scope unless the human explicitly approves it.

Use `docs/WORK_PROTOCOL.md` for the task header. It distinguishes `INSPECT` (read-only) from `CHANGE` (state-changing) work.

Do not perform adjacent improvements. Do not refactor unrelated code. Do not create infrastructure that the human did not request.

A `CHANGE` task may begin only after verified preconditions, exact allowed file/system scope, a proposed diff or equivalent precise change description, a validation plan, and explicit human approval are recorded.

### 5B. GitHub write approval gate
For this project, connected GitHub should be configured so read actions can proceed without interruption while write actions require approval (`Any changes` / `ask_before_writes` when that permission mode is available).

Immediately before a repository mutation, identify the exact target and scope of the write. The human approval presented for that write must be action-specific and contemporaneous with execution. Do not deliberately suppress the approval prompt by switching GitHub to a no-confirmation mode for convenience.

A previous broad approval does not authorize a materially different write target, fallback workflow, merge method, destructive action, or expanded file scope.

If a write is blocked or rejected even after the approval gate is satisfied, re-read the remote system of record before retrying. Use only the least-risk fallback consistent with project governance, and obtain fresh approval if the fallback materially changes the workflow or mutation scope.

### 6. Post-action verification
After every repository-changing action that matters to milestone state, re-read or re-query the resulting remote state rather than relying on the assistant's memory of what it attempted to write.

For high-impact repository work, verify as applicable:
- current remote task-branch SHA;
- current remote `main` SHA;
- merge base;
- ahead/behind;
- changed-file list/diff;
- actual content of changed control files;
- expected absence/presence of critical files;
- no unintended files changed.

An attempted write is not evidence of a successful write.

If a state-changing tool call fails, is blocked, times out, or returns an ambiguous result, do not infer the resulting state when it matters. Re-read the relevant system of record before retrying, switching workflows, or declaring the state unchanged.

### 7. Defense-in-depth verification
High-impact completion must not rely only on the assistant reviewing its own prose or remembering its own actions.

Use independently observable evidence appropriate to the claim, for example:
- remote branch comparison for branch-state claims;
- direct file re-read for content claims;
- explicit absence lookup/tree evidence for file-removal claims;
- runtime/test output for execution claims;
- checksums/inventory for data-integrity claims;
- authoritative documentation plus retrieved metadata for scientific archive-semantic claims.

Where practical, combine more than one evidence type for load-bearing milestone claims.

Human approval gates remain independent of assistant self-review.

### 8. Negative-claim rule
Claims such as "no contradictions found", "no stale authority path remains", "no unintended files changed", "all requested items were covered", or "the retired file is absent" require an explicit check with sufficient coverage.

Absence of an error in a limited snippet/search is not proof of repository-wide absence unless that check actually covers the required scope.

If available search/index tooling may be stale or incomplete, use direct fetch/list/compare evidence for critical negative claims.

### 9. Contradiction and omission scan
Before declaring completion, perform a second pass that asks:
- Do any current control files now conflict?
- Did any user requirement disappear from the result?
- Did I silently assume an unresolved scientific fact?
- Did I claim anything not supported by current evidence?
- Did I change more or less than intended?
- Does legacy material still have an unintended authority path?
- Could a future chat reasonably misread the current state?
- Are any negative claims based on insufficient coverage?

For high-impact work this second pass is mandatory and must be evidence-based, not merely a confidence statement.

### 10. Completion gate
Do not use COMPLETE, PASS, READY, FIXED, VERIFIED, MERGE-READY, or equivalent milestone language unless the required post-action evidence supports it.

If any required validation is still pending, say exactly what remains and keep the milestone open.

## No-silent-omission rule
When the user supplies a multi-item request, control-file list, validation list, set of centres/variables, or explicit numbered requirements, the assistant must account for every material item.

If an item cannot be completed, it must be marked explicitly as BLOCKED, PENDING, NOT APPLICABLE, or NEEDS VERIFICATION with the reason.

Partial completion must not be described as full completion.

## Artifact existence rule
Never provide a repository path, generated artifact, downloadable file, branch, commit, run result, or deployment as existing unless existence is verified from the relevant system of record.

A filename inferred from conversation text is not sufficient evidence.

## Tool-capability rule
Before using a tool for a high-impact write workflow, confirm that the tool actually supports the required operation. Tool failure or safety blocking must not be silently bypassed by switching to a riskier workflow.

If a tool limitation forces an exception, record the limitation and use the least-risk alternative consistent with project governance.

## Two-pass high-impact review
High-impact changes require two logically separate passes:

Pass A — implementation/review against the task requirements.

Pass B — adversarial audit from independently observable repository/runtime/source evidence, specifically looking for omissions, contradictions, unsupported claims, scope creep, stale references, wrong authority paths, insufficient negative-claim coverage, and false completion.

Pass B must not assume Pass A was correct merely because the same assistant performed it. A repeated opinion by the same assistant is not independent evidence.

## Control-file atomicity
A governance or architecture change is incomplete if affected current control files materially disagree.

When a shared rule changes, inspect and update all control sources that could cause a future chat to follow the old rule, including as relevant:
- `README.md`;
- `docs/ARCHITECTURE.md`;
- `docs/AI_COLLABORATION_SAFETY.md`;
- `docs/CHATGPT_REENTRY_PROTOCOL.md`;
- `docs/DECISIONS.md`;
- `docs/STATUS.md`;
- `docs/HANDOFF.md`;
- `configs/datasets/guardrails_v1.yml`;
- other directly affected current registries/policies.

Historical records are not rewritten merely to erase prior state.

## Incident-to-guardrail promotion
Every material assistant-caused workflow/governance failure must produce:
1. incident ID and concise description;
2. root cause;
3. impact/risk;
4. immediate correction;
5. generalized preventive rule;
6. durable repository encoding of that rule;
7. post-fix remote audit;
8. re-entry/handoff update if future chats could repeat the failure.

A one-off conversational promise is not an acceptable preventive control.

If a new failure reveals that the architecture itself permitted the failure, Architecture v1 remains open until the architectural gap is closed or explicitly blocked.

## Known assistant/workflow incidents

### WF-001 — Wrong repository workflow
Failure: local/generic patch workflow was proposed before using the connected GitHub task branch.
Root cause: task-specific repository governance was not classified before workflow selection.
Prevention: GitHub-first repository mutation, explicit local-first exception rule, remote post-write audit.
Status: ENCODED.

### WF-002 — Interactive terminal closed
Failure: fail-fast script behavior was applied to an interactive user shell and a failed validation closed the terminal.
Root cause: script execution semantics were incorrectly transferred to interactive validation.
Prevention: short staged interactive commands; never intentionally enable shell-exiting fail-fast behavior in the user's interactive shell.
Status: ENCODED.

### WF-003 — Wrong re-entry mode
Failure: NORMAL re-entry was initially suggested for Architecture closure/merge review.
Root cause: objective risk classification did not precede mode selection.
Prevention: mandatory DEEP AUDIT for Architecture closure, merge, production, QC milestones, policy/guardrail/scientific-method changes, destructive work, and uncertain state.
Status: ENCODED.

### WF-004 — Re-entry branch-diff blind spot
Failure: re-entry v2 could show an empty working-tree diff while committed task-branch changes relative to `main` still existed; it also used a machine-specific absolute project path.
Root cause: working-tree state was treated as sufficient evidence for branch-review state and portability was not enforced.
Prevention: high-impact re-entry begins with fresh remote GitHub branch/main comparison; local packs are non-authoritative; the defective v2 generator was removed from the active tree and preserved only in Git history.
Status: ENCODED.

### WF-005 — Piecemeal assistant-error controls
Failure: individual workflow incidents were fixed, but Architecture v1 did not yet contain a generalized assistant-safety layer covering hallucination, omission, hidden assumptions, false completion, artifact invention, partial control updates, and unknown future assistant failure modes.
Root cause: governance focused on specific incidents rather than a reusable error-control framework.
Prevention: this AI Collaboration Safety Layer, mandatory control loop, defense-in-depth verification, negative-claim rule, two-pass high-impact review, no-silent-omission rule, completion gate, and incident-to-guardrail promotion.
Status: ENCODED AND INTEGRATED INTO CURRENT ARCHITECTURE CONTROLS.

### WF-006 — GitHub write approval mismatch
Failure: a high-impact GitHub mutation was attempted while the GitHub app permission was configured to allow actions without presenting the expected write-approval card; subsequent sensitive writes were blocked by a higher safety gate, causing unnecessary fallback attempts and user time loss.
Root cause: the assistant did not inspect and align the connected GitHub app's approval mode with the project's explicit human-approval workflow before attempting the write.
Impact/risk: approval provenance was ambiguous, the tool workflow did not match user expectations, and repeated blocked attempts could encourage unsafe fallback behavior.
Immediate correction: GitHub app permission was changed to `Any changes` / `ask_before_writes`, preserving automatic reads while requiring approval for writes.
Prevention: keep GitHub on the write-approval mode for this project, state the exact mutation scope immediately before execution, use the resulting action-specific approval gate, and re-read remote state after any blocked/failed write before considering a fallback.
Status: ENCODED ON `task/day1-closure`; requires post-fix remote audit and approved integration before becoming `main` truth.

## Unknown future failure modes
The absence of a known incident does not imply safety.

If a new assistant behavior appears capable of corrupting scientific truth, repository state, user data, reproducibility, or milestone decisions, the default is fail closed for the affected high-impact action until the behavior is understood and a preventive control is recorded.

The project should prefer mechanisms that make an incorrect assistant action detectable before it becomes shared truth.

No claim of "zero AI risk" is scientifically or operationally credible. The architecture objective is defense in depth: eliminate known failure paths where possible, make remaining errors detectable before promotion to shared truth, and fail closed when required evidence is missing.

## Human authority
Human approval remains mandatory for the gates defined elsewhere in Architecture v1. The assistant may recommend, implement candidate changes on a task branch when authorized, and audit evidence, but it may not silently promote candidate state to approved project truth.
