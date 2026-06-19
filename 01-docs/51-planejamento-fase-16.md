# Fase 16 - Severidade Por Regra De Validacao

## Objetivo

Ampliar o relatorio do validador estatico local para incluir resumo por severidade das regras de validacao.

## Escopo

Artefatos cobertos nesta fase:

- `06-tests/04-validador-estatico.py`
- `06-tests/05-relatorio-validacao-estatica.json`
- `01-docs/28-indice-mestre.md`
- Checklist da Fase 16.

## Fora De Escopo

Nesta fase nao serao alterados:

- Payloads mockados.
- Workflow n8n mockado.
- SQL planejado.
- Prompts.

Nesta fase nao serao executados:

- n8n.
- SQL.
- Banco.
- Redis.
- APIs.
- IA.
- Integracoes externas.
- Instalacao de dependencias.

## Decisao Tecnica

O relatorio deve manter:

- `summary`
- `categories`
- `passed`
- `warnings`
- `failures`

E adicionar:

- `severity_summary`

Severidades iniciais:

- `critical`: workflow, SQL e seguranca.
- `high`: estrutura, JSON e payloads.
- `medium`: testes e memoria.
- `low`: validacoes gerais.

## Criterio De Saida Da Fase 16

- Validador atualizado.
- Relatorio com severidade gerado.
- Resultado sem falhas.
- Indice mestre atualizado.
- Checklist atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.

