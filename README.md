# Portable Nail Imaging Data and Reproducibility Bundle

Versioned aggregate data and audit records supporting the manuscript **“An Edge-AI Framework for Standardized Nail Imaging and Recognition of CKD-Associated Nail Phenotypes: A Computational Feasibility Study.”**

## Scope

This repository contains machine-readable tables for:

- source-dataset provenance and licensing;
- dataset audit counts and protected split sizes;
- seven-model recognition training and protected-test summaries;
- x86_64 recognition deployment measurements;
- segmentation validation, protected-test, and runtime results; and
- routing and image-quality engineering summaries.

The repository does **not** redistribute source nail images, masks, patient data, trained model weights, or image-level predictions. Obtain source images from the original repositories listed in `data/source_dataset_registry.csv` and comply with each provider's terms.

## Repository layout

```text
data/                         Machine-readable aggregate tables
scripts/verify_bundle.py      Schema and internal-consistency checks
DATA_DICTIONARY.md            Field definitions and interpretation notes
THIRD_PARTY_DATA.md           Source-data provenance and reuse boundaries
LICENSE                       License for study-generated code
LICENSE-DATA                  License for study-generated aggregate tables
VERSION                       Frozen bundle version
CHECKSUMS.sha256              SHA-256 file-integrity record
```

## Quick verification

```bash
python scripts/verify_bundle.py
```

The verifier uses only the Python standard library. It checks required files, expected row counts, split totals, and the reported top recognition model.

## Key analytical boundaries

- Recognition results are based on a 64-image protected test set and are not clinical validation.
- Segmentation results are internal estimates from a 671-identity protected test set.
- Routing thresholds and quality-control values are development-stage engineering results.
- x86_64 latency is not Raspberry Pi 5 performance.
- Visible nail phenotypes are non-specific and must not be interpreted as CKD diagnosis.

## Release

The manuscript cites the frozen public release `v1.0.0`. Future corrections should use a new semantic version and preserve prior releases.

## Citation

Please cite the associated manuscript and this repository release. Repository URL:

<https://github.com/zaidsawaff/portable-nail-imaging-data>

