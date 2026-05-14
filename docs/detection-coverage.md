# Detection Coverage Mapping

![Scope](https://img.shields.io/badge/scope-synthetic_lab_only-green)
![Mapping](https://img.shields.io/badge/mapping-MITRE_ATT%26CK_blue_team-blue)

## Purpose

This document maps the lab's synthetic firewall, IDS, and Windows security events to defensive detection themes. The mapping is intended for security engineering and SOC practice only. It does not claim that the sample events prove real adversary behavior.

## Data Sources

| Source | File | Defensive Value |
|--------|------|-----------------|
| Firewall filter logs | `artifacts/sample-logs/firewall.log` | Segmentation validation, denied flow review, rule hit tracking |
| IDS events | `artifacts/sample-logs/ids-alerts.jsonl` | Policy alert review and network telemetry enrichment |
| Windows security events | `artifacts/sample-logs/windows-security-events.jsonl` | Authentication and process creation visibility |

## ATT&CK-Oriented Coverage

| Event Source | Sample Evidence | ATT&CK Tactic | ATT&CK Technique | Detection Goal | Caveat |
|--------------|-----------------|---------------|------------------|----------------|--------|
| Windows Security | Event ID `4625` failed local logon for `lab.test` | Credential Access | T1110 - Brute Force | Identify authentication failures that may require correlation | One failure is not enough to infer brute force |
| Windows Security | Event ID `4624` successful local logon for `student.user` | Defense Evasion / Persistence context | T1078 - Valid Accounts | Track legitimate account use for timeline context | Successful logon alone is normal activity |
| Windows Security | Event ID `4688` process creation for `whoami.exe` | Discovery | T1033 - System Owner/User Discovery | Detect commands that reveal current user context | `whoami.exe` is often benign and requires context |
| Firewall | `USER` to `SERVER` SMB blocked by `FW-007` | Lateral Movement | T1021.002 - SMB/Windows Admin Shares | Validate segmentation blocks unnecessary SMB paths | This is a blocked lab connection, not compromise evidence |
| Firewall | `DMZ` to `MGMT` RDP blocked by `FW-006` | Lateral Movement | T1021.001 - Remote Desktop Protocol | Confirm management plane isolation | This validates control enforcement in the lab |
| IDS | `LAB Synthetic Policy Violation` from `USER` to `DMZ` | Command and Control / Policy | T1105 - Ingress Tool Transfer context | Flag policy-violating cross-zone traffic for analyst review | Signature is synthetic and lab-defined |
| IDS | DNS request to `updates.example.local` | Command and Control context | T1071.004 - DNS | Build DNS visibility and baseline review workflow | The domain is controlled sample data |

## Coverage Summary

| Coverage Area | Current Status | Evidence |
|---------------|----------------|----------|
| Authentication monitoring | Basic | Windows Event IDs `4624` and `4625` |
| Process creation visibility | Basic | Windows Event ID `4688` |
| Segmentation validation | Strong for lab scope | Firewall allow and deny events |
| IDS alert handling | Basic | Two synthetic Suricata-style alert events |
| DNS visibility | Basic | One synthetic DNS metadata event |
| Endpoint response actions | Not implemented | Future roadmap item |
| Alert correlation | Partial | Supported through manual investigation walkthrough |

## Detection Engineering Notes

- Keep detections tied to a specific data source and field.
- Treat single events as leads, not conclusions.
- Use firewall denies as control validation evidence and triage signals.
- Correlate host and network telemetry before escalating severity.
- Document false-positive expectations for administrative commands and expected service traffic.

## Suggested Next Detections

| Priority | Detection Idea | Required Data |
|----------|----------------|---------------|
| High | Multiple failed logons followed by success | Windows security events or identity logs |
| High | DMZ host attempting management subnet access | Firewall denies and asset zone metadata |
| Medium | Unusual process execution on user workstation | Windows process creation logs |
| Medium | New DNS destinations from user endpoints | DNS logs or Zeek metadata |
| Low | Firewall rule hit drift over time | Historical firewall event aggregation |

