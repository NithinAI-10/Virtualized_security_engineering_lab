# SOC Incident Walkthrough

![Scenario](https://img.shields.io/badge/scenario-segmentation_validation-blue)
![Scope](https://img.shields.io/badge/scope-isolated_lab_only-green)

## Scenario

The SOC receives a synthetic lab alert indicating unexpected cross-zone activity. The analyst reviews Windows, firewall, and IDS telemetry to determine whether the activity represents a control failure, a likely compromise, or a policy validation event.

This walkthrough uses only the sample data in this repository.

## Analyst Question

Did the lab controls prevent unauthorized cross-zone access, and is there evidence that the event progressed beyond blocked or synthetic activity?

## Evidence Reviewed

| Source | File | Key Evidence |
|--------|------|--------------|
| Windows events | `artifacts/sample-logs/windows-security-events.jsonl` | Successful logon, failed logon, and benign process creation |
| Firewall logs | `artifacts/sample-logs/firewall.log` | Blocked SMB from `USER` to `SERVER`; blocked RDP from `DMZ` to `MGMT` |
| IDS alerts | `artifacts/sample-logs/ids-alerts.jsonl` | Synthetic policy alert and unexpected DMZ-to-security port alert |

## Timeline

| Time UTC | Source | Event | Analyst Interpretation |
|----------|--------|-------|------------------------|
| 09:02:13 | Windows | Successful local logon by `student.user` | Normal user activity context |
| 09:05:44 | Windows | Failed local logon for `lab.test` | Low-severity authentication lead; single failure only |
| 09:14:22 | Firewall | `USER` to `SERVER` HTTPS allowed by `FW-002` | Expected application access path |
| 09:15:07 | Firewall | `USER` to `SERVER` SMB blocked by `FW-007` | Segmentation blocked unnecessary lateral protocol |
| 09:17:25 | Windows | `whoami.exe` process created by `student.user` | Discovery-like command, but benign without additional indicators |
| 09:21:11 | Firewall | `DMZ` to `MGMT` RDP blocked by `FW-006` | Management isolation worked as designed |
| 09:22:11 | IDS | Synthetic policy violation from `USER` to `DMZ` | Lab-defined policy alert requiring context |
| 09:31:02 | IDS | Unexpected DMZ-to-security port alert | Follow-up review of DMZ egress policy recommended |

## Investigation Steps

1. Confirm the environment scope is the isolated virtual lab.
2. Identify affected zones: `USER`, `SERVER`, `DMZ`, `MGMT`, and `SECURITY`.
3. Review firewall actions before host-level conclusions.
4. Confirm whether blocked flows match the documented firewall baseline.
5. Correlate IDS alerts with firewall denies and expected lab activity.
6. Review Windows events for nearby authentication or process execution context.
7. Document whether controls prevented movement or whether response escalation is needed.

## Findings

| Finding | Severity | Evidence | Rationale |
|---------|----------|----------|-----------|
| SMB from `USER` to `SERVER` was blocked | Low | `FW-007` firewall event | Control worked as designed |
| RDP from `DMZ` to `MGMT` was blocked | Medium | `FW-006` firewall event | Management plane isolation is critical |
| Single failed logon was observed | Low | Windows Event ID `4625` | Single event lacks burst or success correlation |
| Synthetic IDS policy alerts were generated | Medium | IDS alert JSONL | Useful for triage practice and dashboard validation |

## Conclusion

The available evidence supports a control-validation conclusion: the firewall denied unauthorized cross-zone paths, IDS alerts created analyst review opportunities, and Windows telemetry provided endpoint context. There is no evidence in the sample data that unauthorized access succeeded or that the lab host was compromised.

## Recommended Follow-Up

- Add correlation logic for firewall denies followed by IDS alerts from the same source host.
- Add thresholding for repeated Windows failed logons.
- Create a dashboard panel for `DMZ` to `MGMT` deny events.
- Document approved administrative paths and compare them against blocked flows.
- Add analyst notes to the validation report after each lab run.

## Interview Talking Points

- I treated blocked firewall traffic as both a security signal and validation evidence.
- I avoided over-classifying a single failed logon as an incident.
- I correlated endpoint, firewall, and IDS telemetry before writing the conclusion.
- I separated what the evidence proves from what it only suggests.

