# ADR-0002: Use Synthetic Telemetry

## Status

Accepted

## Context

The project needs realistic security evidence for portfolio review, but real production logs can expose private data, credentials, business details, and sensitive infrastructure patterns.

## Decision

Use synthetic firewall, IDS, and Windows security events that model defensive telemetry without representing any real organization.

## Rationale

- Protects privacy and avoids accidental disclosure.
- Keeps the project ethical, reproducible, and safe to publish.
- Allows event examples to be designed around specific learning goals.
- Enables detection coverage documentation without requiring live infrastructure.

## Consequences

| Positive | Tradeoff |
|----------|----------|
| Safe to publish publicly | Synthetic logs are smaller than real enterprise datasets |
| Easy to explain in interviews | Does not prove production-scale detection performance |
| Supports repeatable tests | Requires clear labeling to avoid exaggeration |

## Security Impact

This decision reduces data exposure risk while preserving enough realism to discuss alert triage, segmentation, and evidence handling.

