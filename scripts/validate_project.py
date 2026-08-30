#!/usr/bin/env python3
"""Small fail-closed validator for high-value project Harness invariants.

This validator checks repository/configuration invariants that are already
approved project policy. It does not decide whether those scientific policies
are correct; scientific acceptance remains evidence-based and human-led.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    print("ERROR: PyYAML is required to run scripts/validate_project.py", file=sys.stderr)
    raise SystemExit(2) from exc


ACTIVE_CONFIGS = (
    "configs/datasets/study_v0_1.yml",
    "configs/datasets/guardrails_v1.yml",
    "configs/datasets/system_registry_v1.yml",
    "configs/datasets/variable_registry_v1.yml",
)

REQUIRED_FILES = (
    "AGENTS.md",
    "docs/STATUS.md",
    "docs/ARCHITECTURE.md",
    "docs/OPEN_SCIENTIFIC_QUESTIONS.md",
    "docs/DECISIONS.md",
    *ACTIVE_CONFIGS,
)

LIVE_MAIN_SHA_RE = re.compile(
    r"^\s*[-*]?\s*(?:current\s+)?(?:remote\s+)?main(?:\s+sha)?\s*[:=]\s*?[0-9a-f]{40}\s*$",
    re.IGNORECASE,
)


class ValidationError(Exception):
    """Raised for a project invariant violation."""


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationError(f"{path}: YAML parse failed: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: top-level YAML value must be a mapping")
    return data


def require_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise ValidationError(f"{label}: expected {expected!r}, found {actual!r}")


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    def check(fn) -> None:
        try:
            fn()
        except ValidationError as exc:
            errors.append(str(exc))

    def required_files_exist() -> None:
        missing = [rel for rel in REQUIRED_FILES if not (root / rel).is_file()]
        if missing:
            raise ValidationError("missing required file(s): " + ", ".join(missing))

    check(required_files_exist)

    if errors:
        return errors

    configs: dict[str, dict[str, Any]] = {}
    for rel in ACTIVE_CONFIGS:
        def parse_one(rel=rel) -> None:
            configs[rel] = load_yaml(root / rel)
        check(parse_one)

    if len(configs) != len(ACTIVE_CONFIGS):
        return errors

    study = configs["configs/datasets/study_v0_1.yml"]
    guardrails = configs["configs/datasets/guardrails_v1.yml"]
    systems = configs["configs/datasets/system_registry_v1.yml"]
    variables = configs["configs/datasets/variable_registry_v1.yml"]

    def validate_required_structure() -> None:
        for key in (
            "schema_version",
            "architecture_version",
            "target_verifying_years",
            "target_months",
            "scientific_horizons",
            "centres",
            "variables",
            "analysis_modes",
        ):
            if key not in study:
                raise ValidationError(f"study_v0_1.yml: missing required key {key!r}")
        if not isinstance(systems.get("centres"), dict):
            raise ValidationError("system_registry_v1.yml: 'centres' must be a mapping")
        if not isinstance(variables.get("target_variables"), dict):
            raise ValidationError("variable_registry_v1.yml: 'target_variables' must be a mapping")
        if not isinstance(guardrails.get("guardrails"), dict):
            raise ValidationError("guardrails_v1.yml: 'guardrails' must be a mapping")

    check(validate_required_structure)

    def validate_forbidden_defaults() -> None:
        require_equal(
            study.get("native_lead_mapping"),
            "verify_per_centre_system_product",
            "study.native_lead_mapping",
        )
        require_equal(
            study.get("legacy_global_split"),
            "prohibited",
            "study.legacy_global_split",
        )
        require_equal(
            study.get("global_z950_to_z925_substitution"),
            "prohibited",
            "study.global_z950_to_z925_substitution",
        )

        z950 = variables.get("target_variables", {}).get("z950", {})
        require_equal(
            z950.get("global_substitution_allowed"),
            False,
            "variable_registry.z950.global_substitution_allowed",
        )

        policy = systems.get("policy", {})
        require_equal(
            policy.get("no_cross_centre_assumption_propagation"),
            True,
            "system_registry.policy.no_cross_centre_assumption_propagation",
        )
        require_equal(
            policy.get("no_universal_hindcast_forecast_split"),
            True,
            "system_registry.policy.no_universal_hindcast_forecast_split",
        )
        require_equal(
            policy.get("matching_forecast_reforecast_system_cohort_required"),
            True,
            "system_registry.policy.matching_forecast_reforecast_system_cohort_required",
        )
        require_equal(
            policy.get("unknown_required_mapping_fails_closed"),
            True,
            "system_registry.policy.unknown_required_mapping_fails_closed",
        )

    check(validate_forbidden_defaults)

    def validate_registry_coverage() -> None:
        study_centres = set(study.get("centres") or [])
        registry_centres = set((systems.get("centres") or {}).keys())
        if study_centres != registry_centres:
            raise ValidationError(
                "centre coverage mismatch: "
                f"study={sorted(study_centres)!r}, registry={sorted(registry_centres)!r}"
            )

        study_variables = set(study.get("variables") or [])
        registry_variables = set((variables.get("target_variables") or {}).keys())
        if study_variables != registry_variables:
            raise ValidationError(
                "variable coverage mismatch: "
                f"study={sorted(study_variables)!r}, registry={sorted(registry_variables)!r}"
            )

    check(validate_registry_coverage)

    def validate_single_current_state() -> None:
        if (root / "docs/HANDOFF.md").exists():
            raise ValidationError(
                "docs/HANDOFF.md is retired; docs/STATUS.md is the single current-state artifact"
            )

        status_lines = (root / "docs/STATUS.md").read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(status_lines, start=1):
            normalized = line.replace(chr(96), "").strip()
            if LIVE_MAIN_SHA_RE.match(normalized):
                raise ValidationError(
                    f"docs/STATUS.md:{lineno}: live main SHA must be derived from Git, not copied into STATUS"
                )

    check(validate_single_current_state)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to parent of scripts/)",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    errors = validate(root)

    if errors:
        print(f"PROJECT VALIDATION FAILED ({len(errors)} error(s))")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PROJECT VALIDATION PASSED")
    print(f"- required files: {len(REQUIRED_FILES)} present")
    print(f"- active YAML configs: {len(ACTIVE_CONFIGS)} parsed")
    print("- forbidden scientific defaults: blocked")
    print("- study/registry coverage: consistent")
    print("- current-state authority: single and Git-derived")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
