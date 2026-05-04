#!/usr/bin/env python3

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import eccodes


REPO_ROOT = Path("/home/fibi/projects/c3s_project_v2")
RUN_DIR = REPO_ROOT / "runs" / "2026-05-04_c3s_ecmwf_pressure_levels_open_qc"
RAW_BASE = Path(
    "/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ecmwf/system_51"
)

SUMMARY_CSV = RUN_DIR / "open_qc_summary.csv"
DETAILS_JSON = RUN_DIR / "open_qc_details.json"
STATUS_JSON = RUN_DIR / "status.json"
RUN_MD = RUN_DIR / "run.md"
COMMAND_TXT = RUN_DIR / "command.txt"

BLOCKS = {
    "hindcast": {
        "years": "2000-2016",
        "root": RAW_BASE / "hindcast_2000_2016",
    },
    "forecast": {
        "years": "2017-2025",
        "root": RAW_BASE / "forecast_2017_2025",
    },
}

VARIABLES = {
    "z500": {
        "level": "500hPa",
        "expected_short_name": "z",
        "expected_type_of_level": "isobaricInhPa",
        "expected_level": 500,
    },
    "t850": {
        "level": "850hPa",
        "expected_short_name": "t",
        "expected_type_of_level": "isobaricInhPa",
        "expected_level": 850,
    },
    "z925": {
        "level": "925hPa",
        "expected_short_name": "z",
        "expected_type_of_level": "isobaricInhPa",
        "expected_level": 925,
    },
}

SAMPLE_MONTHS = ["01", "12"]


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sidecar_request_path(path: Path) -> Path:
    return Path(str(path) + ".request.json")


def sidecar_sha256_path(path: Path) -> Path:
    return Path(str(path) + ".sha256")


def expected_grib_path(block: dict, variable: str, level_label: str, month: str) -> Path:
    return block["root"] / variable / (
        "cds__c3s_seasonal__monthly-pressure-levels__ecmwf__s51__"
        f"{variable}__{level_label}__monthly_mean__{block['years']}__"
        f"st{month}__lead1-6__NH0_90.grib"
    )


def read_first_grib_message(path: Path) -> dict:
    with path.open("rb") as handle:
        gid = eccodes.codes_grib_new_from_file(handle)
        if gid is None:
            raise RuntimeError(f"No GRIB message found in {path}")

        try:
            keys = {
                "shortName": eccodes.codes_get(gid, "shortName"),
                "typeOfLevel": eccodes.codes_get(gid, "typeOfLevel"),
                "level": int(eccodes.codes_get(gid, "level")),
                "dataDate": int(eccodes.codes_get(gid, "dataDate")),
                "dataTime": int(eccodes.codes_get(gid, "dataTime")),
                "stepRange": str(eccodes.codes_get(gid, "stepRange")),
                "numberOfPoints": int(eccodes.codes_get(gid, "numberOfPoints")),
                "Ni": int(eccodes.codes_get(gid, "Ni")),
                "Nj": int(eccodes.codes_get(gid, "Nj")),
            }
        finally:
            eccodes.codes_release(gid)

    return keys


def verify_checksum(path: Path, sha_path: Path) -> bool:
    recorded = sha_path.read_text(encoding="utf-8").strip().split()[0]
    actual = sha256sum(path)
    return recorded == actual


def build_rows() -> list[dict]:
    rows = []

    for block_name, block in BLOCKS.items():
        for variable, config in VARIABLES.items():
            for month in SAMPLE_MONTHS:
                path = expected_grib_path(block, variable, config["level"], month)
                request_path = sidecar_request_path(path)
                sha_path = sidecar_sha256_path(path)

                row = {
                    "checked_at_utc": utc_now(),
                    "block": block_name,
                    "years": block["years"],
                    "variable": variable,
                    "level_label": config["level"],
                    "start_month": month,
                    "path": str(path),
                    "grib_exists": path.exists(),
                    "request_json_exists": request_path.exists(),
                    "sha256_exists": sha_path.exists(),
                    "checksum_passed": False,
                    "eccodes_open_passed": False,
                    "shortName": "",
                    "typeOfLevel": "",
                    "level": "",
                    "dataDate": "",
                    "dataTime": "",
                    "stepRange": "",
                    "numberOfPoints": "",
                    "Ni": "",
                    "Nj": "",
                    "metadata_check_passed": False,
                    "error": "",
                    "passed": False,
                }

                try:
                    if not path.exists():
                        raise FileNotFoundError(str(path))
                    if not request_path.exists():
                        raise FileNotFoundError(str(request_path))
                    if not sha_path.exists():
                        raise FileNotFoundError(str(sha_path))

                    row["checksum_passed"] = verify_checksum(path, sha_path)
                    if not row["checksum_passed"]:
                        raise RuntimeError(f"SHA256 check failed for {path}")

                    metadata = read_first_grib_message(path)
                    row["eccodes_open_passed"] = True

                    for key, value in metadata.items():
                        row[key] = value

                    row["metadata_check_passed"] = (
                        row["shortName"] == config["expected_short_name"]
                        and row["typeOfLevel"] == config["expected_type_of_level"]
                        and int(row["level"]) == int(config["expected_level"])
                        and int(row["numberOfPoints"]) > 0
                        and int(row["Ni"]) > 0
                        and int(row["Nj"]) > 0
                    )

                except Exception as exc:
                    row["error"] = repr(exc)

                row["passed"] = all(
                    [
                        row["grib_exists"],
                        row["request_json_exists"],
                        row["sha256_exists"],
                        row["checksum_passed"],
                        row["eccodes_open_passed"],
                        row["metadata_check_passed"],
                    ]
                )

                rows.append(row)

    return rows


