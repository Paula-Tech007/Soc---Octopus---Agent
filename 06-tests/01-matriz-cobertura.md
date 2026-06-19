# Matriz De Cobertura De Testes

## Objetivo

Mapear os cenarios de teste da Fase 7 contra os dominios, agentes e comportamentos esperados do SOC-Octopus-Agent.

## Cobertura Por Dominio

| Cenario | Dominio principal | Entrada | Causa raiz esperada | Risco esperado |
| --- | --- | --- | --- | --- |
| TEST-MOCK-001 | Identidade | Alerta SOC | `identity` | `high` |
| TEST-MOCK-002 | Identidade / VPN | Ticket | `identity` | `medium` |
| TEST-MOCK-003 | Rede | Evento | `network` | `medium` |
| TEST-MOCK-004 | Vulnerabilidades | Pergunta | `vulnerability` | `high` |
| TEST-MOCK-005 | Endpoint / EDR | Alerta SOC | `endpoint` | `high` |
| TEST-MOCK-006 | Cloud / IAM | Evento | `cloud` | `high` |
| TEST-MOCK-007 | Threat Intelligence | Alerta SOC | `external_threat` | `medium` |
| TEST-MOCK-008 | Falso positivo | Evento | `false_positive` | `low` |

## Cobertura Por Especialista

| Especialista | Cenarios |
| --- | --- |
| Cerebro Central / Orquestrador | Todos |
| Alertas SOC | TEST-MOCK-001, TEST-MOCK-005, TEST-MOCK-007, TEST-MOCK-008 |
| Threat Intelligence / OSINT | TEST-MOCK-007 |
| Endpoint / EDR | TEST-MOCK-005 |
| Rede | TEST-MOCK-003, TEST-MOCK-007 |
| Cloud | TEST-MOCK-006 |
| Identidade | TEST-MOCK-001, TEST-MOCK-002, TEST-MOCK-006 |
| Vulnerabilidades | TEST-MOCK-004 |
| Comunicacao | TEST-MOCK-002, TEST-MOCK-008 |
| Executivo | Nao coberto diretamente nesta fase |
| Automacao | Nao coberto diretamente nesta fase |
| Solucao e Remediacao | TEST-MOCK-001 a TEST-MOCK-007 |
| Infraestrutura e Plataformas | TEST-MOCK-003, TEST-MOCK-004 |

## Cobertura De Governanca

| Controle | Cenarios |
| --- | --- |
| `case_id` e `trace_id` obrigatorios | Todos |
| Avaliacao de falso positivo | Todos |
| Nivel de confianca | Todos |
| Aprovacao humana para acao critica | TEST-MOCK-001 a TEST-MOCK-007 |
| Bloqueio de credenciais | Todos |
| Bloqueio de dados reais | Todos |
| Sem chamadas externas | Todos |
| Sem execucao de remediacao | Todos |
| Memoria corporativa apenas futura | TEST-MOCK-008 |

## Lacunas Conhecidas

- Especialista Executivo nao possui cenario dedicado nesta fase.
- Especialista de Automacao nao possui cenario dedicado nesta fase.
- Nao ha teste automatizado executavel.
- Nao ha validacao real dentro do n8n.
- Nao ha teste contra banco ou Redis.

