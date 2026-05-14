# ADR-0003: Use Python Standard Library Automation

## Status

Accepted

## Context

The repository includes helper scripts for parsing firewall logs, summarizing security events, validating Markdown, and performing basic secret scanning. These scripts should work in GitHub Actions and on a student workstation with minimal setup.

## Decision

Use the Python standard library for all current scripts and tests.

## Rationale

- Reduces installation friction for reviewers and recruiters.
- Keeps CI fast and easy to understand.
- Avoids dependency risk for a documentation-focused lab project.
- Makes each script readable in an interview setting.

## Consequences

| Positive | Tradeoff |
|----------|----------|
| No external dependencies required | Less feature-rich than dedicated security tools |
| Faster CI startup | Secret scanning is intentionally basic |
| Easier code review | More advanced parsing may require future libraries |

## Security Impact

This decision improves reproducibility and reduces supply-chain complexity for the portfolio project. The built-in scanner is a safety net, not a replacement for enterprise-grade secret scanning.

