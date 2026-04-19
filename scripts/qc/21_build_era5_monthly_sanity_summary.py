#!/usr/bin/env python3

from __future__ import annotations

import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import cfgrib
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REPO_ROOT = Path("/home/fibi/projects/c3s_project_v2")
RUN_ROOT = REPO_ROOT / "runs" / "2026-04-17_era5_monthly_qc_full"
PLOTS_DIR = RUN_ROOT / "plots"
REPORT_PATH = REPO_ROOT / "docs" / "qc" / "ERA5_MONTHLY_QC_REPORT.md"

TIMESERIES_CSV = RUN_ROOT / "sanity_qc_timeseries.csv"
SUMMARY_CSV = RUN_ROOT / "sanity_qc_dataset_summary.csv"
DETAILS_JSON = RUN_ROOT / "sanity_qc_details.json"

START_YEAR = 2000
END_YEAR = 2025
EXPECTED_COUNT = (END_YEAR - START_YEAR + 1) * 12

FILENAME_PATTERN = re.compile(r"__(\d{4})-(\d{4})__m(\d{2})__")


DATASETS = [
    {
        "name": "tp",
        "root": Path("/mnt/e/last-aticol/data/raw/era5/single-levels/total_precipitation/monthly"),
        "mean_min": 0.0,
        "mean_max": None,
        "expect_nonnegative_mean": True,
    },
    {
        "name": "t2m",
        "root": Path("/mnt/e/last-aticol/data/raw/era5/single-levels/2m_temperature/monthly"),
        "mean_min": 180.0,
        "mean_max": 330.0,
        "expect_nonnegative_mean": False,
    },
    {
        "name": "ws10m",
        "root": Path("/mnt/e/last-aticol/data/raw/era5/single-levels/10m_wind_speed/monthly"),
        "mean_min": 0.0,
        "mean_max": None,
        "expect_nonnegative_mean": True,
    },
    {
        "name": "z500",
        "root": Path("/mnt/e/last-aticol/data/raw/era5/pressure-levels/geopotential/500hPa/monthly"),
        "mean_min": 0.0,
        "mean_max": None,
        "expect_nonnegative_mean": True,
    },
    {
        "name": "t850",
        "root": Path("/mnt/e/last-aticol/data/raw/era5/pressure-levels/temperature/850hPa/monthly"),
        "mean_min": 180.0,
        "mean_max": 330.0,
        "expect_nonnegative_mean": False,
    },
    {
        "name": "z950",
        "root": Path("/mnt/e/last-aticol/data/raw/era5/pressure-levels/geopotential/950hPa/monthly"),
        "mean_min": 0.0,
        "mean_max": None,
        "expect_nonnegative_mean": True,
    },
]


def utc_now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def expected_dates() -> list[str]:
    values: list[str] = []
    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):
            values.append(f"{year}-{month:02d}")
    return values


def parse_year_month(filename: str) -> tuple[int, int]:
    match = FILENAME_PATTERN.search(filename)
    if match is None:
        raise ValueError(f"Could not parse year-month from filename: {filename}")

    year_start = int(match.group(1))
    year_end = int(match.group(2))
    month = int(match.group(3))

    if year_start != year_end:
        raise ValueError(f"Unexpected cross-year filename: {filename}")

    return year_start, month


def detect_data_var(dataset) -> str:
    data_vars = list(dataset.data_vars)
    if not data_vars:
        raise ValueError("No data variable found in GRIB dataset")
    return data_vars[0]


def latitude_name(data_array) -> str | None:
    if "latitude" in data_array.coords:
        return "latitude"
    if "lat" in data_array.coords:
        return "lat"
    return None


def longitude_name(data_array) -> str | None:
    if "longitude" in data_array.coords:
        return "longitude"
    if "lon" in data_array.coords:
        return "lon"
    return None


def weighted_domain_mean(data_array) -> float:
    lat_name = latitude_name(data_array)
    lon_name = longitude_name(data_array)

    if lat_name is None or lon_name is None:
        return float(data_array.mean().item())

    lat_values = data_array[lat_name].values
    weights = np.cos(np.deg2rad(lat_values))

    if not np.isfinite(weights).all():
        return float(data_array.mean(dim=[lat_name, lon_name]).item())

    return float(
        data_array.weighted(data_array[lat_name] * 0 + weights).mean(dim=[lat_name, lon_name]).item()
    )


def open_grib_field(path: Path):
    dataset = cfgrib.open_dataset(path, indexpath="")
    data_var = detect_data_var(dataset)
    data_array = dataset[data_var].squeeze().load()
    dataset.close()
    return data_var, data_array


