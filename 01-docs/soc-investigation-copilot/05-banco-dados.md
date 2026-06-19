# Banco de Dados - SOC Investigation Copilot

## Objetivo

Definir a estrutura PostgreSQL para suportar investigacoes SOC, agentes IA, auditoria, observabilidade e governanca.

---

# Principios

O banco deve garantir:

* Integridade
* Rastreabilidade
* Auditoria
* Escalabilidade
* Performance
* Governanca

---

# Visao Geral

Tabelas principais:

```text
soc_alerts
soc_investigations
soc_agent_results
soc_evidence
soc_audit_log
soc_execution_log
```

Relacionamentos:

```text
soc_alerts
    |
    +--> soc_investigations
              |
              +--> soc_agent_results
              |
              +--> soc_evidence
              |
              +--> soc_audit_log
              |
              +--> soc_execution_log
```

---

# Tabela: soc_alerts

## Objetivo

Armazenar alertas recebidos.

## Campos

```sql
alert_uuid UUID PRIMARY KEY
alert_id VARCHAR(255)
source VARCHAR(100)

correlation_id VARCHAR(255)

severity_original VARCHAR(50)

rule_id VARCHAR(100)
rule_name TEXT

src_ip VARCHAR(100)
dst_ip VARCHAR(100)

hostname VARCHAR(255)
username VARCHAR(255)

event_timestamp TIMESTAMP

raw_payload JSONB

created_at TIMESTAMP
```

## Indices

```sql
idx_alert_id
idx_source
idx_correlation_id
idx_event_timestamp
```

---

# Tabela: soc_investigations

## Objetivo

Representar uma investigacao.

## Campos

```sql
investigation_uuid UUID PRIMARY KEY

alert_uuid UUID

correlation_id VARCHAR(255)

severity_final VARCHAR(50)

executive_summary TEXT

technical_analysis TEXT

approval_required BOOLEAN

status VARCHAR(50)

created_at TIMESTAMP
updated_at TIMESTAMP
```

## Foreign Key

```sql
alert_uuid
-> soc_alerts.alert_uuid
```

---

# Tabela: soc_agent_results

## Objetivo

Armazenar resultados individuais dos agentes.

## Campos

```sql
agent_result_uuid UUID PRIMARY KEY

investigation_uuid UUID

agent_name VARCHAR(255)

agent_version VARCHAR(50)

input_data JSONB

output_data JSONB

confidence_score NUMERIC(5,2)

execution_time_ms INTEGER

status VARCHAR(50)

created_at TIMESTAMP
```

## Foreign Key

```sql
investigation_uuid
-> soc_investigations.investigation_uuid
```

---

# Tabela: soc_evidence

## Objetivo

Armazenar evidencias produzidas durante investigacoes.

## Campos

```sql
evidence_uuid UUID PRIMARY KEY

investigation_uuid UUID

evidence_type VARCHAR(100)

evidence_value TEXT

source VARCHAR(255)

confidence_score NUMERIC(5,2)

created_at TIMESTAMP
```

## Exemplos

```text
IP
Domain
Hash
MITRE Technique
IOC
URL
Hostname
User
```

---

# Tabela: soc_audit_log

## Objetivo

Registrar trilha de auditoria.

## Campos

```sql
audit_uuid UUID PRIMARY KEY

investigation_uuid UUID

event_type VARCHAR(100)

actor_type VARCHAR(100)

actor_name VARCHAR(255)

action TEXT

details JSONB

created_at TIMESTAMP
```

## Exemplos

```text
Agent Executed
Investigation Created
Severity Changed
Approval Requested
Approval Granted
Approval Rejected
```

---

# Tabela: soc_execution_log

## Objetivo

Registrar observabilidade operacional.

## Campos

```sql
execution_uuid UUID PRIMARY KEY

investigation_uuid UUID

workflow_name VARCHAR(255)

node_name VARCHAR(255)

execution_status VARCHAR(50)

execution_time_ms INTEGER

error_message TEXT

created_at TIMESTAMP
```

---

# Estrategia de JSONB

Utilizar JSONB para:

```text
raw_payload
input_data
output_data
details
```

Motivos:

* Flexibilidade
* Evolucao futura
* Performance
* Indexacao parcial

---

# Constraints

Obrigatorias:

```sql
NOT NULL
PRIMARY KEY
FOREIGN KEY
CHECK
```

Exemplos:

```sql
severity_final IN
(
'Low',
'Medium',
'High',
'Critical'
)
```

---

# Retencao

Recomendacao inicial:

```text
soc_execution_log
90 dias

soc_audit_log
1 ano

soc_alerts
1 ano

soc_investigations
2 anos
```

---

# Observabilidade

KPIs futuros:

* Alerts Processed
* Duplicate Rate
* Investigation Time
* Error Rate
* Agent Success Rate
* Approval Rate
* Critical Incidents

---

# Seguranca

Nunca armazenar:

* Senhas
* Secrets
* Tokens
* API Keys

Mascarar dados sensiveis quando necessario.

---

# Criticos para Producao

Obrigatorio:

* Foreign Keys
* Indices
* Auditoria
* Correlation ID
* Retencao definida
* Backup
* Observabilidade

---

# Status Atual

Fase:

Design

Maturidade:

Intermediaria

Prontidao para Producao:

Aprovado para implementacao

Motivo:

Modelo relacional definido e consistente com a arquitetura do projeto.
