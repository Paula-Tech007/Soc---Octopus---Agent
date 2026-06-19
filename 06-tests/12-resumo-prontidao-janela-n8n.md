# Resumo Da Prontidao Da Janela n8n

## Status Consolidado

| Campo | Valor |
| --- | --- |
| Projeto | SOC-Octopus-Agent |
| Status | bloqueado |
| Percentual estimado | 65% |
| Gerado em | 2026-06-19T20:23:28.576036+00:00 |
| Validador | 06-tests/10-validador-prontidao-janela-n8n.py |

## Totais

| Metrica | Total |
| --- | ---: |
| Aprovados | 20 |
| Pendentes | 10 |
| Bloqueantes | 0 |
| Avisos | 1 |
| Total | 31 |

## Decisao Recomendada

- Nao abrir janela de laboratorio. Resolver pendencias bloqueantes e registrar aprovacao humana antes de qualquer acao no n8n.

## Checagens

| ID | Categoria | Status | Checagem | Acao Recomendada |
| --- | --- | --- | --- | --- |
| RDY-0001 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/30-backlog-gates-decisao.md | Nenhuma acao. |
| RDY-0002 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/61-checklist-operacional-importacao-n8n.md | Nenhuma acao. |
| RDY-0003 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/64-registro-decisao-versao-n8n.md | Nenhuma acao. |
| RDY-0004 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/67-criterios-ambiente-laboratorio-n8n.md | Nenhuma acao. |
| RDY-0005 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md | Nenhuma acao. |
| RDY-0006 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/73-modelo-ata-janela-laboratorio-n8n.md | Nenhuma acao. |
| RDY-0007 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/76-criterios-comparacao-automatizada-futura-n8n.md | Nenhuma acao. |
| RDY-0008 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/82-guia-comparador-workflow-n8n.md | Nenhuma acao. |
| RDY-0009 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md | Nenhuma acao. |
| RDY-0010 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/86-roteiro-janela-laboratorio-n8n.md | Nenhuma acao. |
| RDY-0011 | artefatos | aprovado | Artefato obrigatorio encontrado: 01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md | Nenhuma acao. |
| RDY-0012 | artefatos | aprovado | Artefato obrigatorio encontrado: 02-workflows-n8n/soc-octopus-prototipo-mock.json | Nenhuma acao. |
| RDY-0013 | artefatos | aprovado | Artefato obrigatorio encontrado: 06-tests/05-relatorio-validacao-estatica.json | Nenhuma acao. |
| RDY-0014 | artefatos | aprovado | Artefato obrigatorio encontrado: 06-tests/06-resumo-validacao-estatica.md | Nenhuma acao. |
| RDY-0015 | artefatos | aprovado | Artefato obrigatorio encontrado: 06-tests/07-comparador-workflow-n8n.py | Nenhuma acao. |
| RDY-0016 | validacao | aprovado | Validador estatico local sem falhas. | Atualizar novamente antes de qualquer janela real. |
| RDY-0017 | workflow | aprovado | Workflow alvo esta inativo. | Manter workflow inativo na janela futura. |
| RDY-0018 | workflow | aviso | Workflow alvo contem referencias credentials placeholder. | Confirmar no n8n que nenhuma credencial real foi vinculada automaticamente. |
| RDY-0019 | workflow | aprovado | Workflow alvo sem URL externa. | Nenhuma acao. |
| RDY-0020 | workflow | aprovado | Workflow alvo usa apenas tipos de node permitidos. | Nenhuma acao. |
| RDY-0021 | workflow | aprovado | Webhook com autenticacao configurada: 01 - Webhook Ingress Production. | Confirmar credencial correta no n8n antes de qualquer ativacao. |
| RDY-0022 | decisao | pendente | Versao alvo do n8n ainda nao esta decidida. | Preencher e aprovar registro de decisao da versao alvo. |
| RDY-0023 | ambiente | pendente | Campo de identificacao pendente: Janela. | Preencher somente com informacao confirmada por responsavel humano. |
| RDY-0024 | ambiente | pendente | Campo de identificacao pendente: Ambiente. | Preencher somente com informacao confirmada por responsavel humano. |
| RDY-0025 | ambiente | pendente | Campo de identificacao pendente: Versao alvo do n8n. | Preencher somente com informacao confirmada por responsavel humano. |
| RDY-0026 | ambiente | pendente | Campo de identificacao pendente: Responsavel tecnico. | Preencher somente com informacao confirmada por responsavel humano. |
| RDY-0027 | ambiente | pendente | Campo de identificacao pendente: Responsavel pela aprovacao humana. | Preencher somente com informacao confirmada por responsavel humano. |
| RDY-0028 | manifesto | pendente | Gates do manifesto ainda nao marcados. | Preencher e aprovar itens obrigatorios antes da janela. |
| RDY-0029 | checklist | pendente | Checklist operacional contem itens nao marcados. | Preencher e aprovar itens obrigatorios antes da janela. |
| RDY-0030 | matriz | pendente | Matriz de evidencias contem evidencias pendentes. | Preencher e aprovar itens obrigatorios antes da janela. |
| RDY-0031 | ata | pendente | Modelo de ata contem campos pendentes. | Preencher e aprovar itens obrigatorios antes da janela. |

## Observacoes

- Resultado gerado localmente.
- O status bloqueado e esperado enquanto versao, ambiente e aprovacao humana estiverem pendentes.
- Este resumo nao autoriza importacao, exportacao ou execucao no n8n.
