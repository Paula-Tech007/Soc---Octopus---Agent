# Criterios Para Comparacao Automatizada n8n

## Objetivo

Definir criterios para a ferramenta local de comparacao entre um workflow n8n aprovado no projeto e uma exportacao futura do n8n.

A implementacao local fica em:

```text
06-tests/07-comparador-workflow-n8n.py
```

Este documento nao autoriza importacao, exportacao ou execucao de n8n.

## Entradas

Entrada obrigatoria 1:

```text
02-workflows-n8n/soc-octopus-prototipo-mock.json
```

Entrada obrigatoria 2:

```text
Exportacao futura do workflow importado em laboratorio n8n aprovado.
```

A segunda entrada so deve ser usada quando houver exportacao futura aprovada e documentada.

## Principios

- Comparacao deve ser local.
- Comparacao nao deve acessar rede.
- Comparacao nao deve executar n8n.
- Comparacao nao deve alterar os arquivos comparados.
- Comparacao deve produzir relatorio revisavel por humano.
- Divergencias bloqueantes devem impedir proxima etapa.
- Campos internos do n8n devem ser classificados antes de qualquer normalizacao.

## Campos Criticos

Divergencias nos campos abaixo devem ser avaliadas com rigor:

- `active`
- `nodes`
- `nodes[].name`
- `nodes[].type`
- `nodes[].typeVersion`
- `nodes[].parameters`
- `connections`
- `settings`
- `pinData`
- `staticData`
- `meta`
- `credentials`

## Divergencias Bloqueantes

Devem bloquear a proxima etapa:

- `active` diferente de `false`.
- Presenca de `credentials`.
- Presenca de URL externa.
- Presenca de node externo nao aprovado.
- Presenca de node HTTP, webhook, banco, Redis, e-mail, mensageria, Code ou Function.
- Alteracao de `connections` que mude o fluxo linear aprovado.
- Ausencia de node esperado.
- Inclusao de node nao esperado.
- Alteracao de parametro que mude semantica do fluxo mockado.
- Presenca de `pinData` ou `staticData` com dados de execucao.
- Presenca de dado real ou sensivel.

## Divergencias Que Requerem Revisao

Devem exigir revisao humana:

- Campo interno adicionado pelo n8n.
- Identificador interno novo.
- Mudanca de posicao visual.
- Mudanca automatica de `typeVersion`.
- Reordenacao de campos com possivel impacto.
- Alteracao de metadados sem impacto evidente.
- Campo vazio convertido entre `null`, `{}` ou `[]`.

## Divergencias Aceitaveis Com Registro

Podem ser aceitas somente com registro:

- Reordenacao de propriedades JSON sem mudanca semantica.
- Formatacao diferente.
- Metadado interno sem impacto funcional confirmado.
- Campo vazio equivalente confirmado.
- Diferenca visual que nao altere nodes, conexoes ou parametros.

## Normalizacao Permitida Para Comparacao

A ferramenta futura podera normalizar apenas para fins de comparacao:

- Ordem de propriedades JSON.
- Espacamento e formatacao.
- Campos internos explicitamente classificados como aceitaveis.
- Representacao equivalente de campos vazios, quando aprovada.

Normalizacao nao deve sobrescrever arquivos originais.

## Saida Esperada Da Ferramenta Local

Formato minimo esperado:

```text
status: aprovado | aprovado_com_ressalvas | bloqueado
arquivo_base:
arquivo_comparado:
total_divergencias:
divergencias_bloqueantes:
divergencias_requerem_revisao:
divergencias_aceitaveis_com_registro:
decisao_recomendada:
```

## Relatorio De Divergencias

Cada divergencia deve registrar:

- Identificador.
- Caminho JSON do campo.
- Valor no workflow aprovado.
- Valor na exportacao futura.
- Classificacao.
- Justificativa.
- Acao recomendada.

## Criterios De Aceitacao

A comparacao futura so pode ser considerada aprovada se:

- Nao houver divergencia bloqueante.
- Todas as divergencias de revisao forem avaliadas por humano.
- Todas as divergencias aceitas forem registradas.
- Workflow permanecer inativo.
- Nao houver credenciais.
- Nao houver execucao.
- Nao houver dados reais.

## Criterios De Bloqueio

Bloquear a proxima etapa se:

- Houver divergencia bloqueante.
- Houver divergencia nao classificada.
- A exportacao futura nao for JSON valido.
- A origem da exportacao nao estiver documentada.
- A versao alvo do n8n nao estiver registrada.
- O ambiente de laboratorio nao estiver aprovado.
- O responsavel humano nao aprovar o resultado.

## Fora De Escopo Da Ferramenta Local

A ferramenta futura nao deve:

- Importar workflow.
- Exportar workflow.
- Executar workflow.
- Chamar n8n.
- Chamar APIs externas.
- Criar credenciais.
- Alterar workflow aprovado.
- Alterar exportacao futura.
- Decidir sozinha por ajuste funcional.

## Proxima Revisao

Revisar estes criterios antes de usar o comparador contra exportacao real do n8n.
