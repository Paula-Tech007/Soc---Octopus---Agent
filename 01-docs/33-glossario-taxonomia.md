# Glossario E Taxonomia

## Glossario

| Termo | Definicao |
| --- | --- |
| `case_id` | Identificador unico do caso analisado. |
| `trace_id` | Identificador de rastreabilidade da execucao ou fluxo logico. |
| Entrada | Alerta, ticket, evento ou pergunta recebida pelo sistema. |
| Payload mockado | Payload ficticio usado para teste, sem dados reais. |
| Causa raiz | Categoria tecnica principal que explica o caso. |
| Cerebro Central | Orquestrador responsavel por roteamento, governanca e controle de fluxo. |
| Especialista tecnico | Agente especializado em dominio tecnico especifico. |
| Remediacao | Plano de acao recomendado para tratar o caso. |
| Consolidador | Agente responsavel por produzir a saida final revisavel. |
| Memoria corporativa | Base futura de conhecimento aprovado e auditavel. |
| Aprovacao humana | Decisao manual obrigatoria antes de acoes criticas. |
| Falso positivo | Caso que pode ter sido acionado sem representar incidente real. |
| Auditoria | Registro rastreavel de eventos, decisoes e alteracoes. |

## Tipos De Entrada

Valores oficiais iniciais para `input_type`:

| Valor | Uso |
| --- | --- |
| `soc_alert` | Alerta de seguranca ou SIEM. |
| `ticket` | Solicitacao ou incidente aberto por canal de atendimento. |
| `event` | Evento tecnico de log, infraestrutura, rede, cloud ou sistema. |
| `question` | Pergunta consultiva feita ao sistema. |

## Causa Raiz

Valores oficiais iniciais para `probable_root_cause`:

| Valor | Uso |
| --- | --- |
| `identity` | Autenticacao, autorizacao, AD, Entra ID, MFA, SSO ou privilegios. |
| `endpoint` | Host, EDR, processo, malware, isolamento ou artefatos locais. |
| `network` | Firewall, proxy, VPN, DNS, fluxo ou politica de rede. |
| `cloud` | Azure, AWS, GCP, IAM cloud ou recurso cloud. |
| `vulnerability` | CVE, patch, scanner, exposicao ou priorizacao de correcao. |
| `external_threat` | IOC, IP externo, dominio suspeito, campanha ou ameaca externa. |
| `false_positive` | Caso com indicio relevante de benignidade. |
| `unknown` | Dados insuficientes ou causa nao classificada. |

## Especialistas

Valores padronizados para referencia em payloads, testes e logs:

| Valor | Especialista |
| --- | --- |
| `cerebro_central` | Cerebro Central / Orquestrador |
| `alertas_soc` | Especialista em Alertas SOC |
| `threat_intelligence_osint` | Especialista em Threat Intelligence / OSINT |
| `endpoint_edr` | Especialista em Endpoint / EDR |
| `rede` | Especialista em Rede |
| `cloud` | Especialista em Cloud |
| `identidade` | Especialista em Identidade |
| `vulnerabilidades` | Especialista em Vulnerabilidades |
| `comunicacao` | Especialista em Comunicacao |
| `executivo` | Especialista Executivo |
| `automacao` | Especialista em Automacao |
| `solucao_remediacao` | Especialista em Solucao e Remediacao |
| `infraestrutura_plataformas` | Especialista em Infraestrutura e Plataformas |
| `consolidador` | Consolidador |

## Severidade E Risco

Valores oficiais para `severity` e `risk_level`:

| Valor | Definicao |
| --- | --- |
| `low` | Baixo impacto ou evidencia fraca. |
| `medium` | Impacto moderado, contexto incompleto ou necessidade de validacao. |
| `high` | Risco relevante, ativo sensivel ou evidencias consistentes. |
| `critical` | Impacto severo, comprometimento amplo ou urgencia operacional. |

## Confianca

Valores oficiais para `confidence_level`:

| Valor | Definicao |
| --- | --- |
| `low` | Evidencia fraca, muitas lacunas ou alta incerteza. |
| `medium` | Hipotese plausivel com dados suficientes, mas ainda exige validacao. |
| `high` | Evidencias consistentes e baixa ambiguidade. |

## Falso Positivo

Padrao recomendado:

- Em campos booleanos, usar `true` ou `false`.
- Em analises textuais, usar `yes`, `no` ou `possible`.
- Evitar misturar `sim`, `nao`, `possivel`, `yes`, `no` e `possible` no mesmo contrato tecnico.

Valor preferencial em campos textuais futuros:

| Valor | Definicao |
| --- | --- |
| `yes` | Ha indicios claros de falso positivo. |
| `no` | Evidencias favorecem risco real. |
| `possible` | Ha ambiguidade ou contexto insuficiente. |

## Status De Caso

Valores sugeridos:

| Valor | Uso |
| --- | --- |
| `new` | Caso recebido. |
| `validated` | Payload minimo validado. |
| `in_analysis` | Caso em analise. |
| `waiting_human_approval` | Aguardando decisao humana. |
| `analysis_completed_mock` | Analise mockada concluida. |
| `closed_false_positive` | Encerrado como falso positivo confirmado. |
| `closed_remediated` | Encerrado com remediacao validada. |
| `blocked_sensitive_data` | Bloqueado por conter dado sensivel. |

