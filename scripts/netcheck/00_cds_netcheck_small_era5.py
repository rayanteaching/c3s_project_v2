#!/home/fibi/miniforge3/envs/cds_env/bin/python
import hashlib
import json
import random
import time
from datetime import datetime, timezone
from pathlib import Path

import cdsapi
import requests


PROJECT_ROOT = Path("/home/fibi/projects/c3s_project_v2")
RUN_NAME = "wsl_cds_netcheck_era5_small"
RUN_DIR = PROJECT_ROOT / "runs" / RUN_NAME
LOG_DIR = PROJECT_ROOT / "logs"
TMP_ROOT = Path("/mnt/e/last-aticol/tmp/netcheck")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def retrieve_with_retry(client: cdsapi.Client, dataset: str, request: dict, target_tmp: Path, max_retries: int = 5) -> None:
    last_exc = None
    for attempt in range(1, max_retries + 1):
        try:
            if target_tmp.exists():
                target_tmp.unlink()
            client.retrieve(dataset, request, str(target_tmp))
            return
        except Exception as exc:
            last_exc = exc
            wait = 5 + random.randint(0, 5)
            print(f"[{utc_now()}] RETRY {attempt}/{max_retries}: {type(exc).__name__}: {exc}", flush=True)
            if attempt == max_retries:
                break
            time.sleep(wait)
    raise last_exc


def main() -> int:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    TMP_ROOT.mkdir(parents=True, exist_ok=True)

    dataset = "reanalysis-era5-single-levels-monthly-means"
    request = {
        "product_type": "monthly_averaged_reanalysis",
        "variable": ["2m_temperature"],
        "year": ["2000"],
        "month": ["01"],
        "time": ["00:00"],
        "format": "grib",
        "area": [60.0, 0.0, 50.0, 10.0],
        "grid": [5.0, 5.0],
    }

    target = TMP_ROOT / "netcheck__ERA5__t2m__2000-01__smallbox__grid5p0.grib"
    tmp = target.with_suffix(target.suffix + ".tmp")
    req_json = target.with_suffix(target.suffix + ".request.json")
    sha_file = target.with_suffix(target.suffix + ".sha256")

    run_md = RUN_DIR / "run.md"
    command_txt = RUN_DIR / "command.txt"
    status_json = RUN_DIR / "status.json"

    write_text(
        run_md,
        "# Run\n\n"
        "Purpose: verify that CDS access from WSL works end-to-end with a very small ERA5 request.\n"
    )

    write_text(
        command_txt,
        "python scripts/netcheck/00_cds_netcheck_small_era5.py\n"
    )

    status = {
        "run": RUN_NAME,
        "result": "running",
        "reason": "Netcheck started",
        "next_action": "Wait for completion"
    }
    write_text(status_json, json.dumps(status, indent=2))

    payload = {
        "created_at_utc": utc_now(),
        "dataset": dataset,
        "request": request,
        "target": str(target),
    }
    write_text(req_json, json.dumps(payload, indent=2))

    print(f"[{utc_now()}] Checking CDS API root", flush=True)
    resp = requests.get("https://cds.climate.copernicus.eu/api", timeout=30)
    print(f"[{utc_now()}] API status code: {resp.status_code}", flush=True)

    client = cdsapi.Client()

    print(f"[{utc_now()}] Starting ERA5 small download", flush=True)
    retrieve_with_retry(client, dataset, request, tmp, max_retries=5)
    tmp.replace(target)

    digest = sha256_file(target)
    write_text(sha_file, f"{digest}  {target}\n")

    status = {
        "run": RUN_NAME,
        "result": "success",
        "reason": "Small ERA5 request completed successfully",
        "next_action": "Proceed to the first official ERA5 downloader"
    }
    write_text(status_json, json.dumps(status, indent=2))

    print(f"[{utc_now()}] SUCCESS", flush=True)
    print(f"[{utc_now()}] FILE: {target}", flush=True)
    print(f"[{utc_now()}] SHA256: {digest}", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
