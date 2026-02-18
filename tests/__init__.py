"""Test package configuration.

This file ensures that the `src` directory is on `sys.path` so that
tests can import the `pylife` package when running via `pytest` or the
standard library's `unittest` discovery.  Without this file, Python
would not find the package because it lives outside of the test
directory hierarchy.
"""

import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)