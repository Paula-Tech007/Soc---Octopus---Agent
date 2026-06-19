# Contratos De Payloads

## Principio

Os contratos desta fase sao conceituais e servem para padronizar comunicacao entre entrada, orquestrador, especialistas e consolidador.

Eles ainda nao representam schemas finais de banco de dados, APIs ou workflows n8n.

## Campos Base De Entrada

Todo payload de entrada deve conter:

| Campo | Tipo | Obrigatorio | Descricao |
| --- | --- | --- | --- |
| `case_id` | string | sim | Identificador ficticio do caso. |
| `trace_id` | string | sim | Identificador para rastreabilidade da execucao. |
| `input_type` | string | sim | Tipo de entrada: `soc_alert`, `ticket`, `event` ou `question`. |
| `source_system` | string | sim | Origem mockada do dado. |
| `received_at` | string | sim | Data e hora em ISO 8601. |
| `severity` | string | sim | `low`, `medium`, `high` ou `critical`. |
| `title` | string | sim | Titulo resumido. |
| `description` | string | sim | Descricao do caso. |
| `entities` | object | nao | Ativos, usuarios, IPs, dominios e recursos envolvidos. |
| `evidence` | array | nao | Evidencias mockadas. |
| `classification_hint` | string | nao | Hipotese inicial de causa raiz. |
| `governance` | object | sim | Flags de seguranca, aprovacao e dados sensiveis. |

## Tipos De Entrada

### Alerta SOC

Usado para alertas gerados por ferramentas de seguranca ou correlacao.

Deve conter evidencias tecnicas como origem, destino, regra acionada, severidade e observacoes de falso positivo.

### Ticket

Usado para demandas abertas manualmente por equipes, usuarios ou processos internos.

Deve conter solicitante ficticio, categoria, impacto percebido e urgencia.

### Evento

Usado para fatos tecnicos recebidos de logs, plataformas, infraestrutura ou sistemas.

Deve conter detalhes do evento, ativo envolvido e contexto temporal.

### Pergunta

Usado para perguntas diretas feitas ao sistema.

Deve conter pergunta, contexto informado, nivel esperado de detalhe e restricoes.

## Contrato De Saida Consolidada

Toda saida consolidada deve conter:

| Campo | Tipo | Obrigatorio | Descricao |
| --- | --- | --- | --- |
| `case_id` | string | sim | Caso analisado. |
| `trace_id` | string | sim | Rastreabilidade da analise. |
| `status` | string | sim | Estado da analise. |
| `executive_summary` | string | sim | Resumo objetivo para leitura rapida. |
| `probable_root_cause` | string | sim | Causa raiz provavel. |
| `risk_level` | string | sim | Nivel de risco consolidado. |
| `evidence_summary` | array | sim | Evidencias consideradas. |
| `specialists_involved` | array | sim | Especialistas acionados ou previstos. |
| `recommended_solution` | string | sim | Solucao recomendada. |
| `technical_steps` | array | sim | Passos tecnicos sugeridos. |
| `escalation_recommended` | string | sim | Escalonamento recomendado. |
| `security_notes` | array | sim | Observacoes de seguranca. |
| `confidence_level` | string | sim | `low`, `medium` ou `high`. |
| `possible_false_positive` | boolean | sim | Indica possibilidade de falso positivo. |
| `human_approval_required` | boolean | sim | Indica necessidade de aprovacao humana. |
| `audit` | object | sim | Metadados de auditoria e governanca. |

## Taxonomia Inicial De Causa Raiz

- `identity`
- `endpoint`
- `network`
- `cloud`
- `vulnerability`
- `external_threat`
- `false_positive`
- `unknown`