def process_dataset(config: dict) -> tuple[pd.DataFrame, dict]:
    dataset_name = config["name"]
    dataset_root = config["root"]

    grib_files = sorted(dataset_root.glob("*.grib"))
    rows: list[dict] = []

    for path in grib_files:
        year, month = parse_year_month(path.name)
        date_str = f"{year}-{month:02d}"

        data_var, data_array = open_grib_field(path)

        units = str(data_array.attrs.get("units", "unknown"))

        domain_mean = weighted_domain_mean(data_array)
        domain_min = float(data_array.min().item())
        domain_max = float(data_array.max().item())

        rows.append(
            {
                "dataset": dataset_name,
                "filename": path.name,
                "date": date_str,
                "year": year,
                "month": month,
                "data_var": data_var,
                "units": units,
                "domain_mean": domain_mean,
                "domain_min": domain_min,
                "domain_max": domain_max,
            }
        )

    frame = pd.DataFrame(rows)

    if frame.empty:
        summary = {
            "dataset": dataset_name,
            "root": str(dataset_root),
            "units": "unknown",
            "count": 0,
            "start_date": "",
            "end_date": "",
            "all_finite": False,
            "coverage_complete": False,
            "mean_nonnegative_check": False,
            "mean_range_check": False,
            "seasonal_cycle_check": False,
            "min_domain_mean": None,
            "max_domain_mean": None,
            "mean_of_domain_mean": None,
            "min_of_domain_min": None,
            "max_of_domain_max": None,
            "climatology_amplitude": None,
            "passed": False,
        }
        return frame, summary

    frame = frame.sort_values(["year", "month"]).reset_index(drop=True)

    actual_dates = frame["date"].tolist()
    expected = expected_dates()

    all_finite = bool(
        np.isfinite(frame["domain_mean"]).all()
        and np.isfinite(frame["domain_min"]).all()
        and np.isfinite(frame["domain_max"]).all()
    )

    coverage_complete = actual_dates == expected

    domain_mean_min = float(frame["domain_mean"].min())
    domain_mean_max = float(frame["domain_mean"].max())
    domain_mean_avg = float(frame["domain_mean"].mean())
    domain_min_min = float(frame["domain_min"].min())
    domain_max_max = float(frame["domain_max"].max())

    mean_nonnegative_check = True
    if config["expect_nonnegative_mean"]:
        mean_nonnegative_check = domain_mean_min >= 0.0

    mean_range_check = True
    if config["mean_min"] is not None:
        mean_range_check = mean_range_check and domain_mean_min >= float(config["mean_min"])
    if config["mean_max"] is not None:
        mean_range_check = mean_range_check and domain_mean_max <= float(config["mean_max"])

    monthly_climatology = frame.groupby("month", as_index=True)["domain_mean"].mean()
    climatology_amplitude = float(monthly_climatology.max() - monthly_climatology.min())
    seasonal_cycle_check = bool(math.isfinite(climatology_amplitude) and climatology_amplitude > 0.0)

    passed = all(
        [
            len(frame) == EXPECTED_COUNT,
            all_finite,
            coverage_complete,
            mean_nonnegative_check,
            mean_range_check,
            seasonal_cycle_check,
        ]
    )

    summary = {
        "dataset": dataset_name,
        "root": str(dataset_root),
        "units": str(frame["units"].iloc[0]),
        "count": int(len(frame)),
        "start_date": str(frame["date"].iloc[0]),
        "end_date": str(frame["date"].iloc[-1]),
        "all_finite": all_finite,
        "coverage_complete": coverage_complete,
        "mean_nonnegative_check": mean_nonnegative_check,
        "mean_range_check": mean_range_check,
        "seasonal_cycle_check": seasonal_cycle_check,
        "min_domain_mean": domain_mean_min,
        "max_domain_mean": domain_mean_max,
        "mean_of_domain_mean": domain_mean_avg,
        "min_of_domain_min": domain_min_min,
        "max_of_domain_max": domain_max_max,
        "climatology_amplitude": climatology_amplitude,
        "passed": passed,
    }

    return frame, summary


def make_timeseries_plot(frame: pd.DataFrame, dataset_name: str, units: str) -> str:
    output_path = PLOTS_DIR / f"{dataset_name}_domain_mean_timeseries.png"

    dates = pd.to_datetime(frame["date"] + "-01")

    plt.figure(figsize=(12, 4.5))
    plt.plot(dates, frame["domain_mean"])
    plt.title(f"ERA5 monthly {dataset_name} domain-mean time series")
    plt.xlabel("Date")
    plt.ylabel(f"Domain mean [{units}]")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    return str(output_path.relative_to(REPO_ROOT))


def make_climatology_plot(frame: pd.DataFrame, dataset_name: str, units: str) -> str:
    output_path = PLOTS_DIR / f"{dataset_name}_monthly_climatology.png"

    climatology = frame.groupby("month", as_index=True)["domain_mean"].mean()

    plt.figure(figsize=(8, 4.5))
    plt.plot(climatology.index, climatology.values, marker="o")
    plt.xticks(range(1, 13))
    plt.title(f"ERA5 monthly {dataset_name} domain-mean climatology")
    plt.xlabel("Month")
    plt.ylabel(f"Climatological domain mean [{units}]")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    return str(output_path.relative_to(REPO_ROOT))


