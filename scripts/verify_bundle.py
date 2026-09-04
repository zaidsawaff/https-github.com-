#!/usr/bin/env python3
"""Validate the aggregate reproducibility bundle using the standard library."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(name: str) -> list[dict[str, str]]:
    path = DATA / name
    if not path.is_file():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    registry = read_csv("source_dataset_registry.csv")
    audits = read_csv("dataset_audit.csv")
    class_counts = read_csv("general_nail_class_counts.csv")
    recognition = read_csv("recognition_test_metrics.csv")
    segmentation = read_csv("segmentation_test_metrics.csv")

    assert len(registry) == 3
    assert len(audits) == 3
    assert sum(int(row["n"]) for row in class_counts) == 3835

    ckd = next(row for row in audits if row["dataset_id"] == "ckd17")
    assert int(ckd["train_n"]) + int(ckd["validation_n"]) + int(ckd["protected_test_n"]) == 659
    assert int(ckd["historical_valid_count"]) - int(ckd["duplicates_removed"]) == int(ckd["leakage_safe_count"])

    seg = next(row for row in audits if row["dataset_id"] == "segmentation")
    assert int(seg["train_n"]) + int(seg["validation_n"]) + int(seg["protected_test_n"]) == 5955

    assert len(recognition) == 7
    assert all(int(row["test_n"]) == 64 for row in recognition)
    assert max(recognition, key=lambda row: float(row["macro_f1"]))["model"] == "MobileNetV3-Large"

    assert len(segmentation) == 3
    assert all(int(row["test_n"]) == 671 for row in segmentation)
    assert max(segmentation, key=lambda row: float(row["dice_mean"]))["model"] == "LR-ASPP MobileNetV3"

    print("PASS: bundle structure and reported aggregate counts are internally consistent.")


if __name__ == "__main__":
    main()

