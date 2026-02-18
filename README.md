# Conway's Game of Life – Enhanced Version

This repository contains a polished, modular implementation of **Conway's Game of Life**,
the famous zero‑player cellular automaton devised by mathematician John Conway.  It is
designed as a showcase project to demonstrate clean code architecture, testing and
continuous integration.  The original prototype bundled all functionality into a single
script; this refactor separates concerns and adds tooling around the core logic so
anyone can extend or reuse the project with ease.

## Key Features

- **Modular core engine** – The game rules and grid manipulation live in
  `pylife/game_of_life.py`, making the logic easy to test and reuse.
- **Pattern library** – Common starting patterns (glider, blinker, toad, etc.) are
  included in `pylife/patterns.py` for quick experimentation.
- **Pygame interface** – A smooth graphical interface (`pylife/gui.py`) lets you
  watch the simulation evolve, pause/resume, toggle cells with the mouse and adjust
  speed on the fly.
- **Tkinter launcher** – A simple GUI (`main.py`) prompts you for the grid size
  and starting pattern before launching the Pygame simulation.
- **Web simulation** – An HTML+JavaScript demo (`webapp/index.html`) showcases the
  Game of Life in a browser without any Python dependencies.
- **Unit tests** – Tests in `tests/` verify that the core rules behave correctly on
  known patterns using `pytest`.
- **Continuous integration** – A GitHub Actions workflow runs the tests on each push
  to ensure code quality.
- **Packaging metadata** – A `pyproject.toml` is provided to build and distribute
  the `pylife` package.

## Installation

Create a virtual environment (optional) and install the requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Linux you may need to install an extra package for Tkinter, e.g.
`sudo apt install python3‑tk`.

## Running the Simulation

Run the Tkinter front‑end to select the grid size and starting pattern:

```bash
python main.py
```

Alternatively you can run the Pygame simulation directly from code:

```bash
python -m pylife.gui --rows 50 --cols 50 --pattern glider
```

Open `webapp/index.html` in your browser to experiment with the JavaScript
version.

## Project Structure

```
conway_game_of_life/
├── main.py              # Tkinter front‑end launching the Pygame simulation
├── pyproject.toml       # Packaging information for pylife
├── requirements.txt     # Python dependencies
├── webapp/              # Static HTML/JS demo of the Game of Life
├── src/
│   └── pylife/
│       ├── __init__.py   # Makes pylife a package
│       ├── game_of_life.py  # Core Game of Life logic
│       ├── gui.py        # Pygame visualisation and controls
│       └── patterns.py   # Built‑in starting patterns
└── tests/
    └── test_game_of_life.py  # Unit tests for the core logic
```

## Contributing and Improvements

This project is intentionally kept small but fully functional.  There are many
ways to extend it:

- Add more patterns to `pylife/patterns.py`.
- Implement a command‑line interface for running simulations without a GUI.
- Use numpy arrays for faster grid updates.
- Add support for infinite grids with edge wrapping.
- Expand the web demo with pattern loading and exporting.

Pull requests and feedback are welcome!

## License

Distributed under the MIT License.  See `LICENSE` for details.