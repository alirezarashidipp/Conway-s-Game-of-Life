"""Core logic for Conway's Game of Life.

This module defines helper functions and a small class to simulate
Conway's Game of Life on a finite rectangular grid.  A cell is either
alive (1) or dead (0).  Each generation is computed entirely from the
previous one according to Conway's rules:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with exactly three live neighbours becomes a live cell.
3. All other live cells die in the next generation.  Similarly, all other
   dead cells stay dead.

The functions in this module operate on plain Python lists for
simplicity, but the class API exposes a more convenient object that
tracks the generation and provides methods for toggling cells and
resetting the grid.
"""

from __future__ import annotations

from typing import List, Optional
import random
import copy

# Type alias for a 2D grid of integer cells (0 = dead, 1 = alive)
Grid = List[List[int]]


def create_empty_grid(rows: int, cols: int) -> Grid:
    """Return a rows×cols grid initialised with dead cells.

    Args:
        rows: Number of rows.
        cols: Number of columns.

    Returns:
        A new grid filled with zeros.
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]


def create_random_grid(rows: int, cols: int, live_prob: float = 0.2) -> Grid:
    """Generate a random grid with a given probability of a cell being alive.

    Args:
        rows: Number of rows.
        cols: Number of columns.
        live_prob: Probability of each cell being alive (between 0 and 1).

    Returns:
        A new grid with random live and dead cells.
    """
    grid = create_empty_grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 1 if random.random() < live_prob else 0
    return grid


def count_neighbors(grid: Grid, row: int, col: int) -> int:
    """Count the number of live neighbours around a cell.

    Args:
        grid: 2D list representing the current generation.
        row: Row index of the cell.
        col: Column index of the cell.

    Returns:
        The count of live neighbours surrounding the cell.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                count += grid[r][c]
    return count


def step(grid: Grid) -> Grid:
    """Compute the next generation from the current grid.

    This function does not modify the input grid; it returns a new
    grid representing the next state.

    Args:
        grid: The current generation grid.

    Returns:
        A new grid representing the next generation.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    new_grid: Grid = create_empty_grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            neighbours = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                new_grid[i][j] = 1 if neighbours in (2, 3) else 0
            else:
                new_grid[i][j] = 1 if neighbours == 3 else 0
    return new_grid


def apply_pattern(grid: Grid, pattern: Grid, top_left_row: int, top_left_col: int) -> None:
    """Overlay a pattern onto an existing grid in place.

    Cells outside of the grid bounds are ignored.

    Args:
        grid: The grid to modify.
        pattern: The pattern to overlay (list of lists of 0/1).
        top_left_row: Row index for the top‑left corner of the pattern.
        top_left_col: Column index for the top‑left corner of the pattern.
    """
    for i, row_values in enumerate(pattern):
        for j, val in enumerate(row_values):
            r = top_left_row + i
            c = top_left_col + j
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                grid[r][c] = val


class GameOfLife:
    """Object‑oriented wrapper around the Game of Life rules.

    An instance stores its own grid and generation counter and provides
    methods to evolve the state, toggle individual cells and reset the
    world.
    """

    def __init__(self, rows: int, cols: int, initial_grid: Optional[Grid] = None) -> None:
        """Initialise a Game of Life simulation.

        Args:
            rows: Number of rows in the grid.
            cols: Number of columns in the grid.
            initial_grid: Optional starting grid.  If not provided, a
                random grid will be generated.
        """
        self.rows = rows
        self.cols = cols
        if initial_grid is not None:
            # Deep copy to avoid external mutation
            self.grid: Grid = [row.copy() for row in initial_grid]
        else:
            self.grid = create_random_grid(rows, cols)
        self.generation = 0

    def step(self) -> None:
        """Advance the simulation by one generation in place."""
        self.grid = step(self.grid)
        self.generation += 1

    def toggle_cell(self, row: int, col: int) -> None:
        """Toggle the state of a single cell.

        Args:
            row: Row index of the cell to toggle.
            col: Column index of the cell to toggle.
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = 0 if self.grid[row][col] == 1 else 1

    def reset_random(self, live_prob: float = 0.2) -> None:
        """Reset the grid with a new random configuration."""
        self.grid = create_random_grid(self.rows, self.cols, live_prob=live_prob)
        self.generation = 0

    def clear(self) -> None:
        """Set all cells to dead."""
        self.grid = create_empty_grid(self.rows, self.cols)
        self.generation = 0

    def apply_pattern_center(self, pattern: Grid) -> None:
        """Center a pattern within the grid.

        The pattern is placed so that its centre aligns approximately with
        the centre of the grid.

        Args:
            pattern: The pattern to apply (list of lists of 0/1).
        """
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0]) if pattern_rows else 0
        top_left_row = max((self.rows - pattern_rows) // 2, 0)
        top_left_col = max((self.cols - pattern_cols) // 2, 0)
        apply_pattern(self.grid, pattern, top_left_row, top_left_col)