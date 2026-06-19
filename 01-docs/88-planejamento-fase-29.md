# Fase 29 - Validador Local De Prontidao Da Janela n8n

Data de referencia: 2026-06-16

## Objetivo

Implementar uma ferramenta local para avaliar se o pacote operacional da janela de laboratorio n8n esta pronto para revisao humana, mantendo bloqueadas importacao, exportacao e execucao enquanto houver pendencias.

## Escopo

Artefatos cobertos nesta fase:

- `06-tests/10-validador-prontidao-janela-n8n.py`
- `06-tests/11-relatorio-prontidao-janela-n8n.json`
- `06-tests/12-resumo-prontidao-janela-n8n.md`
- `01-docs/89-checklist-fase-29.md`
- `01-docs/90-guia-validador-prontidao-janela-n8n.md`
- Atualizacao do indice mestre.
- Atualizacao da especificacao de validadores.
- Atualizacao do guia do validador estatico local.
- Atualizacao dos documentos operacionais da janela n8n.

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

Nesta fase nao serao alterados:

- Workflows em `02-workflows-n8n`.
- Payloads mockados.
- Prompts.
- SQL planejado.
- Diagramas.

## Decisao Tecnica

O validador de prontidao:

- Usa apenas biblioteca padrao do Python.
- Le documentos e relatorios locais do projeto.
- Verifica artefatos obrigatorios da janela.
- Verifica se o validador estatico local esta sem falhas.
- Verifica se o workflow alvo esta inativo, sem credenciais, sem URLs e com tipos de nodes permitidos.
- Detecta pendencias em versao alvo do n8n, ambiente, responsaveis, ata, checklist e matriz de evidencias.
- Gera relatorio JSON e resumo Markdown.
- Retorna codigo diferente de zero quando o status e `bloqueado`.

## Resultado Inicial

Resultado gerado na Fase 29:

```text
status: bloqueado
percentual_prontidao_estimado: 67%
aprovados: 20
pendentes: 10
bloqueantes: 0
avisos: 0
```

O bloqueio e esperado porque ainda nao ha:

- Versao alvo do n8n decidida.
- Ambiente de laboratorio identificado.
- Janela definida.
- Responsavel tecnico definido.
- Responsavel pela aprovacao humana definido.
- Ata preenchida.
- Checklist operacional preenchido.
- Matriz de evidencias preenchida.

## Criterio De Saida Da Fase 29

- Validador de prontidao criado.
- Relatorio JSON de prontidao gerado.
- Resumo Markdown de prontidao gerado.
- Guia de uso criado.
- Documentos de referencia atualizados.
- Indice mestre atualizado.
- Validador estatico local executado.
- Checklist da fase atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
