# Fase 19 - Pre-validacao Estatica Do Workflow n8n

## Objetivo

Ampliar o validador local para verificar a integridade estrutural do workflow n8n mockado antes de qualquer importacao controlada futura.

## Escopo

Artefatos cobertos nesta fase:

- `02-workflows-n8n/soc-octopus-prototipo-mock.json`
- `06-tests/04-validador-estatico.py`
- `06-tests/05-relatorio-validacao-estatica.json`
- `06-tests/06-resumo-validacao-estatica.md`
- `01-docs/28-indice-mestre.md`
- `01-docs/39-especificacao-validadores-estaticos.md`
- `01-docs/43-guia-validador-estatico-local.md`
- Checklist da Fase 19.

## Fora De Escopo

Nesta fase nao serao alterados:

- Payloads mockados.
- SQL planejado.
- Prompts.
- Diagramas.
- Estrutura funcional do workflow.
- Credenciais ou configuracoes de ambiente.

Nesta fase nao serao executados:

- Importacao no n8n.
- Workflow n8n.
- SQL.
- Banco.
- Redis.
- APIs.
- IA.
- Integracoes externas.
- Instalacao de dependencias.

## Decisao Tecnica

O validador passa a verificar o workflow como JSON estatico, cobrindo:

- Campos top-level obrigatorios.
- Campos estruturais obrigatorios em cada node.
- Unicidade de `id` e `name` dos nodes.
- Posicoes validas dos nodes.
- Tipos de nodes permitidos para a fase mockada.
- Estrutura dos valores em nodes `Set`.
- Conexoes referenciando apenas nodes existentes.
- Metadados de governanca do workflow.
- Ausencia de `pinData` e `staticData` preenchidos.

## Tipos De Node Permitidos Nesta Fase

```text
n8n-nodes-base.manualTrigger
n8n-nodes-base.set
```

## Criterio De Saida Da Fase 19

- Planejamento documentado.
- Checklist criado.
- Validador atualizado com pre-validacao estatica do workflow.
- Relatorio JSON regerado.
- Resumo Markdown regerado.
- Indice mestre atualizado.
- Guia e especificacao do validador atualizados.
- Checklist atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
