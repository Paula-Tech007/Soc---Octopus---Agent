# Plano De Evidencias E Comparacao Pos-importacao n8n

## Objetivo

Definir como registrar evidencias e comparar uma futura importacao controlada do workflow mockado no n8n.

Este documento nao autoriza instalacao, importacao, exportacao, execucao, criacao de credenciais ou chamadas externas.

## Artefatos De Referencia

Workflow aprovado:

```text
02-workflows-n8n/soc-octopus-prototipo-mock.json
```

Documentos obrigatorios antes da importacao:

```text
01-docs/61-checklist-operacional-importacao-n8n.md
01-docs/64-registro-decisao-versao-n8n.md
01-docs/67-criterios-ambiente-laboratorio-n8n.md
01-docs/73-modelo-ata-janela-laboratorio-n8n.md
01-docs/76-criterios-comparacao-automatizada-futura-n8n.md
01-docs/82-guia-comparador-workflow-n8n.md
01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md
01-docs/86-roteiro-janela-laboratorio-n8n.md
01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md
```

## Principios

- Toda evidencia deve ser registrada sem dados reais.
- O workflow deve permanecer inativo.
- A importacao nao deve criar nem vincular credenciais.
- A exportacao futura deve ser usada apenas para comparacao.
- Divergencias devem ser registradas antes de qualquer ajuste.
- Ajustes no workflow devem ocorrer somente em fase separada e aprovada.

## Evidencias Antes Da Importacao

Registrar antes de qualquer importacao futura:

- Data e hora planejadas.
- Responsavel tecnico.
- Responsavel pela aprovacao humana.
- Ambiente de laboratorio.
- Versao alvo do n8n registrada.
- Resultado do validador estatico local.
- Caminho do workflow aprovado.
- Confirmacao de `active=false`.
- Confirmacao de ausencia de credenciais.
- Confirmacao de ausencia de URLs e nodes externos.
- Matriz de evidencias preparada.
- Roteiro de janela revisado.
- Plano de rollback.
- Ata da janela preparada.

## Evidencias Durante A Importacao

Registrar durante a importacao futura:

- Arquivo importado.
- Usuario responsavel pela importacao.
- Alertas ou mensagens exibidas pela interface.
- Identificador interno atribuido pelo n8n, se houver.
- Confirmacao de que nenhuma credencial foi selecionada.
- Confirmacao de que o workflow nao foi ativado.
- Confirmacao de que o workflow nao foi executado.

## Evidencias Apos A Importacao

Registrar apos a importacao futura:

- Estado final do workflow: ativo ou inativo.
- Quantidade de nodes importados.
- Lista de nomes dos nodes importados.
- Tipos dos nodes importados.
- Estado das conexoes.
- Presenca ou ausencia de credenciais vinculadas.
- Presenca ou ausencia de execucoes.
- Presenca ou ausencia de nodes externos.
- Divergencias visuais observadas.
- Decisao final da janela.
- Ata da janela preenchida e encerrada.

## Comparacao Com Exportacao Futura

Se houver aprovacao para exportar novamente o workflow importado, comparar a exportacao futura com o JSON aprovado.

A ferramenta local aprovada para essa comparacao e:

```text
06-tests/07-comparador-workflow-n8n.py
```

Ela deve seguir:

```text
01-docs/76-criterios-comparacao-automatizada-futura-n8n.md
```

Relatorios esperados:

```text
06-tests/08-relatorio-comparacao-workflow-n8n.json
06-tests/09-resumo-comparacao-workflow-n8n.md
```

Comparar:

- `active`.
- `nodes[].name`.
- `nodes[].type`.
- `nodes[].typeVersion`.
- `nodes[].parameters`.
- `connections`.
- `settings`.
- `pinData`.
- `staticData`.
- `meta`.
- Presenca de `credentials`.

## Classificacao De Divergencias

### Bloqueante

- Workflow exportado aparece ativo.
- Campo `credentials` aparece.
- Node externo aparece.
- URL externa aparece.
- Execucao foi registrada.
- Node de codigo, banco, Redis, HTTP, webhook ou mensageria aparece.
- Dado real aparece.

### Requer Revisao

- n8n adiciona campo interno nao presente no JSON original.
- Posicao visual de node muda.
- Ordem de propriedades muda.
- Identificador interno e adicionado.
- Versao do node e ajustada automaticamente.

### Aceitavel Com Registro

- Metadado interno sem impacto funcional.
- Diferenca de formatacao.
- Campo vazio equivalente.
- Reordenacao de propriedades sem alteracao semantica.

## Criterios De Aceitacao

Uma importacao futura so pode ser considerada aceitavel se:

- Workflow permanecer inativo.
- Nenhuma credencial for criada ou vinculada.
- Nenhuma execucao for realizada.
- Nenhum node externo for adicionado.
- Todas as divergencias forem registradas.
- Divergencias bloqueantes forem ausentes.
- Revisao humana aprovar o resultado.

## Criterios De Rollback

Remover o workflow importado ou bloquear a janela se:

- Houver divergencia bloqueante.
- Houver execucao acidental.
- Houver credencial vinculada.
- Houver dado real.
- Houver chamada externa.
- O responsavel nao conseguir confirmar o estado inativo.

## Saida Esperada

Ao final de uma futura janela aprovada, deve existir registro suficiente para responder:

- O que foi importado.
- Onde foi importado.
- Quem importou.
- Qual versao do n8n foi usada.
- Se o workflow permaneceu inativo.
- Se houve credenciais.
- Se houve execucao.
- Quais divergencias foram encontradas.
- Qual foi a decisao final.

Sem essas evidencias, a proxima etapa deve permanecer bloqueada.
