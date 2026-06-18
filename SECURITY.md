# Security Policy

## Reporting Security Issues

If you discover a security issue in this repository, such as accidental exposure of secrets, sensitive data, or unsafe content, contact the repository owner directly or use GitHub private vulnerability reporting if it is enabled.

## Sensitive Data Policy

Do not commit:

- Passwords
- API keys
- Private keys
- Session cookies
- Customer data
- Internal hostnames or IP addresses not intended for publication
- Proprietary detection logic without permission
- Malware samples or binaries

## Safe Publication Policy

This repository is intended for defensive, educational, and authorized research use.

CVE, IOC, red-team, and threat-intelligence content should emphasize:

- Understanding
- Risk reduction
- Detection
- Mitigation
- Responsible validation
- Incident response

Avoid publishing content that enables unauthorized access, stealth, evasion, persistence, destructive execution, or real-world abuse.

## Sanitization Checklist

Before publishing samples:

- [ ] Replace internal hostnames and IPs
- [ ] Replace usernames and email addresses where needed
- [ ] Remove tokens, keys, cookies, and secrets
- [ ] Use documentation-safe domains such as `example.com` or `.invalid`
- [ ] Label synthetic data clearly
- [ ] Add confidence and source context for IOCs
