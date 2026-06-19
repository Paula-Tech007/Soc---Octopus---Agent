# Fase 26 - Pacote De Workflows n8n Mockados Por Cenario

## Objetivo

Criar workflows n8n mockados adicionais para cobrir os cenarios de validacao do SOC-Octopus-Agent, mantendo todos os workflows inativos, sem credenciais e sem integracoes externas.

## Escopo

Artefatos cobertos nesta fase:

- `02-workflows-n8n/soc-octopus-ticket-vpn-mfa-mock.json`
- `02-workflows-n8n/soc-octopus-evento-firewall-mock.json`
- `02-workflows-n8n/soc-octopus-pergunta-vulnerabilidade-mock.json`
- `02-workflows-n8n/soc-octopus-endpoint-processo-suspeito-mock.json`
- `02-workflows-n8n/soc-octopus-cloud-iam-permissao-mock.json`
- `02-workflows-n8n/soc-octopus-ioc-externo-mock.json`
- `02-workflows-n8n/soc-octopus-falso-positivo-manutencao-mock.json`
- `06-tests/04-validador-estatico.py`
- `01-docs/79-catalogo-workflows-n8n-mock.md`
- `01-docs/14-guia-prototipo-n8n-mocks.md`
- `01-docs/28-indice-mestre.md`
- `01-docs/39-especificacao-validadores-estaticos.md`
- `01-docs/43-guia-validador-estatico-local.md`
- Checklist da Fase 26.
- Relatorio e resumo do validador local.

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

Nesta fase nao serao criados:

- Nodes HTTP.
- Webhooks.
- Nodes de banco.
- Nodes de codigo.
- Credenciais.
- Chamadas externas.

## Decisao Tecnica

Os novos workflows seguem o padrao local:

- `active=false`.
- `manualTrigger` como unico gatilho.
- Nodes `Set` para representar etapas mockadas.
- Sem campo `credentials`.
- Sem URLs.
- Sem integracoes externas.
- Sem `pinData` ou `staticData` de execucao.
- Metadados de governanca com `mock_only=true`.

O validador estatico passa a validar todos os arquivos JSON em `02-workflows-n8n`.

## Criterio De Saida Da Fase 26

- Novos workflows mockados criados.
- Catalogo de workflows criado.
- Validador atualizado para todos os workflows.
- Guia n8n atualizado.
- Especificacao e guia do validador atualizados.
- Indice mestre atualizado.
- Relatorio JSON regerado.
- Resumo Markdown regerado.
- Checklist da fase atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
