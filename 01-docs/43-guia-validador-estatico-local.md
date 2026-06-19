# Guia Do Validador Estatico Local

## Arquivo

```text
06-tests/04-validador-estatico.py
```

## Objetivo

Executar validacoes estaticas locais sobre os artefatos mockados e documentais do SOC-Octopus-Agent.

O validador nao chama rede, nao executa n8n, nao executa SQL, nao acessa banco e nao usa dependencias externas.

## Execucao

Na raiz do projeto:

```text
python 06-tests/04-validador-estatico.py
```

Para gerar relatorio JSON:

```text
python 06-tests/04-validador-estatico.py --write-report 06-tests/05-relatorio-validacao-estatica.json
```

Para gerar relatorio JSON e resumo Markdown:

```text
python 06-tests/04-validador-estatico.py --write-report 06-tests/05-relatorio-validacao-estatica.json --write-markdown 06-tests/06-resumo-validacao-estatica.md
```

## Saida

O validador retorna:

- `passed`: validacoes aprovadas.
- `warnings`: pontos que exigem atencao, mas nao bloqueiam.
- `failures`: problemas que devem bloquear evolucao.

## Validacoes Atuais

- Estrutura obrigatoria do projeto.
- JSON valido em payloads, cenarios e workflow.
- Campos obrigatorios de payloads e saida consolidada.
- Flags de governanca em artefatos mockados.
- Todos os workflows em `02-workflows-n8n` inativos, sem credenciais, sem nodes proibidos e sem URLs.
- `possible_false_positive` booleano e `false_positive_assessment` valido nos workflows.
- Integridade estrutural dos workflows: top-level, nodes, tipos permitidos, conexoes e metadados.
- SQL planejado sem comandos de usuario, permissao ou string de conexao.
- Cobertura minima dos cenarios de teste.
- Documentos de memoria futura com revisao ou aprovacao humana.

## Politica De Erro

- Se houver `failures`, o processo retorna codigo diferente de zero.
- Se houver apenas `warnings`, o processo retorna codigo zero.
- Warnings devem ser analisados antes de fases executaveis.

## O Que O Validador Nao Faz

- Nao corrige arquivos.
- Nao normaliza payloads.
- Nao cria credenciais.
- Nao instala pacotes.
- Nao executa comandos externos.
- Nao importa workflow no n8n.
- Nao executa SQL.

## Ferramenta Complementar

O comparador local de workflow n8n fica em:

```text
06-tests/07-comparador-workflow-n8n.py
```

Ele e separado do validador estatico principal e deve ser usado apenas para comparar um workflow aprovado com uma exportacao futura aprovada.

Relatorios padrao:

```text
06-tests/08-relatorio-comparacao-workflow-n8n.json
06-tests/09-resumo-comparacao-workflow-n8n.md
```

O validador local de prontidao da janela n8n fica em:

```text
06-tests/10-validador-prontidao-janela-n8n.py
```

Ele e separado do validador estatico principal e deve ser usado para avaliar pendencias antes de qualquer janela de laboratorio n8n.

Relatorios padrao:

```text
06-tests/11-relatorio-prontidao-janela-n8n.json
06-tests/12-resumo-prontidao-janela-n8n.md
```

O gerador local de plano de pendencias da janela n8n fica em:

```text
06-tests/13-gerador-plano-pendencias-janela-n8n.py
```

Ele e separado do validador estatico principal e deve ser usado para transformar pendencias de prontidao em acoes revisaveis.

Relatorios padrao:

```text
06-tests/14-plano-pendencias-janela-n8n.json
06-tests/15-resumo-plano-pendencias-janela-n8n.md
```

O validador local do formulario P0/P1 da janela n8n fica em:

```text
06-tests/16-validador-formulario-p0-p1-janela-n8n.py
```

Ele e separado do validador estatico principal e deve ser usado para verificar se o formulario P0/P1 possui dados humanos suficientes antes de aplicar valores nos documentos de destino.

Relatorios padrao:

```text
06-tests/17-relatorio-formulario-p0-p1-janela-n8n.json
06-tests/18-resumo-formulario-p0-p1-janela-n8n.md
```

## Limites Conhecidos

- As validacoes sao estaticas.
- A compatibilidade real com n8n ainda depende de importacao futura controlada.
- O SQL nao e validado contra um motor MySQL/MariaDB real.
- A qualidade semantica das respostas de agentes ainda depende de avaliacao humana.
