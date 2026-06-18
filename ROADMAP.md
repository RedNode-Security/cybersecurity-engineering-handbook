# Roadmap

This roadmap converts the knowledge-base vision into practical delivery phases.

## Phase 1 — Foundation

**Goal:** Build a clean, consistent, safe-to-publish knowledge system.

Status: **mostly complete**

Deliverables:

- Repository structure and README
- Documentation templates
- Content safety policy
- Taxonomy and naming convention
- Contribution guide
- Basic validation scripts
- Initial index generation
- One starter page per major domain

Definition of done:

- New notes can be created from templates
- Each domain has a README
- Public publishing boundaries are documented
- Repo can be validated locally and in GitHub Actions

## Phase 2 — Blue Team and Detection Engineering

**Goal:** Build practical detection, triage, and response content.

Status: **in progress**

Deliverables:

- Detection engineering methodology
- Detection-as-code lifecycle
- SOC triage workflow
- Incident response playbooks
- Threat hunting methodology
- Log source reference matrix
- Example detections mapped to attacker behaviors

Initial topics:

- Windows authentication detection
- Account compromise triage
- PowerShell logging and investigation
- Linux authentication and persistence signals
- DNS investigation workflow
- Cloud identity suspicious activity

## Phase 3 — Red Team Methodologies

**Goal:** Document authorized testing methodology and attacker mental models without publishing weaponized content.

Deliverables:

- Rules of engagement checklist
- Reconnaissance methodology
- Attack surface mapping workflow
- Web/API testing methodology
- Active Directory assessment checklist
- Privilege escalation knowledge map

Safety boundary:

- Keep content educational and controlled-lab oriented
- Do not include live exploit chains, destructive payloads, evasion guidance, or instructions for unauthorized access

## Phase 4 — Threat Intelligence and Automation

**Goal:** Convert raw indicators and CVE research into structured intelligence.

Deliverables:

- IOC lifecycle and confidence scoring
- IOC schema and samples
- CVE triage workflow
- Threat actor profile template usage examples
- OSINT collection checklist
- Enrichment pipeline design
- Intelligence confidence scoring guidance

## Phase 5 — AI Security

**Goal:** Build a dedicated AI security section focused on LLM, RAG, agent, and AI SOC risks.

Deliverables:

- Prompt injection threat model
- RAG security checklist
- Agent tool-use control model
- AI SOC architecture
- Data leakage prevention patterns
- Model governance checklist

## Phase 6 — Autonomous Security Systems

**Goal:** Connect knowledge, detection, intelligence, and automation into a controlled autonomous security engineering framework.

Deliverables:

- Autonomous SOC reference architecture
- Detection-to-response automation workflow
- Human-in-the-loop approval model
- Agent safety boundaries
- Evaluation metrics
- Feedback loop design

## Maintenance Rhythm

Weekly:

- Add or update at least one note
- Triage open issues and TODOs
- Validate repository and regenerate index

Monthly:

- Publish one polished portfolio-grade writeup
- Review CVE and IOC taxonomy
- Update roadmap and backlog

Quarterly:

- Refactor stale content
- Review safety policy
- Add project/demo deliverables
- Archive outdated notes
