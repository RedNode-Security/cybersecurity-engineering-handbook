---
title: IR Playbook — Account Compromise
domain: blue-team
category: incident-response
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [incident-response, identity, account-compromise]
difficulty: intermediate
safe_publication: true
---

# IR Playbook — Account Compromise

## Objective

Guide responders through triage, containment, eradication, and recovery for suspected account compromise.

## Scope

In scope:

- Corporate identity accounts
- Cloud accounts
- Privileged accounts
- Service accounts where applicable

Out of scope:

- Full endpoint malware investigation
- Legal notification decisions
- HR disciplinary process

## Trigger Conditions

- Impossible travel or unusual sign-in alert
- MFA fatigue or suspicious MFA reset
- Unusual privileged action
- Password spraying followed by successful login
- User report of suspicious mailbox, messages, or access
- Threat intelligence match involving account activity

## Severity Criteria

| Severity | Criteria |
|---|---|
| Low | Suspicious login with no sensitive access and plausible explanation |
| Medium | Suspicious login with limited access or repeated failed activity |
| High | Confirmed misuse, sensitive data access, or privilege changes |
| Critical | Privileged account compromise or broad tenant/domain impact |

## Triage Steps

1. Identify the account, source IP, device, application, and authentication method.
2. Review successful and failed sign-ins for the previous 24 to 72 hours.
3. Check MFA method changes, password changes, and recovery changes.
4. Review privileged role assignments and group membership changes.
5. Review mailbox rules, forwarding settings, OAuth grants, and suspicious app consent where relevant.
6. Determine whether the user recognizes the activity.
7. Check for related endpoint or cloud alerts.
8. Decide whether containment is required.

## Containment

Potential containment actions:

- Reset password
- Revoke active sessions
- Require MFA re-registration
- Disable account temporarily
- Remove unauthorized roles or group memberships
- Revoke suspicious OAuth grants or tokens
- Block source indicators if appropriate and high confidence

Use human approval for actions that may disrupt business operations.

## Eradication

- Remove malicious mailbox rules or forwarding
- Remove unauthorized application consent
- Remove unauthorized keys, tokens, or sessions
- Fix weak authentication or conditional access gaps
- Review related accounts for similar behavior

## Recovery

- Restore legitimate access
- Confirm MFA and recovery methods
- Notify user of safe account practices
- Monitor account for recurrence
- Close case only after no related suspicious activity remains

## Evidence Preservation

Capture:

- Sign-in logs
- MFA events
- Administrative audit logs
- Role/group changes
- Mailbox rule changes
- Token or OAuth grant changes
- Analyst notes and timeline

## Lessons Learned

- Was detection timely?
- Was MFA or conditional access bypassed or absent?
- Were privileges excessive?
- Did logs provide enough context?
- What automation could reduce response time?

## References

- NIST Computer Security Incident Handling Guide
- Microsoft identity security operations guidance
- MITRE ATT&CK Initial Access and Credential Access tactics: https://attack.mitre.org/
