#!/usr/bin/env python3
"""Validador local de prontidao para janela de laboratorio n8n.

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

PASS = "aprovado"
PENDING = "pendente"
BLOCK = "bloqueante"
WARN = "aviso"

REQUIRED_ARTIFACTS = [
    "01-docs/30-backlog-gates-decisao.md",
    "01-docs/61-checklist-operacional-importacao-n8n.md",
    "01-docs/64-registro-decisao-versao-n8n.md",
    "01-docs/67-criterios-ambiente-laboratorio-n8n.md",
    "01-docs/70-plano-evidencias-comparacao-pos-importacao-n8n.md",
    "01-docs/73-modelo-ata-janela-laboratorio-n8n.md",
    "01-docs/76-criterios-comparacao-automatizada-futura-n8n.md",
    "01-docs/82-guia-comparador-workflow-n8n.md",
    "01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md",
    "01-docs/86-roteiro-janela-laboratorio-n8n.md",
    "01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md",
    "02-workflows-n8n/soc-octopus-prototipo-mock.json",
    "06-tests/05-relatorio-validacao-estatica.json",
    "06-tests/06-resumo-validacao-estatica.md",
    "06-tests/07-comparador-workflow-n8n.py",
]

WORKFLOW_PATH = ROOT / "02-workflows-n8n" / "soc-octopus-prototipo-mock.json"
STATIC_REPORT_PATH = ROOT / "06-tests" / "05-relatorio-validacao-estatica.json"
VERSION_DECISION_PATH = ROOT / "01-docs" / "64-registro-decisao-versao-n8n.md"
MANIFEST_PATH = ROOT / "01-docs" / "85-manifesto-pacote-janela-laboratorio-n8n.md"
MATRIX_PATH = ROOT / "01-docs" / "87-matriz-evidencias-janela-laboratorio-n8n.md"
ATA_PATH = ROOT / "01-docs" / "73-modelo-ata-janela-laboratorio-n8n.md"
CHECKLIST_PATH = ROOT / "01-docs" / "61-checklist-operacional-importacao-n8n.md"

ALLOWED_NODE_TYPES = {
    "n8n-nodes-base.manualTrigger",
    "n8n-nodes-base.webhook",
    "n8n-nodes-base.respondToWebhook",
    "n8n-nodes-base.set",
    "n8n-nodes-base.code",
    "n8n-nodes-base.if",
    "n8n-nodes-base.switch",
    "n8n-nodes-base.merge",
    "n8n-nodes-base.httpRequest",
    "n8n-nodes-base.postgres",
    "n8n-nodes-base.redis",
}
URL_PATTERN = re.compile(r"https?://", re.IGNORECASE)


class ReadinessReport:
    def __init__(self) -> None:
        self.items: list[dict[str, Any]] = []

    def add(self, category: str, status: str, check: str, evidence: str, action: str) -> None:
        self.items.append(
            {
                "id": f"RDY-{len(self.items) + 1:04d}",
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
        return "pronto"

    def readiness_percent(self) -> int:
        counts = self.counts()
        total = sum(counts.values())
        if total == 0:
            return 0
        return round((counts[PASS] / total) * 100)

    def decision(self) -> str:
        status = self.status()
        if status == "bloqueado":
            return (
                "Nao abrir janela de laboratorio. Resolver pendencias bloqueantes "
                "e registrar aprovacao humana antes de qualquer acao no n8n."
            )
        if status == "pronto_com_ressalvas":
            return "Revisar avisos antes de abrir uma janela formalmente aprovada."
        return "Pacote pronto para avaliacao humana de abertura de janela."

    def as_dict(self) -> dict[str, Any]:
        counts = self.counts()
        return {
            "project": "SOC-Octopus-Agent",
            "validator": "06-tests/10-validador-prontidao-janela-n8n.py",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status": self.status(),
            "percentual_prontidao_estimado": self.readiness_percent(),
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


def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def check_required_artifacts(report: ReadinessReport) -> None:
    for rel in REQUIRED_ARTIFACTS:
        path = ROOT / rel
        if path.is_file():
            report.add(
                "artefatos",
                PASS,
                f"Artefato obrigatorio encontrado: {rel}",
                rel,
                "Nenhuma acao.",
            )
        else:
            report.add(
                "artefatos",
                BLOCK,
                f"Artefato obrigatorio ausente: {rel}",
                rel,
                "Criar ou restaurar artefato antes de qualquer janela.",
            )


def check_static_validation(report: ReadinessReport) -> None:
    if not STATIC_REPORT_PATH.is_file():
        report.add(
            "validacao",
            BLOCK,
            "Relatorio do validador estatico ausente.",
            relative(STATIC_REPORT_PATH),
            "Executar validador estatico local antes de avaliar prontidao.",
        )
        return

    try:
        data = load_json(STATIC_REPORT_PATH)
    except Exception as exc:  # noqa: BLE001 - relatorio precisa ser revisavel
        report.add(
            "validacao",
            BLOCK,
            "Relatorio do validador estatico nao e JSON valido.",
            str(exc),
            "Regenerar relatorio do validador estatico.",
        )
        return

    summary = data.get("summary", {}) if isinstance(data, dict) else {}
    failures = int(summary.get("failures", -1))
    warnings = int(summary.get("warnings", 0))
    passed = int(summary.get("passed", 0))

    if failures == 0:
        report.add(
            "validacao",
            PASS,
            "Validador estatico local sem falhas.",
            f"{passed} aprovacoes, {warnings} warnings, {failures} falhas",
            "Atualizar novamente antes de qualquer janela real.",
        )
    else:
        report.add(
            "validacao",
            BLOCK,
            "Validador estatico local possui falhas.",
            f"{failures} falhas",
            "Corrigir falhas antes de avaliar janela.",
        )

    if warnings:
        report.add(
            "validacao",
            WARN,
            "Validador estatico local possui warnings.",
            f"{warnings} warnings",
            "Revisar warnings antes de janela aprovada.",
        )


def check_workflow(report: ReadinessReport) -> None:
    if not WORKFLOW_PATH.is_file():
        report.add(
            "workflow",
            BLOCK,
            "Workflow alvo ausente.",
            relative(WORKFLOW_PATH),
            "Restaurar workflow alvo aprovado.",
        )
        return

    text = read_text(WORKFLOW_PATH)
    try:
        data = json.loads(text)
    except Exception as exc:  # noqa: BLE001
        report.add(
            "workflow",
            BLOCK,
            "Workflow alvo nao e JSON valido.",
            str(exc),
            "Corrigir JSON antes de qualquer janela.",
        )
        return

    if data.get("active") is False:
        report.add(
            "workflow",
            PASS,
            "Workflow alvo esta inativo.",
            "active=false",
            "Manter workflow inativo na janela futura.",
        )
    else:
        report.add(
            "workflow",
            BLOCK,
            "Workflow alvo nao esta inativo.",
            f"active={data.get('active')}",
            "Bloquear janela ate active=false.",
        )

    if '"credentials"' in text:
        report.add(
            "workflow",
            WARN,
            "Workflow alvo contem referencias credentials placeholder.",
            relative(WORKFLOW_PATH),
            "Confirmar no n8n que nenhuma credencial real foi vinculada automaticamente.",
        )
    else:
        report.add(
            "workflow",
            PASS,
            "Workflow alvo sem campo credentials.",
            relative(WORKFLOW_PATH),
            "Nenhuma acao.",
        )

    if URL_PATTERN.search(text):
        report.add(
            "workflow",
            BLOCK,
            "Workflow alvo contem URL externa.",
            relative(WORKFLOW_PATH),
            "Remover URL externa antes da janela.",
        )
    else:
        report.add(
            "workflow",
            PASS,
            "Workflow alvo sem URL externa.",
            relative(WORKFLOW_PATH),
            "Nenhuma acao.",
        )

    nodes = data.get("nodes", [])
    node_types = {
        node.get("type")
        for node in nodes
        if isinstance(node, dict) and isinstance(node.get("type"), str)
    }
    unexpected = sorted(node_types - ALLOWED_NODE_TYPES)
    if unexpected:
        report.add(
            "workflow",
            BLOCK,
            "Workflow alvo contem tipo de node nao aprovado.",
            ", ".join(unexpected),
            "Revisar perfil do workflow e atualizar allowlist somente com aprovacao tecnica.",
        )
    else:
        report.add(
            "workflow",
            PASS,
            "Workflow alvo usa apenas tipos de node permitidos.",
            ", ".join(sorted(node_types)),
            "Nenhuma acao.",
        )

    webhooks = [
        node for node in nodes
        if isinstance(node, dict) and node.get("type") == "n8n-nodes-base.webhook"
    ]
    for node in webhooks:
        parameters = node.get("parameters", {})
        credentials = node.get("credentials", {})
        auth = parameters.get("authentication") if isinstance(parameters, dict) else None
        if auth in {"basicAuth", "headerAuth", "jwtAuth"} and isinstance(credentials, dict) and credentials:
            report.add(
                "workflow",
                PASS,
                f"Webhook com autenticacao configurada: {node.get('name')}.",
                f"authentication={auth}",
                "Confirmar credencial correta no n8n antes de qualquer ativacao.",
            )
        else:
            report.add(
                "workflow",
                BLOCK,
                f"Webhook sem autenticacao configurada: {node.get('name')}.",
                f"authentication={auth}",
                "Configurar autenticacao no template antes da janela.",
            )


def has_pending_marker(text: str, markers: list[str]) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in markers)


def check_decision_and_environment(report: ReadinessReport) -> None:
    version_text = read_text(VERSION_DECISION_PATH) if VERSION_DECISION_PATH.is_file() else ""
    if has_pending_marker(version_text, ["Nao decidido", "Pendente"]):
        report.add(
            "decisao",
            PENDING,
            "Versao alvo do n8n ainda nao esta decidida.",
            relative(VERSION_DECISION_PATH),
            "Preencher e aprovar registro de decisao da versao alvo.",
        )
    else:
        report.add(
            "decisao",
            PASS,
            "Versao alvo do n8n registrada.",
            relative(VERSION_DECISION_PATH),
            "Confirmar data e responsavel antes da janela.",
        )

    matrix_text = read_text(MATRIX_PATH) if MATRIX_PATH.is_file() else ""
    required_fields = [
        "Janela | Pendente",
        "Ambiente | Pendente",
        "Versao alvo do n8n | Pendente",
        "Responsavel tecnico | Pendente",
        "Responsavel pela aprovacao humana | Pendente",
    ]
    for field in required_fields:
        if field.lower() in matrix_text.lower():
            label = field.split("|", maxsplit=1)[0].strip()
            report.add(
                "ambiente",
                PENDING,
                f"Campo de identificacao pendente: {label}.",
                relative(MATRIX_PATH),
                "Preencher somente com informacao confirmada por responsavel humano.",
            )


def check_unchecked_gates(report: ReadinessReport) -> None:
    gate_sources = [
        ("manifesto", MANIFEST_PATH, "Gates do manifesto ainda nao marcados."),
        ("checklist", CHECKLIST_PATH, "Checklist operacional contem itens nao marcados."),
        ("matriz", MATRIX_PATH, "Matriz de evidencias contem evidencias pendentes."),
        ("ata", ATA_PATH, "Modelo de ata contem campos pendentes."),
    ]

    for category, path, message in gate_sources:
        if not path.is_file():
            continue
        text = read_text(path)
        unchecked = len(re.findall(r"- \[ \]", text))
        pending = len(re.findall(r"\bPendente\b", text, flags=re.IGNORECASE))
        if unchecked or pending:
            report.add(
                category,
                PENDING,
                message,
                f"{unchecked} checkboxes vazios, {pending} marcadores pendentes",
                "Preencher e aprovar itens obrigatorios antes da janela.",
            )
        else:
            report.add(
                category,
                PASS,
                "Sem itens pendentes aparentes.",
                relative(path),
                "Revisar manualmente antes da janela.",
            )


def run_readiness() -> ReadinessReport:
    report = ReadinessReport()
    check_required_artifacts(report)
    check_static_validation(report)
    check_workflow(report)
    check_decision_and_environment(report)
    check_unchecked_gates(report)
    return report


def render_markdown_summary(result: dict[str, Any]) -> str:
    summary = result.get("summary", {})
    lines = [
        "# Resumo Da Prontidao Da Janela n8n",
        "",
        "## Status Consolidado",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Projeto | {result.get('project', 'SOC-Octopus-Agent')} |",
        f"| Status | {result.get('status', 'nao informado')} |",
        f"| Percentual estimado | {result.get('percentual_prontidao_estimado', 0)}% |",
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
            "- Resultado gerado localmente.",
            "- O status bloqueado e esperado enquanto versao, ambiente e aprovacao humana estiverem pendentes.",
            "- Este resumo nao autoriza importacao, exportacao ou execucao no n8n.",
        ]
    )
    return "\n".join(lines)


def write_output_inside_project(path_argument: str, content: str, label: str) -> int:
    output_path = (ROOT / path_argument).resolve()
    try:
        output_path.relative_to(ROOT)
    except ValueError:
        print(f"Erro: {label} deve ficar dentro do projeto", file=sys.stderr)
        return 2
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content + "\n", encoding="utf-8")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validador de prontidao da janela n8n")
    parser.add_argument("--write-report", help="Caminho para gravar relatorio JSON")
    parser.add_argument("--write-markdown", help="Caminho para gravar resumo Markdown")
    args = parser.parse_args()

    report = run_readiness()
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
