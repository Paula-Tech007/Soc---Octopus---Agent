# Governanca Da Memoria Corporativa

## Principio

A memoria corporativa futura deve melhorar diagnosticos e recomendacoes do SOC-Octopus-Agent sem comprometer seguranca, privacidade, rastreabilidade ou qualidade tecnica.

Ela nao deve ser um deposito automatico de tudo que o sistema analisou. Deve ser uma base curada, revisada e auditavel.

## O Que Pode Virar Memoria

Itens candidatos:

- Incidentes encerrados com causa raiz confirmada.
- Solucoes aplicadas e validadas.
- Falsos positivos confirmados.
- Procedimentos internos aprovados.
- Licoes aprendidas.
- Causas recorrentes.
- Padroes de escalonamento.
- Ajustes recomendados em regras de alerta.

## O Que Nao Pode Virar Memoria

Itens proibidos:

- Credenciais.
- Tokens.
- Senhas.
- Chaves de API.
- Dados reais de clientes sem politica aprovada.
- Informacoes pessoais nao saneadas.
- Hipoteses nao validadas.
- Diagnosticos contraditorios sem resolucao.
- Recomendacoes rejeitadas por humano.
- Logs brutos com dados sensiveis.
- URLs corporativas reais sem autorizacao.

## Estados De Um Candidato

Estados sugeridos:

- `draft_candidate`: candidato criado, ainda nao revisado.
- `pending_human_review`: aguardando revisao humana.
- `approved_for_memory`: aprovado para memoria futura.
- `rejected`: rejeitado.
- `needs_sanitization`: exige saneamento antes de aprovacao.
- `expired`: conhecimento expirado.
- `deprecated`: conhecimento substituido.

## Processo De Revisao Humana

1. Identificar candidato a memoria.
2. Confirmar origem, `case_id` e `trace_id`.
3. Verificar se ha dados sensiveis.
4. Sanear ou mascarar informacoes quando necessario.
5. Confirmar causa raiz, solucao e evidencias.
6. Atribuir nivel de confianca.
7. Definir escopo de aplicabilidade.
8. Definir prazo de revisao.
9. Aprovar, rejeitar ou devolver para ajuste.

## Campos Minimos Da Memoria Futura

Campos recomendados:

- `memory_id`
- `source_case_id`
- `source_trace_id`
- `memory_type`
- `title`
- `summary`
- `root_cause`
- `validated_solution`
- `evidence_summary`
- `applicability_scope`
- `confidence_level`
- `false_positive_reference`
- `security_notes`
- `approved_by_reference`
- `approved_at`
- `review_due_at`
- `status`
- `created_at`
- `updated_at`

## Tipos De Memoria

Tipos sugeridos:

- `incident_lesson`
- `validated_remediation`
- `confirmed_false_positive`
- `recurring_root_cause`
- `approved_procedure`
- `alert_tuning_recommendation`
- `escalation_pattern`

## Regras De Uso Futuro

- Memoria deve apoiar analise, nao substituir julgamento.
- Memoria deve ser citada como referencia interna, nao como evidencia direta de novo incidente.
- Memoria expirada nao deve ser usada automaticamente.
- Memoria de falso positivo nao deve encerrar novo caso sem validacao contextual.
- Memoria com baixa confianca deve ser usada apenas como sugestao fraca.
- Conflito entre memoria e evidencias atuais deve favorecer as evidencias atuais.

## Auditoria Da Memoria

Eventos auditaveis:

- Criacao de candidato.
- Saneamento.
- Aprovacao.
- Rejeicao.
- Uso em analise futura.
- Atualizacao.
- Expiracao.
- Revogacao.

Cada evento deve preservar:

- Quem aprovou ou alterou.
- Quando ocorreu.
- Qual escopo foi definido.
- Qual justificativa foi registrada.
- Qual caso originou o conhecimento.

