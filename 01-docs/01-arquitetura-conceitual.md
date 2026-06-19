# Arquitetura Conceitual

## Fluxo Principal

```text
Entrada
↓
Normalizacao
↓
Classificacao de Causa Raiz
↓
Cerebro Central
↓
Especialista Responsavel
↓
Especialista de Solucao
↓
Consolidador
↓
Saidas
↓
Memoria Corporativa futura
```

## Componentes

### Entrada

Representa alertas, tickets, eventos e perguntas recebidos pelo sistema. Nesta fase, a entrada e apenas conceitual. Payloads mockados serao definidos em fase posterior.

### Normalizacao

Transforma diferentes formatos de entrada em um modelo padronizado, com campos como identificador do caso, origem, severidade, descricao, evidencias e contexto.

### Classificacao De Causa Raiz

Classifica a causa provavel antes do acionamento dos especialistas. Taxonomia inicial sugerida:

- Identidade.
- Endpoint.
- Rede.
- Cloud.
- Vulnerabilidade.
- Ameaca externa.
- Falso positivo.
- Desconhecido.

### Cerebro Central / Orquestrador

Responsavel por decidir quais especialistas devem ser acionados, consolidar contexto, controlar fluxo, manter rastreabilidade e exigir aprovacao humana quando necessario.

### Especialistas Tecnicos

Cada especialista deve produzir:

- Diagnostico.
- Evidencias.
- Causa provavel.
- Nivel de risco.
- Solucao recomendada.
- Passo a passo tecnico.
- Escalonamento recomendado.
- Observacoes de seguranca.
- Nivel de confianca.
- Possivel falso positivo.

### Especialista De Solucao E Remediacao

Transforma o diagnostico tecnico em recomendacoes praticas, procedimentos de remediacao e criterios de seguranca. Nao deve executar acoes criticas sem aprovacao humana.

### Consolidador

Gera a saida final em formato padronizado, incluindo resumo executivo, diagnostico tecnico, evidencias, recomendacoes, riscos, proximos passos e necessidade de escalonamento.

### Memoria Corporativa

Componente futuro para aprendizado com incidentes anteriores, solucoes aplicadas, falsos positivos, licoes aprendidas e causas recorrentes. Nao sera implementado na Fase 1.

## Governanca

- Toda decisao relevante deve ser rastreavel.
- Toda recomendacao deve ter nivel de confianca.
- Toda acao critica deve exigir aprovacao humana.
- Nenhum dado real de cliente deve ser usado em testes.
- Credenciais, tokens e URLs corporativas nao devem ser documentados nem simulados.

