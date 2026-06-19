# Criterios Para Ambiente De Laboratorio n8n

## Objetivo

Definir criterios minimos para um ambiente de laboratorio n8n destinado a uma futura importacao controlada do workflow mockado.

Este documento nao autoriza instalacao, importacao, execucao, criacao de credenciais ou chamadas externas.

## Principios

- O laboratorio deve ser isolado de ambientes produtivos.
- O laboratorio deve usar apenas dados mockados.
- O workflow deve permanecer inativo apos importacao.
- Importacao e execucao devem ser aprovacoes separadas.
- Qualquer divergencia deve bloquear a proxima etapa ate revisao humana.

## Identificacao Do Ambiente

Antes de qualquer importacao futura, registrar:

- Nome do ambiente.
- Responsavel tecnico.
- Responsavel pela aprovacao humana.
- Objetivo da janela de laboratorio.
- Data e horario planejados.
- Versao alvo do n8n, quando definida.
- Localizacao do workflow aprovado.
- Plano de rollback.

## Requisitos Minimos

- Ambiente nao produtivo.
- Sem dados reais.
- Sem dados de cliente.
- Sem credenciais cadastradas para o workflow.
- Sem integracoes externas.
- Sem automacoes agendadas.
- Sem webhooks expostos.
- Sem nodes externos adicionados ao workflow.
- Sem execucao automatica.
- Acesso restrito aos responsaveis da janela.
- Registro manual das evidencias geradas.

## Controles De Rede

O ambiente deve ser preparado para evitar chamadas externas durante a importacao:

- Sem configuracao de chamadas HTTP no workflow.
- Sem webhooks ativos.
- Sem conectores de banco.
- Sem conectores de mensageria.
- Sem conectores de e-mail.
- Sem conectores de chat.
- Sem acesso a sistemas produtivos.
- Sem uso de dados reais para teste.

## Controles De Credenciais

Durante a preparacao e importacao:

- Nao criar credenciais.
- Nao vincular credenciais.
- Nao reutilizar credenciais existentes.
- Nao inserir valores sensiveis em campos de node.
- Nao registrar segredos em notas, logs ou evidencias.

## Controles De Dados

Permitido:

- Payloads mockados do projeto.
- Identificadores ficticios.
- Enderecos reservados para documentacao ja presentes nos mocks.
- Textos operacionais ficticios.

Proibido:

- Dados reais.
- Dados de cliente.
- Logs reais.
- Alertas produtivos.
- Credenciais.
- Dados pessoais reais.
- Indicadores reais obtidos por consulta externa.

## Criterios Antes Da Importacao

- [ ] `01-docs/64-registro-decisao-versao-n8n.md` preenchido e aprovado.
- [ ] `01-docs/61-checklist-operacional-importacao-n8n.md` revisado.
- [ ] `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md` revisado.
- [ ] Ata baseada em `01-docs/73-modelo-ata-janela-laboratorio-n8n.md` preparada.
- [ ] Validador estatico local executado sem falhas.
- [ ] Ambiente identificado como laboratorio isolado.
- [ ] Responsavel tecnico definido.
- [ ] Responsavel pela aprovacao humana definido.
- [ ] Plano de rollback documentado.
- [ ] Confirmacao de que o workflow ficara inativo.
- [ ] Confirmacao de que execucao exige aprovacao separada.

## Criterios De Abortagem

Abortar a etapa se:

- O ambiente nao for isolado.
- Houver dado real.
- Houver credencial cadastrada ou solicitada.
- O workflow for ativado.
- Uma execucao for disparada.
- Um node externo for adicionado.
- Um conector externo for exigido.
- A versao alvo do n8n nao estiver registrada.
- O validador local apresentar falha.

## Evidencias Esperadas

Registrar, quando a importacao futura for aprovada:

- Identificacao do ambiente.
- Responsavel tecnico.
- Versao alvo do n8n.
- Resultado do validador local.
- Checklist operacional preenchido.
- Plano de evidencias e comparacao preenchido quando aplicavel.
- Ata da janela preenchida.
- Evidencia de workflow inativo.
- Evidencia de ausencia de credenciais.
- Divergencias encontradas.
- Decisao final da janela.

## Saida Esperada

O ambiente sera considerado apto para tentativa futura de importacao somente se todos os criterios bloqueantes forem atendidos e aprovados por revisao humana.

Qualquer excecao deve ser registrada como pendencia e bloquear a importacao.
