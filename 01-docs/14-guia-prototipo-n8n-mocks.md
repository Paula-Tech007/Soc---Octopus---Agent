# Guia Do Prototipo n8n Com Mocks

## Arquivos De Workflow

Workflow original:

```text
02-workflows-n8n/soc-octopus-prototipo-mock.json
```

Catalogo completo:

```text
01-docs/79-catalogo-workflows-n8n-mock.md
```

## Finalidade

Os workflows mockados representam cenarios do fluxo logico multiagente do SOC-Octopus-Agent dentro do n8n.

Eles usam apenas dados mockados e devem ser tratados como material de laboratorio, nao como automacao produtiva.

## Como O Workflow Original Esta Organizado

O workflow possui uma cadeia linear:

1. `01 - Manual Trigger`
2. `02 - Entrada mockada`
3. `03 - Normalizacao mockada`
4. `04 - Classificacao mockada`
5. `05 - Cerebro Central mockado`
6. `06 - Especialista Identidade mockado`
7. `07 - Solucao e Remediacao mockada`
8. `08 - Consolidador mockado`

## O Que O Workflow Faz

- Cria um caso mockado.
- Adiciona campos de normalizacao.
- Adiciona uma classificacao de causa raiz mockada.
- Indica especialistas recomendados.
- Simula uma analise do especialista de Identidade.
- Simula uma recomendacao de remediacao.
- Produz uma saida consolidada para revisao humana.

## O Que O Workflow Nao Faz

- Nao chama APIs.
- Nao usa HTTP Request.
- Nao usa banco de dados.
- Nao usa Redis.
- Nao envia mensagens.
- Nao usa Telegram.
- Nao usa e-mail.
- Nao le arquivos locais.
- Nao grava memoria corporativa.
- Nao executa comandos.
- Nao altera ambientes.
- Nao utiliza credenciais.

## Validacoes Realizadas Nesta Fase

- Sintaxe JSON validada.
- Ausencia de campo `credentials` nos workflows.
- Ausencia de node de HTTP Request.
- Ausencia de node de Telegram.
- Ausencia de node de banco de dados.
- Ausencia de Code node.
- Integridade estrutural validada pelo validador estatico local em todos os workflows.
- Falso positivo normalizado com `possible_false_positive` booleano e `false_positive_assessment` textual nos workflows.

## Importacao Controlada Futura

Antes de qualquer importacao em uma instancia n8n real, usar:

```text
01-docs/61-checklist-operacional-importacao-n8n.md
```

Antes da importacao, a versao alvo do n8n deve estar registrada em:

```text
01-docs/64-registro-decisao-versao-n8n.md
```

O ambiente de laboratorio deve atender aos criterios de:

```text
01-docs/67-criterios-ambiente-laboratorio-n8n.md
```

As evidencias e comparacoes de uma importacao futura devem seguir:

```text
01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md
```

A janela de laboratorio futura deve ser registrada usando:

```text
01-docs/73-modelo-ata-janela-laboratorio-n8n.md
```

A importacao futura deve ocorrer apenas com aprovacao humana explicita, em ambiente isolado, sem credenciais, sem execucao e mantendo o workflow inativo.

## Limites Conhecidos

- O workflow ainda nao foi validado dentro de uma instancia n8n real.
- A estrutura de nodes pode exigir ajuste fino conforme a versao do n8n usada no futuro.
- A classificacao ainda e mockada e nao dinamica.
- O roteamento ainda e linear e nao condicional.
- Nao ha persistencia.
- Nao ha memoria corporativa.

## Proxima Evolucao Recomendada

A validacao real em n8n deve ocorrer apenas quando houver aprovacao explicita para importar o workflow em uma instancia controlada. A execucao do workflow exige aprovacao separada.
