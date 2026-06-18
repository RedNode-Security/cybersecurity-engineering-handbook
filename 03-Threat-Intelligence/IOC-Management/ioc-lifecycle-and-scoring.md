---
title: IOC Lifecycle and Scoring
domain: threat-intelligence
category: ioc-management
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [ioc, threat-intelligence, enrichment]
difficulty: beginner
safe_publication: true
---

# IOC Lifecycle and Scoring

## Overview

An indicator of compromise is useful only when it has context, confidence, source, handling guidance, and an expiration or review date.

## IOC Lifecycle

1. Collection
2. Sanitization
3. Context enrichment
4. Confidence scoring
5. Defensive use decision
6. Deployment or publication
7. Monitoring and feedback
8. Expiration or renewal

## Confidence Factors

| Factor | Questions |
|---|---|
| Source reliability | Is the source known and credible? |
| Indicator type | Is the indicator stable or easily changed? |
| Context | Is the indicator linked to a campaign, malware, or incident? |
| Recency | Was it observed recently? |
| Corroboration | Do multiple independent sources agree? |
| False positive risk | Could this affect legitimate services? |

## Scoring Model

| Confidence | Meaning | Suggested Use |
|---|---|---|
| Low | Limited context or weak source | Enrichment or hunting only |
| Medium | Credible but not fully verified | Alerting or scoped monitoring |
| High | Strong source, context, and corroboration | Alerting, investigation, or blocking after risk review |

## Indicator Use Modes

| Mode | When to Use |
|---|---|
| Enrichment | Low risk, adds context to cases |
| Hunt | Useful for retrospective search |
| Alert | Medium/high confidence with acceptable false positives |
| Block | High confidence and low business impact |
| Correlate | Useful as one signal in multi-factor detection |

## Expiration Guidance

| Indicator Type | Suggested Review Window |
|---|---|
| IP address | 7 to 30 days unless tied to stable infrastructure |
| Domain | 30 to 90 days depending on context |
| URL | 30 to 90 days depending on campaign |
| File hash | Longer lived, but still review relevance |
| Email sender | Short lived unless linked to known infrastructure |

## Sanitization Checklist

- [ ] Remove internal hostnames and private details
- [ ] Use TLP marking
- [ ] Add source and confidence
- [ ] Add first-seen and last-seen dates
- [ ] Add expiration or review date
- [ ] State whether values are real, sanitized, or synthetic

## Automation Strategy

- Validate IOC JSON against schema
- Enrich indicators with source and age
- Flag stale indicators
- Generate SIEM watchlists from approved indicators
- Track false positives and blocklist removals

## References

- MISP Project: https://www.misp-project.org/
- STIX/TAXII: https://oasis-open.github.io/cti-documentation/
- FIRST Traffic Light Protocol: https://www.first.org/tlp/
