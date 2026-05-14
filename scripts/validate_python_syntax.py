#!/usr/bin/env python3
"""Validate Python syntax without writing bytecode files."""

from __future__ import annotations

import argparse
from pathlib import Path


def should_check(path: Path) -> bool:
    return path.is_file() and path.suffix == ".py" and "__pycache__" not in path.parts


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile Python files without writing pyc files.")
    parser.add_argument("path", nargs="?", default=".", type=Path, help="Path to scan")
    args = parser.parse_args()

    files = sorted(path for path in args.path.rglob("*.py") if should_check(path))
    for path in files:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    print(f"Python syntax validation passed for {len(files)} files.")


if __name__ == "__main__":
    main()

