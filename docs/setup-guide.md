# Setup Guide

## Prerequisites

- Workstation with at least 16 GB RAM recommended
- VirtualBox, VMware Workstation, Hyper-V, or Proxmox
- ISO images for Windows evaluation and a Linux distribution
- No public targets, no third-party systems, and no production credentials

## Network Zones

| Zone | CIDR | Purpose |
|------|------|---------|
| USER | `10.10.10.0/24` | Standard endpoint activity |
| SERVER | `10.10.20.0/24` | Internal application and identity services |
| DMZ | `10.10.30.0/24` | Externally exposed lab service simulation |
| SECURITY | `10.10.40.0/24` | SIEM, IDS, and log processing |
| MGMT | `10.10.50.0/24` | Administration and remote console access |

## Build Sequence

1. Create virtual networks for each zone.
2. Deploy the firewall VM with one interface per zone.
3. Configure outbound internet only where required for updates.
4. Deploy the monitoring host in the `SECURITY` zone.
5. Forward firewall logs to the monitoring host.
6. Install endpoint agents on Windows and Linux lab hosts.
7. Validate that synthetic events appear in the SIEM dashboard.

## Validation Checklist

- Firewall denies unexpected cross-zone traffic by default.
- Management access is only allowed from `MGMT`.
- Endpoints send authentication and system logs.
- IDS sensor records synthetic lab-only alert events.
- Dashboard has panels for authentication, firewall denies, IDS alerts, and endpoint health.

## Local Evidence Review

After reviewing or updating sample artifacts, run:

```bash
python scripts/parse_firewall_logs.py
python scripts/summarize_security_events.py
python scripts/generate_lab_inventory.py
```

These commands summarize the synthetic firewall, IDS, and Windows events used in the detection coverage and incident walkthrough docs.

## Local Quality Checks

Before publishing changes to GitHub, run:

```bash
python scripts/validate_python_syntax.py .
python -m unittest discover -s tests -v
python scripts/validate_markdown.py .
python scripts/secret_scan.py .
```

The GitHub Actions workflow runs the same checks for pull requests and pushes.
