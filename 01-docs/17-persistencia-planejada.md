# Persistencia Planejada

## Visao Geral

A persistencia futura do SOC-Octopus-Agent deve separar dados de caso, entradas recebidas, execucoes de agentes, achados tecnicos, planos de remediacao, saidas consolidadas, aprovacoes humanas, auditoria e candidatos a memoria corporativa.

O objetivo e manter rastreabilidade, governanca e capacidade de revisao sem misturar diagnostico, decisao, remediacao e aprendizado.

## Entidades Principais

### `case_records`

Tabela principal do caso.

Responsabilidades:

- Identificar o caso.
- Manter severidade, status, tipo de entrada e causa raiz provavel.
- Preservar `case_id` e `trace_id`.
- Registrar se o caso exige aprovacao humana.

### `input_payloads`

Guarda o payload recebido ou normalizado.

Responsabilidades:

- Manter tipo de entrada.
- Armazenar conteudo JSON.
- Indicar se o payload e mockado.
- Indicar se contem dado real ou credencial.

Regra:

- Payload com credencial ou dado real deve ser bloqueado antes de persistencia produtiva futura.

### `agent_runs`

Registra a execucao logica de cada agente.

Responsabilidades:

- Registrar agente acionado.
- Registrar papel do agente.
- Registrar status da execucao.
- Registrar nivel de confianca.
- Registrar resumo da decisao.

### `specialist_findings`

Guarda diagnosticos tecnicos dos especialistas.

Responsabilidades:

- Armazenar evidencias consideradas.
- Registrar causa provavel.
- Registrar risco.
- Registrar falso positivo.
- Registrar lacunas.

### `remediation_plans`

Guarda recomendacoes de solucao e remediacao.

Responsabilidades:

- Separar passos tecnicos de acoes criticas.
- Registrar se aprovacao humana e obrigatoria.
- Registrar validacao pos-acao.
- Registrar rollback ou contingencia.

### `consolidated_outputs`

Guarda a resposta final consolidada.

Responsabilidades:

- Registrar resumo executivo.
- Registrar diagnostico consolidado.
- Registrar solucao recomendada.
- Registrar risco e confianca finais.
- Registrar saida revisavel por humano.

### `human_approvals`

Guarda decisoes humanas futuras.

Responsabilidades:

- Registrar aprovacao, rejeicao ou pedido de revisao.
- Registrar motivo.
- Registrar escopo da aprovacao.
- Preservar auditoria de decisao.

Regra:

- Nao armazenar credenciais, senhas ou tokens em comentarios de aprovacao.

### `audit_events`

Guarda eventos de auditoria.

Responsabilidades:

- Registrar quem ou qual componente produziu evento.
- Registrar tipo de acao logica.
- Registrar antes/depois quando aplicavel.
- Registrar decisao de governanca.

### `memory_candidates`

Guarda candidatos para memoria corporativa futura.

Responsabilidades:

- Registrar licao aprendida candidata.
- Registrar causa recorrente.
- Registrar solucao candidata.
- Registrar falso positivo confirmado.
- Exigir revisao humana antes de virar conhecimento reutilizavel.

## Relacionamentos

- Um caso pode ter varios payloads de entrada.
- Um caso pode ter varias execucoes de agentes.
- Uma execucao de agente pode gerar achados tecnicos.
- Um caso pode ter um ou mais planos de remediacao.
- Um caso pode ter uma ou mais saidas consolidadas.
- Um caso pode ter varias aprovacoes humanas.
- Um caso pode ter muitos eventos de auditoria.
- Um caso pode gerar candidatos a memoria futura.

## Campos De Governanca Minimos

Toda entidade persistente deve considerar:

- Identificador unico.
- `case_id`.
- `trace_id`.
- Data de criacao.
- Origem do registro.
- Status.
- Indicador de dado mockado.
- Indicador de dado sensivel.
- Necessidade de aprovacao humana.

## Retencao E Revisao

Politicas de retencao ainda nao serao implementadas.

Recomendacao futura:

- Definir retencao por tipo de registro.
- Definir trilha de auditoria imutavel ou append-only.
- Definir processo de saneamento de dados.
- Definir revisao humana antes de memoria corporativa.

