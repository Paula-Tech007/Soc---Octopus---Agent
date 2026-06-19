#!/usr/bin/env python3
"""Validador local do formulario P0/P1 da janela n8n.

Este script usa apenas biblioteca padrao, nao acessa rede, nao executa n8n
e nao altera os artefatos avaliados.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FORM_PATH = ROOT / "01-docs" / "98-formulario-resolucao-p0-p1-janela-n8n.md"

PASS = "aprovado"
PENDING = "pendente"
BLOCK = "bloqueante"
WARN = "aviso"

REQUIRED_SECTIONS = [
    "## Campos P0 Obrigatorios",
    "## Campos P1 Obrigatorios Antes Da Janela",
    "## Escopo Da Proxima Acao",
    "## Campos Que Devem Permanecer Pendentes Ate A Janela",
    "## Aplicacao Dos Dados",
    "## Validacao Apos Preenchimento",
    "## Criterio De Resolucao",
]

REQUIRED_FORBIDDEN_MARKERS = [
    "Executar workflow.",
    "Ativar workflow.",
    "Criar credenciais.",
    "Vincular credenciais.",
    "Usar dados reais.",
    "Chamar APIs externas.",
    "Adicionar nodes externos.",
]

UNRESOLVED_MARKERS = [
    "pendente",
    "confirmar criterio",
    "nao informado",
    "a definir",
]


class FormReport:
    def __init__(self) -> None:
        self.items: list[dict[str, Any]] = []

    def add(self, category: str, status: str, check: str, evidence: str, action: str) -> None:
        self.items.append(
            {
                "id": f"FRM-{len(self.items) + 1:04d}",
                "categoria": category,
                "status": status,
                "checagem": check,
                "evidencia": evidence,
                "acao_recomendada": action,
            }
        )

    def counts(self) -> dict[str, int]:
        return {
            PASS: sum(1 for item in self.items if item["status"] == PASS),
            PENDING: sum(1 for item in self.items if item["status"] == PENDING),
            BLOCK: sum(1 for item in self.items if item["status"] == BLOCK),
            WARN: sum(1 for item in self.items if item["status"] == WARN),
        }

    def status(self) -> str:
        counts = self.counts()
        if counts[BLOCK] or counts[PENDING]:
            return "bloqueado"
        if counts[WARN]:
            return "pronto_com_ressalvas"
        return "pronto_para_aplicacao"

    def decision(self) -> str:
        status = self.status()
        if status == "bloqueado":
            return (
                "Manter resolucao P0/P1 bloqueada. Preencher formulario com dados "
                "humanos confirmados antes de aplicar valores nos documentos de destino."
            )
        if status == "pronto_com_ressalvas":
            return "Revisar avisos antes de aplicar dados nos documentos de destino."
        return "Formulario pronto para aplicacao controlada nos documentos de destino."

    def as_dict(self) -> dict[str, Any]:
        counts = self.counts()
        return {
            "project": "SOC-Octopus-Agent",
            "validator": "06-tests/16-validador-formulario-p0-p1-janela-n8n.py",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status": self.status(),
            "summary": {
                "aprovados": counts[PASS],
                "pendentes": counts[PENDING],
                "bloqueantes": counts[BLOCK],
                "avisos": counts[WARN],
                "total": sum(counts.values()),
            },
            "decisao_recomendada": self.decision(),
            "checks": self.items,
        }


def resolve_inside_project(path_argument: str, label: str) -> Path:
    path = (ROOT / path_argument).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"{label} deve ficar dentro do projeto") from exc
    return path


def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def unresolved(value: str) -> bool:
    normalized = value.strip().lower()
    return not normalized or any(marker in normalized for marker in UNRESOLVED_MARKERS)


def markdown_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def form_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not re.match(r"^\|\s*P[01]-\d{3}\s*\|", line):
            continue
        cells = markdown_cells(line)
        if len(cells) < 5:
            continue
        rows.append(
            {
                "id": cells[0],
                "campo": cells[1],
                "valor": cells[2],
                "evidencia": cells[3],
                "destino": cells[4],
            }
        )
    return rows


def section_text(text: str, heading: str) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    next_heading = re.search(r"^##\s+", text[start + len(heading) :], flags=re.MULTILINE)
    if not next_heading:
        return text[start:]
    end = start + len(heading) + next_heading.start()
    return text[start:end]


def check_required_sections(report: FormReport, text: str) -> None:
    for section in REQUIRED_SECTIONS:
        if section in text:
            report.add(
                "estrutura",
                PASS,
                f"Secao obrigatoria encontrada: {section}",
                section,
                "Nenhuma acao.",
            )
        else:
            report.add(
                "estrutura",
                BLOCK,
                f"Secao obrigatoria ausente: {section}",
                section,
                "Restaurar secao antes de usar o formulario.",
            )


def check_form_fields(report: FormReport, text: str) -> None:
    rows = form_rows(text)
    if not rows:
        report.add(
            "campos",
            BLOCK,
            "Nenhum campo P0/P1 encontrado no formulario.",
            relative(DEFAULT_FORM_PATH),
            "Restaurar tabelas P0/P1 antes de continuar.",
        )
        return

    for row in rows:
        field_id = row["id"]
        category = "p0" if field_id.startswith("P0-") else "p1"
        value_pending = unresolved(row["valor"])
        evidence_pending = unresolved(row["evidencia"])
        if value_pending or evidence_pending:
            missing = []
            if value_pending:
                missing.append("valor confirmado")
            if evidence_pending:
                missing.append("fonte/evidencia")
            report.add(
                category,
                PENDING,
                f"{field_id} ainda requer {', '.join(missing)}: {row['campo']}.",
                f"valor={row['valor']}; evidencia={row['evidencia']}",
                "Preencher somente com informacao confirmada por responsavel humano.",
            )
        else:
            report.add(
                category,
                PASS,
                f"{field_id} preenchido: {row['campo']}.",
                f"destino={row['destino']}",
                "Revisar consistencia antes de aplicar nos documentos de destino.",
            )


def check_scope(report: FormReport, text: str) -> None:
    scope = section_text(text, "## Escopo Da Proxima Acao")
    matches = re.findall(r"^- \[( |x|X)\] (.+)$", scope, flags=re.MULTILINE)
    if not matches:
        report.add(
            "escopo",
            BLOCK,
            "Lista de escopo aprovado nao encontrada.",
            "## Escopo Da Proxima Acao",
            "Restaurar lista de escopo antes de continuar.",
        )
        return

    selected = [label.strip() for marker, label in matches if marker.lower() == "x"]
    if selected:
        report.add(
            "escopo",
            PASS,
            "Escopo da proxima acao possui itens selecionados.",
            "; ".join(selected),
            "Confirmar aprovacao humana antes de aplicar dados.",
        )
    else:
        report.add(
            "escopo",
            PENDING,
            "Nenhum item de escopo da proxima acao foi aprovado.",
            f"{len(matches)} opcoes disponiveis, 0 selecionadas",
            "Selecionar apenas itens aprovados explicitamente por humano.",
        )


def check_forbidden_restrictions(report: FormReport, text: str) -> None:
    missing = [marker for marker in REQUIRED_FORBIDDEN_MARKERS if marker not in text]
    if missing:
        report.add(
            "restricoes",
            BLOCK,
            "Restricoes obrigatorias ausentes no formulario.",
            "; ".join(missing),
            "Restaurar restricoes antes de usar formulario.",
        )
    else:
        report.add(
            "restricoes",
            PASS,
            "Restricoes proibitivas permanecem registradas.",
            f"{len(REQUIRED_FORBIDDEN_MARKERS)} restricoes verificadas",
            "Manter restricoes ate aprovacao separada.",
        )


def check_validation_commands(report: FormReport, text: str) -> None:
    required_commands = [
        "python 06-tests/04-validador-estatico.py",
        "python 06-tests/10-validador-prontidao-janela-n8n.py",
        "python 06-tests/13-gerador-plano-pendencias-janela-n8n.py",
    ]
    missing = [command for command in required_commands if command not in text]
    if missing:
        report.add(
            "validacao",
            BLOCK,
            "Comandos obrigatorios de validacao ausentes.",
            "; ".join(missing),
            "Restaurar comandos antes de aplicar respostas P0/P1.",
        )
    else:
        report.add(
            "validacao",
            PASS,
            "Comandos de validacao apos preenchimento estao registrados.",
            f"{len(required_commands)} comandos verificados",
            "Executar comandos apos aplicar dados humanos confirmados.",
        )


def run_validation(form_path: Path) -> FormReport:
    report = FormReport()
    if not form_path.is_file():
        report.add(
            "artefato",
            BLOCK,
            "Formulario P0/P1 ausente.",
            relative(form_path),
            "Criar formulario antes de continuar.",
        )
        return report

    text = read_text(form_path)
    check_required_sections(report, text)
    check_form_fields(report, text)
    check_scope(report, text)
    check_forbidden_restrictions(report, text)
    check_validation_commands(report, text)
    return report


def render_markdown_summary(result: dict[str, Any]) -> str:
    summary = result.get("summary", {})
    lines = [
        "# Resumo Do Formulario P0/P1 Da Janela n8n",
        "",
        "## Status Consolidado",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Projeto | {result.get('project', 'SOC-Octopus-Agent')} |",
        f"| Status | {result.get('status', 'nao informado')} |",
        f"| Gerado em | {result.get('created_at', 'nao informado')} |",
        f"| Validador | {result.get('validator', 'nao informado')} |",
        "",
        "## Totais",
        "",
        "| Metrica | Total |",
        "| --- | ---: |",
        f"| Aprovados | {summary.get('aprovados', 0)} |",
        f"| Pendentes | {summary.get('pendentes', 0)} |",
        f"| Bloqueantes | {summary.get('bloqueantes', 0)} |",
        f"| Avisos | {summary.get('avisos', 0)} |",
        f"| Total | {summary.get('total', 0)} |",
        "",
        "## Decisao Recomendada",
        "",
        f"- {result.get('decisao_recomendada', 'nao informado')}",
        "",
        "## Checagens",
        "",
        "| ID | Categoria | Status | Checagem | Acao Recomendada |",
        "| --- | --- | --- | --- | --- |",
    ]

    for item in result.get("checks", []):
        lines.append(
            "| "
            f"{item.get('id', '')} | "
            f"{item.get('categoria', '')} | "
            f"{item.get('status', '')} | "
            f"{item.get('checagem', '')} | "
            f"{item.get('acao_recomendada', '')} |"
        )

    lines.extend(
        [
            "",
            "## Observacoes",
            "",
            "- Resultado gerado localmente a partir do formulario P0/P1.",
            "- O status bloqueado e esperado enquanto existirem campos pendentes.",
            "- Este resumo nao autoriza importacao, exportacao ou execucao no n8n.",
        ]
    )
    return "\n".join(lines)


def write_output_inside_project(path_argument: str, content: str, label: str) -> int:
    try:
        output_path = resolve_inside_project(path_argument, label)
    except ValueError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content + "\n", encoding="utf-8")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validador local do formulario P0/P1 n8n")
    parser.add_argument(
        "--form",
        default=str(DEFAULT_FORM_PATH.relative_to(ROOT)),
        help="Formulario Markdown P0/P1",
    )
    parser.add_argument("--write-report", help="Caminho para gravar relatorio JSON")
    parser.add_argument("--write-markdown", help="Caminho para gravar resumo Markdown")
    args = parser.parse_args()

    try:
        form_path = resolve_inside_project(args.form, "formulario")
    except ValueError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2

    report = run_validation(form_path)
    result = report.as_dict()
    output = json.dumps(result, indent=2, ensure_ascii=False)
    print(output)

    if args.write_report:
        write_result = write_output_inside_project(args.write_report, output, "relatorio")
        if write_result:
            return write_result

    if args.write_markdown:
        markdown = render_markdown_summary(result)
        write_result = write_output_inside_project(args.write_markdown, markdown, "resumo Markdown")
        if write_result:
            return write_result

    return 1 if result["status"] == "bloqueado" else 0


if __name__ == "__main__":
    raise SystemExit(main())
