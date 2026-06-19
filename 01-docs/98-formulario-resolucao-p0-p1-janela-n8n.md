# Formulario De Resolucao P0/P1 Da Janela n8n

Data de referencia: 2026-06-17

## Objetivo

Coletar as informacoes humanas necessarias para resolver as pendencias P0 e P1 da janela n8n do SOC-Octopus-Agent.

Este formulario nao autoriza instalacao, importacao, exportacao, execucao, ativacao, credenciais, chamadas externas, SQL, banco, Redis, IA ou integracoes.

## Regra De Preenchimento

Preencher somente com informacao confirmada por responsavel humano.

Nao usar inferencia, sugestao automatica, valor estimado ou dado operacional nao confirmado.

## Campos P0 Obrigatorios

| ID | Campo | Valor Confirmado | Fonte/Evidencia | Documento De Destino |
| --- | --- | --- | --- | --- |
| P0-001 | Versao alvo do n8n | Pendente | Pendente | `01-docs/64-registro-decisao-versao-n8n.md` |
| P0-002 | Fonte usada para confirmar a versao | Pendente | Pendente | `01-docs/64-registro-decisao-versao-n8n.md` |
| P0-003 | Data da confirmacao da versao | Pendente | Pendente | `01-docs/64-registro-decisao-versao-n8n.md` |
| P0-004 | Responsavel pela decisao de versao | Pendente | Pendente | `01-docs/64-registro-decisao-versao-n8n.md` |
| P0-005 | Identificador da janela | Pendente | Pendente | `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`, `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P0-006 | Ambiente de laboratorio | Pendente | Pendente | `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`, `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P0-007 | Tipo de ambiente | Laboratorio isolado | Confirmar criterio atendido | `01-docs/64-registro-decisao-versao-n8n.md`, `01-docs/67-criterios-ambiente-laboratorio-n8n.md` |
| P0-008 | Responsavel tecnico | Pendente | Pendente | `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`, `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P0-009 | Contato do responsavel tecnico | Pendente | Pendente | `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P0-010 | Responsavel pela aprovacao humana | Pendente | Pendente | `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`, `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P0-011 | Contato do responsavel pela aprovacao humana | Pendente | Pendente | `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P0-012 | Status da aprovacao humana da preparacao | Pendente | Pendente | `01-docs/64-registro-decisao-versao-n8n.md`, `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |

## Campos P1 Obrigatorios Antes Da Janela

| ID | Campo | Valor Confirmado | Fonte/Evidencia | Documento De Destino |
| --- | --- | --- | --- | --- |
| P1-001 | Manifesto revisado por humano | Pendente | Pendente | `01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md` |
| P1-002 | Checklist operacional revisado | Pendente | Pendente | `01-docs/61-checklist-operacional-importacao-n8n.md` |
| P1-003 | Matriz de evidencias preparada | Pendente | Pendente | `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md` |
| P1-004 | Ata preparada | Pendente | Pendente | `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P1-005 | Plano de rollback definido | Pendente | Pendente | `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P1-006 | Plano de evidencias revisado | Pendente | Pendente | `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md`, `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P1-007 | Roteiro da janela revisado | Pendente | Pendente | `01-docs/86-roteiro-janela-laboratorio-n8n.md`, `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |
| P1-008 | Escopo aprovado para a proxima acao | Pendente | Pendente | `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` |

## Escopo Da Proxima Acao

Selecionar somente o que foi aprovado explicitamente:

- [ ] Validar documentacao.
- [ ] Revisar checklist operacional.
- [ ] Preparar importacao controlada sem executar.
- [ ] Importar workflow mockado inativo.
- [ ] Exportar workflow importado para comparacao.
- [ ] Comparar exportacao com JSON aprovado.

Mesmo se algum item acima for aprovado, os itens abaixo permanecem proibidos sem aprovacao separada:

- Executar workflow.
- Ativar workflow.
- Criar credenciais.
- Vincular credenciais.
- Usar dados reais.
- Chamar APIs externas.
- Adicionar nodes externos.
- Alterar workflow durante a janela.
- Integrar banco, Redis, mensageria ou IA.

## Campos Que Devem Permanecer Pendentes Ate A Janela

Os campos abaixo nao devem ser preenchidos nesta etapa, porque dependem de uma janela aprovada ou de uma importacao futura:

- Horario real de inicio.
- Arquivo realmente importado.
- Identificador interno atribuido pelo n8n.
- Mensagens visuais da interface.
- Resultado visual da importacao.
- Evidencias apos importacao.
- Divergencias encontradas.
- Resultado final da janela.
- Encerramento da janela.

## Aplicacao Dos Dados

Quando os campos P0/P1 forem fornecidos, aplicar os dados nesta ordem:

1. Atualizar `01-docs/64-registro-decisao-versao-n8n.md`.
2. Atualizar identificacao em `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`.
3. Atualizar identificacao, responsaveis e pre-condicoes em `01-docs/73-modelo-ata-janela-laboratorio-n8n.md`.
4. Atualizar gates aplicaveis em `01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md`.
5. Atualizar itens aplicaveis em `01-docs/61-checklist-operacional-importacao-n8n.md`.
6. Atualizar status de evidencias `PRE` aplicaveis em `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`.

## Validacao Apos Preenchimento

Executar na raiz do projeto:

```text
python 06-tests/04-validador-estatico.py --write-report 06-tests/05-relatorio-validacao-estatica.json --write-markdown 06-tests/06-resumo-validacao-estatica.md
python 06-tests/10-validador-prontidao-janela-n8n.py --write-report 06-tests/11-relatorio-prontidao-janela-n8n.json --write-markdown 06-tests/12-resumo-prontidao-janela-n8n.md
python 06-tests/13-gerador-plano-pendencias-janela-n8n.py --write-report 06-tests/14-plano-pendencias-janela-n8n.json --write-markdown 06-tests/15-resumo-plano-pendencias-janela-n8n.md
```

## Criterio De Resolucao

As pendencias P0/P1 so devem ser consideradas resolvidas quando:

- O validador estatico local estiver sem falhas.
- O validador de prontidao nao retornar `bloqueado`.
- O plano de pendencias nao listar acoes P0 ou P1 abertas.
- A aprovacao humana estiver registrada.
- Importacao, exportacao e execucao continuarem separadas por aprovacao especifica.
