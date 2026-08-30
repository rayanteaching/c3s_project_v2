from __future__ import annotations

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_project.py"
SPEC = importlib.util.spec_from_file_location("validate_project", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


STUDY = """schema_version: 1
architecture_version: 1
target_verifying_years: {start: 2000, end: 2025}
target_months: [12]
scientific_horizons: {H1: 1, H2: 2, H3: 3, H4: 4, H5: 5, H6: 6}
centres: [ecmwf, ukmo, dwd, cmcc, meteo_france, ncep]
variables: [t2m, tp, ws10m, z500, t850, z950]
analysis_modes: [maximum_valid, common_case]
native_lead_mapping: verify_per_centre_system_product
legacy_global_split: prohibited
global_z950_to_z925_substitution: prohibited
"""

GUARDRAILS = """guardrails:
  fail_closed_unknowns: true
"""

SYSTEMS = """policy:
  no_cross_centre_assumption_propagation: true
  no_universal_hindcast_forecast_split: true
  matching_forecast_reforecast_system_cohort_required: true
  unknown_required_mapping_fails_closed: true
centres:
  ecmwf: {}
  ukmo: {}
  dwd: {}
  cmcc: {}
  meteo_france: {}
  ncep: {}
"""

VARIABLES = """target_variables:
  t2m: {}
  tp: {}
  ws10m: {}
  z500: {}
  t850: {}
  z950:
    global_substitution_allowed: false
"""


class ProjectValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="c3s-validator-"))
        for rel in (
            "AGENTS.md",
            "docs/STATUS.md",
            "docs/ARCHITECTURE.md",
            "docs/OPEN_SCIENTIFIC_QUESTIONS.md",
            "docs/DECISIONS.md",
        ):
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("ok\n", encoding="utf-8")

        configs = {
            "study_v0_1.yml": STUDY,
            "guardrails_v1.yml": GUARDRAILS,
            "system_registry_v1.yml": SYSTEMS,
            "variable_registry_v1.yml": VARIABLES,
        }
        for name, content in configs.items():
            path = self.root / "configs" / "datasets" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def assert_fails_with(self, needle: str) -> None:
        errors = VALIDATOR.validate(self.root)
        self.assertTrue(errors, "validator unexpectedly passed")
        self.assertTrue(
            any(needle in error for error in errors),
            f"expected {needle!r} in errors: {errors!r}",
        )

    def test_valid_fixture_passes(self) -> None:
        self.assertEqual(VALIDATOR.validate(self.root), [])

    def test_forbidden_global_z950_substitution_fails(self) -> None:
        path = self.root / "configs/datasets/study_v0_1.yml"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "global_z950_to_z925_substitution: prohibited",
                "global_z950_to_z925_substitution: allowed",
            ),
            encoding="utf-8",
        )
        self.assert_fails_with("study.global_z950_to_z925_substitution")

    def test_registry_coverage_mismatch_fails(self) -> None:
        path = self.root / "configs/datasets/system_registry_v1.yml"
        path.write_text(
            path.read_text(encoding="utf-8").replace("  ncep: {}\n", ""),
            encoding="utf-8",
        )
        self.assert_fails_with("centre coverage mismatch")

    def test_retired_handoff_reintroduction_fails(self) -> None:
        (self.root / "docs/HANDOFF.md").write_text("old authority\n", encoding="utf-8")
        self.assert_fails_with("docs/HANDOFF.md is retired")

    def test_live_main_sha_in_status_fails(self) -> None:
        (self.root / "docs/STATUS.md").write_text(
            "main: 0123456789abcdef0123456789abcdef01234567\n",
            encoding="utf-8",
        )
        self.assert_fails_with("live main SHA must be derived from Git")


if __name__ == "__main__":
    unittest.main()
