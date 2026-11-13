# self-supervised-wetland-segmentation-from-airborne-hyperspectral-imagery

This repository contains the complete implementation of the paper
**Self Supervised Wetland Segmentation from Airborne Hyperspectral Imagery**, accepted at Remote Sensing Letters Annual 2025.

## Components

- `src/` — reference implementation used to produce the published results
- `requirements.txt` — pinned dependencies
- `scripts/` — command line entry points

## Reproducing the results

```
pip install -r requirements.txt
python scripts/run_experiment.py --config configs/default.json
```

The released release tag `v1.0.0` corresponds to the camera-ready artefact.
