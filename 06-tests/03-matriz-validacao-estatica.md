# Matriz De Validacao Estatica

## Objetivo

Mapear regras de validacao estatica contra artefatos existentes do SOC-Octopus-Agent.

Esta matriz e documental e nao executavel.

## Matriz

| Regra | Artefatos | Resultado esperado |
| --- | --- | --- |
| `VAL-001` | Estrutura de pastas | Pastas base existem e nao ha duplicidade. |
| `VAL-002` | `04-payloads-mock/*.json` | JSON valido e campos minimos presentes. |
| `VAL-002` | `06-tests/00-cenarios-validacao-mock.json` | JSON valido e cenarios listados. |
| `VAL-002` | `02-workflows-n8n/soc-octopus-prototipo-mock.json` | JSON valido e workflow importavel em fase futura. |
| `VAL-003` | Payloads mockados | Flags de governanca coerentes com ambiente mockado. |
| `VAL-004` | Payloads, testes e SQL | Enums alinhados com taxonomia oficial. |
| `VAL-005` | Payloads, workflow, SQL e testes | `case_id` e `trace_id` preservados. |
| `VAL-006` | Saida consolidada mockada | Secoes obrigatorias representadas. |
| `VAL-007` | Workflow n8n mockado | Sem credenciais, chamadas externas, nodes de banco ou codigo. |
| `VAL-008` | SQL planejado | Sem credenciais, strings de conexao ou comandos de usuarios. |
| `VAL-009` | Cenarios de teste | Cobertura minima por dominio e governanca. |
| `VAL-010` | Documentos de memoria | Revisao humana obrigatoria e memoria apenas futura. |

## Status Manual Atual

| Regra | Status documental | Observacao |
| --- | --- | --- |
| `VAL-001` | preparado | Estrutura ja validada em fases anteriores. |
| `VAL-002` | preparado | JSONs ja foram parseados manualmente em fases anteriores. |
| `VAL-003` | preparado | Flags existem nos payloads mockados principais. |
| `VAL-004` | requer normalizacao futura | Ha divergencia conhecida em falso positivo textual e booleano. |
| `VAL-005` | preparado | IDs aparecem nos principais artefatos. |
| `VAL-006` | preparado | Saida consolidada mockada possui estrutura base. |
| `VAL-007` | preparado | Workflow mockado ja foi checado contra integracoes externas. |
| `VAL-008` | preparado | SQL planejado ja foi checado contra credenciais e conexoes. |
| `VAL-009` | preparado | Matriz de cobertura existe na Fase 7. |
| `VAL-010` | preparado | Governanca de memoria foi documentada na Fase 8. |

## Uso Futuro

Esta matriz deve orientar uma fase futura de validadores locais, caso aprovada.

Antes de transformar esta matriz em script:

- Revisar enums oficiais.
- Decidir se mocks serao normalizados.
- Definir linguagem e ferramenta.
- Aprovar dependencias.
- Confirmar que nenhum dado real sera usado.

