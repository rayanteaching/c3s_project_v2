#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/home/fibi/projects/c3s_project_v2"
cd "$PROJECT_ROOT"

MODE="${1:-normal}"
OBJECTIVE="${2:-REPLACE_WITH_CURRENT_OBJECTIVE}"

if [[ "$MODE" != "normal" && "$MODE" != "deep" ]]; then
  echo "Usage: bash scripts/make_chatgpt_reentry_pack_v2.sh [normal|deep] \"CURRENT_OBJECTIVE\"" >&2
  exit 2
fi

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
BRANCH="$(git rev-parse --abbrev-ref HEAD | tr '/ ' '__')"
OUT_DIR="runs/reentry"
OUT_FILE="${OUT_DIR}/chatgpt_reentry_pack_v2_${STAMP}_${BRANCH}_${MODE}.md"
mkdir -p "$OUT_DIR"

section() {
  printf '\n============================================================\n%s\n============================================================\n\n' "$1"
}

cat_if_exists() {
  if [[ -f "$1" ]]; then cat "$1"; else echo "MISSING: $1"; fi
}

{
  echo "PROJECT RE-ENTRY PACK — ARCHITECTURE V1"
  echo "Generated UTC: ${STAMP}"
  echo "Mode: ${MODE}"

  section "A. PROJECT IDENTITY"
  echo "Project root: ${PROJECT_ROOT}"
  echo "Current branch: $(git rev-parse --abbrev-ref HEAD)"
  echo "Current commit: $(git rev-parse HEAD)"
  echo "Objective: ${OBJECTIVE}"

  section "B. OPENING RULES"
  echo "Repository evidence wins over chat memory."
  echo "main=approved truth; task branches=candidate state; tracked runs=execution evidence; historical/superseded material is not current policy."
  echo "Read Architecture v1 current files before legacy/bootstrap configs."
  echo "Unknown required scientific facts fail closed."
  echo "Do not propagate centre-specific assumptions across centres."
  echo "If repository evidence conflicts internally, stop and resolve it; do not guess."
  echo "If chat context appears degraded, migrate before another high-impact decision."

  section "C. ARCHITECTURE"
  cat_if_exists docs/ARCHITECTURE.md

  section "D. OPEN SCIENTIFIC QUESTIONS"
  cat_if_exists docs/OPEN_SCIENTIFIC_QUESTIONS.md

  section "E. SCIENTIFIC DECISION TRACEABILITY"
  cat_if_exists docs/SCIENTIFIC_DECISION_TRACEABILITY.md

  section "F. CURRENT CONFIG PRECEDENCE"
  cat_if_exists configs/datasets/CURRENT_CONFIGS.md

  section "G. STUDY CONFIG"
  cat_if_exists configs/datasets/study_v0_1.yml

  section "H. GUARDRAILS"
  cat_if_exists configs/datasets/guardrails_v1.yml

  section "I. SYSTEM REGISTRY"
  cat_if_exists configs/datasets/system_registry_v1.yml

  section "J. VARIABLE REGISTRY"
  cat_if_exists configs/datasets/variable_registry_v1.yml

  section "K. CURRENT STATUS"
  cat_if_exists docs/STATUS.md

  section "L. CURRENT HANDOFF"
  cat_if_exists docs/HANDOFF.md

  section "M. CURRENT DECISIONS"
  cat_if_exists docs/DECISIONS.md

  section "N. GIT STATE"
  git status --short --branch
  echo
  git branch -vv
  echo
  git log --oneline --decorate --graph -n 15
  echo
  git diff --stat || true
  git diff --name-status || true
  git diff --cached --stat || true
  git diff --cached --name-status || true

  if [[ "$MODE" == "deep" ]]; then
    section "O. RE-ENTRY PROTOCOL"
    cat_if_exists docs/CHATGPT_REENTRY_PROTOCOL.md

    section "P. CURRENT SEASONAL DOWNLOAD POLICY"
    cat_if_exists docs/SEASONAL_DOWNLOAD_POLICY.md

    section "Q. SEASONAL KNOWN ISSUES"
    cat_if_exists docs/SEASONAL_KNOWN_ISSUES.md

    section "R. LEGACY BOOTSTRAP CONFIGS — DO NOT TREAT AS CURRENT POLICY"
    cat_if_exists configs/datasets/c3s_seasonal_systems.yml
    echo
    cat_if_exists configs/datasets/c3s_seasonal_variables.yml

    section "S. RECENT ALL-BRANCH HISTORY"
    git log --oneline --decorate --graph --all -n 50

    section "T. TRACKED FILES"
    git ls-files

    section "U. LITERATURE INDEX"
    if [[ -d docs/literature ]]; then
      find docs/literature -maxdepth 3 -type f | sort
    else
      echo "No docs/literature directory found."
    fi
  else
    section "O. NORMAL MODE NOTE"
    echo "Normal mode omits full legacy configs, full tree/history, logs, inventories, and unrelated literature."
    echo "Escalate to deep mode for production, merge, QC milestone, scientific-method/policy change, destructive work, or uncertain state."
  fi

  section "FINAL. REQUIRED ASSISTANT OPENING"
  echo "Summarize branch/SHA, objective, milestone, Architecture/config/guardrail versions, completed work, relevant OPEN questions, risks, next safe step, and missing evidence before high-impact work."
} > "$OUT_FILE"

sha256sum "$OUT_FILE" > "${OUT_FILE}.sha256"
printf '%s\n%s\n' "$OUT_FILE" "${OUT_FILE}.sha256"
