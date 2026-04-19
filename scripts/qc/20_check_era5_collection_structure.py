#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path("/home/fibi/projects/c3s_project_v2")
RUN_ROOT = REPO_ROOT / "runs" / "2026-04-17_era5_monthly_qc_full"
SUMMARY_CSV = RUN_ROOT / "structure_qc_summary.csv"
DETAILS_JSON = RUN_ROOT / "structure_qc_details.json"

START_YEAR = 2000
END_YEAR = 2025
EXPECTED_GRIB_COUNT = (END_YEAR - START_YEAR + 1) * 12

DATASET_ROOTS = [
    (
        "tp",
        Path("/mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly"),
    ),
    (
        "t2m",
        Path("/mnt/e/last-aticol/data/raw/era5/single-levels/2m_temperature/monthly"),
    ),
    (
        "ws10m",
        Path("/mnt/e/last-aticol/data/raw/era5/single-levels/10m_wind_speed/monthly"),
    ),
    (
        "z500",
        Path("/mnt/e/last-aticol/data/raw/era5/pressure-levels/geopotential/500hPa/monthly"),
    ),
    (
        "t850",
        Path("/mnt/e/last-aticol/data/raw/era5/pressure-levels/temperature/850hPa/monthly"),
    ),
    (
        "z950",
        Path("/mnt/e/last-aticol/data/raw/era5/pressure-levels/geopotential/950hPa/monthly"),
    ),
]

FILENAME_PATTERN = re.compile(r"__(\d{4})-(\d{4})__m(\d{2})__")


def utc_now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def build_expected_month_keys() -> list[str]:
    keys: list[str] = []
    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):
            keys.append(f"{year}-{month:02d}")
    return keys


def extract_month_key(filename: str) -> str | None:
    match = FILENAME_PATTERN.search(filename)
    if not match:
        return None

    start_year = int(match.group(1))
    end_year = int(match.group(2))
    month = int(match.group(3))

    if start_year != end_year:
        return None

    return f"{start_year}-{month:02d}"


def collect_dataset_result(dataset_name: str, dataset_root: Path) -> dict:
    checked_at_utc = utc_now_iso()
    expected_month_keys = build_expected_month_keys()
    expected_month_key_set = set(expected_month_keys)

    result = {
        "dataset": dataset_name,
        "root": str(dataset_root),
        "checked_at_utc": checked_at_utc,
        "expected_grib_count": EXPECTED_GRIB_COUNT,
        "grib_count": 0,
        "request_count": 0,
        "sha256_count": 0,
        "missing_request_count": 0,
        "missing_sha256_count": 0,
        "orphan_request_count": 0,
        "orphan_sha256_count": 0,
        "invalid_grib_name_count": 0,
        "duplicate_month_key_count": 0,
        "missing_month_count": 0,
        "missing_months": [],
        "invalid_grib_names": [],
        "duplicate_month_keys": [],
        "missing_request_files": [],
        "missing_sha256_files": [],
        "orphan_request_files": [],
        "orphan_sha256_files": [],
        "passed": False,
        "root_exists": dataset_root.exists(),
    }

    if not dataset_root.exists():
        result["missing_month_count"] = EXPECTED_GRIB_COUNT
        result["missing_months"] = expected_month_keys
        return result

    grib_paths = sorted(dataset_root.glob("*.grib"))
    request_paths = sorted(dataset_root.glob("*.request.json"))
    sha256_paths = sorted(dataset_root.glob("*.sha256"))

    grib_names = [path.name for path in grib_paths]
    request_target_names = [path.name[: -len(".request.json")] for path in request_paths]
    sha256_target_names = [path.name[: -len(".sha256")] for path in sha256_paths]

    grib_name_set = set(grib_names)
    request_target_set = set(request_target_names)
    sha256_target_set = set(sha256_target_names)

    missing_request_files = sorted(grib_name_set - request_target_set)
    missing_sha256_files = sorted(grib_name_set - sha256_target_set)
    orphan_request_files = sorted(request_target_set - grib_name_set)
    orphan_sha256_files = sorted(sha256_target_set - grib_name_set)

    month_keys = []
    invalid_grib_names = []

    for grib_name in grib_names:
        month_key = extract_month_key(grib_name)
        if month_key is None:
            invalid_grib_names.append(grib_name)
        else:
            month_keys.append(month_key)

    month_counter = Counter(month_keys)
    duplicate_month_keys = sorted(
        month_key for month_key, count in month_counter.items() if count > 1
    )
    month_key_set = set(month_keys)
    missing_months = sorted(expected_month_key_set - month_key_set)

    result["grib_count"] = len(grib_paths)
    result["request_count"] = len(request_paths)
    result["sha256_count"] = len(sha256_paths)
    result["missing_request_count"] = len(missing_request_files)
    result["missing_sha256_count"] = len(missing_sha256_files)
    result["orphan_request_count"] = len(orphan_request_files)
    result["orphan_sha256_count"] = len(orphan_sha256_files)
    result["invalid_grib_name_count"] = len(invalid_grib_names)
    result["duplicate_month_key_count"] = len(duplicate_month_keys)
    result["missing_month_count"] = len(missing_months)
    result["missing_months"] = missing_months
    result["invalid_grib_names"] = invalid_grib_names
    result["duplicate_month_keys"] = duplicate_month_keys
    result["missing_request_files"] = missing_request_files
    result["missing_sha256_files"] = missing_sha256_files
    result["orphan_request_files"] = orphan_request_files
    result["orphan_sha256_files"] = orphan_sha256_files

    result["passed"] = all(
        [
            result["root_exists"],
            result["grib_count"] == EXPECTED_GRIB_COUNT,
            result["request_count"] == EXPECTED_GRIB_COUNT,
            result["sha256_count"] == EXPECTED_GRIB_COUNT,
            result["missing_request_count"] == 0,
            result["missing_sha256_count"] == 0,
            result["orphan_request_count"] == 0,
            result["orphan_sha256_count"] == 0,
            result["invalid_grib_name_count"] == 0,
            result["duplicate_month_key_count"] == 0,
            result["missing_month_count"] == 0,
        ]
    )

    return result


