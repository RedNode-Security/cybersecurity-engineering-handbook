---
title: Rules of Engagement Checklist
domain: red-team
category: methodology
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [red-team, authorization, methodology]
difficulty: beginner
safe_publication: true
---

# Rules of Engagement Checklist

## Overview

Rules of engagement define what is authorized, what is prohibited, who is involved, and how issues are handled during a security assessment.

## Why It Matters

Clear authorization protects the organization, testers, users, and systems. It prevents ambiguity and keeps testing aligned with business risk.

## Checklist

- [ ] Written authorization exists
- [ ] Scope is defined by assets, applications, IP ranges, accounts, and dates
- [ ] Out-of-scope systems are listed
- [ ] Testing windows are approved
- [ ] Emergency contacts are defined
- [ ] Stop conditions are defined
- [ ] Data handling requirements are documented
- [ ] Reporting expectations are defined
- [ ] Third-party dependencies are identified
- [ ] Legal and compliance constraints are reviewed

## Scope Fields

| Field | Example |
|---|---|
| Assets | Domains, cloud accounts, applications, IP ranges |
| Time window | Approved testing dates and hours |
| Test types | Reconnaissance, web testing, phishing simulation, cloud review |
| Prohibited actions | Destructive testing, persistence, production data access |
| Contacts | Technical owner, security owner, escalation contact |

## Safety Boundary

This repository documents methodology for authorized assessment only. Do not use these notes for unauthorized testing or activity.

## References

- PTES engagement concepts
- NIST security assessment guidance
