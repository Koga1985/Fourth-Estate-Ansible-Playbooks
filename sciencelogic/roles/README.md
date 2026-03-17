# ScienceLogic SL1 Roles

This directory contains **33 Ansible roles** for automating ScienceLogic SL1 platform operations, including platform installation and hardening, device discovery, monitoring baselines, ITSM integration, governance, reporting, and PowerFlow automation.

## Roles

### Platform Lifecycle

| Role | Description |
|------|-------------|
| **sl1_platform_install** | Installs and bootstraps a new SL1 appliance, setting initial admin credentials, license key, and network configuration. |
| **sl1_platform_config** | Applies day-2 platform configuration including global settings, time zone, SMTP, and global thresholds. |
| **sl1_platform_hardening** | Hardens the SL1 platform per security best practices: TLS version enforcement, session timeouts, API rate limits, and audit log settings. |
| **sl1_upgrade_window** | Manages the SL1 platform upgrade lifecycle, scheduling upgrade windows and validating health before and after. |
| **sl1_database_baseline** | Configures SL1 database parameters, connection pool settings, and backup schedules. |
| **sl1_backup_restore** | Automates SL1 configuration backups to a remote target and documents restore procedures. |

### Discovery and Inventory

| Role | Description |
|------|-------------|
| **sl1_discovery_pipelines** | Creates and manages SL1 discovery sessions (IP range, SNMP, cloud) and assigns discovered devices to device groups. |
| **sl1_inventory_model** | Builds and maintains the SL1 device inventory model, including device classes, attributes, and custom fields. |
| **sl1_coverage_hygiene** | Identifies gaps in monitoring coverage, decommissions stale device records, and reports on unmonitored assets. |

### Monitoring Baselines

| Role | Description |
|------|-------------|
| **sl1_monitoring_baseline** | Applies a standard monitoring baseline to device groups, including polling frequency, collection policies, and availability checks. |
| **sl1_server_baseline** | Deploys server-specific monitoring: CPU, memory, disk, process, and log file collectors aligned to the server baseline standard. |
| **sl1_network_baseline** | Deploys network device monitoring: interface utilization, BGP/OSPF session state, CPU/memory, and environmental sensors. |
| **sl1_cloud_observability** | Configures SL1 cloud monitoring integrations for AWS, Azure, and GCP with metric collection and service discovery. |
| **sl1_kubernetes_observability** | Integrates SL1 with Kubernetes clusters for namespace, pod, and node-level visibility. |
| **sl1_thresholds_baseline** | Applies standard alerting thresholds (utilization, availability, error rates) to device classes and device groups. |
| **sl1_perf_intervals** | Configures data collection intervals and data retention tiers for performance metrics. |

### Events and Alerting

| Role | Description |
|------|-------------|
| **sl1_event_policy_hygiene** | Audits event policies, removes duplicates, normalizes severity mappings, and suppresses known-benign events. |
| **sl1_notify_routing** | Manages SL1 notification policies and action runners, routing alerts to email, SNMP trap, and webhook targets. |

### Dynamic Applications

| Role | Description |
|------|-------------|
| **sl1_dynapp_catalog** | Deploys and versions SL1 Dynamic Application packages from a catalog, aligning device-class assignments. |

### Collector Fleet

| Role | Description |
|------|-------------|
| **sl1_collector_fleet** | Manages the SL1 Data Collector and Message Collector fleet: registration, load balancing, failover configuration, and version management. |

### ITSM Integration

| Role | Description |
|------|-------------|
| **sl1_itsm_pipeline** | Configures SL1 ITSM integration with ServiceNow or Jira, mapping event actions to incident/ticket creation workflows. |
| **sl1_itsm_enrichment** | Enriches SL1 events and tickets with CMDB context, device ownership, and application service mapping before routing. |

### PowerFlow

| Role | Description |
|------|-------------|
| **sl1_powerflow_ops** | Manages SL1 PowerFlow platform operations: application deployments, step configuration, and run schedules. |
| **sl1_powerflow_ci_cd** | Implements a CI/CD pipeline for SL1 PowerFlow application development, including lint, test, and promote stages. |

### Access Control

| Role | Description |
|------|-------------|
| **sl1_rbac_baseline** | Applies the SL1 RBAC baseline, creating user accounts, access hooks, and permission keys aligned to role definitions. |

### Governance and Compliance

| Role | Description |
|------|-------------|
| **sl1_governance_pack** | Assembles a governance evidence pack: access review exports, configuration baselines, and change audit records. |
| **sl1_audit_governance** | Exports SL1 audit logs, produces user activity reports, and validates configuration drift against the approved baseline. |
| **sl1_data_retention** | Configures SL1 data retention policies for performance data, events, logs, and audit records in compliance with retention requirements. |

### Reporting and Dashboards

| Role | Description |
|------|-------------|
| **sl1_dashboard_catalog** | Deploys a standard catalog of SL1 dashboards for infrastructure operations, capacity planning, and service health. |
| **sl1_kpi_scorecards** | Generates SL1 KPI scorecards for infrastructure teams, summarizing availability, MTTR, and alert volume trends. |
| **sl1_cost_metering** | Produces resource consumption and cost metering reports from SL1 device and metric data. |

### MSP and Multi-Tenant

| Role | Description |
|------|-------------|
| **sl1_mssp_orchestrator** | Orchestrates multi-tenant SL1 operations, iterating role execution across multiple SL1 organizations for MSP deployments. |

### Run-Book Automation

| Role | Description |
|------|-------------|
| **sl1_rba_runbooks** | Deploys SL1 Run Book Automation (RBA) policies that trigger automated remediation actions from event conditions. |

## Requirements

- Ansible 2.12+
- Python `requests` library on the control node: `pip install requests`
- SL1 API user with appropriate permissions (device management, configuration read/write)
- Network access to the SL1 API (HTTPS, default port 443) from the Ansible control host

## Quick Start

```bash
ansible-playbook -i inventory site.yml --tags discovery,monitoring --ask-vault-pass
```

## Example Playbook

```yaml
---
- name: SL1 monitoring baseline deployment
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    sl1_api_url: "https://sl1.example.com/api"
    sl1_user: "ansible_bot"
    sl1_password: "{{ vault_sl1_password }}"
    sl1_verify_certs: true

  roles:
    - role: sciencelogic/roles/sl1_discovery_pipelines
    - role: sciencelogic/roles/sl1_monitoring_baseline
    - role: sciencelogic/roles/sl1_thresholds_baseline
    - role: sciencelogic/roles/sl1_notify_routing
```

---

**Last Updated:** 2026-03-17
**Maintained By:** Fourth Estate Infrastructure Team
