# Retencao, Revisao E Qualidade

## Objetivo

Definir diretrizes para retencao, revisao periodica e controle de qualidade da memoria corporativa futura.

## Retencao

Politicas de retencao devem ser definidas antes de qualquer implementacao funcional.

Diretrizes iniciais:

- Incidentes encerrados: reter conforme politica interna futura.
- Auditoria: preferir modelo append-only ou historico imutavel.
- Falsos positivos: revisar periodicamente para evitar conclusoes obsoletas.
- Procedimentos aprovados: revisar quando houver mudanca de tecnologia, ferramenta ou processo.
- Candidatos rejeitados: reter apenas pelo tempo necessario para auditoria.

## Saneamento De Dados

Antes de aprovar memoria:

- Remover credenciais.
- Remover tokens.
- Remover dados pessoais desnecessarios.
- Mascarar identificadores sensiveis.
- Substituir nomes reais por referencias aprovadas.
- Remover URLs corporativas nao autorizadas.
- Reduzir logs brutos a sumarios tecnicos.

## Qualidade Da Memoria

Uma entrada de memoria deve ter:

- Origem rastreavel.
- Evidencias resumidas.
- Causa raiz confirmada ou escopo bem delimitado.
- Solucao validada ou licao claramente descrita.
- Nivel de confianca.
- Limites de aplicabilidade.
- Revisor humano.
- Data de revisao futura.

## Niveis De Confianca

### `high`

Usar quando:

- Causa raiz foi confirmada.
- Solucao foi aplicada e validada.
- Evidencias sao consistentes.
- Baixa ambiguidade.

### `medium`

Usar quando:

- Causa raiz e plausivel.
- Solucao e recomendada, mas nao completamente comprovada.
- Ha lacunas conhecidas.
- Uso futuro exige validacao contextual.

### `low`

Usar quando:

- Conhecimento e apenas indicativo.
- Ha poucas evidencias.
- Ha conflito ou incerteza.
- Nao deve ser usado para decisao automatica.

## Revisao Periodica

Eventos que devem disparar revisao:

- Expiracao por data.
- Mudanca em ferramenta ou processo.
- Alteracao de arquitetura.
- Incidente similar com resultado diferente.
- Falso positivo recorrente.
- Procedimento considerado inseguro.
- Nova exigencia de compliance.

## Criterios De Rejeicao

Um candidato deve ser rejeitado quando:

- Contem dados sensiveis sem saneamento possivel.
- Nao possui origem rastreavel.
- Nao possui evidencia suficiente.
- Foi baseado em hipotese nao validada.
- Conflita com politica de seguranca.
- Reforca procedimento inseguro.
- Depende de ferramenta ou ambiente nao aprovado.

## Uso Em Analises Futuras

Quando a memoria for usada futuramente, a saida deve indicar:

- Qual memoria foi consultada.
- Qual parte foi relevante.
- Nivel de confianca da memoria.
- Se a memoria ainda esta valida.
- Diferencas entre o caso atual e o caso historico.
- Se revisao humana continua necessaria.

## Riscos De Qualidade

- Aprender falso positivo incorretamente.
- Generalizar solucao de um ambiente para outro.
- Usar memoria expirada.
- Reutilizar procedimento inseguro.
- Transformar hipotese em conhecimento.
- Omitir contexto que limita aplicabilidade.

