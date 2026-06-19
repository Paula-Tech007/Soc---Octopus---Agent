# Security Policy

## Supported Scope

This repository currently supports prototype and lab validation only. It is not a production incident-response system.

## Reporting Security Issues

Report suspected exposure of secrets, real customer data, or unsafe workflow behavior to the repository owner before opening public issues.

Include:

- Affected file or workflow.
- Type of exposure or behavior.
- Whether the value appears real or synthetic.
- Suggested containment if known.

## Secret Handling

- Do not commit real API keys, OAuth secrets, bearer tokens, passwords, certificates, private keys, customer data, or n8n `pinData`.
- Use n8n credentials for all secrets.
- Treat any secret pasted into chat, documentation, or Git history as compromised and rotate it.
- Keep local `.env` files untracked. Only commit `.env*.example` files with synthetic values.

## n8n Workflow Rules

- Workflows must remain inactive in exported JSON.
- Webhooks require explicit authentication before activation.
- Production-bound workflows require tested error paths for HTTP, database, Redis, and other fallible nodes.
- External integrations must use placeholder credentials in exported templates.

## Data Classification

Only synthetic data is allowed in this repository. Real SOC alerts, tickets, user data, customer names, hostnames, internal IP inventories, or incident evidence must not be committed.

