# Redis, Auditoria E Memoria Futura

## Uso Previsto De Redis

Redis deve ser tratado como componente temporario, nao como fonte de verdade.

Usos futuros possiveis:

- Estado temporario de execucao multiagente.
- Controle de fila de casos.
- Controle de idempotencia por `trace_id`.
- Cache de classificacao temporaria.
- Rate limit interno.
- Lock temporario para evitar processamento duplicado.
- TTL para contexto transitorio.

## O Que Nao Deve Ficar No Redis

- Credenciais.
- Tokens.
- Senhas.
- Dados reais de clientes sem politica aprovada.
- Registro definitivo de auditoria.
- Memoria corporativa definitiva.
- Decisoes humanas definitivas.

## Chaves Redis Planejadas

Formato sugerido para fase futura:

```text
soc:case:{case_id}:state
soc:trace:{trace_id}:lock
soc:queue:incoming
soc:queue:human-approval
soc:cache:classification:{trace_id}
soc:ttl:context:{trace_id}
```

## TTL Sugerido

Valores indicativos para decisao futura:

- Estado temporario de caso: 24 horas.
- Lock de processamento: 10 minutos.
- Cache de classificacao: 1 hora.
- Contexto transitorio: 6 horas.
- Fila de aprovacao humana: sem TTL automatico ate desenho de governanca.

## Estrategia De Auditoria

Auditoria deve ser persistida em MySQL/MariaDB, nao em Redis.

Eventos minimos:

- Recebimento de entrada.
- Validacao minima.
- Normalizacao.
- Classificacao de causa raiz.
- Decisao do Cerebro Central.
- Acionamento de especialista.
- Diagnostico produzido.
- Recomendacao de remediacao.
- Decisao de aprovacao humana.
- Saida consolidada.
- Candidato a memoria futura.

## Campos Minimos De Auditoria

- `audit_id`
- `case_id`
- `trace_id`
- `event_type`
- `actor_type`
- `actor_name`
- `event_summary`
- `event_payload`
- `created_at`
- `mock_data`
- `human_approval_required`

## Memoria Corporativa Futura

A memoria corporativa nao sera implementada nesta fase.

Quando implementada, ela deve aprender apenas com registros aprovados por humano.

Fontes futuras:

- Incidentes encerrados.
- Solucoes aplicadas.
- Falsos positivos confirmados.
- Licoes aprendidas.
- Causas recorrentes.
- Procedimentos internos aprovados.

## Controle De Qualidade Da Memoria

Antes de virar conhecimento reutilizavel, um candidato deve ter:

- Revisao humana.
- Status de aprovacao.
- Nivel de confianca.
- Escopo de aplicabilidade.
- Data de validade ou revisao.
- Evidencias associadas.
- Indicao se envolve falso positivo.

## Riscos

- Redis pode perder dados se usado como fonte de verdade.
- Memoria sem revisao pode perpetuar diagnosticos incorretos.
- Auditoria incompleta dificulta investigacao posterior.
- Contexto sensivel pode vazar se nao houver saneamento antes da persistencia futura.

