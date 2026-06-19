# Catalogo De Workflows n8n Mockados

## Objetivo

Listar os workflows n8n mockados do SOC-Octopus-Agent e o cenario coberto por cada arquivo.

Todos os workflows deste catalogo sao inativos, mockados, sem credenciais e sem integracoes externas.

## Workflows

| Arquivo | Cenario | Causa raiz | Status |
| --- | --- | --- | --- |
| `02-workflows-n8n/soc-octopus-prototipo-mock.json` | Alerta SOC de autenticacao suspeita | `identity` | Mockado, inativo |
| `02-workflows-n8n/soc-octopus-ticket-vpn-mfa-mock.json` | Ticket de falha VPN/MFA | `identity` | Mockado, inativo |
| `02-workflows-n8n/soc-octopus-evento-firewall-mock.json` | Evento de alteracao em firewall | `network` | Mockado, inativo |
| `02-workflows-n8n/soc-octopus-pergunta-vulnerabilidade-mock.json` | Pergunta sobre vulnerabilidade | `vulnerability` | Mockado, inativo |
| `02-workflows-n8n/soc-octopus-endpoint-processo-suspeito-mock.json` | Processo suspeito em endpoint | `endpoint` | Mockado, inativo |
| `02-workflows-n8n/soc-octopus-cloud-iam-permissao-mock.json` | Permissao excessiva em Cloud IAM | `cloud` | Mockado, inativo |
| `02-workflows-n8n/soc-octopus-ioc-externo-mock.json` | IOC externo sem enriquecimento | `external_threat` | Mockado, inativo |
| `02-workflows-n8n/soc-octopus-falso-positivo-manutencao-mock.json` | Falso positivo por manutencao | `false_positive` | Mockado, inativo |

## Padrao Comum

Cada workflow deve manter:

- `active=false`.
- Ausencia de campo `credentials`.
- Ausencia de URLs.
- Ausencia de nodes externos.
- Uso apenas de `manualTrigger` e `set`.
- Dados ficticios.
- Flags de governanca mockadas.
- Saida revisavel por humano.

## Uso Permitido Nesta Etapa

- Revisao documental.
- Validacao estatica local.
- Comparacao de estrutura.

## Uso Bloqueado Ate Aprovacao

- Importar no n8n.
- Executar no n8n.
- Ativar workflow.
- Criar ou vincular credenciais.
- Adicionar nodes externos.
- Usar dados reais.
