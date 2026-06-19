# Fase 18 - Normalizacao Controlada Do Workflow Mockado

## Objetivo

Normalizar o tratamento de falso positivo no workflow n8n mockado, alinhando o arquivo ao padrao ja adotado nos cenarios de teste e na saida consolidada.

## Escopo

Artefatos cobertos nesta fase:

- `02-workflows-n8n/soc-octopus-prototipo-mock.json`
- `06-tests/04-validador-estatico.py`
- `06-tests/05-relatorio-validacao-estatica.json`
- `06-tests/06-resumo-validacao-estatica.md`
- `01-docs/28-indice-mestre.md`
- `01-docs/39-especificacao-validadores-estaticos.md`
- `01-docs/43-guia-validador-estatico-local.md`
- Checklist da Fase 18.

## Fora De Escopo

Nesta fase nao serao alterados:

- Payloads mockados de entrada.
- Saida consolidada mockada.
- SQL planejado.
- Prompts.
- Diagramas.
- Estrutura de entidades do workflow.

Nesta fase nao serao executados:

- n8n.
- SQL.
- Banco.
- Redis.
- APIs.
- IA.
- Integracoes externas.
- Instalacao de dependencias.

## Decisao De Normalizacao

Padrao adotado no workflow:

```json
{
  "possible_false_positive": true,
  "false_positive_assessment": "possible"
}
```

Regras:

- `possible_false_positive` deve ser booleano.
- `false_positive_assessment` deve usar `yes`, `no` ou `possible`.
- O node de classificacao mockada deve manter o fluxo inativo e sem credenciais.
- A mudanca deve preservar o uso de `values.boolean` e `values.string` do node `Set`.

## Decisao Sobre Entidades

O workflow continua usando `entities_summary` nesta fase.

A preservacao de `entities` como objeto estruturado fica para fase futura com validacao controlada da versao do n8n, para evitar alteracao especulativa no schema do node `Set`.

## Criterio De Saida Da Fase 18

- Planejamento documentado.
- Checklist criado.
- Workflow mockado normalizado para falso positivo.
- Validador atualizado com regra especifica para falso positivo no workflow.
- Relatorio JSON regerado.
- Resumo Markdown regerado.
- Indice mestre atualizado.
- Guia e especificacao do validador atualizados.
- Checklist atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
