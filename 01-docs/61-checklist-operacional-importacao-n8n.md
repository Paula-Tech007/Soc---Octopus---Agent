# Checklist Operacional Para Importacao n8n Controlada

## Objetivo

Orientar uma futura importacao manual e controlada do workflow mockado em uma instancia n8n de laboratorio, sem credenciais e sem integracoes externas.

Este documento e preparatorio. Ele nao autoriza importacao, execucao, instalacao ou criacao de credenciais.

## Artefato Alvo

```text
02-workflows-n8n/soc-octopus-prototipo-mock.json
```

## Pre-condicoes Bloqueantes

Todos os itens abaixo devem estar aprovados antes de qualquer importacao real:

- [ ] Aprovacao humana explicita para importar workflow.
- [ ] Versao alvo do n8n definida e registrada.
- [ ] Registro `01-docs/64-registro-decisao-versao-n8n.md` preenchido e aprovado.
- [ ] Criterios de `01-docs/67-criterios-ambiente-laboratorio-n8n.md` atendidos.
- [ ] Plano `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md` revisado.
- [ ] Ata baseada em `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` preparada.
- [ ] Manifesto `01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md` revisado.
- [ ] Roteiro `01-docs/86-roteiro-janela-laboratorio-n8n.md` revisado.
- [ ] Matriz `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md` preparada.
- [ ] Ambiente n8n isolado, nao produtivo e sem dados reais.
- [ ] Usuario responsavel pela janela de teste definido.
- [ ] Janela de teste documentada.
- [ ] Workflow revisado e mantido com `active=false`.
- [ ] Validador estatico local executado sem falhas.
- [ ] Ausencia de credenciais confirmada no JSON.
- [ ] Ausencia de URLs, chamadas externas e nodes externos confirmada.
- [ ] Plano de rollback definido: excluir workflow importado se houver desvio.

## Proibido Nesta Importacao

- Criar credenciais.
- Vincular credenciais.
- Executar workflow.
- Ativar workflow.
- Adicionar HTTP Request.
- Adicionar Webhook.
- Adicionar banco de dados.
- Adicionar Redis.
- Adicionar e-mail, Telegram, WhatsApp ou mensageria.
- Adicionar Code node ou Function node.
- Usar dados reais.
- Usar dados de cliente.
- Chamar APIs externas.
- Persistir memoria corporativa.

## Conferencia Antes Da Importacao

- [ ] Conferir arquivo alvo.
- [ ] Conferir que o arquivo esta sob `02-workflows-n8n`.
- [ ] Conferir `active=false`.
- [ ] Conferir `meta.mock_only=true`.
- [ ] Conferir `meta.contains_credentials=false`.
- [ ] Conferir `meta.contains_external_integrations=false`.
- [ ] Conferir `pinData` vazio.
- [ ] Conferir `staticData=null`.
- [ ] Conferir nodes permitidos: `manualTrigger` e `set`.
- [ ] Conferir que todos os nodes possuem notas indicando uso mockado.

## Conferencia Durante A Importacao

- [ ] Importar somente o arquivo mockado aprovado.
- [ ] Nao selecionar credenciais.
- [ ] Nao criar conexoes externas.
- [ ] Nao ativar o workflow apos importacao.
- [ ] Nao executar o workflow durante a importacao.
- [ ] Registrar o identificador interno atribuido pelo n8n, se houver.
- [ ] Registrar qualquer alerta visual exibido pela interface.
- [ ] Registrar acoes na ata da janela.

## Conferencia Apos A Importacao

- [ ] Confirmar que o workflow esta inativo.
- [ ] Confirmar que nenhum node possui credencial vinculada.
- [ ] Confirmar que nao ha nodes externos adicionados automaticamente.
- [ ] Confirmar que nenhuma execucao foi disparada.
- [ ] Confirmar que os oito nodes esperados foram importados.
- [ ] Confirmar que as conexoes continuam lineares.
- [ ] Exportar novamente o workflow importado para comparacao futura, se aprovado.
- [ ] Comparar exportacao futura conforme plano de evidencias, se exportacao for aprovada.
- [ ] Registrar divergencias para revisao humana antes de qualquer ajuste.
- [ ] Encerrar a ata com decisao final e pendencias.

## Criterios De Abortagem

Abortar a importacao ou remover o workflow importado se ocorrer qualquer item abaixo:

- Workflow aparecer como ativo.
- Credencial for solicitada ou vinculada.
- Node externo aparecer no fluxo.
- Execucao for disparada sem aprovacao.
- Dado real for identificado.
- Campo sensivel for identificado.
- Interface indicar comportamento inesperado que nao esteja documentado.

## Evidencias A Registrar

- Data e hora da importacao.
- Responsavel pela importacao.
- Versao alvo do n8n.
- Hash ou identificador do arquivo importado, se disponivel.
- Resultado do validador local antes da importacao.
- Resultado visual da importacao.
- Divergencias encontradas.
- Decisao final: manter importado inativo, remover, ou bloquear para revisao.

## Saida Esperada

Resultado aceitavel:

- Workflow importado apenas em ambiente de laboratorio.
- Workflow permanece inativo.
- Nenhuma credencial criada ou vinculada.
- Nenhuma execucao realizada.
- Nenhuma chamada externa configurada.
- Divergencias registradas para revisao humana.

Qualquer resultado diferente deve bloquear a proxima etapa.
