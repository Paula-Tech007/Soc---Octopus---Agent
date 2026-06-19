# Fase 2 - Contratos E Payloads Mockados

## Objetivo

Definir contratos conceituais e payloads mockados para as principais entradas e saidas do SOC-Octopus-Agent.

Esta fase prepara a base para prompts, workflows e testes futuros, mas nao implementa automacao, banco de dados, APIs ou integracoes reais.

## Escopo

Entradas cobertas nesta fase:

- Alerta SOC.
- Ticket.
- Evento.
- Pergunta.

Saida coberta nesta fase:

- Resposta consolidada do sistema.

## Fora De Escopo

Nesta fase nao serao criados:

- Workflows n8n.
- Prompts finais de agentes.
- SQL.
- Codigo executavel.
- Integracoes com APIs.
- Dependencias externas.
- Credenciais, tokens ou URLs corporativas.
- Memoria corporativa funcional.

## Regras De Dados

- Usar somente dados ficticios.
- Usar dominios reservados como `example.test`.
- Usar enderecos IP reservados para documentacao, como `192.0.2.0/24`, `198.51.100.0/24` e `203.0.113.0/24`.
- Nao usar nomes reais de clientes, usuarios, servidores ou empresas.
- Nao simular tokens, secrets, senhas ou chaves de API.

## Criterios De Qualidade

Todo payload deve permitir rastreabilidade minima:

- `case_id`
- `trace_id`
- `input_type`
- `source_system`
- `received_at`

Todo diagnostico futuro deve suportar:

- Evidencias.
- Causa provavel.
- Nivel de risco.
- Solucao recomendada.
- Nivel de confianca.
- Possivel falso positivo.
- Necessidade de aprovacao humana.

