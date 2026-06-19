#!/usr/bin/env python3
"""Comparador local de workflows n8n do SOC-Octopus-Agent.

Este script usa apenas biblioteca padrao, nao acessa rede, nao executa n8n
e nao altera os arquivos JSON comparados.
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

BLOCKING = "bloqueante"
REVIEW = "requer_revisao"
ACCEPTED = "aceitavel_com_registro"

ALLOWED_NODE_TYPES = {
    "n8n-nodes-base.manualTrigger",
    "n8n-nodes-base.set",
    "n8n-nodes-base.webhook",
    "n8n-nodes-base.respondToWebhook",
    "n8n-nodes-base.code",
    "n8n-nodes-base.if",
    "n8n-nodes-base.switch",
    "n8n-nodes-base.merge",
    "n8n-nodes-base.httpRequest",
    "n8n-nodes-base.postgres",
    "n8n-nodes-base.redis",
}

FORBIDDEN_NODE_HINTS = {
    "function": "Function",
    "mysql": "MySQL",
    "email": "E-mail",
    "smtp": "SMTP",
    "imap": "IMAP",
    "pop3": "POP3",
    "rabbitmq": "RabbitMQ",
    "kafka": "Kafka",
    "telegram": "Telegram",
    "slack": "Slack",
}

URL_PATTERN = re.compile(r"https?://", re.IGNORECASE)
SENSITIVE_ASSIGNMENT_PATTERN = re.compile(
    r"(?i)(password|senha|secret|tok" r"en|api[_-]?key)\s*[:=]"
)

EMPTY_VALUES = (None, {}, [])


class ComparisonReport:
    def __init__(self, base_path: Path, candidate_path: Path) -> None:
        self.base_path = base_path
        self.candidate_path = candidate_path
        self.items: list[dict[str, Any]] = []

    def add(
        self,
        path: str,
        base_value: Any,
        candidate_value: Any,
        classification: str,
        reason: str,
        action: str,
    ) -> None:
        self.items.append(
            {
                "id": f"DIV-{len(self.items) + 1:04d}",
                "json_path": path,
                "valor_base": base_value,
                "valor_comparado": candidate_value,
                "classificacao": classification,
                "justificativa": reason,
                "acao_recomendada": action,
            }
        )

    def counts(self) -> dict[str, int]:
        return {
            BLOCKING: sum(1 for item in self.items if item["classificacao"] == BLOCKING),
            REVIEW: sum(1 for item in self.items if item["classificacao"] == REVIEW),
            ACCEPTED: sum(1 for item in self.items if item["classificacao"] == ACCEPTED),
        }

    def status(self) -> str:
        counts = self.counts()
        if counts[BLOCKING]:
            return "bloqueado"
        if counts[REVIEW]:
            return "aprovado_com_ressalvas"
        return "aprovado"

    def decision(self) -> str:
        status = self.status()
        if status == "bloqueado":
            return (
                "Nao avancar. Corrigir ou justificar divergencias bloqueantes "
                "antes de qualquer proxima etapa."
            )
        if status == "aprovado_com_ressalvas":
            return (
                "Submeter divergencias de revisao a aprovacao humana antes de "
                "uso operacional ou importacao controlada."
            )
        return "Workflow comparado preserva a estrutura aprovada no escopo estatico."

    def as_dict(self) -> dict[str, Any]:
        counts = self.counts()
        status = self.status()
        return {
            "project": "SOC-Octopus-Agent",
            "tool": "06-tests/07-comparador-workflow-n8n.py",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "status": status,
            "arquivo_base": relative_display(self.base_path),
            "arquivo_comparado": relative_display(self.candidate_path),
            "total_divergencias": len(self.items),
            "divergencias_bloqueantes": counts[BLOCKING],
            "divergencias_requerem_revisao": counts[REVIEW],
            "divergencias_aceitaveis_com_registro": counts[ACCEPTED],
            "decisao_recomendada": self.decision(),
            "divergencias": self.items,
        }


def relative_display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def resolve_inside_project(path_argument: str, label: str) -> Path:
    path = (ROOT / path_argument).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"{label} deve ficar dentro do projeto") from exc
    return path


def load_json(path: Path, report: ComparisonReport, label: str) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except Exception as exc:  # noqa: BLE001 - erro completo precisa aparecer no relatorio
        report.add(
            "$",
            None,
            None,
            BLOCKING,
            f"{label} nao e JSON valido: {exc}",
            "Gerar nova exportacao JSON valida antes de comparar.",
        )
        return None


def read_text(path: Path, report: ComparisonReport, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        report.add(
            "$",
            None,
            None,
            BLOCKING,
            f"{label} nao pode ser lido: {exc}",
            "Verificar caminho e permissao local do arquivo.",
        )
        return ""


def is_empty_equivalent(base_value: Any, candidate_value: Any) -> bool:
    return base_value in EMPTY_VALUES and candidate_value in EMPTY_VALUES


def walk_values(value: Any, path: str = "$") -> list[tuple[str, Any]]:
    found = [(path, value)]
    if isinstance(value, dict):
        for key, child in value.items():
            found.extend(walk_values(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(walk_values(child, f"{path}[{index}]"))
    return found


def node_map(nodes: Any, report: ComparisonReport, source_label: str) -> dict[str, dict[str, Any]]:
    if not isinstance(nodes, list):
        report.add(
            "$.nodes",
            None,
            nodes,
            BLOCKING,
            f"{source_label} nao possui lista de nodes valida.",
            "Reexportar ou corrigir o workflow antes de comparar.",
        )
        return {}

    mapped: dict[str, dict[str, Any]] = {}
    duplicate_names: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            report.add(
                f"$.nodes[{index}]",
                None,
                node,
                BLOCKING,
                f"{source_label} contem node que nao e objeto JSON.",
                "Remover ou corrigir node invalido.",
            )
            continue
        name = node.get("name")
        if not isinstance(name, str) or not name:
            report.add(
                f"$.nodes[{index}].name",
                None,
                name,
                BLOCKING,
                f"{source_label} contem node sem nome valido.",
                "Reexportar workflow com nomes de nodes preservados.",
            )
            continue
        if name in mapped:
            duplicate_names.add(name)
        mapped[name] = node

    for name in sorted(duplicate_names):
        report.add(
            "$.nodes",
            None,
            name,
            BLOCKING,
            f"{source_label} contem nome de node duplicado.",
            "Garantir nomes unicos de nodes antes de comparar.",
        )

    return mapped


def compare_top_level(base: dict[str, Any], candidate: dict[str, Any], report: ComparisonReport) -> None:
    critical_missing = {"active", "nodes", "connections"}
    base_keys = set(base)
    candidate_keys = set(candidate)

    for key in sorted(base_keys - candidate_keys):
        classification = BLOCKING if key in critical_missing else REVIEW
        report.add(
            f"$.{key}",
            base.get(key),
            None,
            classification,
            "Campo top-level esperado nao existe no workflow comparado.",
            "Revisar exportacao e confirmar se o campo foi removido pelo n8n.",
        )

    for key in sorted(candidate_keys - base_keys):
        if key == "credentials":
            continue
        report.add(
            f"$.{key}",
            None,
            candidate.get(key),
            REVIEW,
            "Campo top-level novo encontrado no workflow comparado.",
            "Classificar impacto do campo antes de aceitar a diferenca.",
        )


def check_candidate_guards(candidate: dict[str, Any], text: str, report: ComparisonReport) -> None:
    if candidate.get("active") is not False:
        report.add(
            "$.active",
            False,
            candidate.get("active"),
            BLOCKING,
            "Workflow comparado nao esta explicitamente inativo.",
            "Manter active=false antes de qualquer importacao ou uso.",
        )

    for path, value in walk_values(candidate):
        if isinstance(value, dict) and "credentials" in value:
            report.add(
                f"{path}.credentials",
                None,
                value.get("credentials"),
                REVIEW,
                "Workflow comparado contem referencias credentials placeholder.",
                "Confirmar que nao ha valores secretos e que nenhuma credencial real foi exportada.",
            )
        if isinstance(value, str) and URL_PATTERN.search(value):
            report.add(
                path,
                None,
                value,
                BLOCKING,
                "Workflow comparado contem URL externa.",
                "Remover chamadas externas do workflow mockado.",
            )

    if SENSITIVE_ASSIGNMENT_PATTERN.search(text):
        report.add(
            "$",
            None,
            "padrao sensivel encontrado",
            BLOCKING,
            "Workflow comparado contem possivel atribuicao de dado sensivel.",
            "Substituir dado sensivel por valor mockado antes de nova comparacao.",
        )

    pin_data = candidate.get("pinData")
    static_data = candidate.get("staticData")
    if pin_data not in EMPTY_VALUES:
        report.add(
            "$.pinData",
            None,
            pin_data,
            BLOCKING,
            "Workflow comparado contem pinData com dados de execucao.",
            "Remover dados de execucao antes de aprovar a exportacao.",
        )
    if static_data not in EMPTY_VALUES:
        report.add(
            "$.staticData",
            None,
            static_data,
            BLOCKING,
            "Workflow comparado contem staticData preenchido.",
            "Remover dados persistidos antes de aprovar a exportacao.",
        )

    meta = candidate.get("meta")
    if isinstance(meta, dict):
        if meta.get("contains_credentials") is True:
            report.add(
                "$.meta.contains_credentials",
                False,
                True,
                BLOCKING,
                "Metadado indica presenca de credenciais.",
                "Reexportar workflow sem credenciais.",
            )
        profile = meta.get("validation_profile")
        if meta.get("contains_external_integrations") is True and profile not in {
            "lab-template",
            "prod-template",
        }:
            report.add(
                "$.meta.contains_external_integrations",
                False,
                True,
                BLOCKING,
                "Metadado indica integracoes externas fora de perfil permitido.",
                "Definir perfil lab-template/prod-template ou remover integracoes externas.",
            )
        if profile is None and meta.get("mock_only") is not True:
            report.add(
                "$.meta.validation_profile",
                "mock-executable | lab-template | prod-template",
                None,
                REVIEW,
                "Metadado nao informa perfil de validacao.",
                "Registrar validation_profile para diferenciar mock, laboratorio e template de producao.",
            )


def check_candidate_nodes(candidate_nodes: dict[str, dict[str, Any]], report: ComparisonReport) -> None:
    for name, node in sorted(candidate_nodes.items()):
        node_type = node.get("type")
        path = f"$.nodes[{name}].type"
        if node_type not in ALLOWED_NODE_TYPES:
            report.add(
                path,
                sorted(ALLOWED_NODE_TYPES),
                node_type,
                BLOCKING,
                "Workflow comparado contem tipo de node nao aprovado.",
                "Manter apenas Manual Trigger e Set neste pacote mockado.",
            )

        lowered_type = str(node_type).lower()
        for hint, label in sorted(FORBIDDEN_NODE_HINTS.items()):
            if hint in lowered_type:
                report.add(
                    path,
                    None,
                    node_type,
                    BLOCKING,
                    f"Workflow comparado contem node proibido: {label}.",
                    "Remover node proibido antes de qualquer proxima etapa.",
                )


def compare_node_order(base_nodes: Any, candidate_nodes: Any, report: ComparisonReport) -> None:
    if not isinstance(base_nodes, list) or not isinstance(candidate_nodes, list):
        return

    base_order = [node.get("name") for node in base_nodes if isinstance(node, dict)]
    candidate_order = [node.get("name") for node in candidate_nodes if isinstance(node, dict)]
    if base_order != candidate_order and set(base_order) == set(candidate_order):
        report.add(
            "$.nodes",
            base_order,
            candidate_order,
            REVIEW,
            "Ordem dos nodes mudou sem inclusao ou remocao aparente.",
            "Confirmar se a reordenacao nao altera leitura ou manutencao do fluxo.",
        )


def compare_nodes(
    base: dict[str, Any],
    candidate: dict[str, Any],
    report: ComparisonReport,
) -> None:
    base_nodes = node_map(base.get("nodes"), report, "Workflow base")
    candidate_nodes = node_map(candidate.get("nodes"), report, "Workflow comparado")

    compare_node_order(base.get("nodes"), candidate.get("nodes"), report)
    check_candidate_nodes(candidate_nodes, report)

    for name in sorted(set(base_nodes) - set(candidate_nodes)):
        report.add(
            f"$.nodes[{name}]",
            base_nodes[name],
            None,
            BLOCKING,
            "Node esperado esta ausente no workflow comparado.",
            "Restaurar node esperado ou justificar nova exportacao.",
        )

    for name in sorted(set(candidate_nodes) - set(base_nodes)):
        report.add(
            f"$.nodes[{name}]",
            None,
            candidate_nodes[name],
            BLOCKING,
            "Node inesperado foi incluido no workflow comparado.",
            "Remover node inesperado ou abrir revisao formal do desenho.",
        )

    for name in sorted(set(base_nodes) & set(candidate_nodes)):
        compare_single_node(name, base_nodes[name], candidate_nodes[name], report)


def compare_single_node(
    name: str,
    base_node: dict[str, Any],
    candidate_node: dict[str, Any],
    report: ComparisonReport,
) -> None:
    if base_node.get("type") != candidate_node.get("type"):
        report.add(
            f"$.nodes[{name}].type",
            base_node.get("type"),
            candidate_node.get("type"),
            BLOCKING,
            "Tipo do node mudou.",
            "Restaurar tipo aprovado do node.",
        )

    if base_node.get("parameters") != candidate_node.get("parameters"):
        report.add(
            f"$.nodes[{name}].parameters",
            base_node.get("parameters"),
            candidate_node.get("parameters"),
            BLOCKING,
            "Parametros do node mudaram e podem alterar a semantica mockada.",
            "Revisar e restaurar parametros aprovados antes de avancar.",
        )

    if base_node.get("typeVersion") != candidate_node.get("typeVersion"):
        report.add(
            f"$.nodes[{name}].typeVersion",
            base_node.get("typeVersion"),
            candidate_node.get("typeVersion"),
            REVIEW,
            "Versao do tipo de node mudou.",
            "Confirmar se a mudanca foi automatica do n8n e sem impacto funcional.",
        )

    if base_node.get("position") != candidate_node.get("position"):
        report.add(
            f"$.nodes[{name}].position",
            base_node.get("position"),
            candidate_node.get("position"),
            REVIEW,
            "Posicao visual do node mudou.",
            "Registrar diferenca visual se nao houver impacto no fluxo.",
        )

    if base_node.get("id") != candidate_node.get("id"):
        report.add(
            f"$.nodes[{name}].id",
            base_node.get("id"),
            candidate_node.get("id"),
            REVIEW,
            "Identificador interno do node mudou.",
            "Confirmar se o n8n regenerou o identificador sem alterar o fluxo.",
        )

    ignored = {"type", "parameters", "typeVersion", "position", "id", "name"}
    for key in sorted((set(base_node) | set(candidate_node)) - ignored):
        if base_node.get(key) != candidate_node.get(key):
            report.add(
                f"$.nodes[{name}].{key}",
                base_node.get(key),
                candidate_node.get(key),
                REVIEW,
                "Campo auxiliar do node mudou.",
                "Classificar impacto do campo antes de aceitar a diferenca.",
            )


def compare_connections(base: dict[str, Any], candidate: dict[str, Any], report: ComparisonReport) -> None:
    if base.get("connections") != candidate.get("connections"):
        report.add(
            "$.connections",
            base.get("connections"),
            candidate.get("connections"),
            BLOCKING,
            "Conexoes do workflow mudaram e podem alterar o fluxo aprovado.",
            "Restaurar fluxo linear aprovado ou abrir revisao formal.",
        )


def compare_mapping_field(
    field: str,
    base: dict[str, Any],
    candidate: dict[str, Any],
    report: ComparisonReport,
) -> None:
    base_value = base.get(field)
    candidate_value = candidate.get(field)
    path = f"$.{field}"
    if base_value == candidate_value:
        return

    if field in {"pinData", "staticData"} and is_empty_equivalent(base_value, candidate_value):
        report.add(
            path,
            base_value,
            candidate_value,
            ACCEPTED,
            "Campo vazio equivalente mudou de representacao.",
            "Registrar equivalencia e manter arquivos originais sem normalizacao.",
        )
        return

    report.add(
        path,
        base_value,
        candidate_value,
        REVIEW,
        f"Campo {field} mudou.",
        "Confirmar impacto da diferenca antes de aceitar a exportacao.",
    )


def compare_workflows(base: Any, candidate: Any, candidate_text: str, report: ComparisonReport) -> None:
    if not isinstance(base, dict):
        report.add(
            "$",
            None,
            base,
            BLOCKING,
            "Workflow base nao e objeto JSON.",
            "Usar workflow base aprovado em formato de objeto JSON.",
        )
        return
    if not isinstance(candidate, dict):
        report.add(
            "$",
            base,
            candidate,
            BLOCKING,
            "Workflow comparado nao e objeto JSON.",
            "Gerar exportacao n8n em formato de objeto JSON.",
        )
        return

    compare_top_level(base, candidate, report)
    check_candidate_guards(candidate, candidate_text, report)
    compare_nodes(base, candidate, report)
    compare_connections(base, candidate, report)

    for field in ("name", "settings", "meta", "pinData", "staticData", "tags"):
        compare_mapping_field(field, base, candidate, report)


def render_markdown_summary(result: dict[str, Any]) -> str:
    lines = [
        "# Resumo Da Comparacao De Workflow n8n",
        "",
        "## Status Consolidado",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Projeto | {result.get('project', 'SOC-Octopus-Agent')} |",
        f"| Status | {result.get('status', 'nao informado')} |",
        f"| Gerado em | {result.get('created_at', 'nao informado')} |",
        f"| Ferramenta | {result.get('tool', 'nao informado')} |",
        f"| Workflow base | {result.get('arquivo_base', 'nao informado')} |",
        f"| Workflow comparado | {result.get('arquivo_comparado', 'nao informado')} |",
        "",
        "## Totais",
        "",
        "| Metrica | Total |",
        "| --- | ---: |",
        f"| Divergencias | {result.get('total_divergencias', 0)} |",
        f"| Bloqueantes | {result.get('divergencias_bloqueantes', 0)} |",
        f"| Requerem revisao | {result.get('divergencias_requerem_revisao', 0)} |",
        "| Aceitaveis com registro | "
        f"{result.get('divergencias_aceitaveis_com_registro', 0)} |",
        "",
        "## Decisao Recomendada",
        "",
        f"- {result.get('decisao_recomendada', 'nao informado')}",
        "",
        "## Divergencias",
        "",
    ]

    divergences = result.get("divergencias", [])
    if not divergences:
        lines.append("- Nenhuma divergencia registrada.")
        lines.append("")
        return "\n".join(lines)

    lines.extend(
        [
            "| ID | Caminho JSON | Classificacao | Justificativa | Acao Recomendada |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in divergences:
        lines.append(
            "| "
            f"{item.get('id', '')} | "
            f"{item.get('json_path', '')} | "
            f"{item.get('classificacao', '')} | "
            f"{item.get('justificativa', '')} | "
            f"{item.get('acao_recomendada', '')} |"
        )
    lines.append("")
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
    parser = argparse.ArgumentParser(description="Comparador local de workflows n8n")
    parser.add_argument("--base", required=True, help="Workflow aprovado usado como base")
    parser.add_argument("--candidate", required=True, help="Workflow exportado para comparar")
    parser.add_argument("--write-report", help="Caminho para gravar relatorio JSON")
    parser.add_argument("--write-markdown", help="Caminho para gravar resumo Markdown")
    args = parser.parse_args()

    try:
        base_path = resolve_inside_project(args.base, "workflow base")
        candidate_path = resolve_inside_project(args.candidate, "workflow comparado")
    except ValueError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 2

    report = ComparisonReport(base_path, candidate_path)
    base_data = load_json(base_path, report, "Workflow base")
    candidate_text = read_text(candidate_path, report, "Workflow comparado")
    candidate_data = load_json(candidate_path, report, "Workflow comparado")

    if base_data is not None and candidate_data is not None:
        compare_workflows(base_data, candidate_data, candidate_text, report)

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
