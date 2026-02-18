"""Tkinter front‑end for Conway's Game of Life.

When executed directly, this module displays a small form that prompts
the user for the grid dimensions and a starting pattern.  When the
"Start Simulation" button is clicked, a Pygame window opens to run
the Game of Life using those parameters.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from pylife.gui import run
from pylife.patterns import PATTERNS

try:
    # messagebox is a submodule; import lazily to avoid unnecessary dependencies
    from tkinter import messagebox  # type: ignore
except Exception:
    messagebox = None


def main() -> None:
    """Launch the configuration window and, upon submission, the simulation."""
    root = tk.Tk()
    root.title("Conway's Game of Life – Launcher")

    # Variables bound to input fields
    rows_var = tk.StringVar(value="50")
    cols_var = tk.StringVar(value="50")
    pattern_var = tk.StringVar(value="random")

    # Layout widgets
    ttk.Label(root, text="Rows:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    rows_entry = ttk.Entry(root, textvariable=rows_var, width=10)
    rows_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(root, text="Columns:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    cols_entry = ttk.Entry(root, textvariable=cols_var, width=10)
    cols_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(root, text="Pattern:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    pattern_options = ["random"] + sorted(PATTERNS.keys())
    pattern_menu = ttk.OptionMenu(root, pattern_var, pattern_var.get(), *pattern_options)
    pattern_menu.grid(row=2, column=1, padx=5, pady=5)

    def on_start() -> None:
        try:
            rows = int(rows_var.get())
            cols = int(cols_var.get())
        except ValueError:
            if messagebox:
                messagebox.showerror("Invalid input", "Rows and columns must be integers.")
            return
        pattern = pattern_var.get()
        if pattern == "random":
            pattern = None
        root.destroy()
        run(rows, cols, pattern=pattern)

    start_button = ttk.Button(root, text="Start Simulation", command=on_start)
    start_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    # Prevent resizing
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()