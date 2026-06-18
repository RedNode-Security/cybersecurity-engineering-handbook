---
title: Threat Hunting Methodology
domain: blue-team
category: threat-hunting
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [threat-hunting, hypothesis, detection]
difficulty: intermediate
safe_publication: true
---

# Threat Hunting Methodology

## Overview

Threat hunting is a proactive search for suspicious behavior that may not have generated a high-confidence alert.

## Why It Matters

Hunting helps discover blind spots, validate assumptions, improve detections, and find weak signals that automated rules may miss.

## Hunting Loop

1. Define hypothesis
2. Identify required telemetry
3. Query and explore data
4. Enrich and pivot
5. Validate findings
6. Document outcome
7. Convert useful logic into detections
8. Improve controls and logging

## Hypothesis Examples

- An attacker using stolen credentials may access rare systems outside a user's normal pattern.
- Malware staging may produce unusual archive creation followed by outbound network activity.
- Cloud misuse may involve new access key creation followed by enumeration actions.

## Hunt Plan Template

| Field | Value |
|---|---|
| Hypothesis |  |
| ATT&CK mapping |  |
| Data sources |  |
| Time range |  |
| Query approach |  |
| Expected benign activity |  |
| Escalation criteria |  |
| Output | Detection, case, tuning, or no finding |

## Outcomes

A hunt should end with at least one of these outcomes:

- Confirmed incident
- New detection
- Detection tuning
- Logging improvement request
- Control improvement request
- Documented negative finding

## Automation Strategy

- Save reusable hunt queries
- Track hunt hypotheses and outcomes
- Convert repeated hunt logic into scheduled detections
- Generate coverage maps by data source and ATT&CK behavior

## References

- MITRE ATT&CK: https://attack.mitre.org/
- Sqrrl Threat Hunting Reference Model
