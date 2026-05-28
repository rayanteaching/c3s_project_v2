# ChatGPT Re-entry Protocol

## Purpose

This document defines how to start or restart ChatGPT-assisted work on this repository without relying on stale chat memory.

The goal is not to load the entire repository into every chat. The goal is to provide the minimum required evidence for the next decision, using predefined evidence checklists and escalating to deep audit mode when risk is high.

## Core rule

The repository is the durable memory and source of truth.

ChatGPT and Codex are temporary reasoning and execution assistants. They must not be treated as the project state database.

If chat memory, user recollection, or a previous summary conflicts with current repository evidence, the repository evidence wins.

## Official project root

/home/fibi/projects/c3s_project_v2

## Evidence priority

Use evidence in this order:

1. Current repository files and command output
2. Generated Project Re-entry Pack from the repository
3. User-provided current terminal output
4. User statements
5. Earlier chat memory, only as weak context

If required evidence is missing, say what is missing and what command or file is needed. Do not guess.

## Re-entry modes

This project uses two re-entry modes.

### Normal re-entry mode

Use normal mode for:
- planning,
- discussion,
- documentation edits,
- small script review,
- low-risk continuation,
- non-destructive diagnosis.

Normal mode should include:

1. Current objective
2. Git status short branch
3. Branch list
4. Recent commits on the current branch
5. Current STATUS.md
6. Current HANDOFF.md
7. Relevant DECISIONS.md excerpts when the task touches project decisions
8. Relevant configs or scripts only when they affect the current task

Normal mode should not include full tracked-file lists, full repository trees, long histories, all inventories, all logs, or unrelated literature notes.

### Deep audit re-entry mode

Use deep audit mode for:
- production downloads,
- merge decisions,
- branch cleanup,
- policy changes,
- QC pass/fail declarations,
- scientific-method decisions,
- destructive file operations,
- recovery after confusing or failed workflows,
- any situation where repository state, data state, or scientific interpretation is uncertain.

Deep audit mode should include, as relevant:

1. Full Git status and branch graph
2. Working tree and staged diffs
3. Relevant official policies
4. Relevant configs
5. Relevant scripts
6. Relevant run metadata
7. Relevant inventories
8. Relevant logs or summarized log tails
9. File existence checks
10. Checksums when data integrity matters
11. Literature or official scientific references when the decision is scientific

## Mandatory opening behavior

At the beginning of a new project chat or after a long/confused workflow, ChatGPT must first summarize:

1. Current branch
2. Current objective
3. Current milestone
4. Completed work
5. Current blockers
6. Current risks
7. Next safe step
8. Missing evidence, if any

ChatGPT must not provide download commands, QC pass/fail declarations, merge commands, destructive commands, or new policy/scientific decisions before this summary is complete.

## Evidence checklist rule

Do not rely on the model to freely guess what context is needed.

Use predefined evidence checklists by task type. Include required evidence first. Ask for additional evidence only when a specific uncertainty remains.

Examples:

### Documentation-only change

Required evidence:
- git status --short --branch
- target document
- current objective
- diff before commit

### Script change

Required evidence:
- git status --short --branch
- target script
- relevant configs
- expected behavior
- test or validation command
- diff before commit

### Commit

Required evidence:
- git status --short --branch
- git diff --stat
- git diff --name-status
- staged diff if staging already happened
- forbidden-file check when data/log paths may be involved

### Merge

Required evidence:
- git status --short --branch
- git branch -vv
- git log --oneline --decorate --graph --all -n 40
- git diff target..source --stat
- milestone closure evidence
- updated STATUS.md and HANDOFF.md

### Production download

Required evidence:
- deep audit mode
- current policy files
- relevant configs
- target script
- output path
- run metadata plan
- disk-space check
- credentials outside Git
- expected file count
- QC plan

### QC pass/fail declaration

Required evidence:
- QC policy or criteria
- QC script
- QC outputs
- inventory
- relevant logs or summaries
- exact pass/fail criteria

### Scientific-method decision

Required evidence:
- current project policy
- relevant configs
- scientific source notes under docs/literature/ or official documentation
- alternatives considered
- consequences for scripts/configs/QC/data interpretation
- DECISIONS.md update if adopted

## Scientific evidence layer

Scientific papers, books, official documentation, and technical references should be summarized under:

docs/literature/

These notes are evidence, not official decisions.

A scientific note becomes an official project decision only when summarized in docs/DECISIONS.md with:
- the decision,
- evidence used,
- reason,
- alternatives considered when relevant,
- consequences,
- affected files,
- status.

Do not load all literature notes into normal chats. Retrieve only the notes relevant to the current scientific decision.

## Human approval gates

ChatGPT and Codex must not autonomously approve or execute high-risk transitions.

Human approval is required before:
- commits,
- merges,
- production downloads,
- destructive file operations,
- policy changes,
- scientific interpretation changes,
- QC pass/fail declarations.

## Tracking policy reminder

Track lightweight workflow-critical files required for reproduction, continuation, understanding, verification, or audit.

Track:
- README.md
- docs/
- configs/
- scripts/
- runs/ metadata
- data/inventory/
- env/
- lightweight *.md, *.txt, *.json, *.yml, *.yaml, *.csv files when part of the official workflow

Do not track:
- data/raw/
- data/processed/
- logs/
- large binary files
- GRIB/NetCDF primary data files
- credentials
- secrets
- bulky binary artifacts

## Milestone closure rule

After every important milestone:

1. Update docs/STATUS.md.
2. Update docs/HANDOFF.md.
3. Update docs/DECISIONS.md if a new decision was made.
4. Update docs/RUNBOOK.md if reusable commands or checks changed.
5. Update run metadata under runs/ if a run was started, completed, failed, resumed, or verified.
6. Update inventory snapshots under data/inventory/ if data state changed.
7. Review Git status and diff.
8. Commit only lightweight workflow state, and only after user approval.

## Output formatting rule

For repository file content, shell command blocks, or copy-paste-ready terminal procedures:

1. Return the artifact inside exactly one fenced code block.
2. Do not split one file across multiple code blocks.
3. If the answer is a file, output only exact file content.
4. If the answer is a shell procedure, output exact commands in execution order.
5. Keep paths, filenames, commands, code, configuration text, and technical artifacts in English.

For discussion, review, diagnosis, teaching, and planning, normal explanatory text is allowed.

## Long text editing rule

For long file content, prefer editing with vi or applying a reviewed patch instead of pasting long heredoc blocks into the terminal.

Use heredoc only for short, low-risk content.
