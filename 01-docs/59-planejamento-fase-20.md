# Fase 20 - Checklist Operacional Para Importacao n8n Controlada

## Objetivo

Criar um checklist operacional para futura importacao controlada do workflow n8n mockado, mantendo a etapa atual sem execucao, sem instalacao e sem integracoes externas.

## Escopo

Artefatos cobertos nesta fase:

- `01-docs/61-checklist-operacional-importacao-n8n.md`
- `01-docs/14-guia-prototipo-n8n-mocks.md`
- `01-docs/28-indice-mestre.md`
- `01-docs/30-backlog-gates-decisao.md`
- Checklist da Fase 20.
- Relatorio e resumo do validador local.

## Fora De Escopo

Nesta fase nao serao alterados:

- Workflow n8n mockado.
- Payloads mockados.
- SQL planejado.
- Prompts.
- Diagramas.
- Validador estatico.

Nesta fase nao serao executados:

- Importacao no n8n.
- Workflow n8n.
- Instalacao do n8n.
- SQL.
- Banco.
- Redis.
- APIs.
- IA.
- Integracoes externas.
- Criacao de credenciais.

## Decisao Tecnica

A fase cria apenas um checklist operacional humano para uma futura janela controlada.

O checklist exige que, antes de qualquer importacao real:

- A versao alvo do n8n seja definida e registrada.
- A instancia seja isolada e nao produtiva.
- O workflow permaneca inativo apos importacao.
- Nenhuma credencial seja criada ou vinculada.
- Nenhum node externo seja adicionado.
- O validador local seja executado antes da tentativa.
- Haja aprovacao humana explicita para a importacao.

## Criterio De Saida Da Fase 20

- Planejamento documentado.
- Checklist operacional criado.
- Guia do prototipo n8n atualizado com referencia ao checklist.
- Backlog e gates atualizados com pre-condicoes de importacao.
- Indice mestre atualizado.
- Relatorio JSON regerado.
- Resumo Markdown regerado.
- Checklist da fase atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
