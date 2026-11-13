"""Self-supervised wetland segmentation for hyperspectral tiles."""

from dataclasses import dataclass

import numpy as np


@dataclass
class Tile:
    bands: np.ndarray
    mask: np.ndarray | None = None


def spectral_index(tile: Tile) -> np.ndarray:
    """Normalised difference vegetation index from two representative bands."""
    red = tile.bands[..., 3].astype(float)
    nir = tile.bands[..., 7].astype(float)
    denominator = np.where((nir + red) == 0, 1.0, nir + red)
    return (nir - red) / denominator


def pseudo_labels(tile: Tile, threshold: float = 0.35) -> np.ndarray:
    return (spectral_index(tile) > threshold).astype(np.uint8)


def patchify(tile: Tile, patch_size: int = 32) -> list[np.ndarray]:
    height, width, _ = tile.bands.shape
    patches = []
    for row in range(0, height - patch_size + 1, patch_size):
        for col in range(0, width - patch_size + 1, patch_size):
            patches.append(tile.bands[row:row + patch_size, col:col + patch_size])
    return patches
