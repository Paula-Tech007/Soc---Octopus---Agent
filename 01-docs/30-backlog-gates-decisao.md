# Backlog E Gates De Decisao

## Objetivo

Organizar proximas possibilidades de evolucao do SOC-Octopus-Agent, mantendo controles de aprovacao antes de qualquer implementacao real.

## Estado Atual Do Backlog

Data de referencia: 2026-06-17

O projeto avancou ate a Fase 33 em escopo documental, validacao local e preparacao de janela n8n controlada.

O pacote atual esta aprovado na validacao estatica, mas permanece bloqueado para janela n8n enquanto existirem pendencias P0 e P1 no plano local de pendencias. A Fase 32 criou o formulario de coleta humana para resolver essas pendencias e a Fase 33 criou o validador local desse formulario.

## Gates Obrigatorios

### Gate 1 - Revisao Humana Consolidada

Antes de evoluir:

- Revisar documentos das Fases 1 a 33.
- Validar se os nomes de agentes estao corretos.
- Validar se os campos dos contratos sao suficientes.
- Validar se os criterios de risco fazem sentido para o SOC.
- Validar se o SQL planejado atende auditoria e retencao.
- Validar se as pendencias P0 e P1 da janela n8n foram resolvidas por responsavel humano.

Resultado esperado:

- Aprovado.
- Aprovado com ajustes.
- Reprovado para revisao.

### Gate 2 - Fechamento Do Pacote Atual

Antes de qualquer janela n8n:

- Resolver acoes P0 do plano local de pendencias.
- Resolver acoes P1 do plano local de pendencias.
- Usar `01-docs/98-formulario-resolucao-p0-p1-janela-n8n.md` como fonte de coleta humana.
- Executar `06-tests/16-validador-formulario-p0-p1-janela-n8n.py`.
- Reexecutar validador estatico local.
- Reexecutar validador de prontidao da janela.
- Reexecutar gerador de plano de pendencias.
- Registrar aprovacao humana especifica para a proxima acao.

### Gate 3 - Escolha Da Proxima Frente

Escolher uma frente:

- Hardening documental.
- Validacao controlada do workflow n8n.
- Testes automatizados locais.
- Implementacao minima de agente local.
- Desenho de seguranca operacional.

### Gate 4 - Autorizacao Para Execucao

Obrigatorio antes de:

- Importar workflow em n8n.
- Executar workflow.
- Executar SQL.
- Criar banco.
- Configurar Redis.
- Integrar IA.
- Criar credenciais.
- Usar APIs reais.
- Instalar dependencias.

Pre-condicoes para importacao n8n controlada:

- Usar `01-docs/61-checklist-operacional-importacao-n8n.md`.
- Registrar versao alvo do n8n em `01-docs/64-registro-decisao-versao-n8n.md`.
- Validar ambiente conforme `01-docs/67-criterios-ambiente-laboratorio-n8n.md`.
- Registrar evidencias conforme `01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md`.
- Registrar a janela em `01-docs/73-modelo-ata-janela-laboratorio-n8n.md`.
- Usar criterios de comparacao futura de `01-docs/76-criterios-comparacao-automatizada-futura-n8n.md`, se houver exportacao aprovada.
- Revisar manifesto do pacote operacional em `01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md`.
- Usar roteiro de janela em `01-docs/86-roteiro-janela-laboratorio-n8n.md`, somente se a janela for aprovada.
- Preencher matriz de evidencias em `01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md`.
- Executar validador estatico local sem falhas.
- Executar validador de prontidao da janela em `06-tests/10-validador-prontidao-janela-n8n.py`.
- Confirmar ambiente isolado e nao produtivo.
- Manter workflow inativo e sem credenciais.
- Obter aprovacao humana especifica para importacao.
- Tratar execucao do workflow como aprovacao separada.

## Backlog Priorizado

### P0 - Governanca E Seguranca

- Revisar todos os pontos de aprovacao humana.
- Definir politica de secrets.
- Definir politica de logs.
- Definir padrao de mascaramento de dados.
- Definir criterio para uso de dados reais no futuro.

### P1 - Hardening Documental

- Revisar contratos de payload.
- Padronizar nomes de campos em portugues ou ingles.
- Definir enums oficiais.
- Definir severidade oficial.
- Definir taxonomia final de causa raiz.
- Criar glossario.

### P2 - Validacao n8n Controlada

- Preencher registro de decisao da versao alvo do n8n.
- Validar criterios de ambiente de laboratorio.
- Preparar plano de evidencias e comparacao.
- Preparar ata da janela de laboratorio.
- Definir criterios de comparacao automatizada futura.
- Revisar pacote operacional de janela de laboratorio.
- Aplicar checklist operacional de importacao controlada.
- Importar workflow mockado em ambiente controlado.
- Validar compatibilidade da versao n8n.
- Ajustar nodes se necessario.
- Manter workflow sem credenciais.
- Validar saida manual.

### P3 - Testes Automatizados Locais

- Criar validador local de JSON.
- Validar campos obrigatorios.
- Validar ausencia de credenciais.
- Validar formato de `case_id` e `trace_id`.
- Validar cobertura dos cenarios.

### P4 - Persistencia Real Controlada

- Revisar SQL com DBA ou responsavel tecnico.
- Definir ambiente.
- Definir usuario e permissoes.
- Definir migracoes.
- Definir backup e retencao.

### P5 - IA E Agentes

- Definir provedor de IA.
- Definir modelo.
- Definir politica de dados enviados ao modelo.
- Definir protecoes contra alucinacao.
- Definir avaliacao humana.
- Definir custo e limites.

### P6 - Memoria Corporativa Funcional

- Definir backend de memoria.
- Definir processo de curadoria.
- Definir aprovacao.
- Definir expiracao.
- Definir auditoria de uso.

## Itens Bloqueados Ate Aprovacao Explicita

- Execucao de n8n.
- SQL real.
- Banco real.
- Redis real.
- APIs reais.
- Telegram.
- E-mail.
- WhatsApp.
- IA integrada.
- RAG.
- Embeddings.
- Banco vetorial.
- Credenciais.
- Dependencias externas.

## Recomendacao De Proxima Frente

A frente recomendada apos a Fase 33 e:

```text
Preenchimento humano do formulario P0/P1
```

Objetivo sugerido:

- Receber versao alvo do n8n, fonte de confirmacao e aprovador.
- Receber identificador da janela e ambiente de laboratorio.
- Receber responsavel tecnico e aprovador humano.
- Aplicar as respostas confirmadas nos documentos de destino.
- Reexecutar validadores locais ate remover o status `bloqueado`.

Essa frente ainda nao deve executar automacoes, integracoes reais ou workflow n8n sem aprovacao separada.
