---
title: API Security Checklist
domain: application-security
category: api-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [api-security, appsec, secure-design]
difficulty: intermediate
safe_publication: true
---

# API Security Checklist

## Overview

API security protects application interfaces from unauthorized access, data exposure, abuse, and insecure integration patterns.

## Authentication

- [ ] All sensitive endpoints require authentication
- [ ] Tokens are validated server-side
- [ ] Expired, malformed, or unsigned tokens are rejected
- [ ] Strong authentication is required for administrative actions
- [ ] Service-to-service authentication is documented

## Authorization

- [ ] Object-level authorization checks are enforced
- [ ] Function-level authorization checks are enforced
- [ ] Administrative endpoints are separated and monitored
- [ ] Authorization decisions are made server-side
- [ ] Tests cover cross-tenant and horizontal access cases

## Input and Data Handling

- [ ] Input validation is applied consistently
- [ ] Error messages do not expose sensitive internals
- [ ] Sensitive data is minimized in responses
- [ ] Pagination and filtering do not leak unauthorized records
- [ ] File upload behavior is restricted and logged

## Abuse Controls

- [ ] Rate limits exist for authentication and expensive actions
- [ ] Brute force and enumeration patterns are monitored
- [ ] Business logic abuse cases are threat-modeled
- [ ] Automated clients are identified where needed

## Logging and Monitoring

- [ ] Authentication failures are logged
- [ ] Authorization failures are logged
- [ ] Administrative actions are logged
- [ ] Sensitive data access is logged
- [ ] Logs include request ID, user ID, source, endpoint, and outcome
- [ ] Logs avoid storing secrets and full tokens

## Detection Opportunities

- Repeated authorization failures across object IDs
- High-volume requests to sensitive endpoints
- Token validation failures from the same client
- Unusual administrative actions
- Cross-tenant access attempts
- Unexpected data export volume

## Secure Design Questions

- What is the trust boundary?
- What identity is making the request?
- What object is being accessed?
- Who owns the object?
- What business action is being performed?
- What should be logged if this action is abused?

## References

- OWASP API Security Top 10: https://owasp.org/API-Security/
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
