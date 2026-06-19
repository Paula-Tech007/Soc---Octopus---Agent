# Manifesto Do Pacote Operacional De Janela De Laboratorio n8n

## Objetivo

Consolidar os artefatos necessarios para uma futura janela de laboratorio n8n do SOC-Octopus-Agent.

Este manifesto nao autoriza instalacao, importacao, exportacao, execucao, ativacao de workflow, criacao de credenciais ou chamadas externas.

## Status Do Pacote

| Campo | Valor |
| --- | --- |
| Projeto | SOC-Octopus-Agent |
| Tipo de pacote | Preparacao operacional |
| Status | Preparado para revisao humana |
| Data de referencia | 2026-06-16 |
| Importacao autorizada | Nao |
| Exportacao autorizada | Nao |
| Execucao autorizada | Nao |
| Credenciais autorizadas | Nao |
| Dados reais autorizados | Nao |

## Artefatos Obrigatorios

| Artefato | Papel | Status |
| --- | --- | --- |
| `01-docs/30-backlog-gates-decisao.md` | Gates e bloqueios gerais | Existente |
| `01-docs/61-checklist-operacional-importacao-n8n.md` | Checklist operacional | Existente |
| `01-docs/64-registro-decisao-versao-n8n.md` | Registro da versao alvo | Pendente de preenchimento humano |
| `01-docs/67-criterios-ambiente-laboratorio-n8n.md` | Criterios do laboratorio | Existente |
| `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md` | Plano de evidencias | Existente |
| `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` | Modelo de ata | Existente |
| `01-docs/76-criterios-comparacao-automatizada-futura-n8n.md` | Criterios de comparacao | Existente |
| `01-docs/82-guia-comparador-workflow-n8n.md` | Guia do comparador local | Existente |
| `01-docs/86-roteiro-janela-laboratorio-n8n.md` | Roteiro operacional | Criado na Fase 28 |
| `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md` | Matriz de evidencias | Criado na Fase 28 |
| `06-tests/06-resumo-validacao-estatica.md` | Resultado do validador local | Atualizar antes da janela |
| `06-tests/09-resumo-comparacao-workflow-n8n.md` | Resultado do comparador local | Usar somente se houver exportacao aprovada |
| `06-tests/12-resumo-prontidao-janela-n8n.md` | Resultado do validador de prontidao | Atualizar antes da janela |
| `06-tests/15-resumo-plano-pendencias-janela-n8n.md` | Plano de pendencias da janela | Usar para priorizar acoes humanas |

## Artefatos De Workflow

Workflow principal preparado para revisao controlada:

```text
02-workflows-n8n/soc-octopus-prototipo-mock.json
```

Pacote adicional de workflows mockados:

```text
02-workflows-n8n/*.json
```

Os workflows permanecem inativos e usam dados sinteticos ou templates sem valores secretos.
Alguns arquivos ja representam `lab-template` ou `prod-template` e podem conter referencias de credenciais n8n placeholder, Webhook, HTTP, PostgreSQL e Redis.
Essas referencias nao autorizam importacao, vinculacao de credenciais, execucao, ativacao ou chamada externa.

## Gates Antes De Qualquer Janela

Todos os itens abaixo devem estar resolvidos antes de qualquer importacao real:

- [ ] Aprovacao humana explicita para a janela.
- [ ] Versao alvo do n8n registrada.
- [ ] Ambiente de laboratorio identificado.
- [ ] Responsavel tecnico definido.
- [ ] Responsavel pela aprovacao humana definido.
- [ ] Ata preparada.
- [ ] Plano de rollback preenchido.
- [ ] Validador estatico local sem falhas.
- [ ] Ausencia de valores secretos confirmada.
- [ ] Perfis dos workflows confirmados (`mock-executable`, `lab-template`, `prod-template`).
- [ ] Referencias de credenciais placeholder revisadas.
- [ ] Webhooks permanecem inativos e autenticacao esta definida no template.
- [ ] Escopo aprovado separado entre importacao, exportacao e execucao.

## Sequencia De Uso Recomendada

1. Revisar este manifesto.
2. Preencher `01-docs/64-registro-decisao-versao-n8n.md`.
3. Validar ambiente com `01-docs/67-criterios-ambiente-laboratorio-n8n.md`.
4. Preencher `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`.
5. Preparar ata com `01-docs/73-modelo-ata-janela-laboratorio-n8n.md`.
6. Executar `06-tests/10-validador-prontidao-janela-n8n.py`.
7. Gerar plano com `06-tests/13-gerador-plano-pendencias-janela-n8n.py`.
8. Usar `01-docs/86-roteiro-janela-laboratorio-n8n.md` apenas na janela aprovada.
9. Usar o comparador local somente se exportacao futura for aprovada.

## Bloqueios Persistentes

Permanecem bloqueados ate aprovacao explicita:

- Importar workflow.
- Exportar workflow.
- Executar workflow.
- Ativar workflow.
- Criar ou vincular credenciais.
- Criar nodes externos.
- Usar dados reais.
- Chamar APIs externas.
- Alterar workflow durante a janela.
- Instalar dependencias.

## Criterio Para Considerar O Pacote Pronto

O pacote fica pronto para revisao humana quando:

- Todos os artefatos obrigatorios estao localizados.
- O validador local esta sem falhas.
- A matriz de evidencias esta disponivel.
- O roteiro esta disponivel.
- As pendencias bloqueantes estao explicitas.

Esse estado nao equivale a aprovacao para executar a janela.
