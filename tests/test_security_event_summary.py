import unittest
from pathlib import Path

from scripts.summarize_security_events import (
    build_timeline,
    read_jsonl,
    summarize_ids,
    summarize_windows,
)


class SecurityEventSummaryTests(unittest.TestCase):
    def test_summarize_ids_counts_alerts_and_dns(self):
        events = read_jsonl(Path("artifacts/sample-logs/ids-alerts.jsonl"))
        summary = summarize_ids(events)

        self.assertEqual(summary["total_events"], 3)
        self.assertEqual(summary["event_types"]["alert"], 2)
        self.assertEqual(summary["event_types"]["dns"], 1)
        self.assertEqual(summary["alert_severities"]["2"], 1)
        self.assertEqual(summary["alert_severities"]["3"], 1)

    def test_summarize_windows_counts_event_ids_and_processes(self):
        events = read_jsonl(Path("artifacts/sample-logs/windows-security-events.jsonl"))
        summary = summarize_windows(events)

        self.assertEqual(summary["total_events"], 3)
        self.assertEqual(summary["event_ids"]["4624"], 1)
        self.assertEqual(summary["event_ids"]["4625"], 1)
        self.assertEqual(summary["event_ids"]["4688"], 1)
        self.assertIn("C:\\Windows\\System32\\whoami.exe", summary["processes"])

    def test_build_timeline_sorts_events(self):
        ids_events = read_jsonl(Path("artifacts/sample-logs/ids-alerts.jsonl"))
        windows_events = read_jsonl(Path("artifacts/sample-logs/windows-security-events.jsonl"))
        timeline = build_timeline(ids_events, windows_events)

        timestamps = [event["timestamp"] for event in timeline]
        self.assertEqual(timestamps, sorted(timestamps))
        self.assertEqual(timeline[0]["source"], "windows")
        self.assertEqual(timeline[-1]["source"], "ids")


if __name__ == "__main__":
    unittest.main()

