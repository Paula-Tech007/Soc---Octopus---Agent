#!/usr/bin/env python3
"""Validador estatico local do SOC-Octopus-Agent.

O validador usa somente biblioteca padrao, nao acessa rede, nao executa n8n,
nao executa SQL e nao altera artefatos de entrada.
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

REQUIRED_DIRS = [
    "01-docs",
    "02-workflows-n8n",
    "03-prompts",
    "04-payloads-mock",
    "05-sql",
    "06-tests",
    "07-diagrams",
]

REQUIRED_GITHUB_FILES = [
    ".gitignore",
    "README.md",
    "SECURITY.md",
    "LICENSE",
]

INPUT_TYPES = {"soc_alert", "ticket", "event", "question"}
ROOT_CAUSES = {
    "identity",
    "endpoint",
    "network",
    "cloud",
    "vulnerability",
    "external_threat",
    "false_positive",
    "unknown",
}
RISK_LEVELS = {"low", "medium", "high", "critical"}
CONFIDENCE_LEVELS = {"low", "medium", "high"}
SEVERITY_ORDER = ["critical", "high", "medium", "low"]

NODE_TYPES_BY_PROFILE = {
    "mock-static": {
        "n8n-nodes-base.manualTrigger",
        "n8n-nodes-base.set",
    },
    "mock-executable": {
        "n8n-nodes-base.manualTrigger",
        "n8n-nodes-base.set",
        "n8n-nodes-base.code",
        "n8n-nodes-base.if",
        "n8n-nodes-base.respondToWebhook",
    },
    "lab-template": {
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
    },
    "prod-template": {
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
    },
}

FALLIBLE_NODE_TYPES = {
    "n8n-nodes-base.httpRequest",
    "n8n-nodes-base.postgres",
    "n8n-nodes-base.redis",
}

WEBHOOK_AUTH_VALUES = {"basicAuth", "headerAuth", "jwtAuth"}

SECRET_VALUE_PATTERNS = {
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "bearer_token": re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b"),
    "private_key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}

SECRET_ASSIGNMENT_PATTERN = re.compile(
    r"(?i)\b(password|passwd|senha|secret|token|api[_-]?key|client_secret)\b"
    r"\s*[:=]\s*"
    r"(?!<valor|valor de|pendente|false|true|null|REPLACE_|SOC_|\\$|\\{\\{|\"\$|'\$)"
    r"[\"']?[A-Za-z0-9_./+=@:-]{12,}"
)

SECRET_ENV_DEFAULT_PATTERN = re.compile(
    r"(?i)\$\{[A-Z0-9_]*(password|passwd|senha|secret|token|api[_-]?key|client_secret)"
    r"[A-Z0-9_]*:-"
    r"(?!<valor|valor de|pendente|false|true|null|REPLACE_)"
    r"[A-Za-z0-9_./+=@:-]{8,}\}"
)

CONNECTION_STRING_PATTERN = re.compile(
    r"(?i)(jdbc:|mysql://|mariadb://|postgres://|postgresql://|server\s*=|uid\s*=)"
)


class ValidationReport:
    def __init__(self) -> None:
        self.passed: list[str] = []
        self.warnings: list[str] = []
        self.failures: list[str] = []
        self.categories: dict[str, dict[str, int]] = {}
        self.severity_summary: dict[str, dict[str, int]] = {
            "critical": {"passed": 0, "warnings": 0, "failures": 0},
            "high": {"passed": 0, "warnings": 0, "failures": 0},
            "medium": {"passed": 0, "warnings": 0, "failures": 0},
            "low": {"passed": 0, "warnings": 0, "failures": 0},
        }

    def pass_(self, message: str) -> None:
        self.passed.append(message)
        self._count("passed", message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)
        self._count("warnings", message)

    def fail(self, message: str) -> None:
        self.failures.append(message)
        self._count("failures", message)

    def _count(self, status: str, message: str) -> None:
        category = self._category_for(message)
        self.categories.setdefault(category, {"passed": 0, "warnings": 0, "failures": 0})
        self.categories[category][status] += 1
        severity = self._severity_for(category, status)
        self.severity_summary[severity][status] += 1

    def _category_for(self, message: str) -> str:
        lowered = message.lower()
        if "github" in lowered or ".gitignore" in lowered or "readme" in lowered:
            return "github"
        if "pasta obrigatoria" in lowered:
            return "estrutura"
        if "json valido" in lowered or "json invalido" in lowered:
            return "json"
        if "payload" in lowered or "governanca" in lowered:
            return "payloads"
        if "workflow" in lowered or "node" in lowered or "webhook" in lowered:
            return "workflow"
        if "sql" in lowered or "postgres" in lowered:
            return "sql"
        if "cenario" in lowered or "cobertura" in lowered:
            return "testes"
        if "memoria" in lowered or "retencao" in lowered:
            return "memoria"
        if (
            "segredo" in lowered
            or "secret" in lowered
            or "credencial" in lowered
            or "token" in lowered
            or "string de conexao" in lowered
        ):
            return "seguranca"
        return "geral"

    def _severity_for(self, category: str, status: str) -> str:
        if status == "failures" and category in {"workflow", "sql", "seguranca"}:
            return "critical"
        if status == "failures":
            return "high"
        if status == "warnings" and category in {"workflow", "sql", "seguranca"}:
            return "medium"
        return "low"

    def as_dict(self) -> dict[str, Any]:
        return {
            "project": "SOC-Octopus-Agent",
            "validator": "06-tests/04-validador-estatico.py",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "summary": {
                "passed": len(self.passed),
                "warnings": len(self.warnings),
                "failures": len(self.failures),
            },
            "categories": dict(sorted(self.categories.items())),
            "severity_summary": self.severity_summary,
            "passed": self.passed,
            "warnings": self.warnings,
            "failures": self.failures,
        }


def load_json(path: Path, report: ValidationReport) -> Any | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception as exc:  # noqa: BLE001
        report.fail(f"JSON invalido: {path.relative_to(ROOT)} ({exc})")
        return None
    report.pass_(f"JSON valido: {path.relative_to(ROOT)}")
    return data


def read_text(path: Path, report: ValidationReport) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        report.fail(f"Falha ao ler {path.relative_to(ROOT)} ({exc})")
        return ""


def iter_strings(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, str):
        found.append(value)
    elif isinstance(value, dict):
        for child in value.values():
            found.extend(iter_strings(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(iter_strings(child))
    return found


def has_credentials(node: dict[str, Any]) -> bool:
    credentials = node.get("credentials")
    return isinstance(credentials, dict) and bool(credentials)


def node_names(nodes: list[dict[str, Any]]) -> set[str]:
    return {node["name"] for node in nodes if isinstance(node.get("name"), str)}


def profile_for(workflow: dict[str, Any], path: Path) -> str:
    meta = workflow.get("meta")
    if isinstance(meta, dict):
        explicit = meta.get("validation_profile")
        if explicit in NODE_TYPES_BY_PROFILE:
            return str(explicit)
        if meta.get("production_ready") is True or meta.get("phase") == "production-ready":
            return "prod-template"
        if meta.get("status") == "lab-template":
            return "lab-template"

    text = json.dumps(workflow, ensure_ascii=False)
    if '"n8n-nodes-base.httpRequest"' in text or '"n8n-nodes-base.postgres"' in text:
        return "lab-template" if path.name.endswith("-intake.json") else "prod-template"
    if '"n8n-nodes-base.code"' in text or '"n8n-nodes-base.respondToWebhook"' in text:
        return "mock-executable"
    return "mock-static"


def check_required_dirs(report: ValidationReport) -> None:
    for rel in REQUIRED_DIRS:
        path = ROOT / rel
        if path.is_dir():
            report.pass_(f"Pasta obrigatoria encontrada: {rel}")
        else:
            report.fail(f"Pasta obrigatoria ausente: {rel}")


def check_github_hygiene(report: ValidationReport) -> None:
    for rel in REQUIRED_GITHUB_FILES:
        path = ROOT / rel
        if path.is_file():
            report.pass_(f"GitHub: artefato encontrado: {rel}")
        else:
            report.fail(f"GitHub: artefato ausente: {rel}")

    gitignore = ROOT / ".gitignore"
    if gitignore.is_file():
        text = read_text(gitignore, report)
        if ".env.*" in text and "!.env*.example" in text:
            report.pass_("GitHub: .gitignore protege env local e preserva exemplos")
        else:
            report.fail("GitHub: .gitignore nao protege corretamente arquivos .env")


def check_consolidated_output(path: Path, data: dict[str, Any], report: ValidationReport) -> None:
    required = {
        "case_id",
        "trace_id",
        "status",
        "executive_summary",
        "probable_root_cause",
        "risk_level",
        "evidence_summary",
        "specialists_involved",
        "recommended_solution",
        "technical_steps",
        "escalation_recommended",
        "security_notes",
        "confidence_level",
        "possible_false_positive",
        "human_approval_required",
        "audit",
    }
    missing = sorted(required - set(data))
    if missing:
        report.fail(f"{path.name}: campos obrigatorios de saida ausentes: {missing}")
        return
    report.pass_(f"{path.name}: campos obrigatorios de saida presentes")

    if data.get("probable_root_cause") not in ROOT_CAUSES:
        report.fail(f"{path.name}: probable_root_cause invalido: {data.get('probable_root_cause')}")
    if data.get("risk_level") not in RISK_LEVELS:
        report.fail(f"{path.name}: risk_level invalido: {data.get('risk_level')}")
    if data.get("confidence_level") not in CONFIDENCE_LEVELS:
        report.fail(f"{path.name}: confidence_level invalido: {data.get('confidence_level')}")
    if not isinstance(data.get("possible_false_positive"), bool):
        report.fail(f"{path.name}: possible_false_positive deve ser boolean")
    if not isinstance(data.get("human_approval_required"), bool):
        report.fail(f"{path.name}: human_approval_required deve ser boolean")

    audit = data.get("audit")
    if isinstance(audit, dict):
        if audit.get("mock_payload") is not True:
            report.fail(f"{path.name}: audit.mock_payload deve ser true")
        if audit.get("contains_real_customer_data") is not False:
            report.fail(f"{path.name}: audit.contains_real_customer_data deve ser false")
        if audit.get("contains_credentials") is not False:
            report.fail(f"{path.name}: audit.contains_credentials deve ser false")
        report.pass_(f"{path.name}: auditoria de saida avaliada")
    else:
        report.fail(f"{path.name}: audit ausente ou invalido")


def check_payloads(report: ValidationReport) -> None:
    payload_dir = ROOT / "04-payloads-mock"
    payloads = sorted(payload_dir.glob("*.json"))
    if not payloads:
        report.fail("Nenhum payload mockado encontrado em 04-payloads-mock")
        return

    required = {
        "case_id",
        "trace_id",
        "input_type",
        "source_system",
        "received_at",
        "severity",
        "title",
        "description",
        "governance",
    }

    for path in payloads:
        data = load_json(path, report)
        if data is None:
            continue

        if path.name == "saida-consolidada-mock.json":
            if isinstance(data, dict):
                check_consolidated_output(path, data, report)
            else:
                report.fail(f"{path.name}: saida consolidada deve ser objeto JSON")
            continue

        missing = sorted(required - set(data))
        if missing:
            report.fail(f"{path.name}: campos obrigatorios ausentes: {missing}")
        else:
            report.pass_(f"{path.name}: campos obrigatorios presentes")

        if data.get("input_type") and data.get("input_type") not in INPUT_TYPES:
            report.fail(f"{path.name}: input_type invalido: {data.get('input_type')}")
        if data.get("severity") and data.get("severity") not in RISK_LEVELS:
            report.fail(f"{path.name}: severity invalida: {data.get('severity')}")
        if data.get("classification_hint") and data.get("classification_hint") not in ROOT_CAUSES:
            report.fail(f"{path.name}: classification_hint invalido: {data.get('classification_hint')}")

        governance = data.get("governance")
        if isinstance(governance, dict):
            if governance.get("contains_real_customer_data") is not False:
                report.fail(f"{path.name}: contains_real_customer_data deve ser false")
            if governance.get("contains_credentials") is not False:
                report.fail(f"{path.name}: contains_credentials deve ser false")
            if governance.get("mock_payload") is not True:
                report.fail(f"{path.name}: mock_payload deve ser true")
            report.pass_(f"{path.name}: flags de governanca avaliadas")
        else:
            report.fail(f"{path.name}: governance ausente ou invalido")


def check_workflow_connections(
    workflow_name: str,
    data: dict[str, Any],
    valid_names: set[str],
    report: ValidationReport,
) -> None:
    connections = data.get("connections")
    if not isinstance(connections, dict):
        report.fail(f"{workflow_name}: workflow sem objeto de conexoes valido")
        return

    ok = True
    for source_name, outputs in connections.items():
        if source_name not in valid_names or not isinstance(outputs, dict):
            ok = False
            continue
        main_outputs = outputs.get("main")
        if not isinstance(main_outputs, list):
            ok = False
            continue
        for output_group in main_outputs:
            if not isinstance(output_group, list):
                ok = False
                continue
            for connection in output_group:
                if not isinstance(connection, dict):
                    ok = False
                    continue
                if connection.get("node") not in valid_names:
                    ok = False
                if connection.get("type") != "main":
                    ok = False
                if not isinstance(connection.get("index"), int) or connection.get("index") < 0:
                    ok = False

    if ok:
        report.pass_(f"{workflow_name}: conexoes referenciam apenas nodes existentes")
    else:
        report.fail(f"{workflow_name}: possui conexao invalida ou node inexistente")


def check_fallible_error_outputs(
    workflow_name: str,
    data: dict[str, Any],
    nodes: list[dict[str, Any]],
    report: ValidationReport,
) -> None:
    connections = data.get("connections")
    if not isinstance(connections, dict):
        return

    for node in nodes:
        if node.get("type") not in FALLIBLE_NODE_TYPES:
            continue
        if node.get("onError") != "continueErrorOutput":
            continue

        node_name = node.get("name")
        node_connections = connections.get(node_name)
        main_outputs = node_connections.get("main") if isinstance(node_connections, dict) else None
        has_error_output = (
            isinstance(main_outputs, list)
            and len(main_outputs) > 1
            and isinstance(main_outputs[1], list)
            and len(main_outputs[1]) > 0
        )
        if has_error_output:
            report.pass_(f"{workflow_name}: node falivel {node_name} possui conexao na saida de erro")
        else:
            report.fail(f"{workflow_name}: node falivel {node_name} usa saida de erro sem conexao dedicada")


def query_has_replacement(parameters: dict[str, Any]) -> bool:
    options = parameters.get("options")
    additional = parameters.get("additionalFields")
    return (
        isinstance(options, dict)
        and bool(options.get("queryReplacement"))
    ) or (
        isinstance(additional, dict)
        and bool(additional.get("queryReplacement"))
    )


def check_postgres_query(workflow_name: str, node: dict[str, Any], report: ValidationReport) -> None:
    parameters = node.get("parameters")
    if not isinstance(parameters, dict):
        return
    query = parameters.get("query")
    if not isinstance(query, str):
        return

    if "$env." in query:
        report.fail(f"{workflow_name}: node {node.get('name')} usa $env em query")

    lower_query = query.lower()
    if "{{" in query and "$json" in query and not query_has_replacement(parameters):
        report.fail(f"{workflow_name}: node {node.get('name')} interpola $json em SQL sem queryReplacement")
    elif "{{" in query and "$json" in query:
        report.pass_(f"{workflow_name}: node {node.get('name')} usa queryReplacement para valores SQL")
    elif "soc_audit_insert_sql" in lower_query:
        report.warn(f"{workflow_name}: node {node.get('name')} usa SQL configurado por variavel; validar no n8n")
    else:
        report.pass_(f"{workflow_name}: node {node.get('name')} sem interpolacao SQL insegura aparente")


def check_respond_node(workflow_name: str, node: dict[str, Any], report: ValidationReport) -> None:
    parameters = node.get("parameters")
    if not isinstance(parameters, dict):
        return
    if parameters.get("respondWith") != "json":
        return
    body = parameters.get("responseBody")
    if isinstance(body, str) and re.match(r"^=\{\{\s*JSON\.stringify\(", body):
        report.fail(f"{workflow_name}: node {node.get('name')} pode retornar JSON double-encoded")
    else:
        report.pass_(f"{workflow_name}: node {node.get('name')} retorna JSON sem stringify externo")


def check_node_security_values(workflow_name: str, node: dict[str, Any], report: ValidationReport) -> None:
    for text in iter_strings(node):
        for label, pattern in SECRET_VALUE_PATTERNS.items():
            if pattern.search(text):
                report.fail(f"{workflow_name}: node {node.get('name')} contem possivel segredo: {label}")
        if SECRET_ASSIGNMENT_PATTERN.search(text):
            report.fail(f"{workflow_name}: node {node.get('name')} contem possivel atribuicao de segredo")
        if SECRET_ENV_DEFAULT_PATTERN.search(text):
            report.fail(f"{workflow_name}: node {node.get('name')} contem fallback sensivel em variavel de ambiente")
        if CONNECTION_STRING_PATTERN.search(text):
            report.fail(f"{workflow_name}: node {node.get('name')} contem possivel string de conexao")


def check_workflow_node(
    workflow_name: str,
    profile: str,
    node: dict[str, Any],
    allowed_types: set[str],
    report: ValidationReport,
) -> None:
    required_fields = {"id", "name", "type", "typeVersion", "position", "parameters"}
    missing = sorted(required_fields - set(node))
    if missing:
        report.fail(f"{workflow_name}: node sem campos estruturais obrigatorios: {missing}")
        return

    node_name = node.get("name")
    node_type = node.get("type")
    if node_type not in allowed_types:
        report.fail(f"{workflow_name}: node {node_name} usa tipo nao permitido no perfil {profile}: {node_type}")
    else:
        report.pass_(f"{workflow_name}: node {node_name} permitido no perfil {profile}")

    position = node.get("position")
    if not (
        isinstance(position, list)
        and len(position) == 2
        and all(isinstance(item, (int, float)) for item in position)
    ):
        report.fail(f"{workflow_name}: node {node_name} possui posicao invalida")

    if node_type == "n8n-nodes-base.webhook" and profile in {"lab-template", "prod-template"}:
        parameters = node.get("parameters", {})
        auth = parameters.get("authentication") if isinstance(parameters, dict) else None
        if auth in WEBHOOK_AUTH_VALUES and has_credentials(node):
            report.pass_(f"{workflow_name}: webhook {node_name} possui autenticacao configurada")
        else:
            report.fail(f"{workflow_name}: webhook {node_name} sem autenticacao ou credencial placeholder")

    if node_type in FALLIBLE_NODE_TYPES:
        if node.get("retryOnFail") is True:
            report.pass_(f"{workflow_name}: node falivel {node_name} possui retryOnFail")
        else:
            report.warn(f"{workflow_name}: node falivel {node_name} sem retryOnFail")

        if node.get("onError") == "continueErrorOutput":
            report.pass_(f"{workflow_name}: node falivel {node_name} usa output de erro dedicado")
        elif node.get("continueOnFail") is True:
            report.warn(f"{workflow_name}: node falivel {node_name} usa continueOnFail; validar erro no n8n antes de producao")
        else:
            report.warn(f"{workflow_name}: node falivel {node_name} sem estrategia local de erro")

    if node_type == "n8n-nodes-base.postgres":
        check_postgres_query(workflow_name, node, report)
    if node_type == "n8n-nodes-base.respondToWebhook":
        check_respond_node(workflow_name, node, report)

    check_node_security_values(workflow_name, node, report)


def check_workflow_meta(workflow_name: str, data: dict[str, Any], profile: str, report: ValidationReport) -> None:
    meta = data.get("meta")
    if not isinstance(meta, dict):
        report.fail(f"{workflow_name}: workflow sem meta valido")
        return

    if meta.get("contains_credentials") is True:
        report.fail(f"{workflow_name}: meta indica presenca de credenciais")
    else:
        report.pass_(f"{workflow_name}: meta nao indica credenciais reais")

    if profile in {"lab-template", "prod-template"}:
        report.pass_(f"{workflow_name}: perfil validado como {profile}")
    elif profile in {"mock-static", "mock-executable"}:
        if any(has_credentials(node) for node in data.get("nodes", []) if isinstance(node, dict)):
            report.fail(f"{workflow_name}: perfil mock contem referencias credentials")
        else:
            report.pass_(f"{workflow_name}: perfil mock sem referencias credentials")

    if data.get("pinData") not in ({}, None):
        report.fail(f"{workflow_name}: workflow contem pinData preenchido")
    if data.get("staticData") not in ({}, None):
        report.fail(f"{workflow_name}: workflow contem staticData preenchido")
    if data.get("pinData") in ({}, None) and data.get("staticData") in ({}, None):
        report.pass_(f"{workflow_name}: workflow sem pinData/staticData de execucao")


def check_workflow_file(path: Path, report: ValidationReport) -> None:
    workflow_name = path.name
    data = load_json(path, report)
    if data is None:
        return
    if not isinstance(data, dict):
        report.fail(f"{workflow_name}: workflow deve ser objeto JSON")
        return

    text = read_text(path, report)
    if "$env." in text:
        report.fail(f"{workflow_name}: workflow usa $env em expressao n8n")
    else:
        report.pass_(f"{workflow_name}: workflow sem $env em expressoes")

    if data.get("active") is False:
        report.pass_(f"{workflow_name}: workflow esta inativo")
    else:
        report.fail(f"{workflow_name}: workflow deve estar com active=false")

    required_top_level = {"name", "active", "nodes", "connections", "settings", "meta"}
    missing_top_level = sorted(required_top_level - set(data))
    if missing_top_level:
        report.fail(f"{workflow_name}: workflow sem campos top-level obrigatorios: {missing_top_level}")
    else:
        report.pass_(f"{workflow_name}: campos top-level obrigatorios presentes")

    nodes_raw = data.get("nodes")
    if not isinstance(nodes_raw, list) or not nodes_raw:
        report.fail(f"{workflow_name}: workflow sem lista de nodes valida")
        return
    nodes = [node for node in nodes_raw if isinstance(node, dict)]

    ids = [node.get("id") for node in nodes if isinstance(node.get("id"), str)]
    names = [node.get("name") for node in nodes if isinstance(node.get("name"), str)]
    if len(ids) == len(set(ids)) and len(names) == len(set(names)):
        report.pass_(f"{workflow_name}: ids e nomes de nodes sao unicos")
    else:
        report.fail(f"{workflow_name}: possui ids ou nomes de nodes duplicados")

    profile = profile_for(data, path)
    allowed_types = NODE_TYPES_BY_PROFILE[profile]
    check_workflow_meta(workflow_name, data, profile, report)
    for node in nodes:
        check_workflow_node(workflow_name, profile, node, allowed_types, report)

    check_fallible_error_outputs(workflow_name, data, nodes, report)
    check_workflow_connections(workflow_name, data, node_names(nodes), report)

    if "possible_false_positive" in text or "false_positive_assessment" in text:
        report.pass_(f"{workflow_name}: contem campos de falso positivo ou equivalente")
    elif profile == "prod-template":
        report.warn(f"{workflow_name}: sem campo explicito de falso positivo")


def check_workflows(report: ValidationReport) -> None:
    workflow_dir = ROOT / "02-workflows-n8n"
    workflow_paths = sorted(workflow_dir.glob("*.json"))
    if not workflow_paths:
        report.fail("Nenhum workflow n8n encontrado em 02-workflows-n8n")
        return
    for path in workflow_paths:
        check_workflow_file(path, report)


def check_sql(report: ValidationReport) -> None:
    sql_paths = sorted((ROOT / "05-sql").glob("*.sql"))
    if not sql_paths:
        report.fail("Nenhum SQL encontrado em 05-sql")
        return

    for path in sql_paths:
        text = read_text(path, report)
        if not text:
            continue
        create_tables = len(re.findall(r"\bCREATE TABLE\b", text, flags=re.IGNORECASE))
        if create_tables >= 1:
            report.pass_(f"{path.relative_to(ROOT)}: contem {create_tables} CREATE TABLE")
        else:
            report.warn(f"{path.relative_to(ROOT)}: nao contem CREATE TABLE")

        forbidden = [
            r"\bCREATE\s+USER\b",
            r"\bGRANT\b",
            r"\bIDENTIFIED\s+BY\b",
            r"\bCREATE\s+DATABASE\b",
        ]
        for pattern in forbidden:
            if re.search(pattern, text, flags=re.IGNORECASE):
                report.fail(f"{path.relative_to(ROOT)}: SQL contem comando proibido: {pattern}")

        if CONNECTION_STRING_PATTERN.search(text):
            report.fail(f"{path.relative_to(ROOT)}: possivel string de conexao encontrada")
        else:
            report.pass_(f"{path.relative_to(ROOT)}: sem string de conexao aparente")


def check_tests(report: ValidationReport) -> None:
    path = ROOT / "06-tests" / "00-cenarios-validacao-mock.json"
    data = load_json(path, report)
    if data is None:
        return
    scenarios = data.get("test_scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        report.fail("Arquivo de cenarios nao contem test_scenarios valido")
        return

    report.pass_(f"Cenarios de teste encontrados: {len(scenarios)}")
    observed_causes = set()
    for scenario in scenarios:
        test_id = scenario.get("test_id", "sem_id")
        root_cause = scenario.get("expected_root_cause")
        risk = scenario.get("expected_risk_level")
        confidence = scenario.get("expected_confidence_level")
        observed_causes.add(root_cause)

        if root_cause not in ROOT_CAUSES:
            report.fail(f"{test_id}: expected_root_cause invalido: {root_cause}")
        if risk not in RISK_LEVELS:
            report.fail(f"{test_id}: expected_risk_level invalido: {risk}")
        if confidence not in CONFIDENCE_LEVELS:
            report.fail(f"{test_id}: expected_confidence_level invalido: {confidence}")
        if not isinstance(scenario.get("possible_false_positive"), bool):
            report.fail(f"{test_id}: possible_false_positive deve ser boolean")
        if not isinstance(scenario.get("human_approval_required"), bool):
            report.fail(f"{test_id}: human_approval_required deve ser boolean")
        if not scenario.get("forbidden_behaviors"):
            report.warn(f"{test_id}: forbidden_behaviors ausente ou vazio")

    minimum = {
        "identity",
        "endpoint",
        "network",
        "cloud",
        "vulnerability",
        "external_threat",
        "false_positive",
    }
    missing = sorted(minimum - observed_causes)
    if missing:
        report.fail(f"Cobertura de causa raiz incompleta: {missing}")
    else:
        report.pass_("Cobertura minima de causa raiz presente nos cenarios")


def check_memory_docs(report: ValidationReport) -> None:
    docs = [
        ROOT / "01-docs" / "24-governanca-memoria-corporativa.md",
        ROOT / "01-docs" / "25-retencao-revisao-qualidade.md",
    ]
    for path in docs:
        text = read_text(path, report).lower()
        if "revisao humana" in text or "aprova" in text:
            report.pass_(f"{path.name}: menciona revisao/aprovacao humana")
        else:
            report.warn(f"{path.name}: nao menciona revisao/aprovacao humana")


def check_project_sensitive_patterns(report: ValidationReport) -> None:
    targets = [
        ROOT / "01-docs",
        ROOT / "02-workflows-n8n",
        ROOT / "03-prompts",
        ROOT / "04-payloads-mock",
        ROOT / "05-sql",
        ROOT / "06-tests",
        ROOT / "README.md",
        ROOT / "SECURITY.md",
        ROOT / "docker-compose.soc-copilot-lab.yml",
    ]
    targets.extend(sorted(ROOT.glob(".env*.example")))
    extensions = {".md", ".json", ".sql", ".py", ".yml", ".yaml"}
    for base in targets:
        paths = [base] if base.is_file() else sorted(base.rglob("*"))
        for path in paths:
            if not path.is_file() or path.suffix.lower() not in extensions:
                continue
            text = read_text(path, report)
            if not text:
                continue
            for label, pattern in SECRET_VALUE_PATTERNS.items():
                if pattern.search(text):
                    report.fail(f"{path.relative_to(ROOT)}: possivel segredo encontrado: {label}")
            if SECRET_ASSIGNMENT_PATTERN.search(text):
                report.fail(f"{path.relative_to(ROOT)}: possivel atribuicao de segredo encontrada")
            if SECRET_ENV_DEFAULT_PATTERN.search(text):
                report.fail(f"{path.relative_to(ROOT)}: fallback sensivel em variavel de ambiente")


def run_validation() -> ValidationReport:
    report = ValidationReport()
    check_required_dirs(report)
    check_github_hygiene(report)
    check_payloads(report)
    check_workflows(report)
    check_sql(report)
    check_tests(report)
    check_memory_docs(report)
    check_project_sensitive_patterns(report)
    return report


def render_markdown_summary(result: dict[str, Any]) -> str:
    summary = result.get("summary", {})
    failures = int(summary.get("failures", 0))
    warnings = int(summary.get("warnings", 0))
    if failures:
        status = "Reprovado"
    elif warnings:
        status = "Aprovado com warnings"
    else:
        status = "Aprovado"

    lines = [
        "# Resumo Da Validacao Estatica",
        "",
        "## Status Consolidado",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Projeto | {result.get('project', 'SOC-Octopus-Agent')} |",
        f"| Status | {status} |",
        f"| Gerado em | {result.get('created_at', 'nao informado')} |",
        f"| Validador | {result.get('validator', 'nao informado')} |",
        "",
        "## Totais",
        "",
        "| Metrica | Total |",
        "| --- | ---: |",
        f"| Aprovacoes | {summary.get('passed', 0)} |",
        f"| Warnings | {summary.get('warnings', 0)} |",
        f"| Falhas | {summary.get('failures', 0)} |",
        "",
        "## Severidades",
        "",
        "| Severidade | Aprovacoes | Warnings | Falhas |",
        "| --- | ---: | ---: | ---: |",
    ]

    severity_summary = result.get("severity_summary", {})
    if isinstance(severity_summary, dict):
        for severity in SEVERITY_ORDER:
            counts = severity_summary.get(severity, {})
            lines.append(
                f"| {severity} | {counts.get('passed', 0)} | "
                f"{counts.get('warnings', 0)} | {counts.get('failures', 0)} |"
            )

    lines.extend(
        [
            "",
            "## Categorias",
            "",
            "| Categoria | Aprovacoes | Warnings | Falhas |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    categories = result.get("categories", {})
    if isinstance(categories, dict):
        for category, counts in sorted(categories.items()):
            if isinstance(counts, dict):
                lines.append(
                    f"| {category} | {counts.get('passed', 0)} | "
                    f"{counts.get('warnings', 0)} | {counts.get('failures', 0)} |"
                )

    lines.extend(["", "## Pendencias", ""])
    failures_list = result.get("failures", [])
    warnings_list = result.get("warnings", [])
    if failures_list:
        lines.append("### Falhas")
        lines.append("")
        for item in failures_list:
            lines.append(f"- {item}")
        lines.append("")
    if warnings_list:
        lines.append("### Warnings")
        lines.append("")
        for item in warnings_list:
            lines.append(f"- {item}")
        lines.append("")
    if not failures_list and not warnings_list:
        lines.append("- Nenhuma falha ou warning registrado.")
        lines.append("")

    lines.extend(
        [
            "## Observacoes",
            "",
            "- Resumo gerado localmente a partir do validador estatico.",
            "- O JSON detalhado continua sendo a fonte tecnica principal.",
            "- Nenhuma integracao externa e executada por este resumo.",
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
    parser = argparse.ArgumentParser(description="Validador estatico local")
    parser.add_argument("--write-report", help="Caminho para gravar relatorio JSON")
    parser.add_argument("--write-markdown", help="Caminho para gravar resumo Markdown")
    args = parser.parse_args()

    report = run_validation()
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

    return 1 if report.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
