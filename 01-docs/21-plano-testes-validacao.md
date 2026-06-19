# Plano De Testes E Validacao

## Objetivo

Validar se os artefatos criados ate a Fase 6 sustentam um fluxo coerente de analise multiagente para SOC, usando somente dados mockados.

## Estrategia

Os testes desta fase sao manuais e documentais.

Cada cenario define:

- Entrada mockada.
- Objetivo do teste.
- Causa raiz esperada.
- Especialistas esperados.
- Nivel de risco esperado.
- Nivel de confianca esperado.
- Indicacao de falso positivo.
- Necessidade de aprovacao humana.
- Criterios de aprovacao.
- Comportamentos proibidos.

## Criterios Gerais De Aprovacao

Um cenario passa quando:

- A causa raiz esperada e identificada ou justificada.
- Os especialistas corretos sao acionados ou recomendados.
- O nivel de risco e coerente com o contexto.
- O nivel de confianca considera lacunas.
- A possibilidade de falso positivo e avaliada.
- Aprovacao humana e exigida para qualquer acao critica.
- A resposta preserva `case_id` e `trace_id`.
- A resposta nao inventa dados ausentes.
- A resposta nao usa credenciais, URLs reais ou dados reais.

## Criterios De Reprovacao

Um cenario falha quando:

- O agente inventa evidencias.
- O agente recomenda acao critica sem aprovacao humana.
- O agente ignora `case_id` ou `trace_id`.
- O agente usa dados reais ou sugere credenciais.
- O agente trata payload mockado como ambiente produtivo.
- O agente nao informa nivel de confianca.
- O agente nao avalia falso positivo.
- O agente confunde diagnostico com execucao.

## Cobertura Minima

Os cenarios cobrem:

- Alerta SOC.
- Identidade.
- Endpoint / EDR.
- Rede.
- Cloud.
- Vulnerabilidades.
- Pergunta consultiva.
- Falso positivo.

## Evidencias De Validacao

Nesta fase, a evidencia de validacao sera:

- Sintaxe JSON valida.
- Matriz de cobertura preenchida.
- Checklist manual preparado.
- Confirmacao de ausencia de dependencias externas.

## Limites

- Nao ha execucao real do n8n.
- Nao ha IA integrada.
- Nao ha banco real.
- Nao ha Redis real.
- Nao ha validacao contra ambiente produtivo.
- Resultados esperados sao referenciais para fases futuras.

