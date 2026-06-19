# Fase 3 - Prompts Base Dos Agentes

## Objetivo

Criar prompts base documentais para orientar o comportamento do Cerebro Central, especialistas tecnicos, especialista de solucao/remediacao e consolidador.

Esta fase prepara a base para fluxos multiagentes futuros, mas nao implementa automacao, n8n, APIs, banco de dados, Redis ou memoria corporativa funcional.

## Escopo

Prompts cobertos nesta fase:

- Padroes gerais de prompt e resposta.
- Cerebro Central / Orquestrador.
- Especialistas tecnicos.
- Especialista de Solucao e Remediacao.
- Consolidador.

## Fora De Escopo

Nesta fase nao serao criados:

- Workflows n8n.
- Codigo executavel.
- SQL.
- Testes automatizados.
- Integracoes reais.
- Dependencias externas.
- Tokens, credenciais, senhas ou URLs corporativas.
- Memoria corporativa funcional.

## Principios De Prompt

- Usar apenas dados fornecidos no payload ou explicitamente marcados como mockados.
- Nao inventar evidencias, ativos, usuarios, dominios ou URLs.
- Separar fatos, hipoteses e recomendacoes.
- Sempre indicar nivel de confianca.
- Sempre indicar possivel falso positivo.
- Sempre indicar se a acao exige aprovacao humana.
- Nao executar acoes; apenas diagnosticar e recomendar.
- Nao solicitar, registrar ou expor credenciais.

## Padrao Esperado De Resposta

Todo agente deve produzir, quando aplicavel:

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

## Criterio De Saida Da Fase 3

- Prompts base documentados.
- Padroes de resposta definidos.
- Responsabilidades dos agentes registradas.
- Estrutura validada.
- Checklist atualizado.
- Aprovacao humana pendente para iniciar a Fase 4.

