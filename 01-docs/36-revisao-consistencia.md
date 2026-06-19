# Revisao De Consistencia

## Objetivo

Registrar uma revisao documental entre os principais artefatos do projeto para identificar alinhamentos, inconsistencias e ajustes recomendados antes de fases executaveis.

## Artefatos Revisados

- Contratos de payload.
- Payloads mockados.
- Prompts base.
- Fluxo logico multiagente.
- Matriz de roteamento.
- Workflow n8n mockado.
- SQL planejado.
- Cenarios de teste.
- Governanca da memoria futura.

## Alinhamentos Confirmados

- `case_id` e `trace_id` aparecem como campos centrais em contratos, payloads, workflow, SQL e testes.
- A causa raiz `identity` esta alinhada entre alerta SOC, prompts, workflow e testes.
- Aprovacao humana aparece como controle recorrente.
- Memoria corporativa permanece futura e dependente de revisao humana.
- Redis e banco aparecem apenas como planejamento.
- O workflow n8n permanece inativo e mockado.
- Os testes reforcam ausencia de execucao real.

## Inconsistencias Identificadas

### 1. `possible_false_positive`

Situacao:

- Em alguns contratos e saidas, `possible_false_positive` aparece como boolean.
- Em alguns cenarios de teste, aparece como texto: `possible`, `yes`.

Recomendacao:

- Usar boolean em payloads estruturados finais.
- Usar campo textual separado em analises futuras, por exemplo `false_positive_assessment`.

### 2. Nomes De Especialistas

Situacao:

- Alguns documentos usam nomes textuais.
- Alguns payloads usam nomes com hifen ou termos resumidos.
- Testes usam snake_case.

Recomendacao:

- Adotar os identificadores oficiais definidos em `33-glossario-taxonomia.md`.

### 3. Entidades No Workflow Mockado

Situacao:

- O workflow mockado resume entidades em `entities_summary`.
- Payloads mockados usam objeto `entities`.

Recomendacao:

- Em futura validacao n8n, preservar objeto estruturado quando possivel.

### 4. Campos De Status

Situacao:

- Existem varios status textuais nos documentos.

Recomendacao:

- Adotar enum oficial de status antes de persistencia real.

### 5. Idioma Dos Campos

Situacao:

- Campos tecnicos estao majoritariamente em ingles.
- Textos e documentos estao em portugues.

Recomendacao:

- Manter campos tecnicos em ingles `snake_case`.
- Manter documentacao operacional em portugues.

## Ajustes Recomendados Antes De Implementacao Real

1. Normalizar `possible_false_positive`.
2. Normalizar nomes de especialistas.
3. Definir enum final de `status`.
4. Revisar SQL contra enums oficiais.
5. Revisar workflow mockado para usar objetos estruturados quando a versao n8n permitir.
6. Criar validacao automatizada somente apos aprovacao explicita.

## Risco Se Nao Ajustar

- Dificuldade de mapear saidas dos agentes para persistencia.
- Regras n8n mais complexas por divergencia de nomes.
- Testes menos confiaveis.
- Relatorios inconsistentes.
- Memoria futura com classificacoes divergentes.

## Conclusao

A base documental esta coerente para a etapa atual. As inconsistencias encontradas sao normais para uma fase de concepcao e devem ser tratadas antes de qualquer execucao real ou integracao produtiva.

