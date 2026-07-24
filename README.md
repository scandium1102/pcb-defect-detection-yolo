# PCB Defect Detection with YOLO

An academic computer-vision case study for multi-class PCB defect detection using YOLO. It focuses on documenting the evaluated taxonomy and the recorded validation results, while excluding the source dataset and training environment.

![Representative predictions](assets/pcb-predictions.jpg)

## Recorded evaluation snapshot

| Label taxonomy | Recorded mAP@0.5 |
| --- | ---: |
| Nine classes | 0.826 |
| Five classes | 0.815 |

The comparison is useful because changing the label taxonomy changes the learning problem. The score difference is not a claim that one setup is universally better; it records the observed result for this coursework experiment.

## Included evidence

- Training curves and precision-recall figures
- Confusion matrices and class-count summaries
- Example predictions
- Separate artifacts for five-class and nine-class experiments

## Scope and limitations

This repository is an academic portfolio record. The original dataset, model weights, training scripts, machine-specific paths, and raw experiment outputs are intentionally excluded because their public-release rights and reproducibility conditions have not been verified. See [docs/evidence.md](docs/evidence.md).

## Repository layout

```text
assets/       Public evaluation figures
docs/         Evidence, boundaries, and limitations
```

## License

Apache-2.0. See [LICENSE](LICENSE).
