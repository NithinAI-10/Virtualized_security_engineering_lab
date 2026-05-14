# Lab Runbook

## Daily Startup

1. Start firewall VM.
2. Start security monitoring VM.
3. Start endpoint and server VMs.
4. Confirm Wazuh agent check-ins.
5. Confirm firewall and IDS logs are arriving.

## Synthetic Event Validation

Use benign local events to confirm telemetry:

- failed local login on a lab-only account
- blocked connection between lab zones
- package update event on Linux
- Windows service start or stop event
- DNS request from a lab endpoint to a controlled test domain

## Analyst Review Workflow

1. Review authentication failures.
2. Review firewall denies.
3. Review IDS alerts.
4. Compare events with expected lab activity.
5. Document control gaps in the validation report.

## Evidence Review Commands

Run these commands after updating sample logs:

```bash
python scripts/parse_firewall_logs.py
python scripts/summarize_security_events.py
python -m unittest discover -s tests -v
```

Use the output to update the incident walkthrough, detection coverage mapping, and executive summary when the sample evidence changes.

## Reporting Workflow

1. Confirm all evidence is synthetic.
2. Run the local validation commands.
3. Update `artifacts/sample-reports/lab-validation-report.md` with technical findings.
4. Update `reports/executive-summary.md` with stakeholder-level outcomes.
5. Add screenshots only from isolated lab systems.
