#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const workflowDir = path.join(root, "02-workflows-n8n");

const workflowFiles = fs
  .readdirSync(workflowDir)
  .filter((name) => name.endsWith(".json"))
  .map((name) => path.join(workflowDir, name));

const fallibleTypes = new Set([
  "n8n-nodes-base.httpRequest",
  "n8n-nodes-base.postgres",
  "n8n-nodes-base.redis",
]);

function walk(value, visitor) {
  if (Array.isArray(value)) {
    for (let index = 0; index < value.length; index += 1) {
      value[index] = walk(value[index], visitor);
    }
    return visitor(value);
  }

  if (value && typeof value === "object") {
    for (const key of Object.keys(value)) {
      value[key] = walk(value[key], visitor);
    }
    return visitor(value);
  }

  return visitor(value);
}

function normalizeExpressionString(value) {
  if (typeof value !== "string") return value;

  return value.replaceAll("$env.", "$vars.");
}

function unwrapJsonStringifyExpression(value) {
  if (typeof value !== "string") return value;

  const jsonStringifyMatch = value.match(/^=\{\{\s*JSON\.stringify\(([\s\S]*)\)\s*\}\}$/);
  if (!jsonStringifyMatch) return value;
  return `={{ ${jsonStringifyMatch[1].trim()} }}`;
}

