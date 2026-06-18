---
title: Windows Authentication Detection
domain: blue-team
category: detection-engineering
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [windows, authentication, detection, identity]
difficulty: intermediate
safe_publication: true
---

# Windows Authentication Detection

## Overview

Windows authentication events provide high-value signals for account misuse, brute force activity, lateral movement, privilege abuse, and suspicious administrative behavior.

## Why It Matters

Identity is often the control plane of an enterprise environment. When an account is compromised, authentication logs are usually among the first data sources that reveal unusual access.

## Key Telemetry

| Source | Examples |
|---|---|
| Windows Security Event Log | Logon, logoff, credential validation, account changes |
| Domain Controller Logs | Kerberos, NTLM, account lockouts, group changes |
| Endpoint Telemetry | Process lineage, network connections, command execution |
| Identity Provider Logs | MFA, conditional access, risky sign-ins |
| VPN / Proxy Logs | Remote access context |

## Common Windows Event IDs

| Event ID | Meaning | Detection Use |
|---|---|---|
| 4624 | Successful logon | New location, unusual logon type, rare host access |
| 4625 | Failed logon | Password guessing, spraying, misconfigured services |
| 4634 | Logoff | Session duration context |
| 4648 | Explicit credentials used | Run-as behavior, lateral movement context |
| 4672 | Special privileges assigned | Privileged logon monitoring |
| 4720 | User account created | Unauthorized account creation |
| 4728 | Member added to global security group | Privilege escalation monitoring |
| 4732 | Member added to local security group | Local admin changes |
| 4740 | Account locked out | Password attack or user issue |
| 4768 | Kerberos authentication ticket requested | Domain authentication baseline |
| 4769 | Kerberos service ticket requested | Service access and lateral movement context |
| 4771 | Kerberos pre-authentication failed | Password guessing signal |
| 4776 | NTLM credential validation | Legacy authentication monitoring |

## Detection Hypotheses

### Unusual Logon Followed by Privileged Activity

If a compromised account is used for privilege abuse, logs may show unusual authentication context followed by privileged actions.

Signals:

- New source host or geography
- Rare logon type for the user
- Privileged event soon after logon
- Access to sensitive server or admin endpoint

### Password Spraying

If an actor attempts password spraying, logs may show many accounts with failed logons from the same source or pattern over a time window.

Signals:

- Many usernames with few failures each
- Same source IP, host, VPN, or user agent
- Failures followed by a success
- Activity outside business hours

### Privileged Group Modification

If an account is used for privilege escalation, logs may show group membership changes involving privileged groups.

Signals:

- Member added to privileged group
- Change made by unusual admin
- Change outside approved change window
- Group addition followed by privileged logon

## False Positives

- Helpdesk password resets
- New employee onboarding
- Admin maintenance windows
- VPN egress changes
- Service account misconfiguration
- Vulnerability scanner authentication failures

## Triage Workflow

1. Identify account, source host, destination host, and logon type.
2. Determine whether the source and destination are normal for the account.
3. Check whether the user recently changed role, device, location, or VPN path.
4. Review events before and after the authentication.
5. Check for privileged group changes, explicit credential use, or unusual process execution.
6. Escalate if activity cannot be explained by approved business context.

## Response Actions

- Disable or reset the account if compromise is likely
- Revoke sessions where supported
- Remove unauthorized group membership
- Isolate affected endpoint if endpoint compromise is suspected
- Preserve logs and timeline evidence
- Review similar activity for related accounts

## Automation Strategy

- Enrich alerts with user role, asset criticality, and historical baseline
- Join identity events with endpoint and VPN data
- Auto-create cases for privileged group modifications
- Require human approval for account disablement until confidence is high

## References

- Microsoft Windows Security Auditing documentation
- MITRE ATT&CK Credential Access and Lateral Movement tactics: https://attack.mitre.org/
