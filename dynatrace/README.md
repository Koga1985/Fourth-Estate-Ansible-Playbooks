# Dynatrace

Ansible automation for the **Dynatrace** observability platform — agent/gateway
deployment, tenant configuration, and NIST 800-53 security hardening.

## Roles (17)

### Deployment
| Role | Purpose |
|------|---------|
| [`dynatrace_oneagent`](roles/dynatrace_oneagent/) | Deploy/configure the OneAgent on Linux/Windows hosts. |
| [`dynatrace_oneagent_lifecycle`](roles/dynatrace_oneagent_lifecycle/) | Fleet lifecycle for installed OneAgents — version assess, host-group/network-zone/mode reconfigure, restart, guarded decommission. |
| [`dynatrace_activegate`](roles/dynatrace_activegate/) | Deploy an ActiveGate (group / network zone). |
| [`dynatrace_kubernetes`](roles/dynatrace_kubernetes/) | Deploy full-stack observability to K8s/OpenShift via the DynaKube CR. |

### Configuration
| Role | Purpose |
|------|---------|
| [`dynatrace_tenant_config`](roles/dynatrace_tenant_config/) | Tenant config via Config / Settings 2.0 (management zones, alerting profiles, auto-tags). |
| [`dynatrace_monitoring_as_code`](roles/dynatrace_monitoring_as_code/) | Provision SLOs, synthetic monitors, dashboards from definitions. |
| [`dynatrace_notifications`](roles/dynatrace_notifications/) | Problem-notification integrations (ServiceNow, Slack, email, PagerDuty, Jira, webhooks). |
| [`dynatrace_synthetic_locations`](roles/dynatrace_synthetic_locations/) | Manage private synthetic locations (ActiveGate synthetic capability) — assess + data-driven apply. |
| [`dynatrace_cloud_integrations`](roles/dynatrace_cloud_integrations/) | Manage AWS/Azure/GCP monitoring connectors — assess + data-driven apply. |
| [`dynatrace_extensions`](roles/dynatrace_extensions/) | Extension Framework 2.0 install/activate — assess + data-driven apply. |
| [`dynatrace_config_backup`](roles/dynatrace_config_backup/) | Read-only export of tenant Config/Settings 2.0 objects to timestamped JSON (DR / change-audit). |

### Security & compliance (NIST 800-53)
| Role | Purpose |
|------|---------|
| [`dynatrace_security_hardening`](roles/dynatrace_security_hardening/) | Tenant security posture (token hygiene, audit access, IP restrictions) — AC/AU/IA/SC. |
| [`dynatrace_iam`](roles/dynatrace_iam/) | Account Management (groups/users/policies/bindings) — AC-2/AC-6. |
| [`dynatrace_data_privacy`](roles/dynatrace_data_privacy/) | PII/IP masking & data privacy — SC-28/SI-12. |
| [`dynatrace_log_monitoring`](roles/dynatrace_log_monitoring/) | Log sensitive-data masking / storage — AU-9/SC-28. |
| [`dynatrace_appsec`](roles/dynatrace_appsec/) | Runtime vulnerability + attack protection — SA-11/RA-5. |
| [`dynatrace_audit_export`](roles/dynatrace_audit_export/) | Export audit log to NDJSON evidence + SIEM forward — AU-6/AU-9/AU-11. |

A master [`site.yml`](site.yml) sequences deploy → config → security/compliance → IAM → backup.
The lifecycle and config-backup roles are opt-in via `enabled_components`
(e.g. `-e '{"enabled_components":["dynatrace_config_backup"]}'`).

All roles are **safe by default** (`apply_changes=false` assesses / reports;
nothing is installed or changed until `-e apply_changes=true`). Tokens are
handled with `no_log`. See each role's README for the grab-and-go quick start.

## Tokens
* **PaaS token** (`InstallerDownload`) — OneAgent / ActiveGate installers.
* **API token** (`ReadConfig`/`WriteConfig`, `settings.*`, `auditLogs.read`,
  `apiTokens.read`) — tenant config + security roles. Store all tokens in Vault.

```bash
ansible-galaxy collection install -r dynatrace/requirements.yml
```
