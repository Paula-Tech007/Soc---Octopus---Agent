# Guia Do Comparador Local De Workflow n8n

## Arquivo

```text
06-tests/07-comparador-workflow-n8n.py
```

## Objetivo

Comparar localmente um workflow n8n aprovado contra outro arquivo JSON de workflow, classificando divergencias para revisao humana.

O comparador nao chama rede, nao executa n8n, nao importa workflow, nao exporta workflow, nao cria credenciais e nao altera os arquivos comparados.

## Entradas

Entrada base:

```text
--base 02-workflows-n8n/soc-octopus-prototipo-mock.json
```

Entrada comparada:

```text
--candidate caminho/do/workflow-exportado.json
```

Os caminhos devem ficar dentro do diretorio do projeto.

## Execucao Basica

Na raiz do projeto:

```text
python 06-tests/07-comparador-workflow-n8n.py --base 02-workflows-n8n/soc-octopus-prototipo-mock.json --candidate 02-workflows-n8n/soc-octopus-prototipo-mock.json
```

## Geracao De Relatorios

Para gerar relatorio JSON e resumo Markdown:

```text
python 06-tests/07-comparador-workflow-n8n.py --base 02-workflows-n8n/soc-octopus-prototipo-mock.json --candidate 02-workflows-n8n/soc-octopus-prototipo-mock.json --write-report 06-tests/08-relatorio-comparacao-workflow-n8n.json --write-markdown 06-tests/09-resumo-comparacao-workflow-n8n.md
```

## Saida

O relatorio informa:

- `status`: `aprovado`, `aprovado_com_ressalvas` ou `bloqueado`.
- `arquivo_base`.
- `arquivo_comparado`.
- `total_divergencias`.
- `divergencias_bloqueantes`.
- `divergencias_requerem_revisao`.
- `divergencias_aceitaveis_com_registro`.
- `decisao_recomendada`.
- Lista detalhada de divergencias.

## Classificacoes

### Bloqueante

Impede a proxima etapa.

Exemplos:

- Workflow comparado ativo.
- Presenca de `credentials`.
- URL externa.
- Node nao aprovado.
- Alteracao de conexoes.
- Inclusao ou ausencia de node.
- Alteracao de parametros.
- Dados de execucao em `pinData` ou `staticData`.

### Requer Revisao

Exige avaliacao humana antes de aceite.

Exemplos:

- Mudanca de `typeVersion`.
- Mudanca de posicao visual.
- Identificador interno alterado.
- Metadado alterado.
- Campo top-level novo.

### Aceitavel Com Registro

Pode ser aceito se registrado.

Exemplos:

- Campo vazio equivalente entre `null`, `{}` ou `[]`.
- Diferenca sem impacto funcional confirmada por humano.

## Politica De Retorno

- `bloqueado`: codigo de retorno diferente de zero.
- `aprovado_com_ressalvas`: codigo de retorno zero.
- `aprovado`: codigo de retorno zero.

## Resultado De Referencia Da Fase 27

Comparacao executada:

```text
base: 02-workflows-n8n/soc-octopus-prototipo-mock.json
candidate: 02-workflows-n8n/soc-octopus-prototipo-mock.json
```

Resultado:

```text
status: aprovado
total_divergencias: 0
divergencias_bloqueantes: 0
divergencias_requerem_revisao: 0
divergencias_aceitaveis_com_registro: 0
```

## Limites Conhecidos

- A ferramenta faz comparacao estatica de JSON.
- A ferramenta nao valida compatibilidade real com uma instancia n8n.
- A ferramenta nao substitui a revisao humana.
- A ferramenta nao substitui a ata de janela de laboratorio.
- A origem de uma exportacao futura deve ser documentada separadamente.
