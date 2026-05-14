# Contributing

Thank you for improving this defensive security lab. The project is designed to be ethical, educational, and isolated-lab only.

## Ground Rules

- Keep all examples synthetic and safe.
- Do not add real credentials, customer data, production logs, or public target details.
- Do not add exploit instructions or unauthorized testing workflows.
- Prefer clear defensive value: monitoring, hardening, validation, detection, reporting, and risk reduction.
- Document assumptions and limitations when adding new evidence or reports.

## Local Validation

Run these commands from the project root:

```bash
python scripts/validate_python_syntax.py .
python -m unittest discover -s tests -v
python scripts/validate_markdown.py .
python scripts/secret_scan.py .
python scripts/parse_firewall_logs.py
python scripts/summarize_security_events.py
python scripts/generate_lab_inventory.py
```

## Documentation Standards

- Start each Markdown file with one level-1 heading.
- Use tables for control evidence, findings, and mappings.
- Keep claims tied to the sample artifacts in this repository.
- Label synthetic data clearly.
- Avoid overstating what a single sample event proves.

## Pull Request Checklist

- [ ] The change stays within defensive, lab-only scope.
- [ ] New logs or reports are synthetic.
- [ ] Markdown validation passes.
- [ ] Python syntax validation passes.
- [ ] Unit tests pass.
- [ ] Basic secret scan passes.
- [ ] README or supporting docs are updated if behavior changed.
