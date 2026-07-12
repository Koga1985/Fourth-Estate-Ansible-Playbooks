# cybervision_monitoring

Ansible role for Cisco Cyber Vision monitoring integrations: syslog/SIEM forwarding (CEF format), SNMPv3, OT-specific alert policies, Cisco ISE pxGrid integration, and health monitoring.

## Requirements

- Ansible 2.15+
- Collection: `community.general` (`ansible-galaxy collection install community.general`)
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cv_center_host` | `"{{ vault_cv_center_hostname }}"` | No | Cyber Vision Center API Connection |
| `cv_api_url` | `"https://{{ cv_center_host }}/api/3.0"` | No | — |
| `cv_api_token` | `"{{ vault_cv_api_token }}"` | No | — |
| `cv_validate_certs` | `true` | No | — |
| `cv_use_proxy` | `false` | No | — |
| `cv_timeout` | `60` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `artifacts_dir` | `"/tmp/cv-artifacts"` | No | — |
| `enable_syslog` | `true` | No | Feature Toggles |
| `enable_snmp` | `true` | No | — |
| `enable_alerts` | `true` | No | — |
| `enable_ise_integration` | `true` | No | — |
| `enable_health_monitoring` | `true` | No | — |
| `cv_syslog_enabled` | `true` | No | Syslog / SIEM Integration |
| `cv_syslog_destinations` | `(see defaults/main.yml)` | No | — |
| `cv_syslog_event_types` | `(see defaults/main.yml)` | No | Event categories to forward to SIEM |
| `cv_snmp_enabled` | `true` | No | SNMP Configuration |
| `cv_snmp_version` | `"v3"` | No | — |
| `cv_snmp_v3_users` | `(see defaults/main.yml)` | No | — |
| `cv_snmp_trap_destinations` | `(see defaults/main.yml)` | No | — |
| `cv_snmp_allowed_hosts` | `(see defaults/main.yml)` | No | — |
| `cv_alerts_enabled` | `true` | No | Alert Policies |
| `cv_alert_policies` | `(see defaults/main.yml)` | No | — |
| `cv_alert_email_enabled` | `true` | No | Email notification settings |
| `cv_alert_smtp_server` | `"{{ vault_cv_smtp_server }}"` | No | — |
| `cv_alert_smtp_port` | `587` | No | — |
| `cv_alert_smtp_tls` | `true` | No | — |
| `cv_alert_from_address` | `"cybervision-alerts@fourthestate.gov"` | No | — |
| `cv_alert_to_addresses` | `(see defaults/main.yml)` | No | — |
| `cv_ise_enabled` | `true` | No | Cisco ISE Integration Publishes OT asset context (IP, MAC, vendor, criticality) to ISE pxGrid for use in Cisco TrustSec segmentation policies |
| `cv_ise_host` | `"{{ vault_cv_ise_hostname }}"` | No | — |
| `cv_ise_pxgrid_node` | `"{{ vault_cv_ise_pxgrid_node }}"` | No | — |
| `cv_ise_client_cert` | `"{{ vault_cv_ise_client_cert }}"` | No | — |
| `cv_ise_client_key` | `"{{ vault_cv_ise_client_key }}"` | No | — |
| `cv_ise_ca_cert` | `"{{ vault_cv_ise_ca_cert }}"` | No | — |
| `cv_ise_publish_assets` | `true` | No | — |
| `cv_ise_publish_vulnerabilities` | `false` | No | ISE pxGrid can be noisy with vuln data |
| `cv_ise_publish_alerts` | `true` | No | — |
| `cv_health_check_interval_minutes` | `5` | No | Health Monitoring |
| `cv_sensor_offline_threshold_minutes` | `15` | No | — |
| `cv_center_disk_warning_percent` | `75` | No | — |
| `cv_center_disk_critical_percent` | `90` | No | — |
| `cv_center_cpu_warning_percent` | `80` | No | — |
| `cv_center_cpu_critical_percent` | `95` | No | — |

## Example Playbook

```yaml
- name: Use cybervision_monitoring
  hosts: all
  gather_facts: false
  roles:
    - role: cybervision_monitoring
      vars:
        apply_changes: false   # set true to apply
