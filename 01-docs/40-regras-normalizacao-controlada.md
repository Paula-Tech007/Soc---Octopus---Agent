# Regras De Normalizacao Controlada

## Objetivo

Definir como normalizar artefatos existentes em fase futura, sem alterar arquivos nesta fase.

## Principio

Normalizacao deve ser aprovada antes de aplicada. Cada alteracao deve preservar rastreabilidade e ser registrada em checklist.

## Ordem Recomendada

1. Revisar inconsistencias documentadas na Fase 10.
2. Aprovar lista de arquivos que poderao ser alterados.
3. Normalizar um grupo pequeno de arquivos por vez.
4. Validar JSON quando aplicavel.
5. Atualizar checklist da fase correspondente.
6. Registrar o que mudou e por que mudou.

## Normalizacao De `possible_false_positive`

Problema:

- Alguns artefatos usam boolean.
- Alguns cenarios usam texto.

Padrao futuro recomendado:

- `possible_false_positive`: boolean.
- `false_positive_assessment`: texto enum com `yes`, `no` ou `possible`.

Exemplo conceitual:

```json
{
  "possible_false_positive": true,
  "false_positive_assessment": "possible"
}
```

## Normalizacao De Especialistas

Usar identificadores oficiais:

- `cerebro_central`
- `alertas_soc`
- `threat_intelligence_osint`
- `endpoint_edr`
- `rede`
- `cloud`
- `identidade`
- `vulnerabilidades`
- `comunicacao`
- `executivo`
- `automacao`
- `solucao_remediacao`
- `infraestrutura_plataformas`
- `consolidador`

## Normalizacao De Entidades

Evitar campos resumidos quando houver possibilidade de objeto estruturado.

Preferir:

```json
{
  "entities": {
    "users": [],
    "hosts": [],
    "source_ips": [],
    "destination_ips": [],
    "domains": [],
    "services": []
  }
}
```

Usar campos resumidos apenas quando a ferramenta futura exigir texto simples.

## Normalizacao De Status

Usar enum controlado:

- `new`
- `validated`
- `in_analysis`
- `waiting_human_approval`
- `analysis_completed_mock`
- `closed_false_positive`
- `closed_remediated`
- `blocked_sensitive_data`

## Normalizacao De Datas

Usar ISO 8601 em todos os campos de data e hora.

Campos comuns:

- `received_at`
- `created_at`
- `updated_at`
- `started_at`
- `finished_at`
- `approved_at`
- `review_due_at`

## Arquivos Que Podem Ser Normalizados Em Fase Futura

Com aprovacao explicita:

- `04-payloads-mock/*.json`
- `06-tests/00-cenarios-validacao-mock.json`
- `02-workflows-n8n/soc-octopus-prototipo-mock.json`
- `05-sql/00-schema-planejado-mysql-mariadb.sql`
- Documentos que referenciem enums antigos.

## Arquivos Que Nao Devem Ser Alterados Sem Motivo Forte

- Checklists historicos ja fechados.
- Planejamentos de fases concluidas.
- Revisoes que registram estado historico.

## Criterios Para Aplicar Normalizacao

Aplicar somente quando:

- A alteracao reduz ambiguidade.
- A alteracao melhora validacao futura.
- A alteracao nao apaga historico relevante.
- A alteracao e pequena e revisavel.
- A alteracao foi aprovada humanamente.

## Riscos

- Perder rastreabilidade historica.
- Quebrar exemplos usados em testes.
- Alterar artefatos sem atualizar documentacao correlata.
- Misturar normalizacao documental com implementacao real.

