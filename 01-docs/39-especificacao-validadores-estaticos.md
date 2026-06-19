# Especificacao De Validadores Estaticos

## Objetivo

Definir regras que validadores futuros deverao aplicar aos artefatos do SOC-Octopus-Agent.

Esta especificacao e documental. Nao e um script, nao e executavel e nao deve ser tratada como automacao pronta.

## Categorias De Validacao

| Codigo | Categoria | Objetivo |
| --- | --- | --- |
| `VAL-001` | Estrutura de projeto | Confirmar pastas obrigatorias. |
| `VAL-002` | Payload JSON | Confirmar JSON valido e campos obrigatorios. |
| `VAL-003` | Governanca | Confirmar flags de mock, credenciais e dados reais. |
| `VAL-004` | Enums | Confirmar valores oficiais. |
| `VAL-005` | Rastreabilidade | Confirmar `case_id` e `trace_id`. |
| `VAL-006` | Saida consolidada | Confirmar secoes obrigatorias. |
| `VAL-007` | Workflow mockado | Confirmar ausencia de integracoes reais. |
| `VAL-008` | SQL planejado | Confirmar ausencia de credenciais e execucao. |
| `VAL-009` | Testes | Confirmar cobertura minima. |
| `VAL-010` | Memoria futura | Confirmar revisao humana obrigatoria. |
| `VAL-011` | Comparacao n8n local | Comparar exportacao futura com workflow aprovado. |
| `VAL-012` | Prontidao da janela n8n | Avaliar pacote operacional antes de janela de laboratorio. |
| `VAL-013` | Plano de pendencias da janela n8n | Converter pendencias de prontidao em acoes revisaveis. |
| `VAL-014` | Formulario P0/P1 da janela n8n | Validar completude do formulario de resolucao P0/P1 antes de aplicar dados. |

## VAL-001 - Estrutura De Projeto

Pastas obrigatorias:

- `01-docs`
- `02-workflows-n8n`
- `03-prompts`
- `04-payloads-mock`
- `05-sql`
- `06-tests`
- `07-diagrams`

Criterio de aprovacao:

- Todas as pastas existem.
- Nenhuma pasta duplicada foi criada.

## VAL-002 - Payload JSON

Arquivos alvo:

- `04-payloads-mock/*.json`
- `06-tests/00-cenarios-validacao-mock.json`
- `02-workflows-n8n/*.json`

Criterio de aprovacao:

- JSON valido.
- Campos obrigatorios presentes quando aplicavel.
- Nenhum payload de teste marcado como dado real.

## VAL-003 - Governanca

Campos esperados:

- `mock_payload`
- `contains_real_customer_data`
- `contains_credentials`
- `human_approval_required_for_action`

Criterio de aprovacao:

- `mock_payload` deve ser `true` em payloads mockados.
- `contains_real_customer_data` deve ser `false`.
- `contains_credentials` deve ser `false`.
- Acoes criticas devem exigir aprovacao humana.

## VAL-004 - Enums

Valores aceitos:

- `input_type`: `soc_alert`, `ticket`, `event`, `question`.
- `probable_root_cause`: `identity`, `endpoint`, `network`, `cloud`, `vulnerability`, `external_threat`, `false_positive`, `unknown`.
- `severity`: `low`, `medium`, `high`, `critical`.
- `risk_level`: `low`, `medium`, `high`, `critical`.
- `confidence_level`: `low`, `medium`, `high`.

Criterio de aprovacao:

- Valores fora da lista devem gerar reprovacao ou revisao humana.

## VAL-005 - Rastreabilidade

Criterio de aprovacao:

- Todo caso deve ter `case_id`.
- Todo fluxo deve ter `trace_id`.
- Saidas devem preservar os mesmos identificadores da entrada.

## VAL-006 - Saida Consolidada

Secoes obrigatorias:

- Resumo executivo.
- Diagnostico.
- Evidencias.
- Causa provavel.
- Nivel de risco.
- Solucao recomendada.
- Passos tecnicos.
- Escalonamento.
- Observacoes de seguranca.
- Nivel de confianca.
- Possivel falso positivo.
- Aprovacao humana.
- Lacunas.

## VAL-007 - Workflow Mockado

Criterio de aprovacao:

- Todo workflow deve estar inativo.
- Todo workflow deve estar sem credenciais.
- Nenhum workflow deve conter chamadas externas.
- Nenhum workflow deve conter nodes de banco.
- Nenhum workflow deve conter node de codigo.
- Nenhum workflow deve enviar mensagens.
- `possible_false_positive` deve ser booleano quando presente no node de classificacao.
- `false_positive_assessment` deve usar `yes`, `no` ou `possible`.
- Deve conter campos top-level obrigatorios: `name`, `active`, `nodes`, `connections`, `settings` e `meta`.
- Cada node deve conter `id`, `name`, `type`, `typeVersion`, `position` e `parameters`.
- `id` e `name` dos nodes devem ser unicos.
- Conexoes devem apontar apenas para nodes existentes.
- Na fase mockada, os tipos permitidos sao `n8n-nodes-base.manualTrigger` e `n8n-nodes-base.set`.
- `pinData` e `staticData` nao devem conter dados de execucao.

