# Backlog

Use this file as the GitHub issue seed list. Each item is written so it can be copied into an issue.

## Label Taxonomy

Recommended labels:

| Label | Purpose |
|---|---|
| `domain:fundamentals` | Core concepts and principles |
| `domain:red-team` | Authorized testing methodology |
| `domain:blue-team` | SOC, IR, hunting, detection |
| `domain:threat-intel` | IOCs, CVEs, actors, OSINT |
| `domain:cloud` | Cloud and Kubernetes security |
| `domain:appsec` | Application and API security |
| `domain:ai-security` | LLM, RAG, agent, and AI SOC security |
| `domain:automation` | SIEM, SOAR, enrichment, scripts |
| `type:content` | Documentation page |
| `type:template` | Template improvement |
| `type:schema` | Structured data schema |
| `type:automation` | Script or workflow |
| `status:draft` | Needs writing |
| `status:review` | Needs review |
| `priority:high` | High-impact work |

## Milestone 1 — Foundation Polish

### Issue: Add final repository license

Labels: `type:content`, `priority:high`

Description:

Choose documentation and code licenses. Add the selected license files and update `README.md`.

Acceptance criteria:

- [ ] Documentation license selected
- [ ] Code/script license selected
- [ ] `README.md` license section updated
- [ ] Contribution policy aligned with license

### Issue: Confirm GitHub Actions are green

Labels: `type:automation`, `priority:high`

Description:

Confirm validation and markdown workflows pass on `main`.

Acceptance criteria:

- [ ] `Validate repository` passes
- [ ] `Markdown Validation` passes
- [ ] `INDEX.md` check passes
- [ ] Failing rules are documented or configured intentionally

## Milestone 2 — Blue Team Foundation

### Issue: Expand Windows event logging fundamentals

Labels: `domain:fundamentals`, `domain:blue-team`, `type:content`

Description:

Create a beginner-friendly Windows event logging guide covering security logs, audit policy, common event IDs, forwarding, and retention.

Acceptance criteria:

- [ ] Explains Windows Security, System, PowerShell, and Defender logs
- [ ] Includes common event IDs and defensive use cases
- [ ] Includes detection and triage considerations
- [ ] Links to Microsoft documentation

### Issue: Add PowerShell detection guide

Labels: `domain:blue-team`, `type:content`

Description:

Document PowerShell logging sources, suspicious behavior patterns, tuning guidance, and safe validation ideas.

Acceptance criteria:

- [ ] Covers Script Block, Module, Transcription, and process telemetry
- [ ] Includes suspicious behavior examples at a defensive level
- [ ] Lists false positives and tuning guidance
- [ ] Provides triage workflow

### Issue: Add DNS investigation workflow

Labels: `domain:blue-team`, `type:content`

Description:

Create a DNS investigation workflow for suspicious domains, beaconing, tunneling indicators, and enrichment.

Acceptance criteria:

- [ ] Lists required telemetry
- [ ] Defines suspicious DNS patterns
- [ ] Includes triage and enrichment steps
- [ ] Includes false positives and limitations

### Issue: Add Linux authentication detection guide

Labels: `domain:blue-team`, `domain:fundamentals`, `type:content`

Description:

Document Linux authentication logs, SSH activity, privilege changes, and persistence indicators.

Acceptance criteria:

- [ ] Covers common Linux auth logs
- [ ] Includes suspicious patterns
- [ ] Includes triage workflow
- [ ] Includes hardening and monitoring recommendations

## Milestone 3 — Threat Intelligence and CVE Operations

### Issue: Add CVE scoring worksheet

Labels: `domain:threat-intel`, `type:template`

Description:

Create a reusable worksheet to prioritize CVEs by exposure, exploitability, asset criticality, compensating controls, and detection coverage.

Acceptance criteria:

- [ ] Includes scoring factors
- [ ] Includes risk decision examples
- [ ] Includes patch and mitigation tracking fields
- [ ] Links to CVE analysis template

### Issue: Add threat actor profile example

Labels: `domain:threat-intel`, `type:content`

Description:

Create a sanitized threat actor profile example using public reporting and clear confidence language.

Acceptance criteria:

- [ ] No unsupported attribution claims
- [ ] TTPs mapped at a high level
- [ ] Defensive recommendations included
- [ ] References included

## Milestone 4 — Cloud, AppSec, AI Security

### Issue: Add cloud identity detection guide

Labels: `domain:cloud`, `domain:blue-team`, `type:content`

Description:

Document suspicious cloud identity behaviors such as impossible travel, unusual privilege changes, new access keys, and risky consent grants.

Acceptance criteria:

- [ ] Covers AWS and Azure concepts at a minimum
- [ ] Lists telemetry sources
- [ ] Includes detection hypotheses
- [ ] Includes response guidance

### Issue: Add OAuth and JWT security guide

Labels: `domain:appsec`, `type:content`

Description:

Create an application security guide for OAuth, JWT, token validation, token storage, and common implementation risks.

Acceptance criteria:

- [ ] Explains JWT structure and validation checks
- [ ] Covers OAuth flow risks
- [ ] Includes secure implementation checklist
- [ ] Includes logging and detection opportunities

### Issue: Add RAG security checklist

Labels: `domain:ai-security`, `type:content`

Description:

Create a RAG security checklist covering untrusted content, retrieval boundaries, data leakage, provenance, and output controls.

Acceptance criteria:

- [ ] Defines RAG trust boundaries
- [ ] Includes prompt injection risks
- [ ] Includes data handling controls
- [ ] Includes monitoring and evaluation ideas

## Milestone 5 — Automation

### Issue: Build IOC enrichment script prototype

Labels: `domain:automation`, `domain:threat-intel`, `type:automation`

Description:

Create a safe local script that reads sanitized IOC JSON, validates fields, and produces an enrichment-ready report skeleton.

Acceptance criteria:

- [ ] Reads IOC JSON file
- [ ] Validates required fields
- [ ] Does not require API keys by default
- [ ] Produces Markdown or JSON output
- [ ] Includes tests or sample execution

### Issue: Add SOAR workflow example

Labels: `domain:automation`, `domain:blue-team`, `type:content`

Description:

Document a human-approved SOAR workflow for account compromise triage and containment.

Acceptance criteria:

- [ ] Includes trigger conditions
- [ ] Includes enrichment steps
- [ ] Defines human approval gates
- [ ] Includes rollback and audit logging guidance
