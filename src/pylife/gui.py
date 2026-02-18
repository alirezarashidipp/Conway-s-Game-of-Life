"""Pygame interface for Conway's Game of Life.

This module contains a simple graphical interface built with Pygame.  It
allows you to watch the Game of Life unfold, pause and resume the
simulation, toggle cells with the mouse and adjust the update speed.  A
command‑line interface is provided via the `cli()` function which is
exposed as an entry point in `pyproject.toml`.
"""

from __future__ import annotations

import argparse
import sys
from typing import Optional

import pygame

from .game_of_life import GameOfLife, create_empty_grid
from .patterns import PATTERNS


def run(rows: int,
        cols: int,
        pattern: Optional[str] = None,
        cell_size: int = 10,
        fps: int = 10) -> None:
    """Launch a Pygame simulation of the Game of Life.

    Args:
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.
        pattern: Optional key of a pattern in `PATTERNS` to centre on the grid.
        cell_size: Size of each cell in pixels.
        fps: Frames per second (simulation step frequency).
    """
    pygame.init()
    width = cols * cell_size
    height = rows * cell_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    # Create initial grid
    if pattern and pattern in PATTERNS:
        grid = create_empty_grid(rows, cols)
        game = GameOfLife(rows, cols, grid)
        game.apply_pattern_center(PATTERNS[pattern])
    else:
        game = GameOfLife(rows, cols)

    running = False  # Whether the simulation is running
    show_gridlines = True  # Whether to draw grid lines

    # Font for status text
    font = pygame.font.SysFont(None, 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle running state
                    running = not running
                elif event.key == pygame.K_r:
                    # Reset to random grid
                    game.reset_random()
                elif event.key == pygame.K_c:
                    # Clear grid
                    game.clear()
                elif event.key in (pygame.K_EQUALS, pygame.K_PLUS):
                    # Increase speed
                    fps = min(fps + 5, 60)
                elif event.key == pygame.K_MINUS:
                    # Decrease speed
                    fps = max(fps - 5, 1)
                elif event.key == pygame.K_g:
                    show_gridlines = not show_gridlines
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle cell on click
                x, y = event.pos
                col = x // cell_size
                row = y // cell_size
                game.toggle_cell(row, col)

        if running:
            game.step()

        # Draw background
        screen.fill((30, 30, 30))

        # Draw cells
        for i in range(rows):
            for j in range(cols):
                if game.grid[i][j] == 1:
                    pygame.draw.rect(
                        screen,
                        (0, 200, 80),
                        (j * cell_size, i * cell_size, cell_size, cell_size),
                    )

        # Optionally draw gridlines for clarity
        if show_gridlines:
            for x in range(0, width, cell_size):
                pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, height))
            for y in range(0, height, cell_size):
                pygame.draw.line(screen, (50, 50, 50), (0, y), (width, y))

        # Display status text
        status_text = f"Generation: {game.generation} | FPS: {fps} | {'Running' if running else 'Paused'}"
        text_surface = font.render(status_text, True, (200, 200, 200))
        screen.blit(text_surface, (10, height - 30))

        pygame.display.flip()
        clock.tick(fps)


def cli(argv: Optional[list[str]] = None) -> None:
    """Entry point for the command‑line interface.

    This function is registered as a console script via the
    `pyproject.toml` configuration so that you can run it with
    ``python -m pylife.gui`` or ``pylife-gui`` from your shell.

    Args:
        argv: Optional list of arguments (for testing).
    """
    parser = argparse.ArgumentParser(description="Conway's Game of Life (Pygame)")
    parser.add_argument("--rows", type=int, default=50, help="Number of rows in the grid")
    parser.add_argument("--cols", type=int, default=50, help="Number of columns in the grid")
    parser.add_argument(
        "--pattern",
        type=str,
        choices=list(PATTERNS.keys()) + [None],
        default=None,
        help="Name of a built‑in pattern to centre on the grid",
    )
    parser.add_argument("--cell-size", type=int, default=10, help="Size of each cell in pixels")
    parser.add_argument("--fps", type=int, default=10, help="Frames per second (simulation speed)")
    args = parser.parse_args(argv)
    run(args.rows, args.cols, args.pattern, args.cell_size, args.fps)


if __name__ == "__main__":
    cli(sys.argv[1:])