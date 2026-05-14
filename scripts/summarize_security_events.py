#!/usr/bin/env python3
"""Summarize synthetic IDS and Windows security events for analyst review."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_IDS_LOG = Path("artifacts/sample-logs/ids-alerts.jsonl")
DEFAULT_WINDOWS_LOG = Path("artifacts/sample-logs/windows-security-events.jsonl")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            events.append(json.loads(line))
    return events


def summarize_ids(events: list[dict[str, Any]]) -> dict[str, object]:
    alert_events = [event for event in events if event.get("event_type") == "alert"]
    signatures = Counter(event["alert"]["signature"] for event in alert_events)
    severities = Counter(str(event["alert"]["severity"]) for event in alert_events)
    event_types = Counter(event.get("event_type", "unknown") for event in events)
    return {
        "total_events": len(events),
        "event_types": dict(event_types),
        "alert_signatures": dict(signatures),
        "alert_severities": dict(severities),
    }


def summarize_windows(events: list[dict[str, Any]]) -> dict[str, object]:
    event_ids = Counter(str(event.get("event_id", "unknown")) for event in events)
    accounts = Counter(event.get("account", "unknown") for event in events)
    process_events = [
        event
        for event in events
        if event.get("event_id") == 4688 and event.get("process")
    ]
    return {
        "total_events": len(events),
        "event_ids": dict(event_ids),
        "accounts": dict(accounts),
        "processes": [event["process"] for event in process_events],
    }


def build_timeline(
    ids_events: list[dict[str, Any]],
    windows_events: list[dict[str, Any]],
) -> list[dict[str, str]]:
    timeline: list[dict[str, str]] = []

    for event in windows_events:
        timeline.append(
            {
                "timestamp": event.get("timestamp", ""),
                "source": "windows",
                "summary": f"{event.get('event_name', 'Windows event')} on {event.get('host', 'unknown')}",
            }
        )

    for event in ids_events:
        if event.get("event_type") == "alert":
            detail = event.get("alert", {}).get("signature", "IDS alert")
        elif event.get("event_type") == "dns":
            detail = f"DNS query {event.get('query', 'unknown')}"
        else:
            detail = event.get("event_type", "IDS event")

        timeline.append(
            {
                "timestamp": event.get("timestamp", ""),
                "source": "ids",
                "summary": detail,
            }
        )

    return sorted(timeline, key=lambda item: item["timestamp"])


def render_text(summary: dict[str, object]) -> str:
    lines = [
        "Security Event Summary",
        "======================",
        "",
        "IDS:",
        json.dumps(summary["ids"], indent=2, sort_keys=True),
        "",
        "Windows:",
        json.dumps(summary["windows"], indent=2, sort_keys=True),
        "",
        "Timeline:",
    ]
    for event in summary["timeline"]:  # type: ignore[union-attr]
        lines.append(f"- {event['timestamp']} [{event['source']}] {event['summary']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize synthetic IDS and Windows security events.")
    parser.add_argument("--ids", type=Path, default=DEFAULT_IDS_LOG, help="IDS JSONL path")
    parser.add_argument("--windows", type=Path, default=DEFAULT_WINDOWS_LOG, help="Windows JSONL path")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args()

    ids_events = read_jsonl(args.ids)
    windows_events = read_jsonl(args.windows)
    summary = {
        "ids": summarize_ids(ids_events),
        "windows": summarize_windows(windows_events),
        "timeline": build_timeline(ids_events, windows_events),
    }

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(render_text(summary))


if __name__ == "__main__":
    main()

