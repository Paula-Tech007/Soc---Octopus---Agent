# Criterios De Qualidade De Payloads

## Objetivo

Definir criterios minimos para avaliar se um payload esta pronto para ser processado pelo SOC-Octopus-Agent em fases futuras.

## Qualidade Minima

Um payload e considerado minimamente processavel quando:

- Possui `case_id`.
- Possui `trace_id`.
- Possui `input_type` valido.
- Possui `source_system`.
- Possui `received_at` em formato ISO 8601.
- Possui `severity` valida.
- Possui `title`.
- Possui `description`.
- Possui objeto `governance`.
- Indica se e mockado.
- Indica se contem dados reais.
- Indica se contem credenciais.

## Bloqueio Obrigatorio

O payload deve ser bloqueado quando:

- `contains_credentials` for `true`.
- `contains_real_customer_data` for `true` em ambiente nao aprovado.
- `case_id` estiver ausente.
- `trace_id` estiver ausente.
- `input_type` nao estiver na lista oficial.
- O payload misturar dados mockados com dados reais.
- Houver segredo, senha, token ou chave em texto livre.

## Qualidade De Evidencias

Evidencias devem:

- Ter tipo.
- Ter resumo.
- Ter timestamp quando aplicavel.
- Referenciar apenas dados fornecidos.
- Evitar logs brutos extensos.
- Nao conter credenciais.
- Nao conter dados reais em fases mockadas.

## Qualidade De Entidades

Entidades devem ser separadas por tipo:

- `users`
- `hosts`
- `source_ips`
- `destination_ips`
- `domains`
- `services`
- `vulnerabilities`
- `cloud_resources`
- `network_devices`

## Qualidade Da Classificacao

A classificacao deve:

- Usar taxonomia oficial.
- Tratar `classification_hint` apenas como sugestao.
- Justificar mudanca de causa raiz.
- Usar `unknown` quando houver dados insuficientes.
- Reduzir confianca quando houver conflito.

## Qualidade Da Saida

A saida deve conter:

- Resumo executivo.
- Diagnostico.
- Evidencias consideradas.
- Causa provavel.
- Nivel de risco.
- Solucao recomendada.
- Passos tecnicos.
- Escalonamento recomendado.
- Observacoes de seguranca.
- Nivel de confianca.
- Possivel falso positivo.
- Aprovacao humana necessaria.
- Lacunas de informacao.

## Criterios De Reprovacao

Uma saida deve ser reprovada quando:

- Inventa evidencias.
- Omite `case_id` ou `trace_id`.
- Recomenda acao critica sem aprovacao humana.
- Trata dados mockados como producao.
- Solicita credenciais.
- Cria URL corporativa ficticia.
- Ignora falso positivo.
- Ignora nivel de confianca.
- Nao registra lacunas relevantes.

## Pontuacao Manual Sugerida

| Criterio | Peso |
| --- | --- |
| Campos obrigatorios presentes | 20 |
| Governanca correta | 20 |
| Evidencias coerentes | 15 |
| Roteamento correto | 15 |
| Risco e confianca coerentes | 10 |
| Falso positivo avaliado | 10 |
| Aprovacao humana aplicada | 10 |

Interpretacao:

- 90 a 100: aprovado.
- 70 a 89: aprovado com ressalvas.
- Abaixo de 70: reprovado.

