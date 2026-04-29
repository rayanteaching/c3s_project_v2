#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/home/fibi/projects/c3s_project_v2"
cd "$PROJECT_ROOT"

OBJECTIVE="${1:-REPLACE_WITH_CURRENT_OBJECTIVE}"

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
BRANCH="$(git rev-parse --abbrev-ref HEAD | tr '/ ' '__')"
OUT_DIR="runs/reentry"
OUT_FILE="${OUT_DIR}/chatgpt_reentry_pack_${STAMP}_${BRANCH}.md"

mkdir -p "$OUT_DIR"

append_section() {
  local title="$1"
  echo
  echo "============================================================"
  echo "$title"
  echo "============================================================"
  echo
}

{
  echo "PROJECT RE-ENTRY PACK"
  echo
  echo "Generated UTC: ${STAMP}"
  echo

  append_section "A. PROJECT IDENTITY"
  echo "Project: C3S seasonal/ERA5 repository"
  echo "Project root: ${PROJECT_ROOT}"
  echo "Current branch: $(git rev-parse --abbrev-ref HEAD)"
  echo "Current commit: $(git rev-parse HEAD)"

  append_section "B. REQUIRED OPENING INSTRUCTION FOR THE NEW CHATGPT PROJECT CHAT"
  echo "We are continuing the C3S seasonal/ERA5 project."
  echo
  echo "Do not rely on memory from previous chats."
  echo
  echo "The current repository state is the final source of truth."
  echo
  echo "First read the Project Re-entry Pack below, including the Git report and all official state files."
  echo
  echo "Then summarize:"
  echo "1. current branch,"
  echo "2. current milestone,"
  echo "3. completed work,"
  echo "4. blockers,"
  echo "5. risks,"
  echo "6. next safe step."
  echo
  echo "Do not give any execution command, download command, QC command, merge command, or new design decision until that summary is complete."

  append_section "C. HARD RULES"
  echo "Repository state is final."
  echo "Do not decide from remembered chat context."
  echo "Read official pre-read files before every continuation, design, execution, correction, download, QC step, merge, or policy decision."
  echo "Track lightweight workflow-critical text files."
  echo "Do not track raw data, processed data, logs, large binary files, credentials, or secrets."
  echo "After every milestone, update STATUS and HANDOFF."
  echo "Update DECISIONS when a new decision is made."
  echo "Update run metadata and inventory snapshots when operational state changes."
  echo "For commands and file content, ChatGPT output must be exactly one fenced code block only."

  append_section "D. CURRENT OBJECTIVE"
  echo "${OBJECTIVE}"

  append_section "E. WHAT NOT TO DO"
  echo "Do not use old chat memory as a source of truth."
  echo "Do not assume the active branch."
  echo "Do not assume a milestone is closed unless STATUS, HANDOFF, run metadata, inventory, and Git history prove it."
  echo "Do not propose downloads before reading policy and state files."
  echo "Do not track data/raw, data/processed, logs, credentials, secrets, or large binaries."
  echo "Do not change official policy files casually."
  echo "Do not merge branches before checking status, diff, branch relation, and milestone closure."

  append_section "F. GIT STATUS SHORT BRANCH"
  git status --short --branch

  append_section "G. BRANCHES"
  git branch -vv

  append_section "H. RECENT COMMITS ON CURRENT BRANCH"
  git log --oneline --decorate --graph -n 30

  append_section "I. RECENT COMMITS ACROSS ALL BRANCHES"
  git log --oneline --decorate --graph --all -n 40

  append_section "J. WORKING TREE DIFF STAT"
  git diff --stat || true

  append_section "K. WORKING TREE DIFF NAME-STATUS"
  git diff --name-status || true

  append_section "L. STAGED DIFF STAT"
  git diff --cached --stat || true

  append_section "M. STAGED DIFF NAME-STATUS"
  git diff --cached --name-status || true

  append_section "N. REPOSITORY TREE"
  tree -a -L 4 -I '.git|__pycache__|*.pyc|data/raw|data/processed|logs' || find . -maxdepth 4 -not -path './.git/*' -not -path './data/raw/*' -not -path './data/processed/*' -not -path './logs/*' | sort

  append_section "O. TRACKED FILES"
  git ls-files

  append_section "P. STATUS INCLUDING IGNORED FILES"
  git status --short --ignored

  append_section "Q. OFFICIAL STATE FILE: docs/CHATGPT_REENTRY_PROTOCOL.md"
  cat docs/CHATGPT_REENTRY_PROTOCOL.md

  append_section "R. OFFICIAL STATE FILE: docs/DECISIONS.md"
  cat docs/DECISIONS.md

  append_section "S. OFFICIAL STATE FILE: docs/SEASONAL_DOWNLOAD_POLICY.md"
  cat docs/SEASONAL_DOWNLOAD_POLICY.md

  append_section "T. OFFICIAL STATE FILE: docs/SEASONAL_KNOWN_ISSUES.md"
  cat docs/SEASONAL_KNOWN_ISSUES.md

  append_section "U. OFFICIAL STATE FILE: docs/STATUS.md"
  cat docs/STATUS.md

  append_section "V. OFFICIAL STATE FILE: docs/HANDOFF.md"
  cat docs/HANDOFF.md

  append_section "W. OFFICIAL CONFIG FILE: configs/datasets/c3s_seasonal_systems.yml"
  cat configs/datasets/c3s_seasonal_systems.yml

  append_section "X. OFFICIAL CONFIG FILE: configs/datasets/c3s_seasonal_variables.yml"
  cat configs/datasets/c3s_seasonal_variables.yml

  append_section "Y. NEXT REQUESTED ASSISTANT ACTION"
  echo "Read this pack first."
  echo "Summarize the real repository state."
  echo "Identify the next safe step for the objective."
  echo "Do not provide operational commands until the state summary is complete."
} > "$OUT_FILE"

sha256sum "$OUT_FILE" > "${OUT_FILE}.sha256"

echo "$OUT_FILE"
echo "${OUT_FILE}.sha256"
