#!/usr/bin/env python3

import argparse
import hashlib
import json
import logging
from pathlib import Path

import cdsapi

DATASET = "seasonal-monthly-single-levels"
CENTRE = "ecmwf"
SYSTEM = "51"
PRODUCT_TYPE = "monthly_mean"
VARIABLES = [
    "2m_temperature",
    "10m_wind_speed",
    "total_precipitation",
]
LEADTIMES = ["1", "2", "3", "4", "5", "6"]
AREA = [90, -180, 0, 180]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download grouped ECMWF C3S seasonal monthly single-level files."
    )
    parser.add_argument("--start-year", type=int, required=True, help="First initialization year.")
    parser.add_argument("--end-year", type=int, required=True, help="Last initialization year.")
    parser.add_argument(
        "--months",
        default="01,02,03,04,05,06,07,08,09,10,11,12",
        help="Comma-separated initialization months in MM format.",
    )
    parser.add_argument("--out-root", required=True, help="Output directory root.")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip files that already have valid request and sha256 sidecars.",
    )
    return parser


def parse_months(value: str) -> list[str]:
    months = [item.strip() for item in value.split(",") if item.strip()]
    valid = {f"{month:02d}" for month in range(1, 13)}
    if not months:
        raise ValueError("No months were provided.")
    bad = [month for month in months if month not in valid]
    if bad:
        raise ValueError(f"Invalid month values: {bad}")
    return months


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def request_sidecar_path(target: Path) -> Path:
    return Path(f"{target}.request.json")


def sha256_sidecar_path(target: Path) -> Path:
    return Path(f"{target}.sha256")


def has_valid_sidecars(target: Path) -> bool:
    if not target.exists():
        return False

    request_path = request_sidecar_path(target)
    sha_path = sha256_sidecar_path(target)

    if not request_path.exists() or not sha_path.exists():
        return False

    expected_line = sha_path.read_text(encoding="utf-8").strip()
    if not expected_line:
        return False

    expected_hash = expected_line.split()[0]
    actual_hash = sha256sum(target)
    return expected_hash == actual_hash


def build_request(start_year: int, end_year: int, month: str) -> dict:
    return {
        "originating_centre": CENTRE,
        "system": SYSTEM,
        "variable": VARIABLES,
        "product_type": PRODUCT_TYPE,
        "year": [str(year) for year in range(start_year, end_year + 1)],
        "month": month,
        "leadtime_month": LEADTIMES,
        "data_format": "grib",
        "area": AREA,
    }


def build_target(out_root: Path, start_year: int, end_year: int, month: str) -> Path:
    filename = (
        "cds__c3s_seasonal__monthly-single-levels__ecmwf__s51__"
        f"t2m-ws10m-tp__surface__monthly_mean__{start_year}-{end_year}__"
        f"st{month}__lead1-6__NH0_90.grib"
    )
    return out_root / filename


def write_request_sidecar(target: Path, request: dict) -> None:
    payload = {
        "dataset": DATASET,
        "request": request,
        "target": str(target),
    }
    request_sidecar_path(target).write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def write_sha256_sidecar(target: Path) -> None:
    digest = sha256sum(target)
    sha256_sidecar_path(target).write_text(
        f"{digest}  {target.name}\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    out_root = Path(args.out_root).expanduser().resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    months = parse_months(args.months)
    client = cdsapi.Client()

    for month in months:
        request = build_request(args.start_year, args.end_year, month)
        target = build_target(out_root, args.start_year, args.end_year, month)

        if args.skip_existing and has_valid_sidecars(target):
            logging.info("SKIP existing verified file: %s", target)
            continue

        temp_target = Path(f"{target}.part")
        if temp_target.exists():
            temp_target.unlink()

        logging.info(
            "START month=%s years=%s-%s target=%s",
            month,
            args.start_year,
            args.end_year,
            target,
        )

        client.retrieve(DATASET, request, str(temp_target))

        if target.exists():
            target.unlink()
        temp_target.replace(target)

        write_request_sidecar(target, request)
        write_sha256_sidecar(target)

        print("OK")
        print(f"GRIB: {target}")
        print(f"REQUEST: {request_sidecar_path(target)}")
        print(f"SHA256: {sha256_sidecar_path(target)}")

    logging.info("ALL DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
