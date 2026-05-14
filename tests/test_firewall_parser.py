import unittest
from pathlib import Path

from scripts.parse_firewall_logs import parse_firewall_line, parse_firewall_log, summarize


class FirewallParserTests(unittest.TestCase):
    def test_parse_firewall_line_extracts_expected_fields(self):
        line = (
            "2026-05-01T09:15:07Z fw01 filterlog: action=block "
            "src_zone=USER src_ip=10.10.10.31 dst_zone=SERVER "
            "dst_ip=10.10.20.15 proto=tcp dst_port=445 rule_id=FW-007"
        )

        record = parse_firewall_line(line)

        self.assertIsNotNone(record)
        self.assertEqual(record["timestamp"], "2026-05-01T09:15:07Z")
        self.assertEqual(record["action"], "block")
        self.assertEqual(record["src_zone"], "USER")
        self.assertEqual(record["dst_zone"], "SERVER")
        self.assertEqual(record["dst_port"], "445")
        self.assertEqual(record["rule_id"], "FW-007")

    def test_summarize_counts_actions_rules_and_denied_flows(self):
        records = parse_firewall_log(Path("artifacts/sample-logs/firewall.log"))
        summary = summarize(records)

        self.assertEqual(summary["total_events"], 4)
        self.assertEqual(summary["actions"]["block"], 2)
        self.assertEqual(summary["actions"]["pass"], 2)
        self.assertEqual(summary["rule_hits"]["FW-006"], 1)
        self.assertEqual(summary["denied_flows"][0]["count"], 1)


if __name__ == "__main__":
    unittest.main()

