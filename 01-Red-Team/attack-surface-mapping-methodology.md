---
title: Attack Surface Mapping Methodology
domain: red-team
category: attack-surface-mapping
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [attack-surface, reconnaissance, methodology]
difficulty: intermediate
safe_publication: true
---

# Attack Surface Mapping Methodology

## Overview

Attack surface mapping identifies exposed assets, identities, applications, cloud resources, and third-party dependencies that may affect organizational risk.

## Authorized Use Only

Perform mapping only for assets you own or are explicitly authorized to assess.

## Mapping Areas

| Area | Questions |
|---|---|
| Domains | Which domains and subdomains are owned? |
| Applications | Which apps are internet-facing or business-critical? |
| Cloud | Which cloud accounts, projects, buckets, and services exist? |
| Identity | Which login portals, SSO providers, and admin interfaces are exposed? |
| Network | Which services are intentionally exposed? |
| Third parties | Which vendors process or expose organizational data? |

## Workflow

1. Confirm authorization and scope.
2. Build an asset inventory from approved sources.
3. Classify assets by owner, environment, exposure, and criticality.
4. Identify externally reachable services.
5. Map authentication and administrative entry points.
6. Review misconfiguration and hygiene indicators.
7. Prioritize findings by business impact and exploitability.
8. Report remediation actions to owners.

## Defensive Output

The output should help defenders answer:

- What do we expose?
- Who owns it?
- Is it expected?
- Is it monitored?
- Is it patched and hardened?
- What should be removed or restricted?

## Automation Strategy

- Maintain an asset inventory
- Detect new exposed services
- Compare exposure against approved baseline
- Notify owners of unknown or risky exposure
- Track remediation over time

## References

- OWASP Web Security Testing Guide
- CISA attack surface management guidance
