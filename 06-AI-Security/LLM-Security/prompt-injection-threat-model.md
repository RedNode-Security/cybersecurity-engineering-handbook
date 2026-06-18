---
title: Prompt Injection Threat Model
domain: ai-security
category: llm-security
status: draft
created: 2026-06-18
updated: 2026-06-18
tags: [llm-security, prompt-injection, threat-modeling]
difficulty: intermediate
safe_publication: true
---

# Prompt Injection Threat Model

## Overview

Prompt injection occurs when untrusted text influences an LLM system to ignore intended instructions, leak data, misuse tools, or produce unsafe output.

## Why It Matters

LLM systems often combine user input, system instructions, retrieved content, tools, and memory. If these trust boundaries are not controlled, untrusted content can influence privileged behavior.

## Assets

- System prompts and policies
- User data
- Retrieved documents
- Tool credentials and permissions
- Conversation memory
- Generated outputs
- Audit logs

## Trust Boundaries

| Boundary | Risk |
|---|---|
| User input to model | Direct instruction manipulation |
| Retrieved content to model | Indirect prompt injection |
| Model to tools | Unauthorized or excessive action |
| Model to user | Data leakage or unsafe recommendation |
| Memory to future sessions | Persistence of malicious instructions |

## Threat Scenarios

### Direct Prompt Injection

A user attempts to override application instructions through direct input.

Defensive controls:

- Instruction hierarchy
- Input classification
- Refusal handling
- Output monitoring
- Least-privilege tool access

### Indirect Prompt Injection

A retrieved document contains instructions that attempt to manipulate the model.

Defensive controls:

- Treat retrieved content as data, not instructions
- Add source and provenance labels
- Filter or segment untrusted content
- Require confirmation before tool use
- Monitor suspicious instruction patterns in retrieved text

### Tool Misuse

A model with tool access takes an action beyond the user's authorization or business intent.

Defensive controls:

- Scope tools narrowly
- Add policy checks outside the model
- Require human approval for high-risk actions
- Log tool requests and responses
- Use allowlisted operations

## Detection Opportunities

- User prompts containing instruction override language
- Retrieved content containing model-facing instructions
- Tool calls inconsistent with user intent
- Repeated refusal boundary testing
- Attempts to access secrets, credentials, or hidden policy
- Outputs containing sensitive data markers

## Design Principles

- Keep policy enforcement outside the model when possible
- Separate instructions from data
- Use least-privilege tools
- Do not expose secrets to the model context unless necessary
- Add human approval for high-impact actions
- Log prompts, retrieved context references, tool calls, and decisions safely

## Automation Strategy

- Scan retrieved content for injection-like patterns
- Score tool calls by risk
- Add approval workflows for sensitive operations
- Build evaluation datasets for prompt injection attempts
- Track model refusal and override attempts

## References

- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- MITRE ATLAS: https://atlas.mitre.org/
