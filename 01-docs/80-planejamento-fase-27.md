# Fase 27 - Comparador Local De Workflows n8n

Data de referencia: 2026-06-16

## Objetivo

Implementar uma ferramenta local para comparar um workflow n8n aprovado no projeto contra uma exportacao futura do n8n, classificando divergencias de forma revisavel por humano.

## Escopo

Artefatos cobertos nesta fase:

- `06-tests/07-comparador-workflow-n8n.py`
- `06-tests/08-relatorio-comparacao-workflow-n8n.json`
- `06-tests/09-resumo-comparacao-workflow-n8n.md`
- `01-docs/81-checklist-fase-27.md`
- `01-docs/82-guia-comparador-workflow-n8n.md`
- Atualizacao dos criterios de comparacao n8n.
- Atualizacao do plano de evidencias pos-importacao n8n.
- Atualizacao da especificacao dos validadores estaticos.
- Atualizacao do guia do validador estatico local.
- Atualizacao do indice mestre.

## Fora De Escopo

Nesta fase nao serao executados:

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
- Instalacao de dependencias.

Nesta fase nao serao alterados:

- Workflows aprovados em `02-workflows-n8n`.
- Payloads mockados.
- Prompts.
- SQL planejado.
- Diagramas.

## Decisao Tecnica

O comparador local segue os criterios documentados para comparacao n8n:

- Usa apenas biblioteca padrao do Python.
- Recebe `--base` e `--candidate`.
- Mantem os arquivos comparados inalterados.
- Gera relatorio JSON e resumo Markdown opcionais.
- Retorna codigo diferente de zero quando o resultado e `bloqueado`.
- Classifica divergencias como `bloqueante`, `requer_revisao` ou `aceitavel_com_registro`.

As divergencias bloqueantes incluem:

- Workflow comparado ativo.
- Presenca de `credentials`.
- URL externa.
- Node nao aprovado.
- Node HTTP, webhook, banco, Redis, e-mail, mensageria, Code ou Function.
- Alteracao de conexoes.
- Inclusao ou ausencia de node.
- Alteracao de parametros de node.
- `pinData` ou `staticData` preenchidos.
- Possivel dado sensivel.

## Resultado Inicial

Foi executada uma comparacao local usando o workflow aprovado contra ele mesmo:

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

## Criterio De Saida Da Fase 27

- Comparador local criado.
- Relatorio JSON de comparacao gerado.
- Resumo Markdown de comparacao gerado.
- Guia de uso do comparador criado.
- Documentos de referencia atualizados.
- Indice mestre atualizado.
- Validador estatico local executado.
- Checklist da fase atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
