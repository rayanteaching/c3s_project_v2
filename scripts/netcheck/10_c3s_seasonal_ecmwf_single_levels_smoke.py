#!/usr/bin/env python3

import argparse
import hashlib
import json
from pathlib import Path

import cdsapi


DATASET = "seasonal-monthly-single-levels"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Smoke test for ECMWF seasonal monthly single-level data on C3S."
    )
    parser.add_argument("--year", required=True, help="Initialization year, e.g. 2000")
    parser.add_argument("--month", required=True, help="Initialization month, e.g. 01")
    parser.add_argument("--leadtime-month", required=True, help="Lead month, e.g. 1")
    parser.add_argument("--variable", required=True, help="C3S variable name, e.g. 2m_temperature")
    parser.add_argument("--out", required=True, help="Output GRIB path")
    return parser


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    args = build_parser().parse_args()

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    request = {
        "originating_centre": "ecmwf",
        "system": "51",
        "variable": args.variable,
        "product_type": "monthly_mean",
        "year": str(args.year),
        "month": str(args.month).zfill(2),
        "leadtime_month": str(args.leadtime_month),
        "data_format": "grib",
        "area": [90, -180, 0, 180],
    }

    request_sidecar = Path(str(out_path) + ".request.json")
    sha_sidecar = Path(str(out_path) + ".sha256")

    request_payload = {
        "dataset": DATASET,
        "request": request,
        "target": str(out_path),
    }
    request_sidecar.write_text(
        json.dumps(request_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    client = cdsapi.Client()
    client.retrieve(DATASET, request, str(out_path))

    digest = sha256_file(out_path)
    sha_sidecar.write_text(f"{digest}  {out_path.name}\n", encoding="utf-8")

    print("OK")
    print(f"GRIB: {out_path}")
    print(f"REQUEST: {request_sidecar}")
    print(f"SHA256: {sha_sidecar}")


if __name__ == "__main__":
    main()
