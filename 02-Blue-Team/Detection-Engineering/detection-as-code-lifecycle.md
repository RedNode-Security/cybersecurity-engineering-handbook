---
title: Detection-as-Code Lifecycle
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [detection-as-code, siem, ci-cd, automation]
difficulty: intermediate
safe_publication: true
---

# Detection-as-Code Lifecycle

## Overview

Detection-as-code treats detections like engineered software artifacts. Rules, metadata, tests, and documentation are version-controlled, reviewed, validated, and deployed through a repeatable process.

## Why It Matters

Without engineering discipline, detections become stale, noisy, duplicated, or undocumented. Detection-as-code improves reliability, reviewability, and operational trust.

## Lifecycle

1. Propose detection idea
2. Write detection metadata
3. Implement rule or query
4. Add test data or validation plan
5. Review for accuracy and safety
6. Deploy to SIEM or analytics platform
7. Monitor alert quality
8. Tune and version updates
9. Retire if obsolete

## Recommended Repository Structure

```text
detections/
  windows/
    unusual-logon-followed-by-privileged-action.yml
  cloud/
    new-access-key-for-rare-admin.yml
tests/
  detections/
    windows-authentication-sample.json
docs/
  triage/
    account-compromise.md
```

This knowledge base does not need to become a full detection repository immediately, but the same pattern should guide documentation quality.

## Required Metadata

| Field | Why it matters |
|---|---|
| Name | Human-readable purpose |
| ID | Stable tracking identifier |
| Status | Draft, reviewed, published, archived |
| Severity | Response priority |
| Confidence | Expected reliability |
| Log source | Required telemetry |
| ATT&CK mapping | Behavior alignment |
| False positives | Tuning and analyst expectations |
| Triage steps | Operational handoff |
| Owner | Maintenance accountability |
| Review date | Lifecycle management |

## Review Checklist

- [ ] Detection hypothesis is clear
- [ ] Logic matches the hypothesis
- [ ] Required log fields are documented
- [ ] False positives are listed
- [ ] Test method is safe and authorized
- [ ] Triage steps are actionable
- [ ] Severity and confidence are justified
- [ ] Rule owner is assigned
- [ ] Review date is set

## Deployment Controls

Use staged deployment:

1. Development
2. Test or lab
3. Silent mode / no-notification mode
4. Low-severity alerting
5. Production alerting
6. Automated response only after sustained validation

## Automation Ideas

- Validate required metadata fields
- Check query syntax where possible
- Generate documentation from rule metadata
- Track alert volume and false positives
- Create review reminders
- Detect stale detections with no recent alerts or no recent tests

## References

- Sigma rule format: https://sigmahq.io/
- MITRE ATT&CK: https://attack.mitre.org/
- Detection Engineering with Splunk Security Content: https://research.splunk.com/