def write_summary_csv(results: list[dict]) -> None:
    fieldnames = [
        "dataset",
        "root",
        "checked_at_utc",
        "expected_grib_count",
        "grib_count",
        "request_count",
        "sha256_count",
        "missing_request_count",
        "missing_sha256_count",
        "orphan_request_count",
        "orphan_sha256_count",
        "invalid_grib_name_count",
        "duplicate_month_key_count",
        "missing_month_count",
        "passed",
    ]

    with SUMMARY_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow({field: result[field] for field in fieldnames})


def write_details_json(results: list[dict]) -> None:
    payload = {
        "run": "2026-04-17_era5_monthly_qc_full",
        "checked_at_utc": utc_now_iso(),
        "expected_year_range": f"{START_YEAR}-{END_YEAR}",
        "expected_grib_count_per_dataset": EXPECTED_GRIB_COUNT,
        "all_passed": all(result["passed"] for result in results),
        "dataset_results": results,
    }

    with DETAILS_JSON.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)


def print_summary(results: list[dict]) -> None:
    print("ERA5 monthly structural QC summary")
    print("=" * 72)

    for result in results:
        print(
            f"{result['dataset']}: "
            f"grib={result['grib_count']}, "
            f"request={result['request_count']}, "
            f"sha256={result['sha256_count']}, "
            f"missing_months={result['missing_month_count']}, "
            f"missing_request={result['missing_request_count']}, "
            f"missing_sha256={result['missing_sha256_count']}, "
            f"orphan_request={result['orphan_request_count']}, "
            f"orphan_sha256={result['orphan_sha256_count']}, "
            f"passed={result['passed']}"
        )

    print("=" * 72)
    print(f"Summary CSV: {SUMMARY_CSV}")
    print(f"Details JSON: {DETAILS_JSON}")


def main() -> int:
    RUN_ROOT.mkdir(parents=True, exist_ok=True)

    results = [
        collect_dataset_result(dataset_name, dataset_root)
        for dataset_name, dataset_root in DATASET_ROOTS
    ]

    write_summary_csv(results)
    write_details_json(results)
    print_summary(results)

    if all(result["passed"] for result in results):
        print("STRUCTURAL_QC_PASS")
        return 0

    print("STRUCTURAL_QC_FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
