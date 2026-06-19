# Matriz De Evidencias Da Janela De Laboratorio n8n

## Objetivo

Organizar as evidencias necessarias para uma futura janela de laboratorio n8n.

Esta matriz nao autoriza importacao, exportacao, execucao, instalacao, criacao de credenciais ou chamadas externas.

## Identificacao

| Campo | Valor |
| --- | --- |
| Projeto | SOC-Octopus-Agent |
| Janela | Pendente |
| Ambiente | Pendente |
| Versao alvo do n8n | Pendente |
| Responsavel tecnico | Pendente |
| Responsavel pela aprovacao humana | Pendente |
| Workflow alvo | `02-workflows-n8n/soc-octopus-prototipo-mock.json` |
| Status da matriz | Preparada para preenchimento futuro |

## Evidencias Antes Da Janela

| ID | Evidencia | Fonte Esperada | Status | Observacao |
| --- | --- | --- | --- | --- |
| PRE-001 | Aprovacao humana da janela | Ata | Pendente |  |
| PRE-002 | Versao alvo registrada | `01-docs/64-registro-decisao-versao-n8n.md` | Pendente |  |
| PRE-003 | Ambiente isolado confirmado | `01-docs/67-criterios-ambiente-laboratorio-n8n.md` | Pendente |  |
| PRE-004 | Checklist operacional revisado | `01-docs/61-checklist-operacional-importacao-n8n.md` | Pendente |  |
| PRE-005 | Plano de evidencias revisado | `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md` | Pendente |  |
| PRE-006 | Ata preparada | `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` | Pendente |  |
| PRE-007 | Validador local sem falhas | `06-tests/06-resumo-validacao-estatica.md` | Pendente |  |
| PRE-008 | Workflow alvo localizado | `02-workflows-n8n/soc-octopus-prototipo-mock.json` | Pendente |  |
| PRE-009 | `active=false` confirmado | Workflow alvo | Pendente |  |
| PRE-010 | Ausencia de valores secretos confirmada | Workflow alvo e validador | Pendente |  |
| PRE-011 | Perfil do workflow confirmado | Workflow alvo e validador | Pendente | `mock-executable`, `lab-template` ou `prod-template` |
| PRE-014 | Referencias de credenciais placeholder revisadas | Workflow alvo e validador | Pendente | Sem valores secretos |
| PRE-015 | Webhook inativo e autenticacao definida no template | Workflow alvo e validador | Pendente | Obrigatorio para `lab-template` e `prod-template` |
| PRE-012 | Plano de rollback definido | Ata | Pendente |  |
| PRE-013 | Validador de prontidao executado | `06-tests/12-resumo-prontidao-janela-n8n.md` | Pendente |  |

## Evidencias Durante A Janela

Preencher somente se a janela for aprovada.

| ID | Evidencia | Fonte Esperada | Status | Observacao |
| --- | --- | --- | --- | --- |
| DUR-001 | Horario de inicio registrado | Ata | Pendente |  |
| DUR-002 | Escopo aprovado confirmado | Ata | Pendente |  |
| DUR-003 | Arquivo importado registrado | Ata | Pendente |  |
| DUR-004 | Nenhuma credencial selecionada | Evidencia visual ou registro manual | Pendente |  |
| DUR-005 | Workflow nao ativado | Evidencia visual ou registro manual | Pendente |  |
| DUR-006 | Workflow nao executado | Evidencia visual ou registro manual | Pendente |  |
| DUR-007 | Mensagens da interface registradas | Ata | Pendente |  |
| DUR-008 | Identificador interno registrado, se houver | Ata | Pendente |  |

## Evidencias Apos A Importacao

Preencher somente se a importacao for aprovada.

| ID | Evidencia | Fonte Esperada | Status | Observacao |
| --- | --- | --- | --- | --- |
| POS-001 | Workflow permaneceu inativo | Evidencia visual ou registro manual | Pendente |  |
| POS-002 | Nenhuma credencial vinculada | Evidencia visual ou registro manual | Pendente |  |
| POS-003 | Nenhuma execucao registrada | Evidencia visual ou registro manual | Pendente |  |
| POS-004 | Nodes esperados presentes | Evidencia visual ou exportacao aprovada | Pendente |  |
| POS-005 | Conexoes lineares preservadas | Evidencia visual ou exportacao aprovada | Pendente |  |
| POS-006 | Nodes externos ausentes | Evidencia visual ou exportacao aprovada | Pendente |  |
| POS-007 | Divergencias visuais registradas | Ata | Pendente |  |
| POS-008 | Decisao final registrada | Ata | Pendente |  |

## Evidencias De Comparacao

Preencher somente se houver exportacao aprovada.

| ID | Evidencia | Fonte Esperada | Status | Observacao |
| --- | --- | --- | --- | --- |
| CMP-001 | Exportacao aprovada registrada | Ata | Pendente |  |
| CMP-002 | Arquivo exportado identificado | Registro manual | Pendente |  |
| CMP-003 | Comparador local executado | `06-tests/09-resumo-comparacao-workflow-n8n.md` | Pendente |  |
| CMP-004 | Divergencias bloqueantes ausentes | Relatorio do comparador | Pendente |  |
| CMP-005 | Divergencias de revisao avaliadas | Ata | Pendente |  |
| CMP-006 | Divergencias aceitas registradas | Ata | Pendente |  |
| CMP-007 | Decisao humana registrada | Ata | Pendente |  |

## Evidencias De Encerramento

| ID | Evidencia | Fonte Esperada | Status | Observacao |
| --- | --- | --- | --- | --- |
| END-001 | Horario de encerramento registrado | Ata | Pendente |  |
| END-002 | Pendencias registradas | Ata | Pendente |  |
| END-003 | Declaracao de restricoes confirmada | Ata | Pendente |  |
| END-004 | Proxima acao definida | Ata | Pendente |  |
| END-005 | Aprovacao humana final registrada | Ata | Pendente |  |

## Criterios De Bloqueio

Bloquear a janela ou a proxima etapa se:

- Qualquer evidencia `PRE` obrigatoria estiver pendente.
- Houver execucao sem aprovacao especifica.
- Houver credencial real criada ou vinculada sem aprovacao separada.
- Houver workflow ativo sem aprovacao.
- Houver dado real.
- Houver chamada externa.
- Houver divergencia bloqueante no comparador.
- A decisao humana final estiver ausente.

## Observacoes

- Evidencias devem ser registradas sem dados reais.
- Evidencias visuais, se usadas no futuro, devem omitir dados sensiveis.
- Campos pendentes nao devem ser preenchidos por inferencia.
- Este documento deve ser copiado ou referenciado pela ata da janela futura.
