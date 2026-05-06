#!/usr/bin/env python3

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from eccodes import codes_get, codes_get_values, codes_grib_new_from_file, codes_release


REPO_ROOT = Path("/home/fibi/projects/c3s_project_v2")

RAW_BASE = Path(
    "/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ecmwf/system_51"
)

RUN_DIR = REPO_ROOT / "runs/2026-05-04_c3s_ecmwf_pressure_levels_scientific_sanity_qc"

VARIABLES = {
    "z500": {
        "short_name": "z",
        "level": 500,
        "level_label": "500hPa",
        "minimum_allowed": 30000.0,
        "maximum_allowed": 70000.0,
        "expected_units": "m**2 s**-2",
    },
    "t850": {
        "short_name": "t",
        "level": 850,
        "level_label": "850hPa",
        "minimum_allowed": 180.0,
        "maximum_allowed": 340.0,
        "expected_units": "K",
    },
    "z925": {
        "short_name": "z",
        "level": 925,
        "level_label": "925hPa",
        "minimum_allowed": -5000.0,
        "maximum_allowed": 20000.0,
        "expected_units": "m**2 s**-2",
    },
}

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

MONTHS = [f"{month:02d}" for month in range(1, 13)]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_checksum(grib_path: Path) -> bool:
    sha_path = Path(f"{grib_path}.sha256")
    if not sha_path.exists():
        return False
    expected = sha_path.read_text(encoding="utf-8").strip().split()[0]
    actual = sha256sum(grib_path)
    return expected == actual


def canonical_path(block_root: Path, variable: str, meta: dict, years: str, month: str) -> Path:
    filename = (
        "cds__c3s_seasonal__monthly-pressure-levels__ecmwf__s51__"
        f"{variable}__{meta['level_label']}__monthly_mean__{years}__"
        f"st{month}__lead1-6__NH0_90.grib"
    )
    return block_root / variable / filename


def safe_get(message, key: str):
    try:
        return codes_get(message, key)
    except Exception:
        return None


def scan_grib(path: Path, max_messages: int) -> dict:
    message_count = 0
    value_count = 0
    min_value = None
    max_value = None
    mean_accumulator = 0.0

    first_short_name = None
    first_type_of_level = None
    first_level = None
    first_data_date = None
    first_data_time = None
    first_step_range = None
    first_number_of_points = None
    first_ni = None
    first_nj = None

    with path.open("rb") as handle:
        while True:
            message = codes_grib_new_from_file(handle)
            if message is None:
                break

            message_count += 1

            if message_count == 1:
                first_short_name = safe_get(message, "shortName")
                first_type_of_level = safe_get(message, "typeOfLevel")
                first_level = safe_get(message, "level")
                first_data_date = safe_get(message, "dataDate")
                first_data_time = safe_get(message, "dataTime")
                first_step_range = safe_get(message, "stepRange")
                first_number_of_points = safe_get(message, "numberOfPoints")
                first_ni = safe_get(message, "Ni")
                first_nj = safe_get(message, "Nj")

            if message_count <= max_messages:
                values = np.asarray(codes_get_values(message), dtype=float)
                if values.size > 0:
                    current_min = float(np.nanmin(values))
                    current_max = float(np.nanmax(values))
                    current_mean = float(np.nanmean(values))
                    min_value = current_min if min_value is None else min(min_value, current_min)
                    max_value = current_max if max_value is None else max(max_value, current_max)
                    mean_accumulator += current_mean
                    value_count += 1

            codes_release(message)

    sampled_mean = mean_accumulator / value_count if value_count else None

    return {
        "message_count": message_count,
        "sampled_message_count": value_count,
        "sampled_min": min_value,
        "sampled_max": max_value,
        "sampled_mean": sampled_mean,
        "shortName": first_short_name,
        "typeOfLevel": first_type_of_level,
        "level": first_level,
        "dataDate": first_data_date,
        "dataTime": first_data_time,
        "stepRange": first_step_range,
        "numberOfPoints": first_number_of_points,
        "Ni": first_ni,
        "Nj": first_nj,
    }


def check_row(block_name: str, block: dict, variable: str, meta: dict, month: str, max_messages: int) -> dict:
    checked_at = utc_now()
    path = canonical_path(block["root"], variable, meta, block["years"], month)
    request_path = Path(f"{path}.request.json")
    sha_path = Path(f"{path}.sha256")

    row = {
        "checked_at_utc": checked_at,
        "block": block_name,
        "years": block["years"],
        "variable": variable,
        "level_label": meta["level_label"],
        "start_month": month,
        "path": str(path),
        "grib_exists": path.exists(),
        "request_json_exists": request_path.exists(),
        "sha256_exists": sha_path.exists(),
        "checksum_passed": False,
        "eccodes_scan_passed": False,
        "message_count": None,
        "sampled_message_count": None,
        "sampled_min": None,
        "sampled_max": None,
        "sampled_mean": None,
        "shortName": None,
        "typeOfLevel": None,
        "level": None,
        "dataDate": None,
        "dataTime": None,
        "stepRange": None,
        "numberOfPoints": None,
        "Ni": None,
        "Nj": None,
        "range_check_passed": False,
        "metadata_check_passed": False,
        "passed": False,
        "error": "",
    }

    try:
        if not path.exists():
            row["error"] = "GRIB file does not exist"
            return row

        row["checksum_passed"] = verify_checksum(path)

        scan = scan_grib(path, max_messages=max_messages)
        row.update(scan)
        row["eccodes_scan_passed"] = True

        row["range_check_passed"] = (
            row["sampled_min"] is not None
            and row["sampled_max"] is not None
            and float(row["sampled_min"]) >= float(meta["minimum_allowed"])
            and float(row["sampled_max"]) <= float(meta["maximum_allowed"])
        )

        row["metadata_check_passed"] = (
            row["shortName"] == meta["short_name"]
            and row["typeOfLevel"] == "isobaricInhPa"
            and int(row["level"]) == int(meta["level"])
            and int(row["numberOfPoints"]) == 32400
            and int(row["Ni"]) == 360
            and int(row["Nj"]) == 90
        )

        row["passed"] = (
            row["grib_exists"]
            and row["request_json_exists"]
            and row["sha256_exists"]
            and row["checksum_passed"]
            and row["eccodes_scan_passed"]
            and row["range_check_passed"]
            and row["metadata_check_passed"]
        )

    except Exception as exc:
        row["error"] = repr(exc)

    return row


