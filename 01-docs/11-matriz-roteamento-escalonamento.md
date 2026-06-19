# Matriz De Roteamento E Escalonamento

## Objetivo

Definir como o Cerebro Central decide quais especialistas devem ser acionados, quando escalar um caso e quando exigir aprovacao humana.

## Matriz De Roteamento Por Causa Raiz

| Causa raiz | Especialistas primarios | Especialistas secundarios | Observacoes |
| --- | --- | --- | --- |
| `identity` | Identidade, Alertas SOC | Solucao e Remediacao, Comunicacao | Casos de AD, Entra ID, MFA, SSO, privilegios e autenticacao. |
| `endpoint` | Endpoint / EDR, Alertas SOC | Infraestrutura e Plataformas, Solucao e Remediacao | Casos de host, processo suspeito, malware, EDR ou isolamento. |
| `network` | Rede, Alertas SOC | Infraestrutura e Plataformas, Solucao e Remediacao | Casos de firewall, proxy, VPN, DNS e fluxo de rede. |
| `cloud` | Cloud, Identidade | Vulnerabilidades, Solucao e Remediacao | Casos de Azure, AWS, GCP, IAM cloud e recursos expostos. |
| `vulnerability` | Vulnerabilidades, Infraestrutura e Plataformas | Cloud, Solucao e Remediacao | Casos de CVE, patch, scanner, exposicao e priorizacao. |
| `external_threat` | Threat Intelligence / OSINT, Alertas SOC | Rede, Solucao e Remediacao | Casos de IOC, dominio suspeito, IP externo ou campanha. |
| `false_positive` | Alertas SOC | Consolidador, Comunicacao | Casos com evidencia de benignidade ou regra ruidosa. |
| `unknown` | Alertas SOC, Automacao | Especialista mais proximo do contexto | Casos inconclusivos ou com dados insuficientes. |

## Criterios De Prioridade

### `critical`

Usar quando houver:

- Possivel comprometimento ativo.
- Conta privilegiada envolvida com evidencia forte.
- Ativo critico exposto com indicio de exploracao.
- Impacto amplo em disponibilidade, confidencialidade ou integridade.
- Multipla recorrencia em curto periodo.

### `high`

Usar quando houver:

- Evidencias consistentes de risco.
- Ativo sensivel envolvido.
- Conta privilegiada com comportamento suspeito.
- Vulnerabilidade critica em ativo exposto.
- Mudanca nao autorizada em controle de seguranca.

### `medium`

Usar quando houver:

- Indicadores relevantes, mas contexto incompleto.
- Impacto limitado.
- Necessidade de validacao adicional.
- Possibilidade moderada de falso positivo.

### `low`

Usar quando houver:

- Baixo impacto.
- Evidencia fraca.
- Contexto predominantemente benigno.
- Caso informativo ou pergunta consultiva.

## Criterios De Escalonamento

Escalonar para especialista tecnico quando:

- A causa raiz for clara e houver dominio tecnico especifico.
- A evidencia exigir interpretacao especializada.
- O caso envolver ativo, usuario ou servico sensivel.
- A recomendacao envolver risco operacional.

Escalonar para lideranca SOC quando:

- Risco for `critical`.
- Houver potencial impacto amplo.
- Houver conflito entre especialistas.
- A decisao exigir excecao de processo.
- Houver necessidade de comunicacao executiva.

Escalonar para Comunicacao quando:

- O caso exigir resposta para solicitante.
- Houver impacto em usuario ou area de negocio.
- Houver necessidade de texto para ticket, e-mail ou canal futuro.

Escalonar para Executivo quando:

- O caso afetar SLA, KPI, MTTR ou relatorio gerencial.
- Houver incidente critico.
- Houver recorrencia relevante.

## Pontos Obrigatorios De Aprovacao Humana

Aprovacao humana e obrigatoria antes de recomendar execucao efetiva de:

- Bloqueio de conta.
- Reset de senha.
- Revogacao de sessao.
- Alteracao de MFA.
- Isolamento de endpoint.
- Bloqueio ou liberacao em firewall.
- Alteracao de proxy, VPN ou DNS.
- Mudanca em permissao, IAM ou RBAC.
- Reinicio de servidor ou servico.
- Rollback de configuracao.
- Aplicacao de patch.
- Alteracao em recurso cloud.
- Envio de comunicacao externa.
- Registro definitivo em memoria corporativa futura.

## Tratamento De Conflitos

Se especialistas divergirem:

- Registrar divergencia.
- Manter evidencias separadas.
- Reduzir nivel de confianca.
- Solicitar revisao humana.
- Evitar recomendacao definitiva ate nova validacao.

## Tratamento De Falso Positivo

Um caso pode ser marcado como possivel falso positivo quando:

- A evidencia for insuficiente.
- O comportamento puder ser explicado por mudanca planejada.
- A origem for conhecida ou esperada no contexto mockado.
- A regra parecer ruidosa.
- Houver ausencia de impacto ou recorrencia.

Mesmo em falso positivo, registrar:

- Evidencias usadas.
- Motivo da classificacao.
- Lacunas.
- Recomendacao de ajuste futuro, se aplicavel.