def write_summary(rows: list[dict]) -> None:
    fieldnames = [
        "checked_at_utc",
        "block",
        "years",
        "variable",
        "level_label",
        "start_month",
        "path",
        "grib_exists",
        "request_json_exists",
        "sha256_exists",
        "checksum_passed",
        "eccodes_open_passed",
        "shortName",
        "typeOfLevel",
        "level",
        "dataDate",
        "dataTime",
        "stepRange",
        "numberOfPoints",
        "Ni",
        "Nj",
        "metadata_check_passed",
        "error",
        "passed",
    ]

    with SUMMARY_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_metadata(rows: list[dict]) -> bool:
    all_passed = all(row["passed"] for row in rows)

    details = {
        "checked_at_utc": utc_now(),
        "dataset": "seasonal-monthly-pressure-levels",
        "originating_centre": "ecmwf",
        "system": "51",
        "qc_type": "lightweight canonical GRIB openability QC using ecCodes",
        "sample_months": SAMPLE_MONTHS,
        "sampled_file_count": len(rows),
        "all_passed": all_passed,
        "summary_csv": str(SUMMARY_CSV.relative_to(REPO_ROOT)),
        "rows": rows,
    }

    status = {
        "status": "passed" if all_passed else "failed",
        "verified": all_passed,
        "dataset": "seasonal-monthly-pressure-levels",
        "originating_centre": "ecmwf",
        "system": "51",
        "qc_type": "lightweight canonical GRIB openability QC using ecCodes",
        "sample_months": SAMPLE_MONTHS,
        "sampled_file_count": len(rows),
        "variables": sorted(VARIABLES.keys()),
        "blocks": sorted(BLOCKS.keys()),
        "summary_csv": str(SUMMARY_CSV.relative_to(REPO_ROOT)),
        "details_json": str(DETAILS_JSON.relative_to(REPO_ROOT)),
        "result": (
            "Canonical ECMWF pressure-level sampled GRIB files passed checksum, openability, and metadata checks."
            if all_passed
            else "One or more canonical ECMWF pressure-level sampled GRIB files failed checksum, openability, or metadata checks."
        ),
    }

    DETAILS_JSON.write_text(json.dumps(details, indent=2), encoding="utf-8")
    STATUS_JSON.write_text(json.dumps(status, indent=2), encoding="utf-8")

    RUN_MD.write_text(
        "# ECMWF seasonal monthly pressure-level openability QC\n\n"
        "## Scope\n"
        "- Dataset: C3S seasonal monthly pressure-levels\n"
        "- Centre: ECMWF\n"
        "- System: 51\n"
        "- Blocks: hindcast_2000_2016 and forecast_2017_2025\n"
        "- Variables: z500, t850, z925\n"
        "- Sample months: st01 and st12\n\n"
        "## Checks\n"
        "- GRIB file exists\n"
        "- request sidecar exists\n"
        "- sha256 sidecar exists\n"
        "- sha256 checksum matches\n"
        "- first GRIB message opens with ecCodes\n"
        "- key metadata are readable and match the expected variable and pressure level\n\n"
        f"## Result\n- Status: {'passed' if all_passed else 'failed'}\n"
        f"- Summary: `{SUMMARY_CSV.relative_to(REPO_ROOT)}`\n"
        f"- Details: `{DETAILS_JSON.relative_to(REPO_ROOT)}`\n",
        encoding="utf-8",
    )

    COMMAND_TXT.write_text(
        "scripts/qc/22_check_c3s_ecmwf_pressure_levels_openability.py\n",
        encoding="utf-8",
    )

    return all_passed


def main() -> int:
    RUN_DIR.mkdir(parents=True, exist_ok=True)

    rows = build_rows()
    write_summary(rows)
    all_passed = write_metadata(rows)

    print(json.dumps(json.loads(STATUS_JSON.read_text(encoding="utf-8")), indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