## VAL-008 - SQL Planejado

Criterio de aprovacao:

- SQL deve estar claramente marcado como nao executado.
- Nao deve conter usuario, senha, host, porta ou string de conexao.
- Nao deve conter comandos de criacao de usuario.
- Nao deve conter comandos de permissao.

## VAL-009 - Testes

Criterio de aprovacao:

- Deve haver cobertura para identidade, endpoint, rede, cloud, vulnerabilidade, ameaca externa e falso positivo.
- Cada cenario deve definir risco esperado.
- Cada cenario deve definir aprovacao humana esperada.
- Cada cenario deve listar comportamentos proibidos.

## VAL-010 - Memoria Futura

Criterio de aprovacao:

- Memoria corporativa deve permanecer futura ate aprovacao explicita.
- Todo candidato a memoria deve exigir revisao humana.
- Nenhum falso positivo deve virar conhecimento definitivo sem aprovacao.
- Dados sensiveis devem ser saneados antes de uso futuro.

## VAL-011 - Comparacao n8n Local

Criterio de aprovacao:

- Comparacao deve ser local e sem rede.
- Comparacao nao deve executar n8n.
- Workflow aprovado deve permanecer inalterado.
- Exportacao futura deve ser comparada contra o workflow aprovado.
- `active` deve permanecer `false`.
- Campo `credentials` deve permanecer ausente.
- Nodes externos, URLs, execucoes e dados reais devem gerar bloqueio.
- Divergencias devem ser classificadas como `bloqueante`, `requer_revisao` ou `aceitavel_com_registro`.
- Resultado deve ser revisavel por humano antes de qualquer ajuste.

Implementacao local:

- `06-tests/07-comparador-workflow-n8n.py`
- `06-tests/08-relatorio-comparacao-workflow-n8n.json`
- `06-tests/09-resumo-comparacao-workflow-n8n.md`

O comparador local nao substitui o validador estatico principal. Ele deve ser usado somente para comparar um workflow aprovado com uma exportacao futura aprovada para analise.

## VAL-012 - Prontidao Da Janela n8n

Criterio de avaliacao:

- Artefatos obrigatorios da janela devem existir.
- Validador estatico local deve estar sem falhas.
- Workflow alvo deve permanecer inativo.
- Workflow alvo deve permanecer sem credenciais.
- Workflow alvo deve permanecer sem URLs externas.
- Workflow alvo deve usar apenas tipos de nodes permitidos.
- Versao alvo do n8n deve estar registrada.
- Ambiente de laboratorio deve estar identificado.
- Responsaveis devem estar definidos.
- Ata, checklist e matriz de evidencias nao devem conter pendencias bloqueantes.

Implementacao local:

- `06-tests/10-validador-prontidao-janela-n8n.py`
- `06-tests/11-relatorio-prontidao-janela-n8n.json`
- `06-tests/12-resumo-prontidao-janela-n8n.md`

O status `bloqueado` e esperado enquanto versao, ambiente, responsaveis e aprovacao humana estiverem pendentes.

## VAL-013 - Plano De Pendencias Da Janela n8n

Criterio de avaliacao:

- Ler relatorio local de prontidao da janela.
- Converter checagens pendentes, bloqueantes ou avisos em acoes.
- Classificar acoes por prioridade.
- Marcar acoes que bloqueiam a janela.
- Nao preencher informacoes operacionais por inferencia.
- Nao autorizar importacao, exportacao ou execucao.

Implementacao local:

- `06-tests/13-gerador-plano-pendencias-janela-n8n.py`
- `06-tests/14-plano-pendencias-janela-n8n.json`
- `06-tests/15-resumo-plano-pendencias-janela-n8n.md`

O status `bloqueado` e esperado enquanto houver acoes P0 ou P1 abertas.

## VAL-014 - Formulario P0/P1 Da Janela n8n

Criterio de avaliacao:

- O formulario P0/P1 deve existir.
- Secoes obrigatorias devem estar presentes.
- Campos P0 devem conter valor confirmado e fonte/evidencia.
- Campos P1 devem conter valor confirmado e fonte/evidencia.
- Escopo da proxima acao deve estar explicitamente selecionado.
- Restricoes proibitivas devem permanecer registradas.
- Comandos de revalidacao apos preenchimento devem estar presentes.
- O validador nao deve aplicar dados nos documentos de destino.
- O validador nao deve autorizar importacao, exportacao ou execucao.

Implementacao local:

- `06-tests/16-validador-formulario-p0-p1-janela-n8n.py`
- `06-tests/17-relatorio-formulario-p0-p1-janela-n8n.json`
- `06-tests/18-resumo-formulario-p0-p1-janela-n8n.md`

O status `bloqueado` e esperado enquanto o formulario tiver campos pendentes ou nenhum escopo aprovado para a proxima acao.

## Resultado Esperado De Um Validador Futuro

Formato sugerido para relatorio futuro:

```text
validador:
artefato:
status: aprovado | reprovado | aprovado_com_ressalvas
regras_aplicadas:
falhas:
ressalvas:
proximos_passos:
```
