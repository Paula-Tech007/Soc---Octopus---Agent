# Fase 25 - Criterios Para Comparacao Automatizada Futura n8n

## Objetivo

Definir criterios para uma futura comparacao automatizada entre o workflow n8n mockado aprovado e uma exportacao futura do n8n, sem implementar automacao nesta fase.

## Escopo

Artefatos cobertos nesta fase:

- `01-docs/76-criterios-comparacao-automatizada-futura-n8n.md`
- `01-docs/28-indice-mestre.md`
- `01-docs/30-backlog-gates-decisao.md`
- `01-docs/39-especificacao-validadores-estaticos.md`
- `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md`
- `01-docs/73-modelo-ata-janela-laboratorio-n8n.md`
- Checklist da Fase 25.
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

- Implementacao de comparador.
- Comparacao real de arquivos.
- Escolha de versao do n8n.
- Pesquisa externa.
- Instalacao do n8n.
- Importacao no n8n.
- Exportacao do n8n.
- Workflow n8n.
- SQL.
- Banco.
- Redis.
- APIs.
- IA.
- Integracoes externas.
- Criacao de credenciais.

## Decisao Tecnica

A comparacao automatizada futura deve ser uma ferramenta local, deterministica, sem rede, sem dependencias externas obrigatorias e sem alterar os arquivos comparados.

Ela devera comparar:

- Workflow aprovado local.
- Exportacao futura do n8n, quando existir e for aprovada.

A ferramenta futura deve classificar divergencias como:

- `bloqueante`
- `requer_revisao`
- `aceitavel_com_registro`

## Criterio De Saida Da Fase 25

- Planejamento documentado.
- Checklist da fase criado.
- Criterios de comparacao automatizada futura criados.
- Especificacao de validadores atualizada.
- Plano de evidencias atualizado.
- Modelo de ata atualizado.
- Backlog e gates atualizados.
- Indice mestre atualizado.
- Relatorio JSON regerado.
- Resumo Markdown regerado.
- Checklist da fase atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
