#!/usr/bin/env python3
"""Gerador local de plano de pendencias da janela n8n.

Este script usa apenas biblioteca padrao, nao acessa rede, nao executa n8n
e nao altera os artefatos avaliados.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_READINESS_REPORT = ROOT / "06-tests" / "11-relatorio-prontidao-janela-n8n.json"

ACTIONABLE_STATUSES = {"pendente", "bloqueante", "aviso"}
BLOCKING_STATUSES = {"pendente", "bloqueante"}

CATEGORY_OWNER = {
    "decisao": "responsavel pela aprovacao humana",
    "ambiente": "responsavel tecnico",
    "manifesto": "responsavel pela aprovacao humana",
    "checklist": "responsavel tecnico",
    "matriz": "responsavel tecnico",
    "ata": "responsavel pela aprovacao humana",
    "validacao": "responsavel tecnico",
    "workflow": "responsavel tecnico",
    "artefatos": "responsavel tecnico",
}

CATEGORY_EVIDENCE = {
    "decisao": "01-docs/64-registro-decisao-versao-n8n.md",
    "ambiente": "01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md",
    "manifesto": "01-docs/85-manifesto-pacote-janela-laboratorio-n8n.md",
    "checklist": "01-docs/61-checklist-operacional-importacao-n8n.md",
    "matriz": "01-docs/87-matriz-evidencias-janela-laboratorio-n8n.md",
    "ata": "01-docs/73-modelo-ata-janela-laboratorio-n8n.md",
    "validacao": "06-tests/06-resumo-validacao-estatica.md",
    "workflow": "02-workflows-n8n/soc-octopus-prototipo-mock.json",
    "artefatos": "01-docs/28-indice-mestre.md",
}

CATEGORY_SEQUENCE = {
    "decisao": 1,
    "ambiente": 2,
    "manifesto": 3,
    "checklist": 4,
    "matriz": 5,
    "ata": 6,
    "validacao": 7,
    "workflow": 8,
    "artefatos": 9,
}


def resolve_inside_project(path_argument: str, label: str) -> Path:
    path = (ROOT / path_argument).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"{label} deve ficar dentro do projeto") from exc
    return path


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def status_from_actions(actions: list[dict[str, Any]]) -> str:
    if any(action["bloqueia_janela"] for action in actions):
        return "bloqueado"
    if actions:
        return "pendente_com_avisos"
    return "sem_pendencias"


def priority_for(item: dict[str, Any]) -> str:
    status = item.get("status")
    category = item.get("categoria")
    if status == "bloqueante":
        return "P0"
    if category in {"decisao", "ambiente"}:
        return "P0"
    if category in {"manifesto", "checklist", "matriz", "ata"}:
        return "P1"
    return "P2"


def action_type_for(category: str) -> str:
    if category == "decisao":
        return "decisao_humana"
    if category == "ambiente":
        return "preenchimento_operacional"
    if category in {"manifesto", "checklist", "matriz", "ata"}:
        return "aprovacao_documental"
    return "correcao_tecnica"


def build_action(item: dict[str, Any], number: int) -> dict[str, Any]:
    category = str(item.get("categoria", "geral"))
    status = str(item.get("status", "pendente"))
    evidence = str(item.get("evidencia", CATEGORY_EVIDENCE.get(category, "nao informado")))
    expected_evidence = CATEGORY_EVIDENCE.get(category, evidence)
    return {
        "id": f"ACT-{number:04d}",
        "origem": item.get("id", "sem_id"),
        "categoria": category,
        "prioridade": priority_for(item),
        "tipo": action_type_for(category),
        "bloqueia_janela": status in BLOCKING_STATUSES,
        "pendencia": item.get("checagem", "Pendencia sem descricao."),
        "evidencia_atual": evidence,
        "evidencia_esperada": expected_evidence,
        "responsavel_sugerido": CATEGORY_OWNER.get(category, "responsavel definido pela janela"),
        "acao_recomendada": item.get("acao_recomendada", "Revisar pendencia antes da janela."),
        "status": "aberta",
    }


def generate_plan(readiness: dict[str, Any]) -> dict[str, Any]:
    checks = readiness.get("checks", [])
    if not isinstance(checks, list):
        checks = []

    pending_items = [
        item
        for item in checks
        if isinstance(item, dict) and item.get("status") in ACTIONABLE_STATUSES
    ]
    pending_items.sort(
        key=lambda item: (
            CATEGORY_SEQUENCE.get(str(item.get("categoria", "")), 99),
            str(item.get("id", "")),
        )
    )
    actions = [build_action(item, index + 1) for index, item in enumerate(pending_items)]
    status = status_from_actions(actions)

    return {
        "project": "SOC-Octopus-Agent",
        "generator": "06-tests/13-gerador-plano-pendencias-janela-n8n.py",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "fonte": readiness.get("validator", "06-tests/10-validador-prontidao-janela-n8n.py"),
        "status_origem": readiness.get("status", "nao informado"),
        "status": status,
        "total_acoes": len(actions),
        "acoes_bloqueiam_janela": sum(1 for action in actions if action["bloqueia_janela"]),
        "acoes_por_prioridade": {
            "P0": sum(1 for action in actions if action["prioridade"] == "P0"),
            "P1": sum(1 for action in actions if action["prioridade"] == "P1"),
            "P2": sum(1 for action in actions if action["prioridade"] == "P2"),
        },
        "decisao_recomendada": decision_for(status, actions),
        "acoes": actions,
    }


def decision_for(status: str, actions: list[dict[str, Any]]) -> str:
    if status == "bloqueado":
        return (
            "Manter janela n8n bloqueada. Resolver acoes P0 e P1 com aprovacao humana "
            "antes de qualquer importacao, exportacao ou execucao."
        )
    if status == "pendente_com_avisos":
        return "Revisar avisos antes de solicitar aprovacao formal da janela."
    return "Nenhuma pendencia acionavel encontrada no relatorio de prontidao."


def render_markdown_summary(plan: dict[str, Any]) -> str:
    priorities = plan.get("acoes_por_prioridade", {})
    lines = [
        "# Plano De Pendencias Da Janela n8n",
        "",
        "## Status Consolidado",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Projeto | {plan.get('project', 'SOC-Octopus-Agent')} |",
        f"| Status | {plan.get('status', 'nao informado')} |",
        f"| Status da origem | {plan.get('status_origem', 'nao informado')} |",
        f"| Gerado em | {plan.get('created_at', 'nao informado')} |",
        f"| Gerador | {plan.get('generator', 'nao informado')} |",
        "",
        "## Totais",
        "",
        "| Metrica | Total |",
        "| --- | ---: |",
        f"| Acoes | {plan.get('total_acoes', 0)} |",
        f"| Acoes que bloqueiam a janela | {plan.get('acoes_bloqueiam_janela', 0)} |",
        f"| P0 | {priorities.get('P0', 0)} |",
        f"| P1 | {priorities.get('P1', 0)} |",
        f"| P2 | {priorities.get('P2', 0)} |",
        "",
        "## Decisao Recomendada",
        "",
        f"- {plan.get('decisao_recomendada', 'nao informado')}",
        "",
        "## Acoes",
        "",
    ]

    actions = plan.get("acoes", [])
    if not actions:
        lines.append("- Nenhuma acao pendente registrada.")
    else:
        lines.extend(
            [
                "| ID | Prioridade | Categoria | Responsavel Sugerido | Pendencia | Acao Recomendada |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for action in actions:
            lines.append(
                "| "
                f"{action.get('id', '')} | "
                f"{action.get('prioridade', '')} | "
                f"{action.get('categoria', '')} | "
                f"{action.get('responsavel_sugerido', '')} | "
                f"{action.get('pendencia', '')} | "
                f"{action.get('acao_recomendada', '')} |"
            )

    lines.extend(
        [
            "",
            "## Observacoes",
            "",
            "- Plano gerado localmente a partir do relatorio de prontidao.",
            "- O plano nao preenche campos operacionais por inferencia.",
            "- Este plano nao autoriza importacao, exportacao ou execucao no n8n.",
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
    parser = argparse.ArgumentParser(description="Gerador local de plano de pendencias n8n")
    parser.add_argument(
        "--readiness-report",
        default=str(DEFAULT_READINESS_REPORT.relative_to(ROOT)),
        help="Relatorio JSON do validador de prontidao",
    )
    parser.add_argument("--write-report", help="Caminho para gravar relatorio JSON")
    parser.add_argument("--write-markdown", help="Caminho para gravar resumo Markdown")
    args = parser.parse_args()

    try:
        readiness_path = resolve_inside_project(args.readiness_report, "relatorio de prontidao")
        readiness = load_json(readiness_path)
    except Exception as exc:  # noqa: BLE001 - erro deve ser reportado ao operador local
        print(f"Erro: falha ao ler relatorio de prontidao ({exc})", file=sys.stderr)
        return 2

    if not isinstance(readiness, dict):
        print("Erro: relatorio de prontidao deve ser objeto JSON", file=sys.stderr)
        return 2

    plan = generate_plan(readiness)
    output = json.dumps(plan, indent=2, ensure_ascii=False)
    print(output)

    if args.write_report:
        write_result = write_output_inside_project(args.write_report, output, "relatorio")
        if write_result:
            return write_result

    if args.write_markdown:
        markdown = render_markdown_summary(plan)
        write_result = write_output_inside_project(args.write_markdown, markdown, "resumo Markdown")
        if write_result:
            return write_result

    return 1 if plan["status"] == "bloqueado" else 0


if __name__ == "__main__":
    raise SystemExit(main())
