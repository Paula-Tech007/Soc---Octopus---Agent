# Fase 6 - Persistencia Planejada

## Objetivo

Desenhar a persistencia futura do SOC-Octopus-Agent, incluindo modelo inicial para MySQL/MariaDB, uso previsto de Redis, estrategia de auditoria e campos preparados para memoria corporativa futura.

Esta fase e apenas de desenho e documentacao. Nenhum banco sera criado, nenhum SQL sera executado e nenhuma integracao sera configurada.

## Escopo

Artefatos cobertos nesta fase:

- Modelo conceitual de dados.
- DDL planejado para MySQL/MariaDB.
- Estrategia de auditoria.
- Uso previsto de Redis.
- Campos para memoria corporativa futura.
- Diagrama ER textual em Mermaid.
- Checklist da Fase 6.

## Fora De Escopo

Nesta fase nao serao criados:

- Banco de dados real.
- Usuario de banco.
- Senha.
- String de conexao.
- Container Docker.
- Execucao de SQL.
- Integracao com n8n.
- Integracao com Redis.
- Persistencia ativa.
- Memoria corporativa funcional.
- Dependencias externas.

## Premissas

- MySQL/MariaDB sera usado futuramente para registros persistentes e auditaveis.
- Redis sera usado futuramente apenas para estado temporario, cache, filas ou controle de execucao.
- Memoria corporativa futura nao deve receber dados automaticamente sem revisao humana.
- Todo registro persistido deve preservar `case_id` e `trace_id`.
- Payloads reais continuam proibidos nesta fase.

## Criterio De Saida Da Fase 6

- Persistencia planejada documentada.
- SQL planejado criado sem execucao.
- Uso previsto de Redis documentado.
- Estrategia de auditoria documentada.
- Diagrama ER textual criado.
- Estrutura validada.
- Checklist atualizado.
- Aprovacao humana pendente para iniciar a Fase 7.

