# Work Protocol

Status: ACTIVE OPERATIONAL CONTROL

Use this short header for every ChatGPT/Codex task.

```text
Mode: INSPECT | CHANGE
Primary deliverable: <exactly one concrete output>
Authority: <fresh remote GitHub SHA>
Preconditions: <facts that must be verified first>
Allowed scope: <files, systems, centre, or data range>
Forbidden: <adjacent work explicitly excluded>
Evidence status: VERIFIED | INFERENCE | TBD
Next action: <one action only>
```

## Rules

- `INSPECT` is read-only. It may investigate and report; it may not write, download production data, merge, alter configuration, or adopt a decision.
- `CHANGE` requires verified preconditions, exact allowed scope, proposed diff or equivalent precise change description, validation plan, and explicit action-specific human approval.
- Declare exactly one primary deliverable. Everything else is out of scope unless separately approved.
- Do not perform adjacent improvements.
- Do not refactor unrelated code.
- Do not create infrastructure the human did not request.
- Classify load-bearing statements as VERIFIED, INFERENCE, or TBD. A required TBD blocks the affected action.
- This protocol adds operational clarity; it does not replace existing approval gates, evidence requirements, or fail-closed rules.
