# Conway's Game of Life

This repository contains a refactored implementation of **Conway's Game of Life**.  The goal of this refactor is to take the original single‑file prototype and organize it into a more maintainable, reusable structure.  The core rules of the Game of Life have been separated from the graphical user interfaces, making it easy to run simulations in different contexts.

## Features

- **Modular design** – game logic lives in `pylife/game_of_life.py`, while the Pygame‑based visualisation is isolated in `pylife/gui.py`.  A simple Tkinter front‑end is provided in `main.py`.
- **Random grid generation** – generate a random initial grid of any size using `create_random_grid`.
- **Interactive simulation** – a Tkinter dialog lets you choose the grid dimensions before launching the simulation.

## Requirements

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

> **Note:** `tkinter` ships with most Python distributions, but on Linux you may need to install an extra package such as `python3‑tk`.

## Running the simulation

After installing the requirements, run the main module to start the Tkinter UI:

```bash
python main.py
```

Enter the number of rows and columns in the dialog and click **Start Simulation**.  A separate window will open showing the grid evolving according to Conway's rules.

## Project structure

```
refactored_conway_game/
├── main.py              # Tkinter front‑end launching the Pygame simulation
├── requirements.txt     # Python dependencies
├── .gitignore           # Files/directories that should not be committed
└── src/
    └── pylife/
        ├── __init__.py   # Makes pylife a package
        ├── game_of_life.py  # Core Game of Life logic
        └── gui.py        # Pygame visualisation of the grid
```

## Future improvements

This refactor intentionally keeps the scope small.  For a truly production‑ready project, consider adding:

- **Automated tests** for the game logic (`pytest` or `unittest`)
- **Continuous integration** (e.g. GitHub Actions) to run tests and linting on pull requests
- **Packaging metadata** (e.g. a `pyproject.toml` with `[project]` settings) if you plan to publish to PyPI
- **Command‑line interface** for non‑GUI usage

## License

The original repository did not specify a licence.  Consider adding an open‑source licence such as MIT or GPL if you intend to distribute this project.
