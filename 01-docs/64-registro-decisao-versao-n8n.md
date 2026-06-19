# Registro De Decisao - Versao Alvo Do n8n

## Status

Nao decidido.

## Objetivo

Registrar a decisao futura sobre a versao alvo do n8n que sera usada para importar e validar o workflow mockado do SOC-Octopus-Agent em ambiente controlado.

Este documento nao autoriza instalacao, importacao, execucao ou criacao de credenciais.

## Contexto

O pacote atual contem workflows inativos em perfis diferentes: `mock-executable`, `lab-template` e `prod-template`.
Alguns templates incluem nodes Webhook, HTTP, PostgreSQL, Redis e referencias de credenciais placeholder, sem valores secretos.

A compatibilidade real depende da versao do n8n usada em uma futura instancia de laboratorio. Por isso, a versao alvo deve ser decidida antes de qualquer importacao.

## Decisao Atual

Nenhuma versao alvo foi selecionada nesta fase.

Motivo:

- Nao houve informacao operacional sobre ambiente n8n disponivel.
- Nao houve aprovacao para consulta externa de versao.
- Nao houve aprovacao para instalacao, importacao ou execucao.
- A etapa atual e apenas documental.

## Campos A Preencher Em Fase Futura

| Campo | Valor |
| --- | --- |
| Versao alvo do n8n | Pendente |
| Fonte usada para confirmar versao | Pendente |
| Data da confirmacao | Pendente |
| Responsavel pela decisao | Pendente |
| Ambiente alvo | Pendente |
| Tipo de ambiente | Laboratorio isolado |
| Criterios do ambiente | `01-docs/67-criterios-ambiente-laboratorio-n8n.md` |
| Workflow alvo | `02-workflows-n8n/soc-octopus-prototipo-mock.json` |
| Resultado esperado | Importacao inativa, sem credenciais e sem execucao |
| Status da aprovacao humana | Pendente |

## Criterios Para Escolha Da Versao

A versao alvo deve:

- Ser definida antes da importacao.
- Ser registrada com data de confirmacao.
- Ser validada contra a estrutura de workflow exportada.
- Permitir importacao dos tipos de nodes usados pelo perfil selecionado.
- Permitir manter o workflow inativo apos importacao.
- Permitir ambiente isolado, sem dados reais.
- Permitir referencias placeholder sem selecionar credenciais reais durante a importacao.
- Exigir validacao separada antes de qualquer node externo, banco, Redis ou Webhook ser executado.

## Evidencias Minimas Para Aprovar

- Fonte da versao registrada.
- Ambiente de laboratorio identificado.
- Criterios de ambiente de laboratorio atendidos.
- Checklist operacional de importacao revisado.
- Validador estatico local executado sem falhas.
- Confirmacao de que importacao e execucao sao aprovacoes separadas.

## Consequencias Da Decisao

Quando uma versao for escolhida:

- O checklist operacional de importacao deve referenciar essa versao.
- Qualquer divergencia de importacao deve ser registrada antes de ajustes.
- Ajustes de workflow devem ser tratados em fase separada.
- Execucao do workflow deve continuar bloqueada ate aprovacao explicita.

## Criterios De Bloqueio

A decisao deve permanecer bloqueada se:

- Nao houver versao alvo documentada.
- Nao houver fonte de confirmacao.
- O ambiente alvo nao for isolado.
- A importacao exigir credenciais reais sem aprovacao separada.
- A importacao alterar nodes externos sem registro de divergencia.
- Houver risco de uso de dados reais.
- Nao houver aprovacao humana explicita.

## Proxima Revisao

Revisar este registro quando houver autorizacao humana para propor uma versao alvo do n8n.
