# Ambiente LAB Local - SOC Investigation Copilot

## 1. Diagnostico

O projeto precisa de um ambiente local e isolado para validar o SOC Investigation Copilot sem usar credenciais, bancos ou Redis corporativos existentes.

Este LAB cria dois servicos dedicados via Docker Compose:

- PostgreSQL dedicado para `soc_copilot_lab`.
- Redis dedicado para cache, deduplicacao, estado temporario e controle de execucao.

O arquivo `05-sql/soc-investigation-copilot-schema.sql` ja existe no projeto e sera usado como script de inicializacao somente no PostgreSQL LAB.

## 2. Plano

1. Criar `.env.soc-copilot-lab` a partir de `.env.soc-copilot-lab.example` e substituir todos os valores `REPLACE_WITH_...` por segredos locais exclusivos do LAB.
2. Revisar as portas locais:
   - PostgreSQL: `5433:5432`.
   - Redis: `6380:6379`.
3. Subir o Compose dedicado `docker-compose.soc-copilot-lab.yml`.
4. Validar healthcheck dos containers.
5. Testar conexao PostgreSQL sem usar bancos existentes.
6. Testar Redis com autenticacao propria do LAB.
7. Criar novas credenciais no n8n, manualmente, sem reutilizar credenciais existentes.

## 3. Arquivos

Arquivos do LAB:

- `docker-compose.soc-copilot-lab.yml`
- `.env.soc-copilot-lab.example`
- `05-sql/soc-investigation-copilot-schema.sql`
- `01-docs/soc-investigation-copilot/07-ambiente-lab.md`

## 4. Como subir o ambiente

Criar o arquivo local de variaveis:

```powershell
Copy-Item .env.soc-copilot-lab.example .env.soc-copilot-lab
```

Antes de executar `config` ou `up`, edite `.env.soc-copilot-lab` e substitua todos os valores `REPLACE_WITH_...` por senhas locais do LAB. Nao reutilize credenciais corporativas ou pessoais.

Subir somente o LAB:

```powershell
docker compose --env-file .env.soc-copilot-lab -f docker-compose.soc-copilot-lab.yml up -d
```

Verificar status:

```powershell
docker compose --env-file .env.soc-copilot-lab -f docker-compose.soc-copilot-lab.yml ps
```

Importante: nao use `docker compose up` sem `-f docker-compose.soc-copilot-lab.yml`, para evitar acionar outro Compose do projeto.

## 5. Como testar PostgreSQL

Teste usando o proprio container LAB:

```powershell
docker exec -it soc-copilot-postgres-lab psql -U soc_copilot_user -d soc_copilot_lab -c "\dt"
```

Teste a partir do host, caso `psql` esteja instalado:

```powershell
psql "host=127.0.0.1 port=5433 dbname=soc_copilot_lab user=soc_copilot_user password=<valor em .env.soc-copilot-lab>" -c "\dt"
```

Consulta minima esperada:

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
```

Tabelas esperadas:

- `soc_alerts`
- `soc_investigations`
- `soc_agent_results`
- `soc_evidence`
- `soc_audit_log`
- `soc_execution_log`

## 6. Como testar Redis

Teste usando o proprio container LAB:

```powershell
docker exec -it soc-copilot-redis-lab sh -lc 'redis-cli -a "$SOC_COPILOT_REDIS_PASSWORD" ping'
```

Resultado esperado:

```text
PONG
```

Teste a partir do host, caso `redis-cli` esteja instalado:

```powershell
redis-cli -h 127.0.0.1 -p 6380 -a "<valor em .env.soc-copilot-lab>" ping
```

Validacao funcional simples:

```powershell
redis-cli -h 127.0.0.1 -p 6380 -a "<valor em .env.soc-copilot-lab>" SET soc:copilot:lab:health ok EX 60
redis-cli -h 127.0.0.1 -p 6380 -a "<valor em .env.soc-copilot-lab>" GET soc:copilot:lab:health
```

## 7. Como configurar credenciais no n8n

Crie credenciais novas no n8n. Nao selecione, edite ou reutilize credenciais existentes.

### PostgreSQL SOC Copilot LAB

Tipo de credencial n8n:

```text
Postgres
```

Nome recomendado:

```text
PostgreSQL SOC Copilot LAB
```

Campos:

```text
Host: host.docker.internal ou IP adequado conforme ambiente
Port: 5433
Database: soc_copilot_lab
User: soc_copilot_user
Password: valor de SOC_COPILOT_POSTGRES_PASSWORD no arquivo local .env.soc-copilot-lab
SSL: disabled para LAB local
```

Se o n8n estiver rodando diretamente no host, use:

```text
Host: 127.0.0.1
```

Se o n8n estiver em container e nao conseguir acessar `host.docker.internal`, use o IP do host acessivel pela rede Docker ou conecte o n8n explicitamente a uma rede de laboratorio aprovada.

### Redis SOC Copilot LAB

Tipo de credencial n8n:

```text
Redis
```

Nome recomendado:

```text
Redis SOC Copilot LAB
```

Campos:

```text
Host: host.docker.internal ou IP adequado conforme ambiente
Port: 6380
Password: valor de SOC_COPILOT_REDIS_PASSWORD no arquivo local .env.soc-copilot-lab
Database: 0
TLS: disabled para LAB local
```

Se o n8n estiver rodando diretamente no host, use:

```text
Host: 127.0.0.1
```

## 8. Riscos

- Exposicao local: as portas 5433 e 6380 ficam disponiveis conforme `SOC_COPILOT_*_BIND_ADDRESS`. O padrao do LAB usa `127.0.0.1` para reduzir exposicao.
- Colisao de portas: se 5433 ou 6380 ja estiverem em uso, ajuste apenas o arquivo `.env.soc-copilot-lab`.
- Confusao de credenciais: usar nomes explicitos no n8n evita vincular workflows ao banco ou Redis errados.
- Persistencia local: volumes Docker mantem dados entre reinicios do LAB.
- Inicializacao do schema: scripts em `/docker-entrypoint-initdb.d` rodam somente na primeira criacao do volume PostgreSQL.

## 9. Criterios de Producao

Classificacao do LAB:

```text
Nivel de maturidade: laboratorio controlado
Risco operacional: baixo, desde que o Compose correto seja usado
Risco de seguranca: baixo para LAB local com bind em 127.0.0.1
Complexidade: baixa
Prontidao para producao: nao aprovado
```

Para producao, ainda seriam obrigatorios:

- Senhas fortes e rotacionadas fora de arquivos versionados.
- Secrets gerenciados por vault ou mecanismo corporativo equivalente.
- Backup e restore testados.
- TLS quando houver trafego fora do host local.
- Politica de retencao.
- Monitoramento de disponibilidade, latencia, erros e capacidade.
- Revisao de indices conforme volumetria real.
- Controle formal de acesso ao banco e ao Redis.

Resultado de aprovacao:

```text
Aprovado com ajustes para LAB local.
Nao aprovado para producao.
```
