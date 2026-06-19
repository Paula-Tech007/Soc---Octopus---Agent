# Roteiro De Janela De Laboratorio n8n

## Objetivo

Definir uma sequencia operacional para uma futura janela de laboratorio n8n, mantendo importacao, exportacao e execucao como aprovacoes separadas.

Este roteiro nao autoriza a janela. Ele deve ser usado somente quando houver aprovacao humana especifica.

## Principios

- Executar somente o escopo aprovado.
- Usar apenas ambiente de laboratorio isolado.
- Usar apenas dados mockados.
- Manter workflow inativo.
- Nao criar nem vincular credenciais.
- Registrar toda divergencia antes de qualquer ajuste.
- Cancelar a janela se um criterio bloqueante aparecer.

## Etapa 0 - Antes De Abrir A Janela

| Passo | Acao | Evidencia |
| --- | --- | --- |
| 0.1 | Confirmar aprovacao humana para a janela | Ata preenchida |
| 0.2 | Confirmar versao alvo do n8n | `01-docs/64-registro-decisao-versao-n8n.md` |
| 0.3 | Confirmar laboratorio isolado | `01-docs/67-criterios-ambiente-laboratorio-n8n.md` |
| 0.4 | Executar validador estatico local | `06-tests/06-resumo-validacao-estatica.md` |
| 0.5 | Preencher matriz de evidencias | `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md` |
| 0.6 | Confirmar plano de rollback | Ata da janela |
| 0.7 | Executar validador de prontidao da janela | `06-tests/12-resumo-prontidao-janela-n8n.md` |

Se qualquer passo falhar, a janela deve permanecer bloqueada.

## Etapa 1 - Inicio Da Janela

| Passo | Acao | Resultado Esperado |
| --- | --- | --- |
| 1.1 | Registrar horario de inicio | Horario anotado na ata |
| 1.2 | Registrar responsaveis presentes | Responsaveis anotados |
| 1.3 | Confirmar escopo aprovado | Itens aprovados marcados |
| 1.4 | Confirmar itens proibidos | Restricoes lidas e aceitas |
| 1.5 | Confirmar que execucao nao esta aprovada por padrao | Execucao bloqueada |

## Etapa 2 - Importacao Se Aprovada

Esta etapa so pode ocorrer se a importacao tiver aprovacao explicita.

| Passo | Acao | Resultado Esperado |
| --- | --- | --- |
| 2.1 | Selecionar somente workflow aprovado | Arquivo correto selecionado |
| 2.2 | Importar sem selecionar credenciais | Nenhuma credencial vinculada |
| 2.3 | Nao ativar workflow | Workflow permanece inativo |
| 2.4 | Nao executar workflow | Nenhuma execucao registrada |
| 2.5 | Registrar mensagens da interface | Evidencias anotadas |
| 2.6 | Registrar identificador interno se existir | Identificador documentado |

## Etapa 3 - Conferencia Pos-importacao

| Passo | Acao | Resultado Esperado |
| --- | --- | --- |
| 3.1 | Confirmar workflow inativo | `active=false` ou estado visual equivalente |
| 3.2 | Confirmar ausencia de credenciais | Nenhuma credencial vinculada |
| 3.3 | Confirmar ausencia de execucoes | Nenhuma execucao registrada |
| 3.4 | Confirmar nodes esperados | Nodes mockados presentes |
| 3.5 | Confirmar conexoes lineares | Fluxo preservado |
| 3.6 | Confirmar ausencia de nodes externos | Nenhum node externo adicionado |

Qualquer falha deve acionar criterio de abortagem.

## Etapa 4 - Exportacao Se Aprovada

Esta etapa so pode ocorrer se a exportacao tiver aprovacao explicita e separada.

| Passo | Acao | Resultado Esperado |
| --- | --- | --- |
| 4.1 | Confirmar que exportacao esta aprovada | Aprovacao registrada |
| 4.2 | Exportar workflow importado | Arquivo exportado para comparacao |
| 4.3 | Registrar origem da exportacao | Origem anotada na ata |
| 4.4 | Confirmar que exportacao nao contem dados reais | Evidencia registrada |

## Etapa 5 - Comparacao Se Exportacao Existir

Usar o comparador local somente se houver arquivo exportado aprovado.

Comando de referencia:

```text
python 06-tests/07-comparador-workflow-n8n.py --base 02-workflows-n8n/soc-octopus-prototipo-mock.json --candidate caminho/do/workflow-exportado.json --write-report 06-tests/08-relatorio-comparacao-workflow-n8n.json --write-markdown 06-tests/09-resumo-comparacao-workflow-n8n.md
```

Resultado esperado:

- Sem divergencias bloqueantes.
- Divergencias de revisao registradas.
- Divergencias aceitas documentadas.
- Decisao humana registrada.

## Etapa 6 - Encerramento

| Passo | Acao | Resultado Esperado |
| --- | --- | --- |
| 6.1 | Registrar resultado final | Ata atualizada |
| 6.2 | Registrar divergencias | Tabela de divergencias preenchida |
| 6.3 | Registrar pendencias | Pendencias documentadas |
| 6.4 | Confirmar restricoes finais | Declaracao marcada |
| 6.5 | Definir proxima acao | Aprovada, bloqueada ou rollback |

## Criterios De Abortagem

Abortar e registrar rollback se ocorrer:

- Workflow ficar ativo.
- Credencial for solicitada ou vinculada.
- Execucao ocorrer sem aprovacao especifica.
- Dado real aparecer.
- Node externo aparecer.
- URL externa aparecer.
- Conexao externa for exigida.
- Responsavel nao conseguir confirmar estado seguro.

## Resultado Aceitavel

Uma janela futura so pode ser considerada aceitavel se:

- O escopo aprovado foi respeitado.
- O workflow permaneceu inativo.
- Nenhuma credencial foi criada ou vinculada.
- Nenhuma execucao ocorreu sem aprovacao.
- Nenhum dado real foi usado.
- Divergencias foram registradas.
- A decisao final foi aprovada por humano.
