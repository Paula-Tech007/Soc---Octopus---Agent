# Fluxo n8n - SOC Investigation Copilot

## Objetivo

Definir o workflow principal do SOC Investigation Copilot utilizando n8n como orquestrador de investigacao, enriquecimento, classificacao e geracao de relatorios.

---

# Visao Geral

Fluxo principal:

```text
Webhook
    |
    +--> Validate Payload
    |
    +--> Generate Correlation ID
    |
    +--> Normalize Alert
    |
    +--> Redis Deduplication
    |
    +--> PostgreSQL Persist Alert
    |
    +--> Intake Agent
    |
    +--> IOC Research Agent
    |
    +--> MITRE Mapping Agent
    |
    +--> Severity Agent
    |
    +--> Report Agent
    |
    +--> Validator Agent
    |
    +--> PostgreSQL Persist Investigation
    |
    +--> Respond to Webhook
```

---

# Workflow 01 - Ingress

## Node 01

Webhook

Responsabilidade:

* Receber alerta
* Receber evento
* Receber ticket

Metodo:

```text
POST
```

---

## Node 02

Validate Payload

Responsabilidade:

* Validar JSON
* Validar campos obrigatorios
* Validar origem

Campos obrigatorios:

* source
* alert_id
* timestamp

Falha:

```text
HTTP 400
```

---

## Node 03

Generate Correlation ID

Responsabilidade:

Gerar:

* correlation_id
* investigation_id
* execution_id

Formato sugerido:

```text
corr-{timestamp}-{random}
```

---

## Node 04

Normalize Alert

Responsabilidade:

Transformar qualquer alerta para estrutura padrao.

Saida:

```json
{
  "source": "",
  "alert_id": "",
  "severity": "",
  "src_ip": "",
  "dst_ip": "",
  "hostname": ""
}
```

---

# Workflow 02 - Deduplicacao

## Node 05

Redis Lookup

Responsabilidade:

Verificar:

```text
soc:investigation:{source}:{alert_id}
```

---

## Node 06

Already Processed?

Tipo:

```text
IF
```

Se verdadeiro:

```text
Respond Duplicate
```

Se falso:

```text
Continuar fluxo
```

---

## Node 07

Redis Store

Responsabilidade:

Registrar alerta processado.

TTL:

```text
3600 segundos
```

---

# Workflow 03 - Persistencia

## Node 08

PostgreSQL Insert Alert

Tabela:

```text
soc_alerts
```

Responsabilidade:

Persistir alerta original.

---

# Workflow 04 - AI Analysis

## Node 09

Intake Agent

Responsabilidade:

Validacao contextual.

---

## Node 10

IOC Research Agent

Responsabilidade:

Enriquecimento.

Entradas:

* IP
* Dominio
* Hash

---

## Node 11

MITRE Mapping Agent

Responsabilidade:

Mapeamento ATT&CK.

Saida:

* Tatica
* Tecnica
* Subtecnica

---

## Node 12

Severity Agent

Responsabilidade:

Aplicar Severity Matrix.

Saida:

* Baixa
* Media
* Alta
* Critica

---

## Node 13

Report Agent

Responsabilidade:

Gerar:

* Executive Summary
* Technical Analysis
* Recommendations
* Next Steps

---

## Node 14

Validator Agent

Responsabilidade:

Validar consistencia final.

Resultado:

* Approved
* Rejected
* Review Required

---

# Workflow 05 - Human Approval

## Node 15

Critical Severity?

Tipo:

```text
IF
```

Condicao:

```text
severity == Critical
OR
severity == High
```

---

## Node 16

Human Approval Queue

Responsabilidade:

Enviar para aprovacao humana.

Primeira versao:

Mockada.

---

# Workflow 06 - Persistencia Final

## Node 17

PostgreSQL Insert Investigation

Tabela:

```text
soc_investigations
```

Responsabilidade:

Persistir resultado consolidado.

---

## Node 18

PostgreSQL Insert Evidence

Tabela:

```text
soc_evidence
```

Responsabilidade:

Persistir evidencias.

---

## Node 19

PostgreSQL Insert Audit

Tabela:

```text
soc_audit_log
```

Responsabilidade:

Persistir auditoria.

---

# Workflow 07 - Resposta

## Node 20

Respond to Webhook

Retornar:

* alert_id
* correlation_id
* severity
* executive_summary
* recommendations
* approval_required

---

# Tratamento de Erros

Todo node critico deve possuir tratamento.

Cobertura minima:

* Redis indisponivel
* PostgreSQL indisponivel
* Agent timeout
* Agent failure
* JSON invalido
* Persistencia falhou

---

# Observabilidade

Registrar:

* correlation_id
* investigation_id
* workflow_execution_id
* node_name
* execution_time
* status

---

# KPIs

Monitorar:

* Alerts Processed
* Duplicate Rate
* Investigation Time
* Error Rate
* Approval Rate
* Critical Alerts
* Cost per Investigation

---

# Criticos para Producao

Obrigatorio:

* Error Handling
* Retry
* Timeout
* Correlation ID
* Redis TTL
* PostgreSQL Constraints
* Logging
* Auditoria
* Human Approval

---

# Status Atual

Fase:

Design

Maturidade:

Intermediaria

Prontidao para Producao:

Nao aprovado

Motivo:

Workflow documentado, mas ainda nao implementado em n8n.
