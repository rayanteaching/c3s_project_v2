#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import platform
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import eccodes
except Exception as exc:
    raise SystemExit(f"ERROR: Python eccodes import failed: {type(exc).__name__}: {exc}")

ENSEMBLE_KEYS = [
    "number",
    "perturbationNumber",
    "forecastNumber",
    "ensembleMember",
    "mars.number",
]

METADATA_KEYS = [
    "shortName",
    "paramId",
    "typeOfLevel",
    "level",
    "dataDate",
    "dataTime",
    "stepRange",
    "step",
    "number",
    "perturbationNumber",
    "forecastNumber",
    "ensembleMember",
    "mars.number",
]


@dataclass
class FileSummary:
    path: Path
    message_count: int = 0
    variable_counts: Counter = field(default_factory=Counter)
    key_values: dict[str, set[str]] = field(default_factory=lambda: {key: set() for key in ENSEMBLE_KEYS})
    variable_member_values: dict[str, dict[str, set[str]]] = field(
        default_factory=lambda: defaultdict(lambda: {key: set() for key in ENSEMBLE_KEYS})
    )
    sample_messages: list[dict[str, Any]] = field(default_factory=list)
    error: str | None = None


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git_value(args: list[str]) -> str:
    try:
        return subprocess.check_output(["git", *args], text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "UNKNOWN"


def safe_get(gid: int, key: str) -> Any:
    try:
        return eccodes.codes_get(gid, key)
    except Exception:
        return None


def normalize_value(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "" or text.upper() == "MISSING":
        return None
    return text


def sort_values(values: set[str]) -> list[str]:
    def key_func(text: str) -> tuple[int, Any]:
        try:
            return (0, int(text))
        except Exception:
            return (1, text)
    return sorted(values, key=key_func)


def format_values(values: set[str], max_items: int = 120) -> str:
    ordered = sort_values(values)
    if not ordered:
        return "-"
    shown = ordered[:max_items]
    suffix = "" if len(ordered) <= max_items else f",...(+{len(ordered) - max_items} more)"
    return ",".join(shown) + suffix


def inspect_grib(path: Path, sample_limit: int = 12) -> FileSummary:
    summary = FileSummary(path=path)

    try:
        with path.open("rb") as handle:
            while True:
                gid = eccodes.codes_grib_new_from_file(handle)
                if gid is None:
                    break

                summary.message_count += 1

                row: dict[str, Any] = {}
                for key in METADATA_KEYS:
                    row[key] = safe_get(gid, key)

                short_name = normalize_value(row.get("shortName")) or "UNKNOWN"
                summary.variable_counts[short_name] += 1

                for key in ENSEMBLE_KEYS:
                    value = normalize_value(row.get(key))
                    if value is not None:
                        summary.key_values[key].add(value)
                        summary.variable_member_values[short_name][key].add(value)

                if len(summary.sample_messages) < sample_limit:
                    summary.sample_messages.append(row)

                eccodes.codes_release(gid)

    except Exception as exc:
        summary.error = f"{type(exc).__name__}: {exc}"

    return summary


def choose_primary_key(key_values: dict[str, set[str]]) -> str | None:
    for key in ENSEMBLE_KEYS:
        if key_values.get(key):
            return key
    return None


def write_report(report_path: Path, directories: list[Path], summaries_by_dir: dict[Path, list[FileSummary]]) -> None:
    lines: list[str] = []

    lines.append("C3S ECMWF SEASONAL ENSEMBLE MEMBER REPORT")
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"Generated UTC: {utc_now()}")
    lines.append(f"Working directory: {Path.cwd()}")
    lines.append(f"Python: {sys.version.split()[0]}")
    lines.append(f"Platform: {platform.platform()}")
    lines.append(f"Git branch: {git_value(['rev-parse', '--abbrev-ref', 'HEAD'])}")
    lines.append(f"Git commit: {git_value(['rev-parse', 'HEAD'])}")
    lines.append("")
    lines.append("Inspected directories:")
    for directory in directories:
        lines.append(f"- {directory}")
    lines.append("")

    for directory in directories:
        summaries = summaries_by_dir[directory]
        lines.append("=" * 80)
        lines.append(f"DIRECTORY SUMMARY: {directory}")
        lines.append("=" * 80)

        grib_files = [summary for summary in summaries if summary.path.suffix == ".grib"]
        failed_files = [summary for summary in summaries if summary.error]

        folder_key_values: dict[str, set[str]] = {key: set() for key in ENSEMBLE_KEYS}
        folder_variable_counts: Counter = Counter()
        folder_variable_member_values: dict[str, dict[str, set[str]]] = defaultdict(
            lambda: {key: set() for key in ENSEMBLE_KEYS}
        )

        for summary in grib_files:
            folder_variable_counts.update(summary.variable_counts)
            for key in ENSEMBLE_KEYS:
                folder_key_values[key].update(summary.key_values[key])
            for variable, key_map in summary.variable_member_values.items():
                for key in ENSEMBLE_KEYS:
                    folder_variable_member_values[variable][key].update(key_map[key])

        primary_key = choose_primary_key(folder_key_values)

        lines.append(f"GRIB file count: {len(grib_files)}")
        lines.append(f"Failed file count: {len(failed_files)}")
        lines.append("")

        lines.append("Detected ensemble-like keys across this directory:")
        any_key = False
        for key in ENSEMBLE_KEYS:
            values = folder_key_values[key]
            if values:
                any_key = True
                lines.append(f"- {key}: count={len(values)} values={format_values(values)}")
        if not any_key:
            lines.append("- No standard ensemble-like key detected.")
        lines.append("")

        if primary_key is not None:
            lines.append("MAIN DIRECTORY RESULT")
            lines.append(f"Primary ensemble member key: {primary_key}")
            lines.append(f"Unique ensemble member count across directory: {len(folder_key_values[primary_key])}")
            lines.append(f"Unique ensemble members across directory: {format_values(folder_key_values[primary_key])}")
        else:
            lines.append("MAIN DIRECTORY RESULT")
            lines.append("Primary ensemble member key: UNKNOWN")
            lines.append("Unique ensemble member count across directory: UNKNOWN")
        lines.append("")

        lines.append("Directory messages by variable:")
        if folder_variable_counts:
            for variable, count in sorted(folder_variable_counts.items()):
                lines.append(f"- {variable}: {count}")
        else:
            lines.append("- None")
        lines.append("")

        lines.append("Directory member counts by variable:")
        if primary_key is not None and folder_variable_member_values:
            for variable in sorted(folder_variable_member_values):
                values = folder_variable_member_values[variable][primary_key]
                lines.append(f"- {variable}: member_count={len(values)} members={format_values(values)}")
        else:
            lines.append("- UNKNOWN")
        lines.append("")

        if failed_files:
            lines.append("Failed files:")
            for summary in failed_files:
                lines.append(f"- {summary.path.name}: {summary.error}")
            lines.append("")

        lines.append("-" * 80)
        lines.append("FILE DETAILS")
        lines.append("-" * 80)

        for summary in sorted(grib_files, key=lambda item: item.path.name):
            file_primary_key = choose_primary_key(summary.key_values)

            lines.append("")
            lines.append(f"File: {summary.path.name}")
            lines.append(f"Path: {summary.path}")
            lines.append(f"Size bytes: {summary.path.stat().st_size if summary.path.exists() else 'MISSING'}")
            lines.append(f"Message count: {summary.message_count}")

            if summary.error:
                lines.append(f"ERROR: {summary.error}")
                continue

            lines.append("Variables:")
            for variable, count in sorted(summary.variable_counts.items()):
                lines.append(f"- {variable}: {count}")

            lines.append("Detected ensemble-like keys:")
            any_file_key = False
            for key in ENSEMBLE_KEYS:
                values = summary.key_values[key]
                if values:
                    any_file_key = True
                    lines.append(f"- {key}: count={len(values)} values={format_values(values)}")
            if not any_file_key:
                lines.append("- No standard ensemble-like key detected.")

            if file_primary_key is not None:
                lines.append("Main file result:")
                lines.append(f"- primary_key: {file_primary_key}")
                lines.append(f"- ensemble_member_count: {len(summary.key_values[file_primary_key])}")
                lines.append(f"- ensemble_members: {format_values(summary.key_values[file_primary_key])}")
                lines.append("Member counts by variable:")
                for variable in sorted(summary.variable_member_values):
                    values = summary.variable_member_values[variable][file_primary_key]
                    lines.append(f"- {variable}: member_count={len(values)} members={format_values(values)}")
            else:
                lines.append("Main file result:")
                lines.append("- ensemble_member_count: UNKNOWN")

            lines.append("First sample messages:")
            for idx, row in enumerate(summary.sample_messages, start=1):
                parts = []
                for key in ["shortName", "typeOfLevel", "level", "dataDate", "dataTime", "stepRange", "number", "perturbationNumber"]:
                    parts.append(f"{key}={row.get(key)}")
                lines.append(f"- {idx:03d}: " + " ".join(parts))

        lines.append("")

    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Report ensemble member counts in C3S ECMWF seasonal GRIB files.")
    parser.add_argument("--hindcast-dir", required=True, type=Path)
    parser.add_argument("--forecast-dir", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()

    directories = [args.hindcast_dir, args.forecast_dir]
    summaries_by_dir: dict[Path, list[FileSummary]] = {}

    for directory in directories:
        if not directory.exists():
            raise SystemExit(f"ERROR: directory does not exist: {directory}")
        if not directory.is_dir():
            raise SystemExit(f"ERROR: path is not a directory: {directory}")

        files = sorted(directory.glob("*.grib"))
        if not files:
            raise SystemExit(f"ERROR: no .grib files found in directory: {directory}")

        summaries_by_dir[directory] = []
        for path in files:
            print(f"[{utc_now()}] Inspecting {path}", flush=True)
            summaries_by_dir[directory].append(inspect_grib(path))

    args.report.parent.mkdir(parents=True, exist_ok=True)
    write_report(args.report, directories, summaries_by_dir)
    print(f"[{utc_now()}] Report written: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
