# Hardening Checklist

| Control Area | Baseline | Evidence |
|--------------|----------|----------|
| Account security | Disable unused local accounts | Local user inventory |
| Password policy | Enforce length and lockout policy | Windows security policy export |
| Patch management | Apply current OS and package updates | Patch status screenshot |
| Logging | Forward auth, process, and system logs | SIEM agent heartbeat |
| Firewall | Deny inbound by default | Firewall rule export |
| Remote access | Restrict admin protocols to `MGMT` | Rule table and test result |
| Services | Disable unnecessary services | Service baseline comparison |
| Backups | Snapshot critical lab VMs before major changes | Snapshot inventory |

## Notes

This checklist is intentionally conservative. It focuses on configuration hygiene, visibility, and control evidence rather than offensive validation.

