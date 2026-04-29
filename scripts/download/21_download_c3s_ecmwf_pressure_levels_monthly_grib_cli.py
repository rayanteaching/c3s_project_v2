#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import cdsapi


DATASET = "seasonal-monthly-pressure-levels"
ORIGINATING_CENTRE = "ecmwf"
DEFAULT_SYSTEM = "51"
DEFAULT_OUTPUT_ROOT = Path("/mnt/e/last-aticol/data/raw/c3s/seasonal/monthly-pressure-levels/ecmwf/system_51")
DEFAULT_AREA = [90, -180, 0, 180]
DEFAULT_GRID = [1.0, 1.0]
DEFAULT_LEADTIME_MONTHS = ["1", "2", "3", "4", "5", "6"]

TARGETS = [
    {
        "label": "z500",
        "variable": "geopotential",
        "pressure_level": "500",
        "units": "m2 s-2",
        "note": "raw geopotential, not geopotential height",
    },
    {
        "label": "t850",
        "variable": "temperature",
        "pressure_level": "850",
        "units": "K",
        "note": "raw temperature",
    },
    {
        "label": "z925",
        "variable": "geopotential",
        "pressure_level": "925",
        "units": "m2 s-2",
        "note": "raw geopotential, not geopotential height; seasonal substitute for z950",
    },
]


