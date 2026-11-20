#!/usr/bin/env python3
"""Summarize observed print-shop jobs from a CSV file (Python standard library only)."""

import argparse
import csv
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

REQUIRED_COLUMNS = {
    "job_id", "time_received", "submission_method", "pages", "copies",
    "print_type", "configuration_required", "processing_start",
    "processing_end", "queue_wait_minutes", "vendor_interrupted", "issue",
}
TIME_FORMAT = "%H:%M"


def parse_args():
    parser = argparse.ArgumentParser(description="Analyze observed print-shop jobs.")
    parser.add_argument(
        "csv_path", nargs="?", default="data/data.csv",
        help="Input CSV path (default: data/data.csv, relative to current directory)",
    )
    return parser.parse_args()


def mean(values):
    return sum(values) / len(values) if values else 0.0


def read_jobs(path):
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV is empty or has no header row.")
        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))

        jobs = []
        for line_number, row in enumerate(reader, start=2):
            try:
                row["pages"] = int(row["pages"])
                row["copies"] = int(row["copies"])
                row["queue_wait_minutes"] = float(row["queue_wait_minutes"])
                start = datetime.strptime(row["processing_start"].strip(), TIME_FORMAT)
                end = datetime.strptime(row["processing_end"].strip(), TIME_FORMAT)
                received = datetime.strptime(row["time_received"].strip(), TIME_FORMAT)
                duration = (end - start).total_seconds() / 60
                if duration < 0:
                    duration += 24 * 60  # supports jobs crossing midnight
                if row["pages"] < 0 or row["copies"] < 1 or row["queue_wait_minutes"] < 0:
                    raise ValueError("pages, copies, and queue wait must be non-negative (copies >= 1)")
                row["_start"] = start
                row["_end"] = end
                row["_received"] = received
                row["_duration"] = duration
                jobs.append(row)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid data on CSV line {line_number}: {exc}") from exc

    if not jobs:
        raise ValueError("CSV contains a header but no job records.")
    return jobs


def group_stats(jobs, field):
    groups = defaultdict(list)
    for job in jobs:
        groups[job[field].strip() or "(blank)"].append(job["queue_wait_minutes"])
    return groups


def print_group_comparison(title, jobs, field):
    print(f"\n{title}")
    print(f"{'Category':<24}{'Jobs':>6}{'Avg wait':>12}{'Max wait':>12}")
    print("-" * 54)
    for category, waits in sorted(group_stats(jobs, field).items()):
        print(f"{category:<24}{len(waits):>6}{mean(waits):>11.1f}m{max(waits):>11.0f}m")


def count_overlapping_jobs(jobs):
    """Count pairs whose recorded processing intervals overlap."""
    ordered = sorted(jobs, key=lambda job: job["_start"])
    overlaps = 0
    for index, current in enumerate(ordered):
        for later in ordered[index + 1:]:
            if later["_start"] >= current["_end"]:
                break
            if later["_start"] < current["_end"] and later["_end"] > current["_start"]:
                overlaps += 1
    return overlaps


def main():
    args = parse_args()
    path = Path(args.csv_path)
    try:
        jobs = read_jobs(path)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    waits = [job["queue_wait_minutes"] for job in jobs]
    durations = [job["_duration"] for job in jobs]
    methods = Counter(job["submission_method"].strip() or "(blank)" for job in jobs)
    issues = Counter(
        job["issue"].strip() for job in jobs
        if job["issue"] and job["issue"].strip().lower() not in {"none", "n/a", "na"}
    )
    no_issue_reported = sum(
        not job["issue"] or job["issue"].strip().lower() in {"none", "n/a", "na"}
        for job in jobs
    )
    interrupted = sum(job["vendor_interrupted"].strip().lower() == "yes" for job in jobs)
    configured = sum(job["configuration_required"].strip().lower() == "yes" for job in jobs)

    print("PRINT-SHOP WORKFLOW ANALYSIS")
    print("=" * 30)
    print(f"Input file:                 {path}")
    print(f"Total jobs observed:        {len(jobs)}")
    print(f"Average queue wait:         {mean(waits):.2f} minutes")
    print(f"Median queue wait:          {sorted(waits)[len(waits)//2] if len(waits) % 2 else (sorted(waits)[len(waits)//2-1] + sorted(waits)[len(waits)//2]) / 2:.2f} minutes")
    print(f"Maximum queue wait:         {max(waits):.0f} minutes")
    print(f"Average processing time:    {mean(durations):.2f} minutes")
    print(f"Jobs needing configuration: {configured}/{len(jobs)}")
    print(f"Jobs with vendor interruption: {interrupted}/{len(jobs)}")

    print("\nSUBMISSION METHODS")
    for method, count in sorted(methods.items()):
        print(f"  {method}: {count}")

    print_group_comparison("QUEUE WAIT BY CONFIGURATION", jobs, "configuration_required")
    print_group_comparison("QUEUE WAIT BY VENDOR INTERRUPTION", jobs, "vendor_interrupted")
    print_group_comparison("QUEUE WAIT BY PRINT TYPE", jobs, "print_type")

    print("\nRECORDED ISSUES")
    print(f"  No issue reported: {no_issue_reported}")
    if issues:
        for issue, count in issues.most_common():
            print(f"  {issue}: {count}")
    else:
        print("  No issues recorded.")

    overlap_count = count_overlapping_jobs(jobs)
    print("\nDATA QUALITY CHECK")
    print(f"  Rows with blank issue field: {sum(not job['issue'] or not job['issue'].strip() for job in jobs)}")
    print(f"  Overlapping processing-interval pairs: {overlap_count}")
    if overlap_count:
        print("  Review these timestamps if all jobs are expected to use one printer.")

    print("\nINTERPRETATION")
    config_groups = group_stats(jobs, "configuration_required")
    interruption_groups = group_stats(jobs, "vendor_interrupted")
    if "Yes" in config_groups and "No" in config_groups:
        print(
            f"  Jobs marked as requiring configuration waited {mean(config_groups['Yes']):.1f} min on average, "
            f"vs {mean(config_groups['No']):.1f} min for jobs not requiring it."
        )
    if "Yes" in interruption_groups and "No" in interruption_groups:
        print(
            f"  Jobs marked with vendor interruption waited {mean(interruption_groups['Yes']):.1f} min on average, "
            f"vs {mean(interruption_groups['No']):.1f} min without interruption."
        )
    print("  These are observed associations, not proof of causation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