```

## Tags

```bash
--tags monitoring    # All monitoring tasks
--tags syslog,siem   # Syslog/SIEM only
--tags snmp          # SNMP only
--tags alerts        # Alert policies only
--tags ise,pxgrid    # ISE integration only
--tags health        # Health monitoring only
```

## Quick Start

```bash
# Dry-run
ansible-playbook -i inventory site.yml --tags monitoring --ask-vault-pass

# Apply all monitoring config
ansible-playbook -i inventory site.yml --tags monitoring -e "apply_changes=true" --ask-vault-pass

# Apply only ISE integration
ansible-playbook -i inventory site.yml --tags ise -e "apply_changes=true" --ask-vault-pass
```

## Features

| Module | Task File | Description |
|--------|-----------|-------------|
| Syslog/SIEM | `syslog.yml` | CEF/LEEF event forwarding to SIEM |
| SNMP | `snmp.yml` | SNMPv3 users, trap destinations, allowed hosts |
| Alerts | `alerts.yml` | OT alert policies and email notifications |
| ISE Integration | `ise_integration.yml` | pxGrid asset context publishing for TrustSec |
| Health Monitoring | `health_monitoring.yml` | Center and sensor health metrics + thresholds |
| Validation | `validation.yml` | Post-configuration validation |

## Pre-Configured Alert Policies

| Policy | Category | Severity | Description |
|--------|----------|----------|-------------|
| New-OT-Device | asset_discovery | high | Unknown device appeared on OT network |
| SIS-IT-Communication | anomaly | critical | Safety system communicating outside OT boundary |
| Critical-Vulnerability | vulnerability | critical | CVSS >= 9.0 on critical OT asset |
| Auth-Failure-Spike | authentication | high | 5+ auth failures in 10 minutes |
| Sensor-Offline | sensor_status | high | Sensor offline > 15 minutes |

## Cisco ISE Integration

Cyber Vision publishes OT asset context (IP, MAC, vendor, device type, criticality) to Cisco ISE via pxGrid. ISE uses this context in TrustSec SGT policies for OT network segmentation.

Prerequisites:
1. Cisco ISE pxGrid node enabled and accessible
2. Cyber Vision pxGrid client certificate issued by ISE CA
3. pxGrid account approved in ISE admin UI

## Key Variables

```yaml
# Syslog
cv_syslog_destinations:
  - host: "siem.example.com"
    format: "cef"              # CEF recommended for most SIEMs
    severity: "warning"

# SNMP
cv_snmp_version: "v3"          # v1/v2 disabled per STIG
cv_snmp_allowed_hosts:
  - "10.0.10.0/24"             # Restrict to management subnet

# ISE
cv_ise_enabled: true
cv_ise_host: "{{ vault_cv_ise_hostname }}"
cv_ise_publish_assets: true
cv_ise_publish_alerts: true
```

## Required Vault Variables

```yaml
vault_cv_center_hostname: "cybervision.example.com"
vault_cv_api_token: "your-api-bearer-token"

# Syslog
vault_syslog_server_primary: "siem.example.com"
vault_syslog_server_secondary: "siem-backup.example.com"

# SNMP
vault_cv_snmp_auth_password: "snmp-auth-min-8-chars"
vault_cv_snmp_priv_password: "snmp-priv-min-8-chars"
vault_snmp_trap_host: "10.0.10.100"
vault_snmp_management_subnet: "10.0.10.0/24"

# Alerts
vault_cv_smtp_server: "smtp.example.com"
vault_cv_alert_email_primary: "soc@example.com"
vault_cv_alert_email_secondary: "noc@example.com"

# ISE pxGrid
vault_cv_ise_hostname: "ise.example.com"
vault_cv_ise_pxgrid_node: "ise-pxgrid.example.com"
vault_cv_ise_client_cert: "{{ lookup('file', 'files/cv-pxgrid.crt') }}"
vault_cv_ise_client_key: "{{ lookup('file', 'files/cv-pxgrid.key') }}"
vault_cv_ise_ca_cert: "{{ lookup('file', 'files/ise-ca.crt') }}"
```

## Generated Artifacts

| Artifact | Description |
|----------|-------------|
| `cv_syslog_config.json` | Syslog destinations and event types |
| `cv_snmp_config.json` | SNMP users and trap destinations |
| `cv_alert_policies.json` | Alert policy names and severities |
| `cv_ise_integration.json` | ISE pxGrid integration settings |
| `cv_health_report.json` | Center and sensor health metrics |
| `cv_monitoring_validation.json` | Post-config validation results |

## License

MIT
