# Fase 33 - Validador Local Do Formulario P0/P1

Data de referencia: 2026-06-17

## Objetivo

Criar uma ferramenta local para validar se o formulario P0/P1 da janela n8n possui informacoes humanas suficientes para serem aplicadas nos documentos de destino.

## Escopo

Artefatos cobertos nesta fase:

- `06-tests/16-validador-formulario-p0-p1-janela-n8n.py`
- `06-tests/17-relatorio-formulario-p0-p1-janela-n8n.json`
- `06-tests/18-resumo-formulario-p0-p1-janela-n8n.md`
- `01-docs/101-checklist-fase-33.md`
- `01-docs/102-guia-validador-formulario-p0-p1-janela-n8n.md`
- Atualizacao do indice mestre.
- Atualizacao da revisao consolidada.
- Atualizacao da especificacao de validadores.
- Atualizacao do guia do validador estatico local.

## Fora De Escopo

Nesta fase nao serao executados:

- Instalacao de n8n.
- Importacao de workflow.
- Exportacao de workflow.
- Execucao de workflow.
- Ativacao de workflow.
- Criacao ou vinculacao de credenciais.
- Chamadas externas.
- SQL.
- Banco.
- Redis.
- IA.
- Integracoes externas.

Nesta fase nao serao preenchidos:

- Versao alvo do n8n.
- Identificador da janela.
- Ambiente de laboratorio.
- Responsavel tecnico.
- Responsavel pela aprovacao humana.
- Ata da janela.
- Matriz de evidencias.
- Checklist operacional real.

## Decisao Tecnica

O validador do formulario P0/P1:

- Usa apenas biblioteca padrao do Python.
- Le somente o formulario Markdown local.
- Verifica se secoes obrigatorias existem.
- Verifica campos P0 e P1 com valor confirmado e fonte/evidencia.
- Verifica se ha escopo aprovado para a proxima acao.
- Verifica se restricoes proibitivas continuam registradas.
- Verifica se os comandos de validacao apos preenchimento estao presentes.
- Retorna codigo diferente de zero quando o formulario permanece `bloqueado`.

## Resultado Inicial

Resultado esperado no estado atual:

```text
status: bloqueado
aprovados: 9
pendentes: 21
bloqueantes: 0
avisos: 0
```

O bloqueio e esperado porque o formulario ainda contem campos pendentes e nao ha escopo aprovado para a proxima acao.

## Criterio De Saida Da Fase 33

- Validador local do formulario criado.
- Relatorio JSON gerado.
- Resumo Markdown gerado.
- Guia de uso criado.
- Especificacao de validadores atualizada.
- Guia do validador estatico local atualizado.
- Indice mestre atualizado.
- Validador estatico local executado.
- Projeto pausado aguardando respostas humanas para o formulario P0/P1.
