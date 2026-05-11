# ChatGPT Re-entry Protocol

## Purpose

This document defines the official procedure for starting or restarting any ChatGPT-assisted work on this repository.

The goal is to prevent decisions based on stale conversation memory and to force every new continuation to start from the current repository state.

## Repository-first rule

The current repository state is the final source of truth.

If remembered chat context conflicts with tracked repository files, the repository files win.

No new design, execution, correction, download, QC step, merge, branch decision, or policy change should be made before reading the official pre-read files.

## Official project root

/home/fibi/projects/c3s_project_v2

## Mandatory pre-read files

Every new ChatGPT project chat must start by reading these files:

docs/CHATGPT_REENTRY_PROTOCOL.md
docs/DECISIONS.md
docs/SEASONAL_DOWNLOAD_POLICY.md
docs/SEASONAL_KNOWN_ISSUES.md
docs/GIT_WORKFLOW.md
docs/STATUS.md
docs/HANDOFF.md
docs/RUNBOOK.md
configs/datasets/c3s_seasonal_systems.yml
configs/datasets/c3s_seasonal_variables.yml

If another policy, runbook, checklist, or operational file becomes official workflow state, it must be added to this list.

## Mandatory pre-read command

cd /home/fibi/projects/c3s_project_v2

cat docs/CHATGPT_REENTRY_PROTOCOL.md
cat docs/DECISIONS.md
cat docs/SEASONAL_DOWNLOAD_POLICY.md
cat docs/SEASONAL_KNOWN_ISSUES.md
cat docs/GIT_WORKFLOW.md
cat docs/STATUS.md
cat docs/HANDOFF.md
cat docs/RUNBOOK.md
cat configs/datasets/c3s_seasonal_systems.yml
cat configs/datasets/c3s_seasonal_variables.yml

## Mandatory Git report

Every new ChatGPT project chat must include a fresh Git report generated from the repository root.

Minimum required commands:

git status --short --branch
git branch -vv
git log --oneline --decorate --graph -n 30
git log --oneline --decorate --graph --all -n 40
git diff --stat
git diff --name-status
git diff --cached --stat
git diff --cached --name-status
git ls-files
git status --short --ignored
tree -a -L 4 -I '.git|__pycache__|*.pyc|data/raw|data/processed|logs'

## Required re-entry pack sections

Every Project Re-entry Pack must contain these sections:

1. Project identity
2. Hard rules
3. Current objective
4. What not to do
5. Git report
6. Official state files
7. Current repository tree
8. Tracked workflow files
9. Modified and untracked files
10. Next requested assistant action

## Required opening instruction for a new ChatGPT project chat

Use this instruction at the top of every new project chat:

We are continuing the C3S seasonal/ERA5 project.

Do not rely on memory from previous chats.

The current repository state is the final source of truth.

First read the Project Re-entry Pack below, including the Git report and all official state files.

Then summarize:
1. current branch,
2. current milestone,
3. completed work,
4. blockers,
5. risks,
6. next safe step.

Do not give any execution command, download command, QC command, merge command, or new design decision until that summary is complete.

## Tracking policy reminder

Track lightweight text-based workflow files required for reproduction, continuation, understanding, or audit.

Track:

README.md
docs/
configs/
scripts/
runs/ metadata
data/inventory/
env/
*.md
*.txt
*.json
*.yml
*.yaml
*.csv

Do not track:

data/raw/
data/processed/
logs/
large binary files
credentials
secrets

## Milestone close rule

After every important milestone:

1. Update docs/STATUS.md.
2. Update docs/HANDOFF.md.
3. Update docs/DECISIONS.md if a new project decision was made.
4. Update run metadata under runs/ if a run was started, completed, failed, resumed, or verified.
5. Update inventory snapshots under data/inventory/ if data state changed.
6. Commit the workflow state to Git.

## Output formatting rule for ChatGPT

For repository file content, shell command blocks, or copy-paste instructions, ChatGPT must return exactly one fenced code block and nothing outside it.

Do not split one file across multiple code blocks.

Do not add explanations before or after the code block.

Keep paths, filenames, commands, and technical text in English.
