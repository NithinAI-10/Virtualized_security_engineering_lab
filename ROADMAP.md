# Roadmap

## Vision

Build a polished defensive lab portfolio project that demonstrates security engineering discipline: architecture, segmentation, telemetry, detection coverage, SOC triage, evidence quality, and clear risk communication.

## Completed

| Area | Status | Evidence |
|------|--------|----------|
| Segmented lab architecture | Complete | `architecture/security-lab-topology.mmd` |
| Firewall rule baseline | Complete | `configs/firewall-rules.csv` |
| Synthetic telemetry | Complete | `artifacts/sample-logs/` |
| Hardening checklist | Complete | `docs/hardening-checklist.md` |
| Validation report | Complete | `artifacts/sample-reports/lab-validation-report.md` |
| Detection coverage mapping | Complete | `docs/detection-coverage.md` |
| SOC incident walkthrough | Complete | `docs/incident-walkthrough.md` |
| Parser and summary scripts | Complete | `scripts/` |
| CI quality checks | Complete | `.github/workflows/ci.yml` |
| Unit tests | Complete | `tests/` |

## Near-Term Improvements

| Priority | Improvement | Why It Matters |
|----------|-------------|----------------|
| High | Add real screenshots from a local isolated lab | Improves GitHub visual credibility |
| High | Generate charts from parser output | Makes evidence easier to review quickly |
| Medium | Add Linux authentication sample logs | Expands endpoint visibility beyond Windows |
| Medium | Add web proxy sample logs from the DMZ | Improves network investigation realism |
| Medium | Add backup and restore validation report | Shows operational resilience thinking |

## Longer-Term Improvements

| Priority | Improvement | Why It Matters |
|----------|-------------|----------------|
| Medium | Add Ansible or Terraform lab provisioning | Demonstrates repeatable security engineering |
| Medium | Add ATT&CK coverage matrix image | Improves recruiter and interview presentation |
| Low | Add hardware sizing profiles | Helps other students reproduce the lab |
| Low | Add dashboard screenshot templates | Speeds up final portfolio publishing |

## Out Of Scope

- Testing public IP addresses or third-party systems.
- Publishing real enterprise logs or credentials.
- Adding exploit instructions or offensive playbooks.
- Automating response actions against non-lab systems.

