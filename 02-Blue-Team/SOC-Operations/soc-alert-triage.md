---
title: SOC Alert Triage Workflow
domain: blue-team
category: soc-operations
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [soc, triage, alerting]
difficulty: beginner
safe_publication: true
---

# SOC Alert Triage Workflow

## Overview

Alert triage is the process of determining whether a security alert represents benign activity, suspicious activity, or a confirmed incident.

## Triage Goals

- Validate whether the alert is real
- Determine affected users, systems, and data
- Establish scope and impact
- Decide whether escalation is needed
- Preserve evidence for follow-up

## Standard Workflow

1. Read the alert summary and detection logic.
2. Identify affected identity, asset, application, or cloud resource.
3. Review the timeline before and after the alert.
4. Enrich with asset criticality, user role, location, and vulnerability context.
5. Check for related alerts or threat intelligence matches.
6. Determine likely classification.
7. Escalate, close, or tune.

## Classification

| Classification | Meaning |
|---|---|
| Benign true positive | Expected behavior that matched the rule |
| False positive | Rule logic matched incorrectly |
| Suspicious | Needs more investigation |
| Confirmed incident | Malicious or policy-violating activity confirmed |
| Duplicate | Already handled in another case |

## Evidence to Capture

- Alert name and ID
- Timestamp and time zone
- User and host identifiers
- Source and destination context
- Relevant logs and screenshots
- Analyst notes and assumptions
- Escalation decision and owner

## Escalation Criteria

Escalate when:

- Privileged identity is involved
- Sensitive asset is involved
- Malware execution is suspected
- Data exposure is possible
- Multiple related alerts appear
- Triage cannot explain the activity

## Automation Strategy

Automate enrichment, not judgment:

- Asset criticality lookup
- User department and manager lookup
- Recent authentication summary
- Recent endpoint alerts
- Known maintenance window lookup
- Threat intelligence enrichment
- Case template creation

Keep containment actions human-approved unless the action is low-risk and highly reliable.

## References

- NIST incident handling guidance
- MITRE ATT&CK: https://attack.mitre.org/
