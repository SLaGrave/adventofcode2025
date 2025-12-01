"""Script to run my AoC 2025 python implementations.
"""

import argparse
import importlib
import pathlib


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="pyaoc25")
    parser.add_argument("day", type=int, help="The day to run")
    parser.add_argument("input", type=pathlib.Path)
    args = parser.parse_args()

    mod = importlib.import_module(f"python_impl.day{args.day:0>2}")

    mod.run(data_location=args.input)