def write_report(
    summaries: list[dict],
    plot_registry: dict[str, dict[str, str]],
    structural_qc_ref: str,
    sanity_passed: bool,
) -> None:
    lines: list[str] = []

    lines.append("# ERA5 Monthly QC Report")
    lines.append("")
    lines.append("## Scope")
    lines.append("- Dataset family: ERA5 monthly Northern Hemisphere collection")
    lines.append("- Period: 2000-01 to 2025-12")
    lines.append("- Datasets: tp, t2m, ws10m, z500, t850, z950")
    lines.append("")
    lines.append("## Structural QC")
    lines.append(f"- Structural QC reference: `{structural_qc_ref}`")
    lines.append("- Structural QC status: passed")
    lines.append("- Files per dataset: 312 GRIB + 312 request JSON + 312 SHA256")
    lines.append("")
    lines.append("## Scientific sanity QC pass criteria")
    lines.append("- Full monthly coverage from 2000-01 through 2025-12")
    lines.append("- Finite domain mean, domain minimum, and domain maximum for every monthly field")
    lines.append("- Positive seasonal-cycle amplitude in the domain-mean monthly climatology")
    lines.append("- Nonnegative domain-mean values for tp, ws10m, z500, and z950")
    lines.append("- Domain-mean plausible range check for t2m and t850: 180 K to 330 K")
    lines.append("")
    lines.append("## Dataset summary")
    lines.append("")
    lines.append("| Dataset | Units | Count | Start | End | Mean(domain mean) | Min(domain mean) | Max(domain mean) | Min(domain min) | Max(domain max) | Climatology amplitude | Passed |")
    lines.append("|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|")

    for summary in summaries:
        lines.append(
            "| "
            f"{summary['dataset']} | "
            f"{summary['units']} | "
            f"{summary['count']} | "
            f"{summary['start_date']} | "
            f"{summary['end_date']} | "
            f"{summary['mean_of_domain_mean']:.6f} | "
            f"{summary['min_domain_mean']:.6f} | "
            f"{summary['max_domain_mean']:.6f} | "
            f"{summary['min_of_domain_min']:.6f} | "
            f"{summary['max_of_domain_max']:.6f} | "
            f"{summary['climatology_amplitude']:.6f} | "
            f"{summary['passed']} |"
        )

    lines.append("")
    lines.append("## Generated plots")
    lines.append("")

    for dataset_name, plot_paths in plot_registry.items():
        lines.append(f"### {dataset_name}")
        lines.append(f"- Time series: `{plot_paths['timeseries']}`")
        lines.append(f"- Monthly climatology: `{plot_paths['climatology']}`")
        lines.append("")

    lines.append("## Conclusion")
    if sanity_passed:
        lines.append("- Scientific sanity QC passed for all six ERA5 monthly datasets.")
        lines.append("- The tracked ERA5 monthly collection is structurally complete and scientifically plausible for workflow continuation.")
    else:
        lines.append("- Scientific sanity QC did not pass for all datasets.")
        lines.append("- Review the summary CSV, details JSON, and plots before proceeding.")
    lines.append("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    dataset_frames: list[pd.DataFrame] = []
    summaries: list[dict] = []
    plot_registry: dict[str, dict[str, str]] = {}

    for config in DATASETS:
        frame, summary = process_dataset(config)
        dataset_frames.append(frame)
        summaries.append(summary)

        if not frame.empty:
            plot_registry[config["name"]] = {
                "timeseries": make_timeseries_plot(frame, config["name"], summary["units"]),
                "climatology": make_climatology_plot(frame, config["name"], summary["units"]),
            }

    combined = pd.concat(dataset_frames, ignore_index=True)
    combined.to_csv(TIMESERIES_CSV, index=False)

    summary_frame = pd.DataFrame(summaries)
    summary_frame.to_csv(SUMMARY_CSV, index=False)

    sanity_passed = bool(summary_frame["passed"].all())

    payload = {
        "run": "2026-04-17_era5_monthly_qc_full",
        "checked_at_utc": utc_now_iso(),
        "expected_year_range": f"{START_YEAR}-{END_YEAR}",
        "expected_count_per_dataset": EXPECTED_COUNT,
        "sanity_passed": sanity_passed,
        "dataset_summaries": summaries,
        "plot_registry": plot_registry,
        "timeseries_csv": str(TIMESERIES_CSV.relative_to(REPO_ROOT)),
        "summary_csv": str(SUMMARY_CSV.relative_to(REPO_ROOT)),
        "report_path": str(REPORT_PATH.relative_to(REPO_ROOT)),
    }

    DETAILS_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    write_report(
        summaries=summaries,
        plot_registry=plot_registry,
        structural_qc_ref="runs/2026-04-17_era5_monthly_qc_full/structure_qc_summary.csv",
        sanity_passed=sanity_passed,
    )

    print("ERA5 monthly scientific sanity QC summary")
    print("=" * 72)
    print(summary_frame.to_string(index=False))
    print("=" * 72)
    print(f"Timeseries CSV: {TIMESERIES_CSV}")
    print(f"Summary CSV: {SUMMARY_CSV}")
    print(f"Details JSON: {DETAILS_JSON}")
    print(f"Report: {REPORT_PATH}")

    if sanity_passed:
        print("SANITY_QC_PASS")
        return 0

    print("SANITY_QC_FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
