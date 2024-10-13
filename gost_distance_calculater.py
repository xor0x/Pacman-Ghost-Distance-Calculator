"""Ghost distance calculator."""

from __future__ import annotations

import numpy as np

from distance_calculator import DistanceCalculator

WALL = 1
GHOST = 2
PACMAN = 3


class GhostDistanceCalculator(DistanceCalculator):
    """Ghost distance class."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__()
        self.board: np.ndarray = np.ndarray


    def load_file(self, file_path: str) -> None:
        """Load numpy file."""
        self.board = np.load(file_path)


    def calculate_distances(self) -> list[tuple[tuple[int, int], int]]:
        """Calculate and return sorted list of ghost positions and distances."""
        pacman_pos: tuple[int, int] = self._find_pacman(self.board)
        ghost_positions: list[tuple[int, int]] = self._find_ghosts(self.board)

        distances: list = []
        for ghost_pos in ghost_positions:
            distance = self._cal_distance(self.board, pacman_pos, ghost_pos)
            if distance is not None:
                distances.append((ghost_pos, distance))

        return sorted(distances, key=lambda x: x[1])


    def _find_pacman(self, board: np.ndarray) -> tuple[int, int]:
        """Find and return Pacman's position."""
        pacman_pos: tuple = np.where(board == PACMAN)
        return (pacman_pos[0][0], pacman_pos[1][0])


    def _find_ghosts(self, board: np.ndarray) -> list[tuple[int, int]]:
        """Find and return list of ghost positions."""
        ghost_positions: tuple = np.where(board == GHOST)
        return list(zip(ghost_positions[0], ghost_positions[1]))


    def _cal_distance(self, board: np.ndarray, start: tuple[int, int], end: tuple[int, int]) -> int:
        """Calculate shortest path distance."""
        queue: list[tuple[tuple[int, int], int]] = [(start, 0)]
        visited: set[tuple[int, int]] = {start}

        while queue:
            (x, y), dist = queue.pop(0)

            if (x, y) == end:
                return dist

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < board.shape[0]
                    and 0 <= ny < board.shape[1]
                    and board[nx, ny] != WALL
                    and (nx, ny) not in visited
                ):
                    queue.append(((nx, ny), dist + 1))
                    visited.add((nx, ny))
        return None
