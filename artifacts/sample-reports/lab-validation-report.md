# Lab Validation Report

## Scope

Validation covered the isolated virtual lab only. No public systems or third-party services were tested.

## Controls Reviewed

| Control | Status | Evidence |
|---------|--------|----------|
| Segmented VLANs | Pass | Firewall rules separate user, server, DMZ, security, and management zones |
| Default deny | Pass | `FW-008` blocks unapproved traffic |
| Centralized logging | Pass | Endpoint, firewall, and IDS logs are present in sample artifacts |
| Management isolation | Pass | `ANY` to `MGMT` is denied except approved admin path |
| Dashboard readiness | Pass | Dashboard JSON includes panels for authentication, firewall denies, and IDS alerts |

## Findings

| ID | Severity | Finding | Recommendation |
|----|----------|---------|----------------|
| LAB-001 | Medium | DMZ logging depends on syslog availability | Add local log retention and forwarding health checks |
| LAB-002 | Low | Asset inventory is manually maintained | Generate inventory from source-of-truth data during each lab update |

## Conclusion

The lab design demonstrates practical security engineering fundamentals: segmentation, monitoring, hardening, detection coverage mapping, and evidence collection. Future work should focus on automation, screenshot evidence from a completed lab build, and generated charts from the parsing scripts.
