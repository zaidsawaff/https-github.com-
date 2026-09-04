# Data dictionary

All numeric tables are UTF-8 CSV files with a header row. Empty values and `NA` denote evidence that was not available or not applicable; they are never imputed.

## `source_dataset_registry.csv`

- `dataset_id`: stable short identifier used in this bundle.
- `dataset_name`: public source-dataset title.
- `source_url`: original provider page.
- `source_license`: provider-stated license.
- `role`: analytical role in the study.
- `raw_items`: source item count before study audit, when reported.
- `redistributed`: always `no`; source files are not included here.

## `dataset_audit.csv`

- `historical_valid_count`: readable or historically valid source units.
- `leakage_safe_count`: unique, conflict-free units retained after the stricter audit.
- `duplicates_removed`: exact duplicates removed where this quantity was available.
- `train_n`, `validation_n`, `protected_test_n`: fixed analytical roles.
- `notes`: limitations or interpretation.

## Recognition tables

- `recognition_training_history.csv`: recovered training endpoints. `generalization_gap` is training macro-F1 minus validation macro-F1.
- `recognition_test_metrics.csv`: accuracy, balanced accuracy, and macro-F1 on the common protected 64-image test set.
- `recognition_deployment_metrics.csv`: x86_64 CPU measurements for parity-valid exported representations; these are not Raspberry Pi results.

## Segmentation tables

- `segmentation_validation_metrics.csv`: validation-only architecture selection results.
- `segmentation_test_metrics.csv`: protected 671-identity test performance and bootstrap confidence intervals.
- `segmentation_runtime_metrics.csv`: x86_64 CPU export-parity and runtime results for the selected LR-ASPP model.

## `routing_quality_summary.csv`

Each row is one engineering endpoint. `cohort` identifies the development or challenge set, `value` is the reported point estimate, and `status` distinguishes rejected designs, development-stage evidence, or provisional controls.

