#!/usr/bin/env python3
"""Run lightweight Markdown quality checks for project documentation."""

from __future__ import annotations

import argparse
from pathlib import Path


def validate_markdown(path: Path) -> list[str]:
    issues: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    if not lines:
        issues.append(f"{path}: file is empty")
        return issues

    if not lines[0].startswith("# "):
        issues.append(f"{path}: first line should be a level-1 heading")

    for line_number, line in enumerate(lines, start=1):
        if line.rstrip() != line:
            issues.append(f"{path}:{line_number}: trailing whitespace")
        if "\t" in line:
            issues.append(f"{path}:{line_number}: tab character found")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Markdown files.")
    parser.add_argument("path", nargs="?", default=".", type=Path, help="Path to scan")
    args = parser.parse_args()

    markdown_files = sorted(args.path.rglob("*.md"))
    issues: list[str] = []
    for markdown_file in markdown_files:
        issues.extend(validate_markdown(markdown_file))

    if issues:
        print("Markdown validation failed:")
        for issue in issues:
            print(f"- {issue}")
        raise SystemExit(1)

    print(f"Markdown validation passed for {len(markdown_files)} files.")


if __name__ == "__main__":
    main()