function stringifyHttpJsonBody(value) {
  if (typeof value !== "string") return value;
  if (/^=\{\{\s*JSON\.stringify\(/.test(value)) return value;

  const jsonObjectMatch = value.match(/^=\{\{\s*(\$json\.[\s\S]*?)\s*\}\}$/);
  if (!jsonObjectMatch) return value;
  return `={{JSON.stringify(${jsonObjectMatch[1].trim()})}}`;
}

function setWebhookAuth(node) {
  if (node.type !== "n8n-nodes-base.webhook") return;
  node.parameters ??= {};

  if (!node.parameters.authentication || node.parameters.authentication === "none") {
    node.parameters.authentication = "headerAuth";
  }

  node.credentials ??= {};
  node.credentials.httpHeaderAuth ??= {
    id: "REPLACE_WITH_WEBHOOK_HEADER_AUTH_CREDENTIAL_ID",
    name: "Webhook Header Auth",
  };
}

function setFallibleNodeDefaults(node) {
  if (!fallibleTypes.has(node.type)) return;

  node.retryOnFail = true;
  node.maxTries = 3;
  node.waitBetweenTries = 5000;
  node.onError = "continueErrorOutput";
  delete node.continueOnFail;

  if (node.type === "n8n-nodes-base.httpRequest") {
    node.parameters ??= {};
    if (node.parameters.bodyParametersJson) {
      node.parameters.bodyParametersJson = stringifyHttpJsonBody(node.parameters.bodyParametersJson);
    }
    node.parameters.options ??= {};
    node.parameters.options.timeout ??= 30000;
  }
}

function setFallibleErrorConnections(workflow) {
  workflow.connections ??= {};

  for (const node of workflow.nodes ?? []) {
    if (!fallibleTypes.has(node.type)) continue;

    const nodeConnections = workflow.connections[node.name];
    const mainOutputs = nodeConnections?.main;
    if (!Array.isArray(mainOutputs) || !Array.isArray(mainOutputs[0]) || mainOutputs[0].length === 0) {
      continue;
    }

    if (!Array.isArray(mainOutputs[1]) || mainOutputs[1].length === 0) {
      mainOutputs[1] = JSON.parse(JSON.stringify(mainOutputs[0]));
    }
  }
}

function parameterizeAlertInsert(node) {
  if (node.type !== "n8n-nodes-base.postgres") return;
  if (node.name !== "11 - PostgreSQL Insert Alert") return;

  node.parameters ??= {};
  node.parameters.operation = "executeQuery";
  node.parameters.query = [
    "INSERT INTO soc_alerts (",
    "  tenant_id,",
    "  alert_id,",
    "  source,",
    "  correlation_id,",
    "  severity_original,",
    "  rule_id,",
    "  rule_name,",
    "  src_ip,",
    "  dst_ip,",
    "  hostname,",
    "  username,",
    "  event_timestamp,",
    "  raw_payload",
    ") VALUES (",
    "  $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13::jsonb",
    ")",
    "ON CONFLICT (tenant_id, source, alert_id)",
    "DO NOTHING",
    "RETURNING alert_uuid, alert_id, correlation_id;",
  ].join("\n");
  node.parameters.options ??= {};
  node.parameters.options.queryReplacement =
    "={{ [$json.tenant_id, $json.alert_id, $json.source, $json.correlation_id, $json.severity_original, $json.rule_id, $json.rule_name, $json.src_ip, $json.dst_ip, $json.hostname, $json.username, $json.timestamp, JSON.stringify($json.raw_payload)] }}";
}

function parameterizeAuditInsert(node) {
  if (node.type !== "n8n-nodes-base.postgres") return;
  if (!/Persistir Auditoria PostgreSQL/.test(node.name)) return;

  node.parameters ??= {};
  node.parameters.operation = "executeQuery";
  node.parameters.query = [
    "INSERT INTO soc_audit_log (",
    "  event_type,",
    "  actor_type,",
    "  actor_name,",
    "  action,",
    "  details",
    ") VALUES (",
    "  $1, $2, $3, $4, $5::jsonb",
    ")",
    "RETURNING audit_uuid;",
  ].join("\n");
  node.parameters.options ??= {};
  node.parameters.options.queryReplacement =
    "={{ ['workflow_execution', 'n8n_workflow', $json.soc_octopus_output?.workflow_name || 'SOC-Octopus-Agent', $json.soc_octopus_output?.status || $json.soc_octopus_output?.execution_status || 'analysis_completed', JSON.stringify($json.soc_octopus_output || $json)] }}";
  delete node.parameters.additionalFields;
}

function normalizeMeta(workflow, fileName) {
  workflow.meta ??= {};
  workflow.meta.project ??= fileName.startsWith("soc-investigation")
    ? "SOC Investigation Copilot"
    : "SOC-Octopus-Agent";

  if (workflow.meta.validation_profile) return;

  if (workflow.meta.production_ready === true || workflow.meta.phase === "production-ready") {
    workflow.meta.validation_profile = "prod-template";
  } else if (workflow.meta.status === "lab-template" || fileName.endsWith("-intake.json")) {
    workflow.meta.validation_profile = "lab-template";
  } else {
    workflow.meta.validation_profile = "mock-executable";
  }
}

function removeDuplicateRespondNode(workflow) {
  const seen = new Set();
  workflow.nodes = workflow.nodes.filter((node) => {
    const key = `${node.id}::${node.name}`;
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

function normalizeRespondBody(node) {
  if (node.type !== "n8n-nodes-base.respondToWebhook") return;
  if (!node.parameters || !node.parameters.responseBody) return;

  node.parameters.responseBody = unwrapJsonStringifyExpression(node.parameters.responseBody);
}

for (const workflowPath of workflowFiles) {
  const fileName = path.basename(workflowPath);
  const workflow = JSON.parse(fs.readFileSync(workflowPath, "utf8"));

  walk(workflow, normalizeExpressionString);

  normalizeMeta(workflow, fileName);
  removeDuplicateRespondNode(workflow);

  for (const node of workflow.nodes ?? []) {
    setWebhookAuth(node);
    setFallibleNodeDefaults(node);
    normalizeRespondBody(node);
    parameterizeAlertInsert(node);
    parameterizeAuditInsert(node);
  }
  setFallibleErrorConnections(workflow);

  fs.writeFileSync(workflowPath, `${JSON.stringify(workflow, null, 2)}\n`, "utf8");
}

console.log(`Normalized ${workflowFiles.length} workflow JSON files.`);
