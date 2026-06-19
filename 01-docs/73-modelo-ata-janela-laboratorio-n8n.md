# Modelo De Ata - Janela De Laboratorio n8n

## Objetivo

Padronizar o registro de uma futura janela de laboratorio n8n relacionada ao workflow mockado do SOC-Octopus-Agent.

Este modelo nao autoriza instalacao, importacao, exportacao, execucao, criacao de credenciais ou chamadas externas.

## Identificacao Da Janela

| Campo | Valor |
| --- | --- |
| Identificador da janela | Pendente |
| Data planejada | Pendente |
| Hora de inicio planejada | Pendente |
| Hora de fim planejada | Pendente |
| Ambiente de laboratorio | Pendente |
| Versao alvo do n8n | Pendente |
| Workflow alvo | `02-workflows-n8n/soc-octopus-prototipo-mock.json` |
| Objetivo da janela | Pendente |
| Status da aprovacao humana | Pendente |

## Responsaveis

| Papel | Nome | Contato | Aprovacao |
| --- | --- | --- | --- |
| Responsavel tecnico | Pendente | Pendente | Pendente |
| Responsavel pela aprovacao humana | Pendente | Pendente | Pendente |
| Observador ou revisor | Pendente | Pendente | Pendente |

## Escopo Aprovado

Marcar somente os itens aprovados para a janela futura:

- [ ] Validar documentacao.
- [ ] Revisar checklist operacional.
- [ ] Importar workflow mockado.
- [ ] Exportar workflow importado para comparacao.
- [ ] Comparar exportacao com JSON aprovado.
- [ ] Registrar divergencias.

Itens nao aprovados permanecem proibidos.

## Fora De Escopo

- Executar workflow.
- Ativar workflow.
- Criar credenciais.
- Vincular credenciais.
- Usar dados reais.
- Chamar APIs externas.
- Adicionar nodes externos.
- Alterar workflow durante a janela.
- Integrar banco, Redis, e-mail, mensageria ou IA.

## Pre-condicoes

| Item | Status | Evidencia |
| --- | --- | --- |
| Registro de decisao da versao n8n aprovado | Pendente | `01-docs/64-registro-decisao-versao-n8n.md` |
| Criterios de laboratorio atendidos | Pendente | `01-docs/67-criterios-ambiente-laboratorio-n8n.md` |
| Checklist operacional revisado | Pendente | `01-docs/61-checklist-operacional-importacao-n8n.md` |
| Plano de evidencias revisado | Pendente | `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md` |
| Criterios de comparacao futura revisados | Pendente | `01-docs/76-criterios-comparacao-automatizada-futura-n8n.md` |
| Manifesto do pacote operacional revisado | Pendente | `01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md` |
| Roteiro da janela revisado | Pendente | `01-docs/86-roteiro-janela-laboratorio-n8n.md` |
| Matriz de evidencias preparada | Pendente | `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md` |
| Validador local sem falhas | Pendente | `06-tests/06-resumo-validacao-estatica.md` |
| Plano de rollback definido | Pendente | Campo abaixo |

## Plano De Rollback

Descrever como desfazer a importacao futura se houver desvio:

```text
Pendente.
```

## Evidencias Antes Da Janela

| Evidencia | Status | Observacao |
| --- | --- | --- |
| Workflow aprovado localizado | Pendente |  |
| `active=false` confirmado | Pendente |  |
| Ausencia de credenciais confirmada | Pendente |  |
| Ausencia de URLs confirmada | Pendente |  |
| Ambiente isolado confirmado | Pendente |  |
| Dados reais ausentes | Pendente |  |

## Registro Durante A Janela

| Horario | Acao | Responsavel | Resultado | Observacao |
| --- | --- | --- | --- | --- |
| Pendente | Pendente | Pendente | Pendente | Pendente |

## Evidencias Apos A Janela

| Evidencia | Status | Observacao |
| --- | --- | --- |
| Workflow permaneceu inativo | Pendente |  |
| Nenhuma credencial vinculada | Pendente |  |
| Nenhuma execucao registrada | Pendente |  |
| Oito nodes esperados presentes | Pendente |  |
| Conexoes lineares preservadas | Pendente |  |
| Nodes externos ausentes | Pendente |  |
| Divergencias registradas | Pendente |  |
| Criterios de comparacao futura aplicados quando aprovados | Pendente |  |

## Divergencias Encontradas

| ID | Tipo | Descricao | Severidade | Decisao |
| --- | --- | --- | --- | --- |
| Pendente | Pendente | Pendente | Pendente | Pendente |

Severidades sugeridas:

- `bloqueante`
- `requer_revisao`
- `aceitavel_com_registro`

## Decisoes Da Janela

| Decisao | Responsavel | Justificativa | Proxima Acao |
| --- | --- | --- | --- |
| Pendente | Pendente | Pendente | Pendente |

## Resultado Final

Selecionar uma opcao ao encerrar a janela futura:

- [ ] Aprovado sem divergencias bloqueantes.
- [ ] Aprovado com divergencias registradas.
- [ ] Bloqueado para revisao.
- [ ] Rollback executado.
- [ ] Janela cancelada.

## Pendencias

| Pendencia | Responsavel | Prazo | Observacao |
| --- | --- | --- | --- |
| Pendente | Pendente | Pendente | Pendente |

## Declaracao De Restricoes

Confirmar ao final:

- [ ] Nenhum dado real foi usado.
- [ ] Nenhuma credencial foi criada.
- [ ] Nenhuma credencial foi vinculada.
- [ ] Nenhuma execucao foi realizada sem aprovacao.
- [ ] Nenhuma chamada externa foi configurada.
- [ ] Nenhum ajuste foi feito fora de fase aprovada.

## Encerramento

| Campo | Valor |
| --- | --- |
| Responsavel pelo encerramento | Pendente |
| Data e hora de encerramento | Pendente |
| Status final | Pendente |
| Aprovacao para proxima etapa | Pendente |
