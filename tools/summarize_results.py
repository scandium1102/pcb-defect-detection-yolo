"""Recompute the published PCB comparison from the transcribed AP values."""

import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def summarize(path):
    groups = {"9": {}, "5": {}}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            group = row["taxonomy"]
            label = row["class"]
            if group not in groups or not label or label in groups[group]:
                raise ValueError(f"unexpected taxonomy or repeated class: {group}/{label}")
            ap = Decimal(row["ap50"])
            if not ap.is_finite() or not 0 <= ap <= 1:
                raise ValueError(f"invalid AP: {group}/{label}")
            count = int(row["instances"]) if row["instances"] else None
            if group == "5" and (count is None or count <= 0):
                raise ValueError(f"missing or invalid count: {label}")
            groups[group][label] = (ap, count)

    summary = {}
    for group, values in groups.items():
        if len(values) != int(group):
            raise ValueError(f"expected {group} classes; found {len(values)}")
        scores = {label: ap for label, (ap, _) in values.items()}
        summary[group] = {
            "map50": sum(scores.values()) / len(scores),
            "lowest_class": min(scores, key=scores.get),
            "highest_class": max(scores, key=scores.get),
        }
    return summary, sum(count for _, count in groups["5"].values())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, default=ROOT / "data/reported_metrics.csv")
    args = parser.parse_args()
    try:
        summary, total = summarize(args.csv)
    except (OSError, KeyError, InvalidOperation, ValueError) as exc:
        parser.error(str(exc))
    for group, metrics in summary.items():
        print(f"{group} classes: mAP@0.5 {metrics['map50']:.3f}; "
              f"lowest AP {metrics['lowest_class']}; highest AP {metrics['highest_class']}")
    delta = summary["5"]["map50"] - summary["9"]["map50"]
    print(f"Five-minus-nine mAP@0.5: {delta:+.3f}")
    print(f"Five-class annotated instances: {total:,}")


if __name__ == "__main__":
    main()
