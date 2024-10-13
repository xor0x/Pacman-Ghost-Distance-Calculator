"""Caluculator."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class DistanceCalculator(ABC):
    """Distance Calculator interface."""

    @abstractmethod
    def calculate_distances(self, board: np.ndarray) -> list[tuple[tuple[int, int], int]]:
        """Calculate distances from Pacman to ghosts."""
