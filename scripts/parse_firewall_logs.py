#!/usr/bin/env python3
"""Parse synthetic firewall logs and summarize zone control activity."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Iterable


DEFAULT_LOG = Path("artifacts/sample-logs/firewall.log")
FIREWALL_PATTERN = re.compile(
    r"^(?P<timestamp>\S+)\s+"
    r"(?P<host>\S+)\s+filterlog:\s+"
    r"(?P<fields>.+)$"
)


def parse_key_values(raw_fields: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for item in raw_fields.split():
        key, separator, value = item.partition("=")
        if separator:
            fields[key] = value
    return fields


def parse_firewall_line(line: str) -> dict[str, str] | None:
    match = FIREWALL_PATTERN.match(line.strip())
    if not match:
        return None

    record = {
        "timestamp": match.group("timestamp"),
        "host": match.group("host"),
    }
    record.update(parse_key_values(match.group("fields")))
    return record


def parse_firewall_log(path: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = parse_firewall_line(line)
        if record is not None:
            records.append(record)
    return records


def summarize(records: Iterable[dict[str, str]]) -> dict[str, object]:
    materialized = list(records)
    actions = Counter(record.get("action", "unknown") for record in materialized)
    rules = Counter(record.get("rule_id", "unknown") for record in materialized)
    denied_flows = Counter(
        (
            record.get("src_zone", "unknown"),
            record.get("dst_zone", "unknown"),
            record.get("dst_port", "unknown"),
            record.get("rule_id", "unknown"),
        )
        for record in materialized
        if record.get("action") == "block"
    )

    return {
        "total_events": len(materialized),
        "actions": dict(actions),
        "rule_hits": dict(rules),
        "denied_flows": [
            {
                "src_zone": src_zone,
                "dst_zone": dst_zone,
                "dst_port": dst_port,
                "rule_id": rule_id,
                "count": count,
            }
            for (src_zone, dst_zone, dst_port, rule_id), count in denied_flows.most_common()
        ],
    }


def render_text(summary: dict[str, object]) -> str:
    lines = [
        "Firewall Log Summary",
        "====================",
        f"Total events: {summary['total_events']}",
        "",
        "Actions:",
    ]
    for action, count in sorted(summary["actions"].items()):  # type: ignore[union-attr]
        lines.append(f"- {action}: {count}")

    lines.append("")
    lines.append("Rule hits:")
    for rule_id, count in sorted(summary["rule_hits"].items()):  # type: ignore[union-attr]
        lines.append(f"- {rule_id}: {count}")

    lines.append("")
    lines.append("Denied flows:")
    for flow in summary["denied_flows"]:  # type: ignore[union-attr]
        lines.append(
            f"- {flow['src_zone']} -> {flow['dst_zone']} port {flow['dst_port']} "
            f"blocked by {flow['rule_id']} ({flow['count']} event)"
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize synthetic firewall filter logs.")
    parser.add_argument("--input", type=Path, default=DEFAULT_LOG, help="Firewall log path")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    records = parse_firewall_log(args.input)
    summary = summarize(records)
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(render_text(summary))


if __name__ == "__main__":
    main()

