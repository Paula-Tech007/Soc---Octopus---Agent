# Arquitetura do SOC Investigation Copilot

## 1. Objetivo da Arquitetura

Esta arquitetura define como o SOC Investigation Copilot deve processar alertas de seguranca de forma padronizada, segura, observavel e escalavel.

O objetivo e criar uma base enterprise para investigacao assistida por IA utilizando:

- n8n
- Webhook
- Redis
- PostgreSQL
- AI Agents
- Human in the Loop
- Observabilidade
- Governanca

---

## 2. Visao Geral

O fluxo principal sera:

1. Receber alerta via Webhook.
2. Validar payload.
3. Gerar Correlation ID.
4. Normalizar dados.
5. Verificar duplicidade no Redis.
6. Persistir alerta no PostgreSQL.
7. Executar agentes especializados.
8. Consolidar resultado.
9. Validar resposta final.
10. Retornar analise estruturada.
11. Registrar auditoria.

---

## 3. Componentes

### Webhook Ingress

Responsavel por receber alertas externos.

Deve validar:

- Metodo HTTP
- Payload
- Headers
- Autenticacao quando aplicavel
- Tamanho da requisicao

---

### Normalization Layer

Responsavel por transformar diferentes formatos de alerta em um modelo padrao.

Campos minimos:

- alert_id
- source
- timestamp
- rule_id
- rule_name
- severity_original
- src_ip
- dst_ip
- user
- hostname
- process
- command
- file_hash
- domain
- url

---

### Correlation Layer

Responsavel por criar e manter rastreabilidade.

Deve gerar:

- correlation_id
- investigation_id
- execution_id

---

### Redis Layer

Responsavel por:

- Deduplicacao
- Idempotencia
- Cache temporario
- Controle de reprocessamento

Chave sugerida:

```text
soc:investigation:{source}:{alert_id}