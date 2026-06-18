---
title: SOC Reference Architecture
domain: architecture
category: soc-architecture
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [soc, architecture, detection, incident-response]
difficulty: intermediate
safe_publication: true
---

# SOC Reference Architecture

## Overview

A Security Operations Center combines people, process, telemetry, detection, response, and continuous improvement to reduce security risk.

## Core Components

| Component | Purpose |
|---|---|
| Telemetry sources | Identity, endpoint, network, cloud, application, email logs |
| SIEM or data lake | Centralize, normalize, search, and correlate events |
| Detection content | Convert threat knowledge into alerts and hunts |
| Case management | Track triage, evidence, decisions, and closure |
| SOAR / automation | Enrich and orchestrate repeatable workflows |
| Threat intelligence | Add context to indicators, actors, campaigns, and CVEs |
| Metrics | Measure alert quality, response time, coverage, and gaps |

## Data Flow

```text
Telemetry → Collection → Normalization → Detection → Enrichment → Triage → Response → Lessons Learned → Improved Controls
```

## Design Principles

- Prioritize high-value assets and identities
- Make telemetry quality visible
- Keep detections documented and testable
- Automate enrichment before containment
- Use human approval for high-risk actions
- Feed incident learnings back into detections and controls

## Detection Coverage Model

Coverage should be measured across:

- ATT&CK behaviors
- Critical assets
- Identity tiers
- Cloud control plane actions
- High-risk application actions
- Known incident scenarios

## Operational Metrics

- Mean time to detect
- Mean time to triage
- Mean time to contain
- Alert true positive rate
- Alert false positive rate
- Detection coverage by data source
- Log source health
- Case backlog and aging

## Automation Opportunities

- Alert enrichment
- Duplicate alert grouping
- IOC expiration checks
- Case template creation
- User and asset context lookup
- Detection health reporting
- Post-incident action tracking

## References

- NIST Cybersecurity Framework
- NIST incident handling guidance
- MITRE ATT&CK: https://attack.mitre.org/
