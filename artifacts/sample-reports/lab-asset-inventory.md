# Lab Asset Inventory

| Hostname | Zone | IP Address | Role | Telemetry |
|----------|------|------------|------|-----------|
| fw01 | EDGE | 10.10.0.1 | Virtual firewall | Firewall syslog |
| win11-user01 | USER | 10.10.10.21 | Windows endpoint | Windows Security events |
| ubuntu-user01 | USER | 10.10.10.31 | Linux endpoint | auth.log and syslog |
| linux-web01 | DMZ | 10.10.30.20 | Reverse proxy | Nginx access and error logs |
| wazuh01 | SECURITY | 10.10.40.10 | SIEM manager | Agent and alert telemetry |
| ids01 | SECURITY | 10.10.40.20 | IDS sensor | Suricata eve.json |
| admin01 | MGMT | 10.10.50.10 | Admin workstation | Admin activity logs |

Generated from `scripts/generate_lab_inventory.py`.