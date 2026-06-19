# Guia Do Validador Local Do Formulario P0/P1 Da Janela n8n

## Arquivo

```text
06-tests/16-validador-formulario-p0-p1-janela-n8n.py
```

## Objetivo

Validar localmente se o formulario P0/P1 possui informacoes humanas suficientes para permitir aplicacao controlada nos documentos de destino.

O validador nao chama rede, nao executa n8n, nao importa workflow, nao exporta workflow, nao cria credenciais, nao altera os arquivos avaliados e nao preenche campos operacionais por inferencia.

## Entrada Padrao

```text
01-docs/98-formulario-resolucao-p0-p1-janela-n8n.md
```

## Execucao

Na raiz do projeto:

```text
python 06-tests/16-validador-formulario-p0-p1-janela-n8n.py
```

Para gerar relatorio JSON:

```text
python 06-tests/16-validador-formulario-p0-p1-janela-n8n.py --write-report 06-tests/17-relatorio-formulario-p0-p1-janela-n8n.json
```

Para gerar relatorio JSON e resumo Markdown:

```text
python 06-tests/16-validador-formulario-p0-p1-janela-n8n.py --write-report 06-tests/17-relatorio-formulario-p0-p1-janela-n8n.json --write-markdown 06-tests/18-resumo-formulario-p0-p1-janela-n8n.md
```

## Saida

O validador informa:

- `status`.
- Totais de aprovados, pendentes, bloqueantes e avisos.
- Decisao recomendada.
- Lista de checagens.

## Regras Avaliadas

- Secoes obrigatorias do formulario.
- Campos P0 com valor confirmado e fonte/evidencia.
- Campos P1 com valor confirmado e fonte/evidencia.
- Escopo aprovado para proxima acao.
- Restricoes proibitivas registradas.
- Comandos de validacao apos preenchimento.

## Status

- `bloqueado`: ha campos pendentes, bloqueantes ou escopo ainda nao aprovado.
- `pronto_com_ressalvas`: ha avisos sem pendencias bloqueantes.
- `pronto_para_aplicacao`: formulario sem pendencias detectadas.

## Limites Conhecidos

- O validador nao confirma se a informacao fornecida e verdadeira.
- O validador nao substitui aprovacao humana.
- O validador nao aplica valores nos documentos de destino.
- O validador nao autoriza importacao, exportacao ou execucao no n8n.
