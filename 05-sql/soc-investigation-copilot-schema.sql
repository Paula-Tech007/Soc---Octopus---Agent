-- SOC Investigation Copilot - PostgreSQL Schema
-- Version: 1.0.0

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS soc_alerts (
    alert_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id VARCHAR(100) NOT NULL DEFAULT 'default',
    alert_id VARCHAR(255) NOT NULL,
    source VARCHAR(100) NOT NULL,
    correlation_id VARCHAR(255) NOT NULL,
    severity_original VARCHAR(50),
    rule_id VARCHAR(100),
    rule_name TEXT,
    src_ip VARCHAR(100),
    dst_ip VARCHAR(100),
    hostname VARCHAR(255),
    username VARCHAR(255),
    event_timestamp TIMESTAMP,
    raw_payload JSONB NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT uq_soc_alerts_tenant_source_alert_id UNIQUE (tenant_id, source, alert_id)
);

CREATE TABLE IF NOT EXISTS soc_investigations (
    investigation_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    alert_uuid UUID NOT NULL,
    correlation_id VARCHAR(255) NOT NULL,
    severity_final VARCHAR(50) NOT NULL,
    executive_summary TEXT,
    technical_analysis TEXT,
    approval_required BOOLEAN NOT NULL DEFAULT FALSE,
    status VARCHAR(50) NOT NULL DEFAULT 'created',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_soc_investigations_alert
        FOREIGN KEY (alert_uuid)
        REFERENCES soc_alerts(alert_uuid)
        ON DELETE CASCADE,

    CONSTRAINT chk_soc_investigations_severity
        CHECK (severity_final IN ('Low', 'Medium', 'High', 'Critical')),

    CONSTRAINT chk_soc_investigations_status
        CHECK (status IN ('created', 'processing', 'approved', 'rejected', 'review_required', 'failed'))
);

CREATE TABLE IF NOT EXISTS soc_agent_results (
    agent_result_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    investigation_uuid UUID NOT NULL,
    agent_name VARCHAR(255) NOT NULL,
    agent_version VARCHAR(50) DEFAULT '1.0.0',
    input_data JSONB,
    output_data JSONB,
    confidence_score NUMERIC(5,2),
    execution_time_ms INTEGER,
    status VARCHAR(50) NOT NULL DEFAULT 'completed',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_soc_agent_results_investigation
        FOREIGN KEY (investigation_uuid)
        REFERENCES soc_investigations(investigation_uuid)
        ON DELETE CASCADE,

    CONSTRAINT chk_soc_agent_results_confidence
        CHECK (confidence_score IS NULL OR (confidence_score >= 0 AND confidence_score <= 100)),

    CONSTRAINT chk_soc_agent_results_status
        CHECK (status IN ('completed', 'failed', 'timeout', 'skipped'))
);

CREATE TABLE IF NOT EXISTS soc_evidence (
    evidence_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    investigation_uuid UUID NOT NULL,
    evidence_type VARCHAR(100) NOT NULL,
    evidence_value TEXT NOT NULL,
    source VARCHAR(255),
    confidence_score NUMERIC(5,2),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_soc_evidence_investigation
        FOREIGN KEY (investigation_uuid)
        REFERENCES soc_investigations(investigation_uuid)
        ON DELETE CASCADE,

    CONSTRAINT chk_soc_evidence_confidence
        CHECK (confidence_score IS NULL OR (confidence_score >= 0 AND confidence_score <= 100))
);

CREATE TABLE IF NOT EXISTS soc_audit_log (
    audit_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    investigation_uuid UUID,
    event_type VARCHAR(100) NOT NULL,
    actor_type VARCHAR(100) NOT NULL,
    actor_name VARCHAR(255),
    action TEXT NOT NULL,
    details JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_soc_audit_log_investigation
        FOREIGN KEY (investigation_uuid)
        REFERENCES soc_investigations(investigation_uuid)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS soc_execution_log (
    execution_uuid UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    investigation_uuid UUID,
    correlation_id VARCHAR(255),
    workflow_name VARCHAR(255) NOT NULL,
    node_name VARCHAR(255),
    execution_status VARCHAR(50) NOT NULL,
    execution_time_ms INTEGER,
    error_message TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_soc_execution_log_investigation
        FOREIGN KEY (investigation_uuid)
        REFERENCES soc_investigations(investigation_uuid)
        ON DELETE SET NULL,

    CONSTRAINT chk_soc_execution_log_status
        CHECK (execution_status IN ('success', 'failed', 'running', 'skipped', 'timeout'))
);

CREATE INDEX IF NOT EXISTS idx_soc_alerts_alert_id
    ON soc_alerts(alert_id);

CREATE INDEX IF NOT EXISTS idx_soc_alerts_tenant_id
    ON soc_alerts(tenant_id);

CREATE INDEX IF NOT EXISTS idx_soc_alerts_source
    ON soc_alerts(source);

CREATE INDEX IF NOT EXISTS idx_soc_alerts_correlation_id
    ON soc_alerts(correlation_id);

CREATE INDEX IF NOT EXISTS idx_soc_alerts_event_timestamp
    ON soc_alerts(event_timestamp);

CREATE INDEX IF NOT EXISTS idx_soc_investigations_alert_uuid
    ON soc_investigations(alert_uuid);

CREATE INDEX IF NOT EXISTS idx_soc_investigations_correlation_id
    ON soc_investigations(correlation_id);

CREATE INDEX IF NOT EXISTS idx_soc_investigations_severity_final
    ON soc_investigations(severity_final);

CREATE INDEX IF NOT EXISTS idx_soc_agent_results_investigation_uuid
    ON soc_agent_results(investigation_uuid);

CREATE INDEX IF NOT EXISTS idx_soc_agent_results_agent_name
    ON soc_agent_results(agent_name);

CREATE INDEX IF NOT EXISTS idx_soc_evidence_investigation_uuid
    ON soc_evidence(investigation_uuid);

CREATE INDEX IF NOT EXISTS idx_soc_evidence_type
    ON soc_evidence(evidence_type);

CREATE INDEX IF NOT EXISTS idx_soc_audit_log_investigation_uuid
    ON soc_audit_log(investigation_uuid);

CREATE INDEX IF NOT EXISTS idx_soc_audit_log_event_type
    ON soc_audit_log(event_type);

CREATE INDEX IF NOT EXISTS idx_soc_execution_log_investigation_uuid
    ON soc_execution_log(investigation_uuid);

CREATE INDEX IF NOT EXISTS idx_soc_execution_log_correlation_id
    ON soc_execution_log(correlation_id);

CREATE INDEX IF NOT EXISTS idx_soc_execution_log_status
    ON soc_execution_log(execution_status);
