# SOC Investigation Copilot

## 1. Objetivo

O SOC Investigation Copilot e um projeto de automacao inteligente para apoiar investigacoes de alertas de seguranca, eventos Wazuh, IOCs, incidentes e tickets SOC.

O objetivo principal e reduzir tempo de triagem, padronizar analises, enriquecer evidencias e apoiar a tomada de decisao com uso de n8n, AI Agents, Redis, PostgreSQL e boas praticas de seguranca corporativa.

---

## 2. Problema que o Projeto Resolve

Em operacoes SOC, analistas precisam lidar com:

- Alto volume de alertas
- Eventos duplicados
- Alertas sem contexto
- Falta de padronizacao na triagem
- Dificuldade para classificar severidade
- Investigacoes repetitivas
- Falta de evidencias consolidadas
- Tempo elevado para criar resumo tecnico e executivo

Este projeto resolve esses pontos criando um fluxo automatizado e governado de investigacao assistida por IA.

---

## 3. Escopo Inicial

A primeira versao sera mockada e controlada.

Inclui:

- Entrada via Webhook n8n
- Payload de alerta Wazuh ou SIEM
- Normalizacao do alerta
- Deduplicacao com Redis
- Persistencia em PostgreSQL
- Analise por AI Agents
- Classificacao de severidade
- Mapeamento MITRE ATTACK
- Geracao de relatorio
- Saida estruturada

Nao inclui nesta primeira fase:

- Bloqueio automatico
- Contencao automatica
- Acoes destrutivas
- Integracao produtiva com clientes reais
- Uso de credenciais sensiveis reais

---

## 4. Principios de Arquitetura

O projeto deve seguir:

- Simplicidade
- Seguranca
- Observabilidade
- Reutilizacao
- Idempotencia
- Governanca
- Escalabilidade
- Human in the Loop para acoes criticas

---

## 5. Agentes Planejados

### Intake Agent

Responsavel por:

- Receber alerta
- Validar payload
- Identificar tipo de evento
- Preparar dados para os proximos agentes

### IOC Research Agent

Responsavel por:

- Analisar IPs
- Analisar dominios
- Analisar hashes
- Enriquecer indicadores
- Buscar reputacao

### MITRE Mapping Agent

Responsavel por:

- Mapear taticas
- Mapear tecnicas
- Relacionar comportamento com MITRE ATTACK

### Severity Agent

Responsavel por:

- Aplicar matriz de severidade
- Avaliar impacto
- Avaliar urgencia
- Definir classificacao final

### Report Agent

Responsavel por:

- Gerar resumo executivo
- Gerar analise tecnica
- Listar evidencias
- Gerar recomendacoes
- Definir proximos passos

### Validator Agent

Responsavel por:

- Revisar consistencia
- Validar saida estruturada
- Detectar lacunas
- Aprovar ou reprovar resultado

---

## 6. Componentes Tecnicos

### n8n

Responsavel por orquestrar:

- Webhook
- Normalizacao
- Redis
- PostgreSQL
- AI Agents
- Resposta final

### Redis

Utilizado para:

- Deduplicacao
- Controle de reprocessamento
- Cache temporario
- Idempotencia

### PostgreSQL

Utilizado para:

- Persistencia de alertas
- Historico de investigacoes
- Evidencias
- Resultados de agentes
- Auditoria

### AI Agents

Utilizados para:

- Analise contextual
- Classificacao
- Enriquecimento
- Relatorio
- Validacao

---

## 7. Segurança

O projeto deve validar:

- Prompt Injection
- Tool Injection
- Agent Injection
- Dados sensiveis
- Credenciais hardcoded
- Tokens hardcoded
- Permissoes excessivas
- Falta de HITL em acoes criticas

Nenhum agente pode executar acao destrutiva sem aprovacao humana.

---

## 8. Observabilidade

Toda execucao deve possuir:

- Correlation ID
- Logs
- Status por etapa
- Tempo de execucao
- Erros
- Resultado final
- Decisao dos agentes

---

## 9. Saida Esperada

A saida final deve conter:

- Alert ID
- Correlation ID
- Severidade
- Resumo executivo
- Analise tecnica
- Evidencias
- MITRE ATTACK
- Riscos
- Recomendacoes
- Proximos passos
- Status de aprovacao

---

## 10. Criterios de Producao

Para ser considerado pronto para producao, o projeto deve possuir:

- Workflow n8n sem nodes orfaos
- Tratamento de erro
- Retry quando aplicavel
- Timeout configurado
- Deduplicacao
- Persistencia
- Observabilidade
- Logs
- Validacao de entrada
- Validacao de saida
- Segurança de credenciais
- Human in the Loop para acoes criticas

---

## 11. Classificacao Inicial

Status atual:

- Fase: Design
- Maturidade: Inicial
- Risco operacional: Baixo
- Risco de seguranca: Baixo
- Prontidao para producao: Nao aprovado

Motivo:

O projeto ainda esta em fase de arquitetura e documentacao. Nenhum workflow produtivo foi implementado ainda.