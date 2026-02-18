"""Common starting patterns for Conway's Game of Life.

Each pattern is represented as a 2D list of integers where 1 denotes a
live cell and 0 denotes a dead cell.  You can overlay these patterns onto
an existing grid using the helper functions in `pylife.game_of_life` or
the `apply_pattern_center` method of `GameOfLife`.
"""

from __future__ import annotations

from typing import Dict, List

# Define a few classic patterns
GLIDER: List[List[int]] = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
]

BLINKER: List[List[int]] = [
    [1, 1, 1],
]

BLOCK: List[List[int]] = [
    [1, 1],
    [1, 1],
]

TOAD: List[List[int]] = [
    [0, 1, 1, 1],
    [1, 1, 1, 0],
]

BEACON: List[List[int]] = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 1],
]

PATTERNS: Dict[str, List[List[int]]] = {
    "glider": GLIDER,
    "blinker": BLINKER,
    "block": BLOCK,
    "toad": TOAD,
    "beacon": BEACON,
}

__all__ = ["PATTERNS", "GLIDER", "BLINKER", "BLOCK", "TOAD", "BEACON"]