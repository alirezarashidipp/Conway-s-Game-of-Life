"""Unit tests for the Game of Life core logic.

These tests verify that the rules are implemented correctly by
checking a few classic patterns.  If you extend the pattern library
or modify the update rules, consider adding additional tests here.
"""

from pylife.game_of_life import GameOfLife
from pylife.patterns import PATTERNS


def embed_pattern(pattern, rows, cols):
    """Helper: embed a pattern in the centre of a blank grid and return it."""
    grid = [[0] * cols for _ in range(rows)]
    p_rows = len(pattern)
    p_cols = len(pattern[0])
    start_row = (rows - p_rows) // 2
    start_col = (cols - p_cols) // 2
    for i in range(p_rows):
        for j in range(p_cols):
            grid[start_row + i][start_col + j] = pattern[i][j]
    return grid


def test_block_still_life_stays_same():
    """A 2×2 block should remain unchanged across generations."""
    pattern = PATTERNS["block"]
    grid = embed_pattern(pattern, 4, 4)
    game = GameOfLife(4, 4, grid)
    # Step once; should not change
    game.step()
    assert game.grid == grid


def test_blinker_oscillates_with_period_two():
    """A blinker (3‑cell line) should flip orientation every generation."""
    pattern = PATTERNS["blinker"]
    grid = embed_pattern(pattern, 5, 5)
    game = GameOfLife(5, 5, grid)
    # After one step the pattern should change
    game.step()
    after_one = [row.copy() for row in game.grid]
    assert after_one != grid
    # After a second step it should revert to original
    game.step()
    assert game.grid == grid


def test_glider_moves_diagonally():
    """A glider should move one cell down and to the right after four steps."""
    # Place glider near the top-left corner of a larger grid
    initial = embed_pattern(PATTERNS["glider"], 10, 10)
    game = GameOfLife(10, 10, initial)
    # Step four times
    for _ in range(4):
        game.step()
    # After four steps a glider will have moved one cell down and to the right
    # relative to its initial position.  Recreate the expected grid accordingly.
    expected = [[0] * 10 for _ in range(10)]
    p_rows = len(PATTERNS["glider"])
    p_cols = len(PATTERNS["glider"][0])
    # Compute initial embedding position used in embed_pattern
    init_row = (10 - p_rows) // 2
    init_col = (10 - p_cols) // 2
    new_row = init_row + 1
    new_col = init_col + 1
    for i in range(p_rows):
        for j in range(p_cols):
            expected[new_row + i][new_col + j] = PATTERNS["glider"][i][j]
    assert game.grid == expected