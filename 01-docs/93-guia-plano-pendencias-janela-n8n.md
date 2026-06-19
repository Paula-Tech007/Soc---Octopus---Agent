# Guia Do Plano Local De Pendencias Da Janela n8n

## Arquivo

```text
06-tests/13-gerador-plano-pendencias-janela-n8n.py
```

## Objetivo

Gerar um plano local de pendencias a partir do relatorio de prontidao da janela n8n.

O gerador nao chama rede, nao executa n8n, nao importa workflow, nao exporta workflow, nao cria credenciais, nao altera os arquivos avaliados e nao preenche campos operacionais por inferencia.

## Entrada Padrao

```text
06-tests/11-relatorio-prontidao-janela-n8n.json
```

## Execucao

Na raiz do projeto:

```text
python 06-tests/13-gerador-plano-pendencias-janela-n8n.py
```

Para gerar relatorio JSON:

```text
python 06-tests/13-gerador-plano-pendencias-janela-n8n.py --write-report 06-tests/14-plano-pendencias-janela-n8n.json
```

Para gerar relatorio JSON e resumo Markdown:

```text
python 06-tests/13-gerador-plano-pendencias-janela-n8n.py --write-report 06-tests/14-plano-pendencias-janela-n8n.json --write-markdown 06-tests/15-resumo-plano-pendencias-janela-n8n.md
```

## Saida

O plano informa:

- `status`.
- `total_acoes`.
- `acoes_bloqueiam_janela`.
- Acoes por prioridade.
- Decisao recomendada.
- Lista de acoes abertas.

## Prioridades

### P0

Acoes essenciais para destravar a avaliacao da janela:

- Decisao da versao alvo do n8n.
- Identificacao de janela.
- Identificacao de ambiente.
- Definicao de responsaveis.

### P1

Acoes documentais que ainda bloqueiam a janela:

- Manifesto.
- Checklist operacional.
- Matriz de evidencias.
- Ata da janela.

### P2

Acoes tecnicas ou avisos que nao existem no estado atual.

## Resultado De Referencia Da Fase 30

Resultado atual:

```text
status: bloqueado
total_acoes: 10
acoes_bloqueiam_janela: 10
P0: 6
P1: 4
P2: 0
```

## Limites Conhecidos

- O plano depende do relatorio de prontidao mais recente.
- O plano nao consulta n8n.
- O plano nao valida ambiente real.
- O plano nao substitui revisao humana.
- O plano nao autoriza importacao, exportacao ou execucao.
