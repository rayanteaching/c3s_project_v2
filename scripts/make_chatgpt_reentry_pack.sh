#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/home/fibi/projects/c3s_project_v2"
cd "$PROJECT_ROOT"

MODE="${1:-normal}"
OBJECTIVE="${2:-REPLACE_WITH_CURRENT_OBJECTIVE}"

if [[ "$MODE" != "normal" && "$MODE" != "deep" ]]; then
  echo "Usage: $0 [normal|deep] \"CURRENT_OBJECTIVE\"" >&2
  exit 2
fi

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
BRANCH="$(git rev-parse --abbrev-ref HEAD | tr '/ ' '__')"
OUT_DIR="runs/reentry"
OUT_FILE="${OUT_DIR}/chatgpt_reentry_pack_${STAMP}_${BRANCH}_${MODE}.md"

mkdir -p "$OUT_DIR"

append_section() {
  local title="$1"
  echo
  echo "============================================================"
  echo "$title"
  echo "============================================================"
  echo
}

cat_if_exists() {
  local path="$1"
  if [[ -f "$path" ]]; then
    cat "$path"
  else
    echo "MISSING: $path"
  fi
}

{
  echo "PROJECT RE-ENTRY PACK"
  echo
  echo "Generated UTC: ${STAMP}"
  echo "Mode: ${MODE}"
  echo

  append_section "A. PROJECT IDENTITY"
  echo "Project: C3S seasonal/ERA5 repository"
  echo "Project root: ${PROJECT_ROOT}"
  echo "Current branch: $(git rev-parse --abbrev-ref HEAD)"
  echo "Current commit: $(git rev-parse HEAD)"

  append_section "B. CURRENT OBJECTIVE"
  echo "${OBJECTIVE}"

  append_section "C. OPENING INSTRUCTION FOR CHATGPT"
  echo "We are continuing the C3S seasonal/ERA5 project."
  echo "Do not rely on memory from previous chats."
  echo "The repository is the durable memory and source of truth."
  echo "Use this re-entry pack as repository evidence."
  echo
  echo "First summarize:"
  echo "1. current branch,"
  echo "2. current objective,"
  echo "3. current milestone,"
  echo "4. completed work,"
  echo "5. blockers,"
  echo "6. risks,"
  echo "7. next safe step,"
  echo "8. missing evidence, if any."
  echo
  echo "Do not provide download commands, QC pass/fail declarations, merge commands, destructive commands, or new policy/scientific decisions before that summary is complete."

  append_section "D. CORE RULES"
  echo "Repository evidence wins over chat memory."
  echo "Do not guess when evidence is missing."
  echo "Use normal mode for low-risk continuation."
  echo "Use deep audit mode for production downloads, merges, QC pass/fail declarations, policy changes, scientific-method decisions, destructive operations, branch cleanup, or recovery after confusion."
  echo "ChatGPT and Codex require human approval before commits, merges, production downloads, destructive file operations, policy changes, scientific interpretation changes, or QC pass/fail declarations."
  echo "Scientific notes under docs/literature are evidence notes, not official decisions. Adopted decisions must be recorded in docs/DECISIONS.md."

  append_section "E. GIT STATUS SHORT BRANCH"
  git status --short --branch

  append_section "F. BRANCHES"
  git branch -vv

  append_section "G. RECENT COMMITS ON CURRENT BRANCH"
  git log --oneline --decorate --graph -n 12

  append_section "H. WORKING TREE DIFF SUMMARY"
  git diff --stat || true
  echo
  git diff --name-status || true

  append_section "I. STAGED DIFF SUMMARY"
  git diff --cached --stat || true
  echo
  git diff --cached --name-status || true

  append_section "J. CURRENT STATE FILE: docs/STATUS.md"
  cat_if_exists docs/STATUS.md

  append_section "K. CURRENT HANDOFF FILE: docs/HANDOFF.md"
  cat_if_exists docs/HANDOFF.md

  append_section "L. DECISIONS SUMMARY SOURCE: docs/DECISIONS.md"
  echo "Read this section for project decisions relevant to the current objective."
  echo "For normal mode, do not treat unrelated historical decisions as active task context."
  echo
  cat_if_exists docs/DECISIONS.md

  if [[ "$MODE" == "deep" ]]; then
    append_section "M. DEEP AUDIT: RECENT COMMITS ACROSS ALL BRANCHES"
    git log --oneline --decorate --graph --all -n 50

    append_section "N. DEEP AUDIT: REPOSITORY TREE"
    tree -a -L 4 -I '.git|__pycache__|*.pyc|data/raw|data/processed|logs' || find . -maxdepth 4 -not -path './.git/*' -not -path './data/raw/*' -not -path './data/processed/*' -not -path './logs/*' | sort

    append_section "O. DEEP AUDIT: TRACKED FILES"
    git ls-files

    append_section "P. DEEP AUDIT: STATUS INCLUDING IGNORED FILES"
    git status --short --ignored

    append_section "Q. DEEP AUDIT: OFFICIAL RE-ENTRY PROTOCOL"
    cat_if_exists docs/CHATGPT_REENTRY_PROTOCOL.md

    append_section "R. DEEP AUDIT: GIT WORKFLOW"
    cat_if_exists docs/GIT_WORKFLOW.md

    append_section "S. DEEP AUDIT: SEASONAL DOWNLOAD POLICY"
    cat_if_exists docs/SEASONAL_DOWNLOAD_POLICY.md

    append_section "T. DEEP AUDIT: SEASONAL KNOWN ISSUES"
    cat_if_exists docs/SEASONAL_KNOWN_ISSUES.md

    append_section "U. DEEP AUDIT: RUNBOOK"
    cat_if_exists docs/RUNBOOK.md

    append_section "V. DEEP AUDIT: SEASONAL SYSTEMS CONFIG"
    cat_if_exists configs/datasets/c3s_seasonal_systems.yml

    append_section "W. DEEP AUDIT: SEASONAL VARIABLES CONFIG"
    cat_if_exists configs/datasets/c3s_seasonal_variables.yml

    append_section "X. DEEP AUDIT: LITERATURE INDEX"
    if [[ -d docs/literature ]]; then
      find docs/literature -maxdepth 2 -type f | sort
    else
      echo "No docs/literature directory found."
    fi
  else
    append_section "M. NORMAL MODE NOTE"
    echo "This is a normal re-entry pack."
    echo "It intentionally omits full repository tree, full tracked-file list, long all-branch history, ignored-file listing, full policies, inventories, logs, and literature notes."
    echo "Escalate to deep mode if the task involves production downloads, merges, QC pass/fail declarations, policy changes, scientific-method decisions, destructive operations, branch cleanup, or confused/stale state."

    append_section "N. AVAILABLE LITERATURE NOTES"
    if [[ -d docs/literature ]]; then
      find docs/literature -maxdepth 2 -type f | sort
    else
      echo "No docs/literature directory found."
    fi
  fi

  append_section "Y. NEXT REQUESTED ASSISTANT ACTION"
  echo "Read this pack first."
  echo "Summarize the real repository state."
  echo "Identify the next safe step for the objective."
  echo "Ask for missing evidence if the task requires more context."
} > "$OUT_FILE"

sha256sum "$OUT_FILE" > "${OUT_FILE}.sha256"

echo "$OUT_FILE"
echo "${OUT_FILE}.sha256"