def write_csv(path: Path, rows: list[dict]) -> None:
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
        "eccodes_scan_passed",
        "message_count",
        "sampled_message_count",
        "sampled_min",
        "sampled_max",
        "sampled_mean",
        "shortName",
        "typeOfLevel",
        "level",
        "dataDate",
        "dataTime",
        "stepRange",
        "numberOfPoints",
        "Ni",
        "Nj",
        "range_check_passed",
        "metadata_check_passed",
        "passed",
        "error",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_run_files(rows: list[dict], max_messages: int) -> None:
    RUN_DIR.mkdir(parents=True, exist_ok=True)

    summary_csv = RUN_DIR / "scientific_sanity_summary.csv"
    details_json = RUN_DIR / "scientific_sanity_details.json"
    status_json = RUN_DIR / "status.json"
    run_md = RUN_DIR / "run.md"
    command_txt = RUN_DIR / "command.txt"

    write_csv(summary_csv, rows)

    details = {
        "checked_at_utc": utc_now(),
        "dataset": "seasonal-monthly-pressure-levels",
        "originating_centre": "ecmwf",
        "system": "51",
        "variables": sorted(VARIABLES.keys()),
        "blocks": sorted(BLOCKS.keys()),
        "months": MONTHS,
        "max_messages_per_file": max_messages,
        "rows": rows,
    }

    details_json.write_text(
        json.dumps(details, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    passed = all(bool(row["passed"]) for row in rows)

    status = {
        "status": "passed" if passed else "failed",
        "verified": passed,
        "dataset": "seasonal-monthly-pressure-levels",
        "originating_centre": "ecmwf",
        "system": "51",
        "qc_type": "sampled scientific sanity QC using ecCodes",
        "blocks": sorted(BLOCKS.keys()),
        "variables": sorted(VARIABLES.keys()),
        "months": MONTHS,
        "checked_file_count": len(rows),
        "max_messages_per_file": max_messages,
        "summary_csv": str(summary_csv.relative_to(REPO_ROOT)),
        "details_json": str(details_json.relative_to(REPO_ROOT)),
        "result": (
            "Canonical ECMWF pressure-level files passed sampled scientific sanity checks."
            if passed
            else "One or more canonical ECMWF pressure-level files failed sampled scientific sanity checks."
        ),
    }

    status_json.write_text(
        json.dumps(status, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    run_md.write_text(
        "\n".join(
            [
                "# ECMWF seasonal pressure-level scientific sanity QC",
                "",
                "## Scope",
                "- Dataset: seasonal-monthly-pressure-levels",
                "- Centre: ECMWF",
                "- System: 51",
                "- Blocks: hindcast_2000_2016 and forecast_2017_2025",
                "- Variables: z500, t850, z925",
                "- Months: all 12 initialization months",
                "",
                "## Method",
                "- Use canonical pressure-level GRIB files only.",
                "- Verify GRIB/request/SHA256 sidecars.",
                "- Verify SHA256 checksums.",
                "- Open each file with ecCodes.",
                "- Sample a fixed number of GRIB messages per file.",
                "- Check variable metadata, grid shape, pressure level, and plausible sampled value ranges.",
                "",
                "## Result",
                f"- Status: {status['status']}",
                f"- Checked files: {len(rows)}",
                f"- Max sampled messages per file: {max_messages}",
                f"- Summary CSV: `{summary_csv.relative_to(REPO_ROOT)}`",
                f"- Details JSON: `{details_json.relative_to(REPO_ROOT)}`",
                "",
            ]
        ),
        encoding="utf-8",
    )

    command_txt.write_text(
        "/home/fibi/projects/c3s_project_v2/scripts/qc/23_check_c3s_ecmwf_pressure_levels_scientific_sanity.py\n",
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scientific sanity QC for canonical ECMWF seasonal pressure-level GRIB files."
    )
    parser.add_argument(
        "--max-messages-per-file",
        type=int,
        default=12,
        help="Maximum number of GRIB messages to sample per file.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    rows = []
    for block_name, block in BLOCKS.items():
        for variable, meta in VARIABLES.items():
            for month in MONTHS:
                rows.append(
                    check_row(
                        block_name=block_name,
                        block=block,
                        variable=variable,
                        meta=meta,
                        month=month,
                        max_messages=args.max_messages_per_file,
                    )
                )

    write_run_files(rows, max_messages=args.max_messages_per_file)

    passed = all(bool(row["passed"]) for row in rows)

    print(json.dumps(json.loads((RUN_DIR / "status.json").read_text(encoding="utf-8")), indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

