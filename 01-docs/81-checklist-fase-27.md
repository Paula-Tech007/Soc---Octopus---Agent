# Checklist Da Fase 27

Data de referencia: 2026-06-16

## Objetivo

Criar comparador local de workflows n8n, sem importar, exportar, executar, instalar ou integrar nada nesta fase.

## Checklist

- [x] Revalidar diretorio do projeto.
- [x] Revisar criterios de comparacao n8n existentes.
- [x] Implementar comparador local com biblioteca padrao do Python.
- [x] Garantir que o comparador nao altere arquivos de entrada.
- [x] Implementar classificacao `bloqueante`.
- [x] Implementar classificacao `requer_revisao`.
- [x] Implementar classificacao `aceitavel_com_registro`.
- [x] Detectar workflow ativo.
- [x] Detectar campo `credentials`.
- [x] Detectar URL externa.
- [x] Detectar node nao aprovado.
- [x] Detectar node proibido.
- [x] Detectar alteracao de conexoes.
- [x] Detectar inclusao ou ausencia de node.
- [x] Detectar alteracao de parametros.
- [x] Detectar `pinData` ou `staticData` preenchidos.
- [x] Gerar relatorio JSON de comparacao.
- [x] Gerar resumo Markdown de comparacao.
- [x] Criar guia de uso do comparador.
- [x] Atualizar criterios de comparacao.
- [x] Atualizar plano de evidencias pos-importacao n8n.
- [x] Atualizar especificacao dos validadores.
- [x] Atualizar guia do validador estatico local.
- [x] Atualizar indice mestre.
- [x] Executar validador estatico local apos atualizacoes finais.
- [x] Atualizar relatorio JSON local do validador.
- [x] Gerar resumo Markdown local do validador.
- [x] Registrar resultado final do validador.
- [ ] Aguardar aprovacao humana para qualquer nova fase.

## Concluido

- Comparador local criado em `06-tests/07-comparador-workflow-n8n.py`.
- Relatorio inicial criado em `06-tests/08-relatorio-comparacao-workflow-n8n.json`.
- Resumo inicial criado em `06-tests/09-resumo-comparacao-workflow-n8n.md`.
- Guia de uso criado em `01-docs/82-guia-comparador-workflow-n8n.md`.
- Comparacao de referencia executada com base e candidato iguais.
- Resultado do comparador: aprovado, 0 divergencias.
- Validador estatico executado localmente.
- Relatorio JSON do validador atualizado.
- Resumo Markdown do validador atualizado.
- Resultado do validador: 176 aprovacoes, 0 warnings e 0 falhas.

## Pendente

- Aprovacao humana para nova fase.

## Depende De Aprovacao

- Importar workflow no n8n.
- Exportar workflow do n8n.
- Executar workflow n8n.
- Criar credenciais.
- Vincular credenciais.
- Adicionar nodes externos.
- Alterar workflows aprovados.
- Alterar payloads mockados.
- Alterar SQL planejado.
- Alterar prompts.
- Alterar diagramas.
- Criar banco, Redis ou integracao.
- Integrar IA.
- Instalar dependencias externas.

## Riscos Identificados

- A comparacao contra exportacao real ainda depende de uma exportacao futura aprovada.
- Campos internos do n8n podem exigir revisao humana mesmo quando nao houver impacto funcional.
- O comparador nao substitui a ata de janela nem o checklist operacional de laboratorio.

## Proximos Passos Propostos

1. Aguardar aprovacao humana para nova fase.
2. Avaliar comparacao contra exportacao real somente apos janela de laboratorio aprovada.
3. Manter bloqueadas importacao, exportacao e execucao de n8n ate nova aprovacao.
