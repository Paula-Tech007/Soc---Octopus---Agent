-- SOC-Octopus-Agent
-- Fase 6 - Schema planejado para MySQL/MariaDB
-- Este arquivo e documental. Nao executar sem aprovacao humana explicita.
-- Nao contem credenciais, usuarios, senhas, hosts ou strings de conexao.

CREATE TABLE case_records (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    input_type VARCHAR(32) NOT NULL,
    source_system VARCHAR(128) NOT NULL,
    severity VARCHAR(16) NOT NULL,
    status VARCHAR(32) NOT NULL,
    title VARCHAR(255) NOT NULL,
    probable_root_cause VARCHAR(64) DEFAULT NULL,
    risk_level VARCHAR(16) DEFAULT NULL,
    confidence_level VARCHAR(16) DEFAULT NULL,
    possible_false_positive BOOLEAN NOT NULL DEFAULT FALSE,
    human_approval_required BOOLEAN NOT NULL DEFAULT TRUE,
    mock_data BOOLEAN NOT NULL DEFAULT TRUE,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    UNIQUE KEY uq_case_records_case_id (case_id),
    KEY idx_case_records_trace_id (trace_id),
    KEY idx_case_records_status (status),
    KEY idx_case_records_root_cause (probable_root_cause)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE input_payloads (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    payload_stage VARCHAR(32) NOT NULL,
    payload_json JSON NOT NULL,
    contains_real_customer_data BOOLEAN NOT NULL DEFAULT FALSE,
    contains_credentials BOOLEAN NOT NULL DEFAULT FALSE,
    mock_payload BOOLEAN NOT NULL DEFAULT TRUE,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    KEY idx_input_payloads_case_id (case_id),
    KEY idx_input_payloads_trace_id (trace_id),
    CONSTRAINT fk_input_payloads_case_id
        FOREIGN KEY (case_id) REFERENCES case_records (case_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE agent_runs (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    agent_name VARCHAR(128) NOT NULL,
    agent_role VARCHAR(128) NOT NULL,
    run_status VARCHAR(32) NOT NULL,
    decision_summary TEXT DEFAULT NULL,
    confidence_level VARCHAR(16) DEFAULT NULL,
    started_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    finished_at DATETIME(6) DEFAULT NULL,
    PRIMARY KEY (id),
    KEY idx_agent_runs_case_id (case_id),
    KEY idx_agent_runs_trace_id (trace_id),
    KEY idx_agent_runs_agent_name (agent_name),
    CONSTRAINT fk_agent_runs_case_id
        FOREIGN KEY (case_id) REFERENCES case_records (case_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE specialist_findings (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    agent_run_id BIGINT UNSIGNED DEFAULT NULL,
    specialist_name VARCHAR(128) NOT NULL,
    diagnosis TEXT NOT NULL,
    evidence_json JSON DEFAULT NULL,
    probable_cause VARCHAR(128) DEFAULT NULL,
    risk_level VARCHAR(16) DEFAULT NULL,
    confidence_level VARCHAR(16) DEFAULT NULL,
    possible_false_positive BOOLEAN NOT NULL DEFAULT FALSE,
    information_gaps TEXT DEFAULT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    KEY idx_specialist_findings_case_id (case_id),
    KEY idx_specialist_findings_trace_id (trace_id),
    KEY idx_specialist_findings_specialist_name (specialist_name),
    CONSTRAINT fk_specialist_findings_case_id
        FOREIGN KEY (case_id) REFERENCES case_records (case_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_specialist_findings_agent_run_id
        FOREIGN KEY (agent_run_id) REFERENCES agent_runs (id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE remediation_plans (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    remediation_summary TEXT NOT NULL,
    prerequisites_json JSON DEFAULT NULL,
    technical_steps_json JSON DEFAULT NULL,
    critical_actions_json JSON DEFAULT NULL,
    validation_steps_json JSON DEFAULT NULL,
    rollback_plan TEXT DEFAULT NULL,
    human_approval_required BOOLEAN NOT NULL DEFAULT TRUE,
    confidence_level VARCHAR(16) DEFAULT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    KEY idx_remediation_plans_case_id (case_id),
    KEY idx_remediation_plans_trace_id (trace_id),
    CONSTRAINT fk_remediation_plans_case_id
        FOREIGN KEY (case_id) REFERENCES case_records (case_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE consolidated_outputs (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    output_status VARCHAR(32) NOT NULL,
    executive_summary TEXT NOT NULL,
    consolidated_diagnosis TEXT NOT NULL,
    recommended_solution TEXT DEFAULT NULL,
    risk_level VARCHAR(16) DEFAULT NULL,
    confidence_level VARCHAR(16) DEFAULT NULL,
    possible_false_positive BOOLEAN NOT NULL DEFAULT FALSE,
    human_approval_required BOOLEAN NOT NULL DEFAULT TRUE,
    output_json JSON DEFAULT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    KEY idx_consolidated_outputs_case_id (case_id),
    KEY idx_consolidated_outputs_trace_id (trace_id),
    CONSTRAINT fk_consolidated_outputs_case_id
        FOREIGN KEY (case_id) REFERENCES case_records (case_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE human_approvals (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    approval_scope VARCHAR(128) NOT NULL,
    approval_status VARCHAR(32) NOT NULL,
    approver_reference VARCHAR(128) DEFAULT NULL,
    decision_reason TEXT DEFAULT NULL,
    decided_at DATETIME(6) DEFAULT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    KEY idx_human_approvals_case_id (case_id),
    KEY idx_human_approvals_trace_id (trace_id),
    KEY idx_human_approvals_status (approval_status),
    CONSTRAINT fk_human_approvals_case_id
        FOREIGN KEY (case_id) REFERENCES case_records (case_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE audit_events (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    audit_id VARCHAR(96) NOT NULL,
    case_id VARCHAR(64) DEFAULT NULL,
    trace_id VARCHAR(96) DEFAULT NULL,
    event_type VARCHAR(96) NOT NULL,
    actor_type VARCHAR(64) NOT NULL,
    actor_name VARCHAR(128) NOT NULL,
    event_summary TEXT NOT NULL,
    event_payload JSON DEFAULT NULL,
    mock_data BOOLEAN NOT NULL DEFAULT TRUE,
    human_approval_required BOOLEAN NOT NULL DEFAULT FALSE,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    UNIQUE KEY uq_audit_events_audit_id (audit_id),
    KEY idx_audit_events_case_id (case_id),
    KEY idx_audit_events_trace_id (trace_id),
    KEY idx_audit_events_event_type (event_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE memory_candidates (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    case_id VARCHAR(64) NOT NULL,
    trace_id VARCHAR(96) NOT NULL,
    candidate_type VARCHAR(64) NOT NULL,
    lesson_summary TEXT NOT NULL,
    root_cause VARCHAR(128) DEFAULT NULL,
    recommended_procedure TEXT DEFAULT NULL,
    false_positive_confirmed BOOLEAN NOT NULL DEFAULT FALSE,
    confidence_level VARCHAR(16) DEFAULT NULL,
    review_status VARCHAR(32) NOT NULL DEFAULT 'pending_human_review',
    reviewer_reference VARCHAR(128) DEFAULT NULL,
    reviewed_at DATETIME(6) DEFAULT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    KEY idx_memory_candidates_case_id (case_id),
    KEY idx_memory_candidates_trace_id (trace_id),
    KEY idx_memory_candidates_review_status (review_status),
    CONSTRAINT fk_memory_candidates_case_id
        FOREIGN KEY (case_id) REFERENCES case_records (case_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

