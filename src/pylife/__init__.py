"""Top-level package for the Game of Life.

This package exposes the core game logic and the Pygame interface.  See
`pylife.game_of_life` for the core rules implementation and `pylife.gui`
for a graphical simulation.
"""

from .game_of_life import GameOfLife, create_random_grid  # noqa: F401
from .patterns import PATTERNS  # noqa: F401