TRANSIENT_ERROR_MARKERS = [
    "SSLEOFError",
    "Max retries exceeded",
    "Read timed out",
    "Connection reset",
    "Remote end closed connection",
    "EOF occurred in violation of protocol",
    "Connection aborted",
    "temporarily unavailable",
    "timeout",
    "Too Many Requests",
    "Service Unavailable",
    "Gateway Time-out",
    "Bad Gateway",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_csv_strings(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_area(value: str) -> list[float]:
    parts = [float(x.strip()) for x in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("area must have four comma-separated values: north,west,south,east")
    return parts


def parse_grid(value: str) -> list[float]:
    parts = [float(x.strip()) for x in value.split(",")]
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("grid must have two comma-separated values: lat,lon")
    return parts


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def write_text(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def is_transient_error(exc: BaseException) -> bool:
    msg = repr(exc)
    return any(marker.lower() in msg.lower() for marker in TRANSIENT_ERROR_MARKERS)


def build_request(
    *,
    system: str,
    target: dict[str, str],
    years: list[str],
    start_month: str,
    leadtime_months: list[str],
    area: list[float],
    grid: list[float],
) -> dict[str, Any]:
    return {
        "originating_centre": ORIGINATING_CENTRE,
        "system": system,
        "variable": target["variable"],
        "pressure_level": target["pressure_level"],
        "year": years,
        "month": start_month,
        "leadtime_month": leadtime_months,
        "product_type": "monthly_mean",
        "data_format": "grib",
        "download_format": "unarchived",
        "area": area,
        "grid": grid,
    }


def target_file_name(
    *,
    block: str,
    start_year: int,
    end_year: int,
    system: str,
    target_label: str,
    start_month: str,
    leadtime_months: list[str],
) -> str:
    lt_first = int(leadtime_months[0])
    lt_last = int(leadtime_months[-1])
    return (
        f"cds__{DATASET}__ecmwf__system_{system}__{block}__"
        f"{start_year}_{end_year}__{target_label}__m{start_month}__"
        f"lt{lt_first:02d}-{lt_last:02d}__NH0_90__grid_1p0.grib"
    )


def retrieve_with_retry(
    *,
    client: cdsapi.Client,
    dataset: str,
    request: dict[str, Any],
    target_path: Path,
    max_retries: int,
    sleep_seconds: int,
    dry_run: bool,
) -> None:
    part_path = target_path.with_suffix(target_path.suffix + ".part")

    if dry_run:
        print(f"[DRY-RUN] Would retrieve {target_path}", flush=True)
        return

    for attempt in range(1, max_retries + 1):
        try:
            if part_path.exists():
                part_path.unlink()
            print(f"[{utc_now()}] START attempt={attempt} target={target_path}", flush=True)
            client.retrieve(dataset, request, str(part_path))
            if not part_path.exists():
                raise RuntimeError(f"CDS retrieval finished but part file was not created: {part_path}")
            if part_path.stat().st_size <= 0:
                raise RuntimeError(f"CDS retrieval produced empty file: {part_path}")
            part_path.replace(target_path)
            print(f"[{utc_now()}] DONE target={target_path} size={target_path.stat().st_size}", flush=True)
            return
        except Exception as exc:
            print(f"[{utc_now()}] ERROR attempt={attempt} target={target_path} error={exc!r}", flush=True)
            if attempt >= max_retries or not is_transient_error(exc):
                raise
            delay = sleep_seconds * attempt
            print(f"[{utc_now()}] RETRY after_seconds={delay}", flush=True)
            time.sleep(delay)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download ECMWF C3S seasonal monthly pressure-level GRIB files for z500, t850, and z925."
    )
    parser.add_argument("--block", choices=["hindcast", "forecast"], required=True)
    parser.add_argument("--start-year", type=int, required=True)
    parser.add_argument("--end-year", type=int, required=True)
    parser.add_argument("--system", default=DEFAULT_SYSTEM)
    parser.add_argument("--start-months", default="01,02,03,04,05,06,07,08,09,10,11,12")
    parser.add_argument("--leadtime-months", default="1,2,3,4,5,6")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT))
    parser.add_argument("--area", type=parse_area, default="90,-180,0,180")
    parser.add_argument("--grid", type=parse_grid, default="1.0,1.0")
    parser.add_argument("--max-retries", type=int, default=6)
    parser.add_argument("--sleep-seconds", type=int, default=120)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.start_year > args.end_year:
        raise SystemExit("ERROR: start-year must be <= end-year")

    years = [str(y) for y in range(args.start_year, args.end_year + 1)]
    start_months = [f"{int(m):02d}" for m in parse_csv_strings(args.start_months)]
    leadtime_months = [str(int(m)) for m in parse_csv_strings(args.leadtime_months)]

    if not leadtime_months:
        raise SystemExit("ERROR: leadtime-months is empty")

    output_root = Path(args.output_root)
    block_dir = output_root / f"{args.block}_{args.start_year}_{args.end_year}"

    print(f"[{utc_now()}] DATASET={DATASET}", flush=True)
    print(f"[{utc_now()}] BLOCK={args.block}", flush=True)
    print(f"[{utc_now()}] YEARS={args.start_year}-{args.end_year}", flush=True)
    print(f"[{utc_now()}] SYSTEM={args.system}", flush=True)
    print(f"[{utc_now()}] OUTPUT_ROOT={output_root}", flush=True)
    print(f"[{utc_now()}] TARGETS={','.join(t['label'] for t in TARGETS)}", flush=True)
    print(f"[{utc_now()}] START_MONTHS={','.join(start_months)}", flush=True)
    print(f"[{utc_now()}] LEADTIME_MONTHS={','.join(leadtime_months)}", flush=True)

    if not args.dry_run:
        block_dir.mkdir(parents=True, exist_ok=True)

    client = cdsapi.Client()

    for target in TARGETS:
        target_dir = block_dir / target["label"]
        if not args.dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)

        for start_month in start_months:
            request = build_request(
                system=args.system,
                target=target,
                years=years,
                start_month=start_month,
                leadtime_months=leadtime_months,
                area=args.area,
                grid=args.grid,
            )
            filename = target_file_name(
                block=args.block,
                start_year=args.start_year,
                end_year=args.end_year,
                system=args.system,
                target_label=target["label"],
                start_month=start_month,
                leadtime_months=leadtime_months,
            )
            target_path = target_dir / filename
            request_path = Path(str(target_path) + ".request.json")
            sha_path = Path(str(target_path) + ".sha256")

            if target_path.exists() and request_path.exists() and sha_path.exists() and not args.force:
                print(f"[{utc_now()}] SKIP existing complete target={target_path}", flush=True)
                continue

            if target_path.exists() and not args.force:
                raise SystemExit(f"ERROR: target exists without complete sidecars, inspect manually: {target_path}")

            if args.force:
                for p in [target_path, request_path, sha_path, target_path.with_suffix(target_path.suffix + ".part")]:
                    if p.exists():
                        p.unlink()

            sidecar = {
                "created_at_utc": utc_now(),
                "dataset": DATASET,
                "originating_centre": ORIGINATING_CENTRE,
                "system": args.system,
                "block": args.block,
                "start_year": args.start_year,
                "end_year": args.end_year,
                "target": target,
                "start_month": start_month,
                "leadtime_months": leadtime_months,
                "area": args.area,
                "grid": args.grid,
                "request": request,
                "target_path": str(target_path),
            }

            retrieve_with_retry(
                client=client,
                dataset=DATASET,
                request=request,
                target_path=target_path,
                max_retries=args.max_retries,
                sleep_seconds=args.sleep_seconds,
                dry_run=args.dry_run,
            )

            if not args.dry_run:
                digest = sha256_file(target_path)
                write_text(sha_path, f"{digest}  {target_path.name}\n")
                sidecar["completed_at_utc"] = utc_now()
                sidecar["sha256"] = digest
                sidecar["size_bytes"] = target_path.stat().st_size
                write_json(request_path, sidecar)
                print(f"[{utc_now()}] WROTE sidecars for target={target_path}", flush=True)

    print(f"[{utc_now()}] COMPLETE block={args.block} years={args.start_year}-{args.end_year}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
