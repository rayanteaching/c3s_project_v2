#!/home/fibi/miniforge3/envs/cds_env/bin/python
import argparse
import hashlib
import json
import random
import time
from datetime import datetime, timezone
from pathlib import Path

import cdsapi


PROJECT_ROOT = Path("/home/fibi/projects/c3s_project_v2")
RAW_DIR = Path("/mnt/e/last-aticol/data/raw/era5/pressure-levels/geopotential/500hPa/monthly")

DATASET = "reanalysis-era5-pressure-levels-monthly-means"
PRODUCT_TYPE = "monthly_averaged_reanalysis"
VARIABLE = "geopotential"
PRESSURE_LEVEL = "500"

REGION_NAME = "NH0_90"
AREA = [90.0, -180.0, 0.0, 180.0]
GRID_NAME = "grid_1p0"
GRID = [1.0, 1.0]

VAR_TAG = "z500"
LEVEL_TAG = "500hPa"


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_sha256_sidecar(target: Path, sidecar: Path) -> None:
    digest = sha256_file(target)
    sidecar.write_text(f"{digest}  {str(target)}\n", encoding="utf-8")


def read_sha256_sidecar(sidecar: Path):
    line = sidecar.read_text(encoding="utf-8").strip()
    parts = line.split()
    if len(parts) < 2:
        raise ValueError(f"Invalid sha256 sidecar: {sidecar}")
    return parts[0], " ".join(parts[1:])


def verify_one(target: Path, sidecar: Path) -> bool:
    if not target.exists() or not sidecar.exists():
        return False
    expected_hash, expected_path = read_sha256_sidecar(sidecar)
    if expected_path != str(target):
        return False
    actual_hash = sha256_file(target)
    return actual_hash == expected_hash


def build_filename(year: int, month: int) -> str:
    y = f"{year:04d}"
    m = f"m{month:02d}"
    return (
        f"cds__era5_pl_monthly__ERA5__reanalysis__{VAR_TAG}__{LEVEL_TAG}"
        f"__monthly__{y}-{y}__{m}__{REGION_NAME}__{GRID_NAME}.grib"
    )


def build_request(year: int, month: int) -> dict:
    return {
        "product_type": [PRODUCT_TYPE],
        "variable": [VARIABLE],
        "pressure_level": [PRESSURE_LEVEL],
        "year": [f"{year:04d}"],
        "month": [f"{month:02d}"],
        "time": ["00:00"],
        "data_format": "grib",
        "area": AREA,
        "grid": GRID,
    }


def retrieve_with_retry(client: cdsapi.Client, request: dict, tmp: Path, max_retries: int, sleep_sec: int) -> None:
    last_exc = None
    for attempt in range(1, max_retries + 1):
        try:
            if tmp.exists():
                tmp.unlink()
            client.retrieve(DATASET, request, str(tmp))
            return
        except Exception as exc:
            last_exc = exc
            msg = str(exc)
            is_transient = (
                "SSLEOFError" in msg
                or "Max retries exceeded" in msg
                or "Read timed out" in msg
                or "Connection reset" in msg
                or "Remote end closed connection" in msg
                or "EOF occurred in violation of protocol" in msg
            )
            if (not is_transient) or (attempt == max_retries):
                raise
            wait = sleep_sec + random.randint(0, 5)
            print(
                f"RETRY {attempt}/{max_retries} after error: "
                f"{type(exc).__name__}: {msg}",
                flush=True,
            )
            time.sleep(wait)
    if last_exc is not None:
        raise last_exc


def sidecar_paths(target: Path):
    req_json = target.with_suffix(target.suffix + ".request.json")
    sha_sidecar = target.with_suffix(target.suffix + ".sha256")
    tmp = target.with_suffix(target.suffix + ".tmp")
    return req_json, sha_sidecar, tmp


def verify_year(year: int) -> bool:
    for month in range(1, 13):
        target = RAW_DIR / build_filename(year, month)
        req_json, sha_sidecar, _tmp = sidecar_paths(target)

        if not req_json.exists():
            return False
        if not verify_one(target, sha_sidecar):
            return False
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start-year", type=int, default=2000)
    ap.add_argument("--end-year", type=int, default=2025)
    ap.add_argument("--year", type=int)
    ap.add_argument("--month", type=int)
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--max-retries", type=int, default=8)
    ap.add_argument("--retry-sleep", type=int, default=15)
    args = ap.parse_args()

    if args.year is not None or args.month is not None:
        if args.year is None or args.month is None:
            raise SystemExit("If using --year/--month, provide both.")
        years = [args.year]
        months = [args.month]
    else:
        if args.start_year > args.end_year:
            raise SystemExit("--start-year must be <= --end-year")
        years = list(range(args.start_year, args.end_year + 1))
        months = list(range(1, 13))

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    client = cdsapi.Client()

    for year in years:
        if months == list(range(1, 13)):
            print(f"===== START YEAR {year} =====", flush=True)
            print(utc_stamp(), flush=True)

        for month in months:
            if month < 1 or month > 12:
                raise SystemExit("month must be 1..12")

            target = RAW_DIR / build_filename(year, month)
            req_json, sha_sidecar, tmp = sidecar_paths(target)

            if not args.overwrite and verify_one(target, sha_sidecar):
                print(f"SKIP VERIFIED: {target}", flush=True)
                continue

            request = build_request(year, month)

            payload = {
                "created_at_utc": utc_stamp(),
                "dataset": DATASET,
                "request": request,
                "target": str(target),
            }
            req_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

            if tmp.exists():
                tmp.unlink()
            if target.exists():
                target.unlink()

            retrieve_with_retry(client, request, tmp, args.max_retries, args.retry_sleep)
            tmp.replace(target)

            write_sha256_sidecar(target, sha_sidecar)

            if not verify_one(target, sha_sidecar):
                raise SystemExit(f"VERIFY FAILED: {target}")

            print("OK", flush=True)
            print(f"GRIB: {target}", flush=True)
            print(f"REQUEST: {req_json}", flush=True)
            print(f"SHA256: {sha_sidecar}", flush=True)

        if months == list(range(1, 13)):
            print(f"===== DONE YEAR {year} =====", flush=True)
            print(utc_stamp(), flush=True)

            if not verify_year(year):
                raise SystemExit(f"VERIFY YEAR FAILED: {year}")

            print(f"===== VERIFIED YEAR {year} =====", flush=True)
            print(utc_stamp(), flush=True)

    if months == list(range(1, 13)) and (args.year is None and args.month is None):
        print("ALL DONE", flush=True)


if __name__ == "__main__":
    main()
