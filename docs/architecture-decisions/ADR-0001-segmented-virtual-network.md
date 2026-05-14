# ADR-0001: Use Segmented Virtual Network Zones

## Status

Accepted

## Context

The lab needs to demonstrate enterprise security engineering concepts while remaining small enough to run on a student workstation. A flat network would be easier to build, but it would not show realistic trust boundaries or control validation.

## Decision

Use separate virtual zones for `USER`, `SERVER`, `DMZ`, `SECURITY`, and `MGMT`, with a virtual firewall enforcing allowed paths.

## Rationale

- Segmentation is a core security engineering concept.
- Firewall rule evidence can be reviewed without unsafe testing.
- The model supports SOC investigation practice because blocked and allowed flows have business context.
- Management access can be isolated from user and DMZ traffic.

## Consequences

| Positive | Tradeoff |
|----------|----------|
| Stronger architecture story for interviews | More setup steps than a flat lab |
| Clear control validation evidence | Requires careful rule documentation |
| Better blast-radius explanation | Requires extra virtual network interfaces |

## Security Impact

This decision supports least privilege, reduced lateral movement exposure, and management-plane isolation in an isolated lab environment.

