# Padroes De Campos E Enums

## Convencoes Gerais

- Usar `snake_case` para nomes de campos.
- Usar valores enumerados em minusculas.
- Usar underscore para valores compostos.
- Preservar `case_id` e `trace_id` em todas as etapas.
- Evitar abreviacoes obscuras.
- Evitar alternar portugues e ingles em campos tecnicos.

## Campos Obrigatorios De Entrada

Todo payload de entrada deve conter:

| Campo | Tipo | Padrao |
| --- | --- | --- |
| `case_id` | string | `CASE-MOCK-0001` |
| `trace_id` | string | `TRACE-MOCK-YYYYMMDD-0001` |
| `input_type` | string enum | `soc_alert`, `ticket`, `event`, `question` |
| `source_system` | string | Nome ficticio da origem |
| `received_at` | string datetime | ISO 8601 |
| `severity` | string enum | `low`, `medium`, `high`, `critical` |
| `title` | string | Titulo curto |
| `description` | string | Descricao objetiva |
| `governance` | object | Flags de governanca |

## Campos Recomendados De Entrada

| Campo | Tipo | Uso |
| --- | --- | --- |
| `entities` | object | Usuarios, hosts, IPs, dominios, servicos e recursos. |
| `evidence` | array | Evidencias mockadas. |
| `classification_hint` | string enum | Sugestao inicial de causa raiz. |
| `requester` | object | Dados ficticios de solicitante em tickets. |
| `question` | object | Texto e restricoes da pergunta. |

## Campos Obrigatorios De Governanca

| Campo | Tipo | Regra |
| --- | --- | --- |
| `contains_real_customer_data` | boolean | Deve ser `false` em fases mockadas. |
| `contains_credentials` | boolean | Deve ser `false`. |
| `human_approval_required_for_action` | boolean | Deve ser `true` quando houver acao critica possivel. |
| `mock_payload` | boolean | Deve ser `true` em payloads de teste. |

## Campos Obrigatorios De Saida Consolidada

| Campo | Tipo | Regra |
| --- | --- | --- |
| `case_id` | string | Mesmo valor da entrada. |
| `trace_id` | string | Mesmo valor da entrada. |
| `status` | string enum | Estado da analise. |
| `executive_summary` | string | Resumo direto. |
| `probable_root_cause` | string enum | Causa raiz padronizada. |
| `risk_level` | string enum | Nivel de risco. |
| `confidence_level` | string enum | Nivel de confianca. |
| `possible_false_positive` | boolean | Indicador booleano. |
| `human_approval_required` | boolean | Obrigatorio. |
| `audit` | object | Metadados de auditoria. |

## Padrao Para IDs

| Campo | Padrao |
| --- | --- |
| `case_id` | `CASE-MOCK-NNNN` |
| `trace_id` | `TRACE-MOCK-YYYYMMDD-NNNN` |
| `audit_id` | `AUDIT-MOCK-YYYYMMDD-NNNN` |
| `memory_id` | `MEM-MOCK-YYYYMMDD-NNNN` |

## Enums Oficiais Iniciais

### `input_type`

```text
soc_alert
ticket
event
question
```

### `probable_root_cause`

```text
identity
endpoint
network
cloud
vulnerability
external_threat
false_positive
unknown
```

### `risk_level` E `severity`

```text
low
medium
high
critical
```

### `confidence_level`

```text
low
medium
high
```

### `approval_status`

```text
pending
approved
rejected
needs_more_context
```

### `review_status`

```text
pending_human_review
approved_for_memory
rejected
needs_sanitization
expired
deprecated
```

## Inconsistencias A Corrigir Em Fases Futuras

- Alguns exemplos usam `possible_false_positive` como string textual e outros como boolean.
- Alguns nomes de especialistas usam hifen em textos de exemplo.
- O workflow mockado usa campos resumidos em string para entidades e evidencias.
- Os prompts estao em formato textual, enquanto contratos estao em formato JSON.

Esses pontos nao impedem a documentacao atual, mas devem ser normalizados antes de implementacao real.

