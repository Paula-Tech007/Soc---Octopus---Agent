# Fase 30 - Plano Local De Pendencias Da Janela n8n

Data de referencia: 2026-06-16

## Objetivo

Criar uma ferramenta local para transformar o relatorio de prontidao da janela n8n em um plano acionavel de pendencias, sem preencher campos operacionais por inferencia e sem executar n8n.

## Escopo

Artefatos cobertos nesta fase:

- `06-tests/13-gerador-plano-pendencias-janela-n8n.py`
- `06-tests/14-plano-pendencias-janela-n8n.json`
- `06-tests/15-resumo-plano-pendencias-janela-n8n.md`
- `01-docs/92-checklist-fase-30.md`
- `01-docs/93-guia-plano-pendencias-janela-n8n.md`
- Atualizacao do indice mestre.
- Atualizacao da especificacao de validadores.
- Atualizacao do guia do validador estatico local.
- Atualizacao do manifesto do pacote operacional.
- Atualizacao do guia do validador de prontidao.

## Fora De Escopo

Nesta fase nao serao executados:

- Instalacao de n8n.
- Importacao de workflow.
- Exportacao de workflow.
- Execucao de workflow.
- Ativacao de workflow.
- Criacao ou vinculacao de credenciais.
- Chamadas externas.
- SQL.
- Banco.
- Redis.
- IA.
- Integracoes externas.

Nesta fase nao serao preenchidos:

- Versao alvo do n8n.
- Ambiente de laboratorio.
- Responsavel tecnico.
- Responsavel pela aprovacao humana.
- Ata da janela.
- Matriz de evidencias.
- Checklist operacional real.

## Decisao Tecnica

O gerador de plano de pendencias:

- Usa apenas biblioteca padrao do Python.
- Le o relatorio local de prontidao.
- Converte checagens `pendente`, `bloqueante` e `aviso` em acoes.
- Classifica acoes por prioridade `P0`, `P1` ou `P2`.
- Sugere responsavel por papel, sem nomear pessoas.
- Mantem todas as acoes como abertas.
- Retorna codigo diferente de zero quando o plano permanece `bloqueado`.

## Resultado Inicial

Resultado gerado na Fase 30:

```text
status: bloqueado
total_acoes: 10
acoes_bloqueiam_janela: 10
P0: 6
P1: 4
P2: 0
```

As acoes P0 cobrem:

- Decisao da versao alvo do n8n.
- Identificacao da janela.
- Identificacao do ambiente.
- Registro da versao alvo na matriz.
- Definicao do responsavel tecnico.
- Definicao do responsavel pela aprovacao humana.

As acoes P1 cobrem:

- Gates do manifesto.
- Checklist operacional.
- Matriz de evidencias.
- Ata da janela.

## Criterio De Saida Da Fase 30

- Gerador local de plano de pendencias criado.
- Relatorio JSON do plano gerado.
- Resumo Markdown do plano gerado.
- Guia de uso criado.
- Documentos de referencia atualizados.
- Indice mestre atualizado.
- Validador estatico local executado.
- Checklist da fase atualizado.
- Projeto pausado aguardando aprovacao humana para nova fase.
