# Roadmap

## Vision

Continue developing the **Virtualized Security Engineering, SOC & Incident Response Lab** into a polished defensive-security portfolio project that demonstrates architecture, segmentation, telemetry, detection engineering, SOC triage, incident response, automation, control validation, and clear risk communication.

## Completed

| Area | Status | Evidence |
|------|--------|----------|
| Segmented lab architecture | Complete | `architecture/security-lab-topology.mmd` |
| Firewall rule baseline | Complete | `configs/firewall-rules.csv` |
| Synthetic Windows/firewall/IDS telemetry | Complete | `artifacts/sample-logs/` |
| Hardening checklist | Complete | `docs/hardening-checklist.md` |
| Validation report | Complete | `artifacts/sample-reports/lab-validation-report.md` |
| Detection coverage mapping | Complete | `docs/detection-coverage.md` |
| SOC incident walkthrough | Complete | `docs/incident-walkthrough.md` |
| Analyst parsing and summary utilities | Complete | `scripts/` |
| CI quality checks | Complete | `.github/workflows/ci.yml` |
| Unit tests | Complete | `tests/` |
| Architecture Decision Records | Complete | `docs/architecture-decisions/` |
| Recruiter-facing README refresh | Complete | `README.md` |
| Portfolio screenshot set | Complete | `screenshots/` |
| Executive-summary alignment | Complete | `reports/executive-summary.md` |

## Evidence Guidance

The project intentionally keeps evidence types clear:

- **Synthetic evidence** is used where reproducibility and safe public sharing matter most.
- **Documentation-rendered screenshots** show detection coverage, incident workflows, parser output, and validation artifacts.
- **Isolated-lab captures** may be added when they strengthen technical credibility and can be safely sanitized.

No screenshot or artifact should imply production ownership, customer access, or activity against systems outside the isolated lab.

## Near-Term Improvements

| Priority | Improvement | Why It Matters |
|----------|-------------|----------------|
| High | Add more sanitized isolated-lab captures where available | Strengthens technical credibility while preserving safe disclosure |
| High | Generate charts from parser output | Makes firewall, IDS, and event trends easier to review quickly |
| Medium | Add Linux authentication sample logs | Expands endpoint visibility beyond Windows |
| Medium | Add web/proxy sample logs from the DMZ | Improves network investigation realism |
| Medium | Add additional incident scenarios | Broadens triage, correlation, and ATT&CK coverage |
| Medium | Add backup and restore validation report | Demonstrates resilience and operational recovery thinking |

## Longer-Term Improvements

| Priority | Improvement | Why It Matters |
|----------|-------------|----------------|
| Medium | Add Ansible or Terraform lab provisioning | Demonstrates repeatable security engineering and infrastructure automation |
| Medium | Add ATT&CK coverage matrix visualization | Improves recruiter and interview presentation |
| Medium | Add detection-rule validation scenarios | Demonstrates iterative detection engineering and tuning |
| Low | Add hardware sizing profiles | Helps others reproduce the lab on different systems |
| Low | Add additional dashboard/report templates | Improves analyst and stakeholder presentation |

## Portfolio Quality Goals

Future work should continue to improve the project without sacrificing credibility. Every enhancement should support at least one of the following goals:

1. Make the defensive architecture easier to understand.
2. Improve the quality or breadth of telemetry.
3. Strengthen incident-investigation realism.
4. Improve evidence-based detection coverage.
5. Increase repeatability through automation and tests.
6. Improve communication to technical and non-technical audiences.
7. Clearly distinguish lab evidence, synthetic evidence, assumptions, and validated results.

## Out Of Scope

- Testing public IP addresses or third-party systems without explicit authorization.
- Publishing real enterprise logs, credentials, customer data, or sensitive production screenshots.
- Claiming production SOC, SIEM, or enterprise infrastructure ownership based on lab work.
- Adding exploit instructions or offensive playbooks unrelated to defensive validation.
- Automating response actions against non-lab systems.

