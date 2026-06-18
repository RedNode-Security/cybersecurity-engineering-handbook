---
title: Log Source Reference Matrix
domain: blue-team
category: log-source-strategy
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [logging, telemetry, siem, detection]
difficulty: beginner
safe_publication: true
---

# Log Source Reference Matrix

## Overview

A log source strategy defines which telemetry sources are needed to detect, investigate, and respond to security-relevant behavior.

## Why It Matters

Detections fail when required telemetry is missing, incomplete, delayed, or not normalized. A reference matrix helps prioritize log onboarding and coverage gaps.

## Matrix

| Domain | Log Source | Key Questions | Example Use Cases |
|---|---|---|---|
| Identity | IdP sign-in logs | Who authenticated, from where, with what result? | Account compromise, MFA fatigue, impossible travel |
| Windows | Security Event Log | What authentication, privilege, and account events occurred? | Lateral movement, privilege abuse, password spraying |
| Endpoint | EDR telemetry | What process, file, registry, and network actions occurred? | Malware triage, suspicious scripting, persistence |
| Network | DNS logs | What domains were resolved by which hosts? | C2 discovery, tunneling suspicion, domain enrichment |
| Network | Proxy logs | What URLs were requested and allowed? | Phishing, malware download, policy violations |
| Cloud | Cloud audit logs | What control-plane actions occurred? | New keys, privilege changes, public exposure |
| Application | Application audit logs | Who accessed what data and what action was taken? | Fraud, data access abuse, business logic misuse |
| Email | Mail gateway logs | What messages were delivered, blocked, or clicked? | Phishing triage, campaign tracking |

## Prioritization Criteria

Prioritize logs that are:

- Linked to high-value assets
- Required for common incident types
- Needed for compliance or audit evidence
- High signal for identity, endpoint, cloud, and network behavior
- Available with useful fields and retention

## Log Quality Checklist

- [ ] Events contain stable timestamps
- [ ] Time zone is normalized
- [ ] Host and user fields are populated
- [ ] Source and destination fields are available where relevant
- [ ] Data is retained long enough for investigations
- [ ] Logs can be joined with asset and identity context
- [ ] Known blind spots are documented

## Automation Strategy

- Build a coverage dashboard
- Detect missing or delayed log sources
- Track log volume anomalies
- Map detections to required telemetry
- Alert when high-value sources stop sending data

## References

- NIST Computer Security Incident Handling Guide
- MITRE ATT&CK Data Sources: https://attack.mitre.org/datasources/
