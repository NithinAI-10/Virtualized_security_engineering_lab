#!/usr/bin/env python3
"""Basic repository secret scanner for CI safety checks."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_EXCLUDES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
}

PATTERNS = {
    "aws_access_key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "github_token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "slack_token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    "private_key": re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "assigned_secret": re.compile(
        r"(?i)(api_key|secret|token|password)\s*[:=]\s*['\"][^'\"]{12,}['\"]"
    ),
}


def should_scan(path: Path) -> bool:
    if any(part in DEFAULT_EXCLUDES for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in {
        ".conf",
        ".csv",
        ".json",
        ".jsonl",
        ".md",
        ".mmd",
        ".py",
        ".txt",
        ".yaml",
        ".yml",
    }


def scan_file(path: Path) -> list[str]:
    findings: list[str] = []
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings

    for line_number, line in enumerate(content.splitlines(), start=1):
        for name, pattern in PATTERNS.items():
            if pattern.search(line):
                findings.append(f"{path}:{line_number}: possible {name}")
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a basic secret scan over text files.")
    parser.add_argument("path", nargs="?", default=".", type=Path, help="Path to scan")
    args = parser.parse_args()

    findings: list[str] = []
    for path in args.path.rglob("*"):
        if should_scan(path):
            findings.extend(scan_file(path))

    if findings:
        print("Potential secrets found:")
        for finding in findings:
            print(f"- {finding}")
        raise SystemExit(1)

    print("No obvious secrets found.")


if __name__ == "__main__":
    main()

