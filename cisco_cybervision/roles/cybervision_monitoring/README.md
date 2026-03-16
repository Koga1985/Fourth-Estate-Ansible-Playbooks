# cybervision_monitoring

Ansible role for Cisco Cyber Vision monitoring integrations: syslog/SIEM forwarding (CEF format), SNMPv3, OT-specific alert policies, Cisco ISE pxGrid integration, and health monitoring.

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

## Tags

```bash
--tags monitoring    # All monitoring tasks
--tags syslog,siem   # Syslog/SIEM only
--tags snmp          # SNMP only
--tags alerts        # Alert policies only
--tags ise,pxgrid    # ISE integration only
--tags health        # Health monitoring only
```
