#!/home/fibi/miniforge3/envs/cds_env/bin/python
import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="Root directory to scan")
    ap.add_argument("--pattern", required=True, help="Glob pattern, for example *.grib")
    ap.add_argument("--out", required=True, help="Output CSV file")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.out).resolve()

    if not root.exists():
        raise SystemExit(f"Root directory does not exist: {root}")

    out.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for path in sorted(root.glob(args.pattern)):
        if not path.is_file():
            continue
        stat = path.stat()
        rows.append(
            {
                "scanned_at_utc": utc_now(),
                "root": str(root),
                "filename": path.name,
                "absolute_path": str(path),
                "size_bytes": stat.st_size,
                "mtime_epoch": int(stat.st_mtime),
            }
        )

    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scanned_at_utc",
                "root",
                "filename",
                "absolute_path",
                "size_bytes",
                "mtime_epoch",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
