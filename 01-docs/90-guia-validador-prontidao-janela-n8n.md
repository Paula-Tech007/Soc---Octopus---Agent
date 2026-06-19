# Guia Do Validador De Prontidao Da Janela n8n

## Arquivo

```text
06-tests/10-validador-prontidao-janela-n8n.py
```

## Objetivo

Avaliar localmente se o pacote operacional da janela de laboratorio n8n esta pronto para revisao humana.

O validador nao chama rede, nao executa n8n, nao importa workflow, nao exporta workflow, nao cria credenciais e nao altera os arquivos avaliados.

## Execucao

Na raiz do projeto:

```text
python 06-tests/10-validador-prontidao-janela-n8n.py
```

Para gerar relatorio JSON:

```text
python 06-tests/10-validador-prontidao-janela-n8n.py --write-report 06-tests/11-relatorio-prontidao-janela-n8n.json
```

Para gerar relatorio JSON e resumo Markdown:

```text
python 06-tests/10-validador-prontidao-janela-n8n.py --write-report 06-tests/11-relatorio-prontidao-janela-n8n.json --write-markdown 06-tests/12-resumo-prontidao-janela-n8n.md
```

## Saida

O relatorio informa:

- `status`: `pronto`, `pronto_com_ressalvas` ou `bloqueado`.
- `percentual_prontidao_estimado`.
- Totais de checagens aprovadas, pendentes, bloqueantes e avisos.
- Decisao recomendada.
- Lista detalhada de checagens.

## Checagens Atuais

- Presenca dos artefatos obrigatorios do pacote de janela.
- Resultado do validador estatico local.
- Workflow alvo inativo.
- Ausencia de `credentials` no workflow alvo.
- Ausencia de URL externa no workflow alvo.
- Uso apenas de nodes permitidos no workflow alvo.
- Versao alvo do n8n registrada.
- Ambiente de laboratorio identificado.
- Responsaveis definidos.
- Ata, checklist, manifesto e matriz sem pendencias aparentes.

## Politica De Retorno

- `bloqueado`: codigo de retorno diferente de zero.
- `pronto_com_ressalvas`: codigo de retorno zero.
- `pronto`: codigo de retorno zero.

## Resultado De Referencia Da Fase 29

Resultado atual:

```text
status: bloqueado
percentual_prontidao_estimado: 67%
aprovados: 20
pendentes: 10
bloqueantes: 0
avisos: 0
```

Esse bloqueio e esperado porque ainda faltam decisao de versao alvo, ambiente de laboratorio, responsaveis, ata, checklist e matriz preenchidos.

## Ferramenta Complementar

Para transformar as pendencias em acoes revisaveis:

```text
python 06-tests/13-gerador-plano-pendencias-janela-n8n.py --write-report 06-tests/14-plano-pendencias-janela-n8n.json --write-markdown 06-tests/15-resumo-plano-pendencias-janela-n8n.md
```

## Limites Conhecidos

- A ferramenta faz verificacao estatica de arquivos locais.
- A ferramenta nao consulta versao real do n8n.
- A ferramenta nao valida uma instancia n8n.
- A ferramenta nao substitui revisao humana.
- A ferramenta nao autoriza importacao, exportacao ou execucao.
