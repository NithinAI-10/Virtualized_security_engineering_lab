#!/usr/bin/env python3
"""Generate a Markdown inventory for the virtual security lab."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Asset:
    hostname: str
    zone: str
    ip_address: str
    role: str
    telemetry: str


ASSETS = [
    Asset("fw01", "EDGE", "10.10.0.1", "Virtual firewall", "Firewall syslog"),
    Asset("win11-user01", "USER", "10.10.10.21", "Windows endpoint", "Windows Security events"),
    Asset("ubuntu-user01", "USER", "10.10.10.31", "Linux endpoint", "auth.log and syslog"),
    Asset("linux-web01", "DMZ", "10.10.30.20", "Reverse proxy", "Nginx access and error logs"),
    Asset("wazuh01", "SECURITY", "10.10.40.10", "SIEM manager", "Agent and alert telemetry"),
    Asset("ids01", "SECURITY", "10.10.40.20", "IDS sensor", "Suricata eve.json"),
    Asset("admin01", "MGMT", "10.10.50.10", "Admin workstation", "Admin activity logs"),
]


def render_inventory(assets: list[Asset]) -> str:
    rows = [
        "# Lab Asset Inventory",
        "",
        "| Hostname | Zone | IP Address | Role | Telemetry |",
        "|----------|------|------------|------|-----------|",
    ]
    for asset in assets:
        rows.append(
            f"| {asset.hostname} | {asset.zone} | {asset.ip_address} | "
            f"{asset.role} | {asset.telemetry} |"
        )
    rows.append("")
    rows.append("Generated from `scripts/generate_lab_inventory.py`.")
    return "\n".join(rows)


def main() -> None:
    output_path = Path("artifacts/sample-reports/lab-asset-inventory.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_inventory(ASSETS), encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()

