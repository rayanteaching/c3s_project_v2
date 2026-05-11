#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import cdsapi

DATASET = "seasonal-monthly-pressure-levels"
ORIGINATING_CENTRE = "ncep"
SYSTEM = "2"
AREA_NH = [90, -180, 0, 180]

VARIABLES = {
    "z500": {
        "cds_variable": "geopotential",
        "pressure_level": "500",
        "level_label": "500hPa",
        "expected_short_name": "z",
        "expected_level": 500,
    },
    "t850": {
        "cds_variable": "temperature",
        "pressure_level": "850",
        "level_label": "850hPa",
        "expected_short_name": "t",
        "expected_level": 850,
    },
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_grib_metadata(path: Path, max_samples: int = 30) -> dict[str, Any]:
    try:
        import eccodes
    except Exception as exc:
        return {
            "eccodes_available": False,
            "message_count": None,
            "sample_messages": [],
            "error": repr(exc),
        }

    keys = [
        "shortName",
        "typeOfLevel",
        "level",
        "dataDate",
        "dataTime",
        "stepRange",
        "number",
        "forecastMonth",
        "edition",
        "Ni",
        "Nj",
        "numberOfPoints",
    ]

    samples: list[dict[str, Any]] = []
    message_count = 0

    with path.open("rb") as handle:
        while True:
            gid = eccodes.codes_grib_new_from_file(handle)
            if gid is None:
                break
            message_count += 1
            if len(samples) < max_samples:
                item: dict[str, Any] = {}
                for key in keys:
                    try:
                        item[key] = eccodes.codes_get(gid, key)
                    except Exception:
                        item[key] = None
                samples.append(item)
            eccodes.codes_release(gid)

    return {
        "eccodes_available": True,
        "message_count": message_count,
        "sample_messages": samples,
        "error": "",
    }


def build_request(variable_key: str, year: str, month: str, leadtime_month: str) -> dict[str, Any]:
    spec = VARIABLES[variable_key]
    return {
        "originating_centre": ORIGINATING_CENTRE,
        "system": SYSTEM,
        "variable": [spec["cds_variable"]],
        "pressure_level": [spec["pressure_level"]],
        "product_type": ["monthly_mean"],
        "year": [year],
        "month": [month],
        "leadtime_month": [leadtime_month],
        "data_format": "grib",
        "area": AREA_NH,
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="NCEP CFSv2 pressure-level smoke test for C3S seasonal monthly GRIB data."
    )
    parser.add_argument("--variable-key", choices=sorted(VARIABLES), required=True)
    parser.add_argument("--year", required=True)
    parser.add_argument("--month", required=True)
    parser.add_argument("--leadtime-month", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    target = Path(args.out)
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists() and not args.overwrite:
        raise SystemExit(f"Target exists; use --overwrite only if intentional: {target}")

    request = build_request(args.variable_key, args.year, args.month, args.leadtime_month)
    spec = VARIABLES[args.variable_key]

    request_sidecar = target.with_suffix(target.suffix + ".request.json")
    sha_sidecar = target.with_suffix(target.suffix + ".sha256")
    metadata_sidecar = target.with_suffix(target.suffix + ".metadata.json")
    part_path = target.with_suffix(target.suffix + ".part")

    request_payload = {
        "created_at_utc": utc_now(),
        "dataset": DATASET,
        "purpose": "NCEP CFSv2 pressure-level smoke test before production activation",
        "originating_centre": ORIGINATING_CENTRE,
        "system": SYSTEM,
        "forecast_system": "CFSv2-v20110310",
        "variable_key": args.variable_key,
        "expected_short_name": spec["expected_short_name"],
        "expected_level": spec["expected_level"],
        "request": request,
        "target": str(target),
    }
    write_json(request_sidecar, request_payload)

    if part_path.exists():
        part_path.unlink()

    client = cdsapi.Client()
    client.retrieve(DATASET, request, str(part_path))
    part_path.replace(target)

    digest = sha256sum(target)
    sha_sidecar.write_text(f"{digest}  {target.name}\n", encoding="utf-8")

    grib_metadata = read_grib_metadata(target)
    summary = {
        "checked_at_utc": utc_now(),
        "status": "downloaded",
        "dataset": DATASET,
        "originating_centre": ORIGINATING_CENTRE,
        "system": SYSTEM,
        "variable_key": args.variable_key,
        "year": args.year,
        "month": args.month,
        "leadtime_month": args.leadtime_month,
        "target": str(target),
        "sha256": digest,
        "request_json": str(request_sidecar),
        "sha256_file": str(sha_sidecar),
        "metadata_json": str(metadata_sidecar),
        "grib_metadata": grib_metadata,
    }
    write_json(metadata_sidecar, summary)

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
