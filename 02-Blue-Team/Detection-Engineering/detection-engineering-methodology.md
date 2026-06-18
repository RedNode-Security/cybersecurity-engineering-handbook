---
title: Detection Engineering Methodology
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection, siem, threat-hunting, engineering]
difficulty: intermediate
safe_publication: true
---

# Detection Engineering Methodology

## Overview

Detection engineering is the practice of converting threat knowledge into reliable, testable, documented, and maintainable detections.

A good detection is not just a query. It is an engineering artifact with a hypothesis, required telemetry, logic, tuning guidance, test plan, triage steps, ownership, and a review cycle.

## Why It Matters

Security teams often fail because alerts are noisy, poorly documented, or disconnected from response. Detection engineering reduces that gap by making each detection measurable and operational.

## Method

### 1. Define the Behavior

Start with behavior, not tool names or indicators.

Good:

- A user authenticates from an unusual location and then performs a privileged action.
- A host creates a suspicious scheduled task after a script execution.
- A new cloud access key is created for an identity that rarely performs administrative actions.

Weak:

- Detect bad IPs.
- Detect malware.
- Detect suspicious activity.

### 2. Write the Detection Hypothesis

Format:

```text
If <threat behavior> occurs, then <telemetry source> should show <observable pattern>.
```

Example:

```text
If an account is misused after credential theft, identity logs may show unusual authentication context followed by privileged actions or access to sensitive systems.
```

### 3. Map Required Telemetry

Document exactly what is needed:

- Log source
- Event names or IDs
- Required fields
- Retention
- Latency
- Known blind spots

### 4. Build Logic

Detection logic should be understandable and reviewable. Prefer explicit field names and clear thresholds.

Logic categories:

- Known-bad indicator match
- Suspicious single event
- Sequence of events
- Statistical anomaly
- Rare event
- Peer-group deviation
- Policy violation

### 5. Validate Safely

Validation should use owned lab data, approved simulations, or historical benign data.

Avoid unsafe validation against systems you do not own or operate.

### 6. Tune

Tuning should preserve the detection hypothesis. Do not tune away the behavior being detected.

Track:

- False positive sources
- Suppression criteria
- Expected benign admin behavior
- Business exceptions
- Risk accepted by owner

### 7. Document Triage

Every detection should tell the analyst what to do next.

Minimum triage:

1. Identify affected asset and identity.
2. Review surrounding activity.
3. Check change tickets or approved administrative actions.
4. Enrich with asset criticality and user role.
5. Escalate if the behavior remains suspicious.

### 8. Monitor Detection Health

Track:

- Alert volume
- True positive rate
- False positive rate
- Mean time to triage
- Mean time to close
- Last test date
- Last owner review

## Detection Engineering Artifact Model

| Field | Purpose |
|---|---|
| Hypothesis | Defines what the detection is expected to catch |
| Telemetry | Defines required data sources and fields |
| Logic | Converts behavior into a rule, query, or model |
| Tuning | Controls noise without destroying signal |
| Triage | Guides analyst response |
| Test plan | Proves the detection can work |
| Owner | Keeps the detection maintained |
| Review date | Prevents stale detections |

## Attack Perspective

Attackers benefit when defenders only search for static indicators. Behavior-based detection raises attacker cost by focusing on actions required to progress an intrusion.

## Defense Perspective

Defenders should prioritize detections that are:

- High-impact
- Mapped to important assets
- Supported by reliable telemetry
- Triageable by analysts
- Connected to response actions

## Automation Strategy

Automate:

- Metadata checks
- Query deployment
- Detection testing
- Alert enrichment
- Case creation
- Metrics reporting

Keep high-risk containment actions human-approved until confidence is proven.

## References

- MITRE ATT&CK: https://attack.mitre.org/
- Sigma: https://sigmahq.io/
- Elastic Detection Engineering: https://www.elastic.co/security-labs
- Splunk Security Content: https://research.splunk.com/
