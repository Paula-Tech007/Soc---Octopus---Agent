# Fase 5 - Prototipo n8n Com Mocks

## Objetivo

Criar um prototipo inicial de workflow n8n usando somente dados ficticios, sem integracoes reais, sem credenciais e sem chamadas externas.

O prototipo deve representar o fluxo logico definido na Fase 4 em formato de workflow simples, para futura importacao e validacao manual no n8n.

## Escopo

Artefatos cobertos nesta fase:

- Workflow n8n mockado em JSON.
- Guia de uso e limites do prototipo.
- Checklist da Fase 5.
- Validacao de sintaxe JSON.
- Verificacao documental de ausencia de credenciais e integracoes externas.

## Fora De Escopo

Nesta fase nao serao criados:

- Integracoes com APIs reais.
- Chamadas HTTP.
- Credenciais.
- Tokens.
- Webhooks publicos.
- Banco de dados.
- Redis.
- Telegram.
- E-mail.
- WhatsApp.
- SQL operacional.
- Memoria corporativa funcional.
- Dependencias externas.
- Execucao automatizada em ambiente produtivo.

## Desenho Do Prototipo

O workflow sera linear e manual:

```text
Manual Trigger
↓
Entrada mockada
↓
Normalizacao mockada
↓
Classificacao mockada
↓
Cerebro Central mockado
↓
Especialista de Identidade mockado
↓
Solucao e Remediacao mockada
↓
Consolidador mockado
```

## Regras De Seguranca

- O workflow deve permanecer inativo por padrao.
- O workflow nao deve conter credenciais.
- O workflow nao deve conter URLs reais.
- O workflow nao deve executar contencao, bloqueio, reset, isolamento ou alteracao de configuracao.
- Toda acao critica deve ser marcada como dependente de aprovacao humana.

## Criterio De Saida Da Fase 5

- Workflow mockado criado.
- Documentacao de uso criada.
- JSON validado.
- Estrutura validada.
- Checklist atualizado.
- Aprovacao humana pendente para iniciar a Fase 6.

