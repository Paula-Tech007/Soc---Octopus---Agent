# Fluxo Logico Multiagente

## Visao Geral

O fluxo logico do SOC-Octopus-Agent organiza a analise em etapas controladas. Cada etapa recebe contexto, produz uma saida rastreavel e limita o avanco automatico quando houver risco, incerteza ou necessidade de acao critica.

```text
Entrada
↓
Validacao minima
↓
Normalizacao
↓
Classificacao de causa raiz
↓
Orquestracao pelo Cerebro Central
↓
Analise dos especialistas tecnicos
↓
Solucao e remediacao recomendada
↓
Consolidacao
↓
Saida revisavel
↓
Memoria corporativa futura
```

## Etapa 1 - Entrada

Entradas aceitas no desenho atual:

- Alerta SOC.
- Ticket.
- Evento.
- Pergunta.

Requisitos minimos:

- `case_id`
- `trace_id`
- `input_type`
- `source_system`
- `received_at`
- `severity`
- `title`
- `description`
- `governance`

Se campos obrigatorios estiverem ausentes, o caso deve ser classificado como incompleto e enviado para revisao humana ou enriquecimento futuro.

## Etapa 2 - Validacao Minima

Objetivo:

- Confirmar se o payload e processavel.
- Confirmar se os dados sao mockados nesta fase.
- Verificar se ha indicio de credencial, token ou dado real.
- Confirmar rastreabilidade com `case_id` e `trace_id`.

Saidas possiveis:

- `valid_input`
- `incomplete_input`
- `blocked_sensitive_data`

Regra de governanca:

- Se houver credenciais, tokens ou dados reais, a analise deve ser bloqueada para saneamento do payload.

## Etapa 3 - Normalizacao

Objetivo:

- Padronizar os campos recebidos.
- Separar entidades, evidencias, contexto e governanca.
- Preparar dados para o Cerebro Central.

Saida esperada:

- Payload normalizado.
- Lista de lacunas.
- Indicacao de confianca inicial.

## Etapa 4 - Classificacao De Causa Raiz

Taxonomia inicial:

- `identity`
- `endpoint`
- `network`
- `cloud`
- `vulnerability`
- `external_threat`
- `false_positive`
- `unknown`

Regras:

- Usar `classification_hint` apenas como sugestao, nao como verdade final.
- Se as evidencias forem insuficientes, usar `unknown`.
- Se houver sinais contraditorios, registrar conflito e reduzir confianca.

## Etapa 5 - Cerebro Central / Orquestrador

Responsabilidades:

- Decidir especialistas a acionar.
- Preservar rastreabilidade.
- Definir prioridade inicial.
- Registrar lacunas.
- Identificar necessidade de aprovacao humana.
- Bloquear execucao automatica de acoes criticas.

Saida esperada:

- Classificacao de causa raiz.
- Especialistas recomendados.
- Justificativa de roteamento.
- Prioridade inicial.
- Requisitos de aprovacao humana.

## Etapa 6 - Especialistas Tecnicos

Cada especialista deve produzir:

- Diagnostico.
- Evidencias consideradas.
- Causa provavel.
- Nivel de risco.
- Solucao recomendada.
- Passo a passo tecnico.
- Escalonamento recomendado.
- Observacoes de seguranca.
- Nivel de confianca.
- Possivel falso positivo.

Regra:

- Especialistas nao executam acoes. Apenas analisam e recomendam.

## Etapa 7 - Especialista De Solucao E Remediacao

Objetivo:

- Transformar diagnosticos em recomendacao pratica.
- Separar acoes de baixo risco e acoes criticas.
- Indicar pre-requisitos.
- Indicar validacao pos-acao.
- Indicar rollback ou contingencia quando aplicavel.

Regra:

- Qualquer acao de bloqueio, isolamento, reset, revogacao, alteracao de permissao, mudanca de firewall ou alteracao de configuracao exige aprovacao humana.

## Etapa 8 - Consolidador

Objetivo:

- Produzir saida unica e auditavel.
- Resolver ou registrar conflitos entre especialistas.
- Indicar risco, confianca e falso positivo.
- Gerar resposta revisavel por humano.

Saida esperada:

- Resumo executivo.
- Diagnostico consolidado.
- Evidencias.
- Causa raiz provavel.
- Solucao recomendada.
- Passos tecnicos.
- Escalonamento.
- Observacoes de seguranca.
- Aprovacao humana necessaria.

## Etapa 9 - Saidas

Saidas futuras possiveis:

- Ticket.
- E-mail.
- Telegram.
- Relatorio executivo.
- Registro de auditoria.

Na Fase 4, essas saidas sao apenas conceituais.

## Etapa 10 - Memoria Corporativa Futura

Memoria corporativa nao sera implementada nesta fase.

Quando aprovada em fase futura, podera armazenar:

- Incidentes anteriores.
- Solucoes aplicadas.
- Falsos positivos.
- Licoes aprendidas.
- Causas recorrentes.
- Procedimentos internos.

Regra futura:

- A memoria so deve ser alimentada apos revisao humana.

