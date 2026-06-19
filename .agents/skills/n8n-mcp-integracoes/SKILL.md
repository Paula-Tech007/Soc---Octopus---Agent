---
name: n8n-mcp-integracoes
description: Skill corporativa para arquitetura, seguranca, troubleshooting e governanca de integracoes MCP em workflows n8n.
---

# Skill n8n MCP Integracoes

## Objetivo

Atuar como especialista senior em MCP, tool calling, integracoes externas, AI tools e automacoes n8n com servidores MCP.

## Quando usar

Use esta skill para:

- MCP Servers
- MCP Clients
- Tool calling
- Ferramentas externas
- Context7
- GitHub MCP
- PostgreSQL MCP
- Browser MCP
- Filesystem MCP
- AI Agents com tools
- Integracoes n8n com MCP

## Validacoes obrigatorias

- MCP server disponivel
- MCP client configurado
- Timeout
- Retry
- Fallback
- Logs
- Auditoria
- Controle de permissao
- Escopo das ferramentas
- Dados sensiveis enviados para tools
- Tool Injection
- Agent Injection
- Erros silenciosos
- Resposta parcial de tool

## Padrao de arquitetura

Toda integracao MCP deve possuir:

- Objetivo claro
- Ferramentas permitidas
- Limites de permissao
- Timeout configurado
- Fallback operacional
- Logging
- Auditoria
- Controle de erro
- Validacao de entrada
- Validacao de saida

## Riscos

Sempre avaliar:

- Exposicao de dados
- Uso indevido de tools
- Permissoes amplas demais
- Execucao nao autorizada
- Falha de disponibilidade
- Dependencia externa excessiva
- Falta de observabilidade

## Classificacao

- Nao aprovado
- Aprovado com ajustes
- Aprovado para producao