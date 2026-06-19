# Plano De Pendencias Da Janela n8n

## Status Consolidado

| Campo | Valor |
| --- | --- |
| Projeto | SOC-Octopus-Agent |
| Status | bloqueado |
| Status da origem | bloqueado |
| Gerado em | 2026-06-19T20:23:28.023512+00:00 |
| Gerador | 06-tests/13-gerador-plano-pendencias-janela-n8n.py |

## Totais

| Metrica | Total |
| --- | ---: |
| Acoes | 11 |
| Acoes que bloqueiam a janela | 10 |
| P0 | 6 |
| P1 | 4 |
| P2 | 1 |

## Decisao Recomendada

- Manter janela n8n bloqueada. Resolver acoes P0 e P1 com aprovacao humana antes de qualquer importacao, exportacao ou execucao.

## Acoes

| ID | Prioridade | Categoria | Responsavel Sugerido | Pendencia | Acao Recomendada |
| --- | --- | --- | --- | --- | --- |
| ACT-0001 | P0 | decisao | responsavel pela aprovacao humana | Versao alvo do n8n ainda nao esta decidida. | Preencher e aprovar registro de decisao da versao alvo. |
| ACT-0002 | P0 | ambiente | responsavel tecnico | Campo de identificacao pendente: Janela. | Preencher somente com informacao confirmada por responsavel humano. |
| ACT-0003 | P0 | ambiente | responsavel tecnico | Campo de identificacao pendente: Ambiente. | Preencher somente com informacao confirmada por responsavel humano. |
| ACT-0004 | P0 | ambiente | responsavel tecnico | Campo de identificacao pendente: Versao alvo do n8n. | Preencher somente com informacao confirmada por responsavel humano. |
| ACT-0005 | P0 | ambiente | responsavel tecnico | Campo de identificacao pendente: Responsavel tecnico. | Preencher somente com informacao confirmada por responsavel humano. |
| ACT-0006 | P0 | ambiente | responsavel tecnico | Campo de identificacao pendente: Responsavel pela aprovacao humana. | Preencher somente com informacao confirmada por responsavel humano. |
| ACT-0007 | P1 | manifesto | responsavel pela aprovacao humana | Gates do manifesto ainda nao marcados. | Preencher e aprovar itens obrigatorios antes da janela. |
| ACT-0008 | P1 | checklist | responsavel tecnico | Checklist operacional contem itens nao marcados. | Preencher e aprovar itens obrigatorios antes da janela. |
| ACT-0009 | P1 | matriz | responsavel tecnico | Matriz de evidencias contem evidencias pendentes. | Preencher e aprovar itens obrigatorios antes da janela. |
| ACT-0010 | P1 | ata | responsavel pela aprovacao humana | Modelo de ata contem campos pendentes. | Preencher e aprovar itens obrigatorios antes da janela. |
| ACT-0011 | P2 | workflow | responsavel tecnico | Workflow alvo contem referencias credentials placeholder. | Confirmar no n8n que nenhuma credencial real foi vinculada automaticamente. |

## Observacoes

- Plano gerado localmente a partir do relatorio de prontidao.
- O plano nao preenche campos operacionais por inferencia.
- Este plano nao autoriza importacao, exportacao ou execucao no n8n.
