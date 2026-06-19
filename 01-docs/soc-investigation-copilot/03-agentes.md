# Agentes do SOC Investigation Copilot

## Objetivo

Definir responsabilidades, entradas, saidas, permissoes, riscos e criterios operacionais dos agentes utilizados pelo SOC Investigation Copilot.

---

# Arquitetura Geral

Modelo adotado:

```text
Orchestrator
    |
    +--> Intake Agent
    +--> IOC Research Agent
    +--> MITRE Mapping Agent
    +--> Severity Agent
    +--> Report Agent
    +--> Validator Agent
```

O n8n sera o orquestrador principal na primeira versao.

---

# Intake Agent

## Objetivo

Receber e validar alertas de seguranca.

## Entradas

* Alerta Wazuh
* Evento SIEM
* Ticket
* Payload Webhook

## Saidas

* Alerta normalizado
* Correlation ID
* Investigation ID

## Responsabilidades

* Validar payload
* Normalizar estrutura
* Identificar origem
* Validar campos obrigatorios

## Ferramentas

* Parser
* Normalization Engine

## Permissoes

* Leitura apenas

## Riscos

* Payload malformado
* Dados incompletos

## KPIs

* Taxa de validacao
* Taxa de erro

---

# IOC Research Agent

## Objetivo

Investigar indicadores de comprometimento.

## Entradas

* IP
* Dominio
* URL
* Hash
* Hostname

## Saidas

* Reputacao
* Evidencias
* Indicadores enriquecidos

## Responsabilidades

* Correlacionar IOCs
* Enriquecer contexto
* Identificar comportamento suspeito

## Ferramentas Futuras

* VirusTotal
* AbuseIPDB
* AlienVault OTX
* MISP
* OpenCTI

## Permissoes

* Consulta somente

## Riscos

* Fontes externas indisponiveis
* Dados inconsistentes

## KPIs

* IOC Success Rate
* IOC Enrichment Rate

---

# MITRE Mapping Agent

## Objetivo

Mapear comportamento para MITRE ATT&CK.

## Entradas

* Regra
* Evento
* IOC
* Evidencias

## Saidas

* Tatica
* Tecnica
* Subtecnica

## Responsabilidades

* Classificar comportamento
* Associar ATT&CK

## Permissoes

* Leitura

## KPIs

* Cobertura ATT&CK
* Precisao do mapeamento

---

# Severity Agent

## Objetivo

Determinar severidade do incidente.

## Entradas

* Alerta
* IOC
* MITRE
* Contexto

## Saidas

* Baixa
* Media
* Alta
* Critica

## Responsabilidades

* Aplicar Severity Matrix
* Avaliar impacto
* Avaliar urgencia

## Permissoes

* Leitura

## KPIs

* Precisao da classificacao
* Divergencia humana

---

# Report Agent

## Objetivo

Gerar relatorio consolidado.

## Entradas

* Resultado dos agentes

## Saidas

* Executive Summary
* Technical Analysis
* Recommendations
* Next Steps

## Responsabilidades

* Consolidar informacoes
* Gerar relatorio estruturado

## Permissoes

* Leitura

## KPIs

* Qualidade do relatorio
* Tempo de geracao

---

# Validator Agent

## Objetivo

Validar consistencia do resultado.

## Entradas

* Relatorio consolidado

## Saidas

* Aprovado
* Reprovado
* Necessita revisao

## Responsabilidades

* Detectar inconsistencias
* Verificar evidencias
* Avaliar confianca

## Permissoes

* Leitura

## KPIs

* Taxa de aprovacao
* Taxa de correcao

---

# Observabilidade dos Agentes

Todos os agentes devem registrar:

* correlation_id
* investigation_id
* agent_name
* execution_time
* status
* error_message
* decision_summary

---

# Seguranca

Todos os agentes devem validar:

* Prompt Injection
* Tool Injection
* Agent Injection
* Dados sensiveis
* Permissoes excessivas

Nenhum agente pode executar acao destrutiva.

---

# Human In The Loop

Obrigatorio quando:

* Severidade Alta
* Severidade Critica
* Acao de contencao
* Bloqueio
* Revogacao de acesso

---

# Criterios de Producao

Cada agente deve possuir:

* Objetivo definido
* Inputs definidos
* Outputs definidos
* KPIs definidos
* Observabilidade implementada
* Seguranca validada
* Testes executados

---

# Status Atual

Fase: Design

Maturidade: Inicial

Prontidao para Producao: Nao aprovado

Motivo:

Os agentes estao definidos conceitualmente, mas ainda nao foram implementados nem testados.
