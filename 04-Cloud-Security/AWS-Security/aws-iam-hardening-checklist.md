---
title: AWS IAM Hardening Checklist
domain: cloud-security
category: aws-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [aws, iam, cloud, hardening]
difficulty: intermediate
safe_publication: true
---

# AWS IAM Hardening Checklist

## Overview

AWS IAM controls who can access AWS resources and what actions they can perform. IAM misconfiguration is one of the highest-impact cloud security risks.

## Why It Matters

Cloud identity is the cloud control plane. Excessive privileges, long-lived keys, weak federation, and missing monitoring can lead to broad compromise.

## Checklist

### Root Account

- [ ] Root account has MFA enabled
- [ ] Root access keys do not exist
- [ ] Root account use is monitored
- [ ] Root credentials are stored in a controlled emergency process

### Users and Roles

- [ ] Prefer roles and federation over long-lived IAM users
- [ ] Use least privilege policies
- [ ] Avoid wildcard administrative permissions unless justified
- [ ] Review unused users, roles, and permissions
- [ ] Remove stale access keys

### Access Keys

- [ ] Inventory all active keys
- [ ] Rotate keys based on policy
- [ ] Alert on new access key creation
- [ ] Alert on old unused keys becoming active
- [ ] Avoid embedding keys in code or CI logs

### Policies

- [ ] Review policies with wildcard actions or resources
- [ ] Use permission boundaries where appropriate
- [ ] Use service control policies in multi-account environments
- [ ] Separate human and workload permissions

### Monitoring

- [ ] Enable CloudTrail where applicable
- [ ] Monitor IAM policy changes
- [ ] Monitor role assumption patterns
- [ ] Alert on privilege escalation paths
- [ ] Send logs to a central security account or SIEM

## Detection Hypotheses

- New access key created for a rarely used IAM user
- Privileged policy attached outside change window
- Role assumed from unusual source or principal
- Root account used for non-emergency action
- CloudTrail logging disabled or modified

## Response Guidance

- Revoke or deactivate suspicious keys
- Remove unauthorized policies
- Revert risky trust policy changes
- Review CloudTrail around the event
- Check for follow-on actions such as data access or persistence

## Automation Strategy

- Schedule IAM credential reports
- Detect unused permissions
- Alert on new admin privileges
- Generate access review tickets
- Enforce policy-as-code checks before deployment

## References

- AWS IAM Documentation: https://docs.aws.amazon.com/iam/
- AWS CloudTrail Documentation: https://docs.aws.amazon.com/cloudtrail/
- CIS AWS Foundations Benchmark
