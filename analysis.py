"""Validate and analyze the Cookie Cats retention experiment."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

REQUIRED_COLUMNS = {
    "userid",
    "version",
    "sum_gamerounds",
    "retention_1",
    "retention_7",
}
VERSIONS = ("gate_30", "gate_40")


def parse_bool(value: str, field: str, row_number: int) -> int:
    """Convert a CSV Boolean value to zero or one with an actionable error."""
    normalized = value.strip().lower()
    if normalized in {"true", "1"}:
        return 1
    if normalized in {"false", "0"}:
        return 0
    raise ValueError(
        f"Row {row_number}: {field} must be True/False or 1/0, got {value!r}"
    )


def load_rows(path: Path) -> list[dict[str, object]]:
    """Load the experiment CSV and fail fast on data-quality violations."""
    if not path.is_file():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Download it and save it at this path."
        )
    rows: list[dict[str, object]] = []
    seen_users: set[int] = set()
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
        for row_number, raw in enumerate(reader, start=2):
            user_id = int(raw["userid"])
            if user_id in seen_users:
                raise ValueError(f"Row {row_number}: duplicate userid {user_id}")
            seen_users.add(user_id)
            version = raw["version"].strip()
            if version not in VERSIONS:
                raise ValueError(f"Row {row_number}: unexpected version {version!r}")
            rounds_text = raw["sum_gamerounds"].strip()
            rounds = float(rounds_text) if rounds_text else None
            if rounds is not None and rounds < 0:
                raise ValueError(f"Row {row_number}: sum_gamerounds cannot be negative")
            rows.append(
                {
                    "userid": user_id,
                    "version": version,
                    "sum_gamerounds": rounds,
                    "retention_1": parse_bool(
                        raw["retention_1"], "retention_1", row_number
                    ),
                    "retention_7": parse_bool(
                        raw["retention_7"], "retention_7", row_number
                    ),
                }
            )
    if not rows:
        raise ValueError("Dataset contains no player rows")
    return rows


def two_proportion_ztest(
    success_a: int, total_a: int, success_b: int, total_b: int
) -> tuple[float, float]:
    """Return the z-statistic and two-sided p-value for two proportions."""
    pooled = (success_a + success_b) / (total_a + total_b)
    standard_error = math.sqrt(pooled * (1 - pooled) * (1 / total_a + 1 / total_b))
    if standard_error == 0:
        return 0.0, 1.0
    statistic = (success_a / total_a - success_b / total_b) / standard_error
    p_value = math.erfc(abs(statistic) / math.sqrt(2))
    return statistic, p_value


def retention_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Calculate treatment rates, effect sizes, and significance tests."""
    output: list[dict[str, object]] = []
    for metric in ("retention_1", "retention_7"):
        totals = {
            version: sum(row["version"] == version for row in rows)
            for version in VERSIONS
        }
        retained = {
            version: sum(int(row[metric]) for row in rows if row["version"] == version)
            for version in VERSIONS
        }
        rates = {version: retained[version] / totals[version] for version in VERSIONS}
        statistic, p_value = two_proportion_ztest(
            retained["gate_30"],
            totals["gate_30"],
            retained["gate_40"],
            totals["gate_40"],
        )
        output.append(
            {
                "metric": metric,
                "gate_30_players": totals["gate_30"],
                "gate_40_players": totals["gate_40"],
                "gate_30_rate": rates["gate_30"],
                "gate_40_rate": rates["gate_40"],
                "gate_40_minus_gate_30": rates["gate_40"] - rates["gate_30"],
                "z_statistic": statistic,
                "p_value": p_value,
                "significant_at_0_05": p_value < 0.05,
            }
        )
    return output


def rounds_bucket(rounds: float) -> str:
    """Map complete-case game rounds to a dashboard bucket."""
    if rounds == 0:
        return "0"
    if rounds < 30:
        return "1-29"
    if rounds < 40:
        return "30-39"
    if rounds < 90:
        return "40-89"
    return "90+"


def progress_summary(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Summarize complete-case progress segments without causal interpretation."""
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        rounds = row["sum_gamerounds"]
        if rounds is not None:
            groups[(rounds_bucket(float(rounds)), str(row["version"]))].append(row)
    output = []
    for (bucket, version), group in sorted(groups.items()):
        output.append(
            {
                "rounds_bucket": bucket,
                "version": version,
                "players": len(group),
                "day_1_retention": sum(int(row["retention_1"]) for row in group)
                / len(group),
                "day_7_retention": sum(int(row["retention_7"]) for row in group)
                / len(group),
            }
        )
    return output


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    """Write analysis rows to CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Run validation and export analysis-ready summaries."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/cookie_cats.csv"))
    parser.add_argument("--output", type=Path, default=Path("output"))
    args = parser.parse_args()
    rows = load_rows(args.input)
    write_csv(args.output / "retention_summary.csv", retention_summary(rows))
    progress = progress_summary(rows)
    if progress:
        write_csv(args.output / "progress_summary.csv", progress)


if __name__ == "__main__":
    main()
