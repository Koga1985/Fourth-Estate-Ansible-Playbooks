# ise_integration__logging

Configures Cisco ISE remote syslog targets, logging category settings, and SIEM integration. This role ensures that ISE sends the correct event streams — authentication, authorization, posture, guest, and system events — to the appropriate external logging infrastructure. It is a foundational role for meeting DISA STIG audit logging requirements and enabling real-time security monitoring.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access
- A reachable syslog server and/or SIEM endpoint
- Ansible Vault for credential management

## Role Variables

### ISE Connection

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | **Yes** | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | **Yes** | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | **Yes** | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | No | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | No | Route ISE API calls through a proxy |
| `ise_debug` | `false` | No | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Syslog Servers

| Variable | Default | Required | Description |
|---|---|---|
| `syslog_servers` | (required) | No | List of remote syslog targets; each entry has `name`, `ip_address`, optional `port` (default `514`), and optional `protocol` (default `UDP`) |

### Logging Categories

| Variable | Default | Required | Description |
|---|---|---|
| `logging_categories` | (required) | No | List of ISE logging category configurations to push to the MnT API |

### SIEM Integration

| Variable | Default | Required | Description |
|---|---|---|
| `siem_integration_enabled` | (required) | No | Enable direct SIEM integration via API |
| `siem_api_endpoint` | (required when enabled) | No | SIEM API base URL |
| `siem_api_token` | `{{ vault_siem_api_token }}` | **Yes** | Bearer token for SIEM API |
| `siem_log_types` | (required when enabled) | No | List of log type identifiers to forward |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_integration__logging_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant logging settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_integration__logging_log_level` | `INFO` | No | Log verbosity level |
| `ise_integration__logging_log_to_syslog` | `true` | No | Forward control-plane events to syslog |
| `ise_integration__logging_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_integration__logging_notify_on_completion` | `false` | No | Send email on completion |
| `ise_integration__logging_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_integration__logging_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Configure ISE logging and SIEM integration
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    syslog_servers:
      - name: "Primary-SIEM-Syslog"
        ip_address: "10.0.0.50"
        port: 514
        protocol: "UDP"
      - name: "Secondary-Syslog"
        ip_address: "10.0.0.51"
        port: 6514
        protocol: "TCP"
    siem_integration_enabled: true
    siem_api_endpoint: "https://siem.example.com"
    siem_log_types:
      - "RADIUS_Authentication"
      - "RADIUS_Accounting"
      - "Admin_Audit"
      - "Posture"
  roles:
    - role: cisco/roles/ise_integration__logging
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `logging` | All logging configuration tasks |
| `syslog` | Syslog server registration tasks |
| `categories` | Logging category configuration tasks |
| `siem` | SIEM integration tasks |
| `integration` | External integration tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- SIEM integration tasks use the external SIEM API and are independent of the ISE ERS API.
- All credentials must be stored in Ansible Vault.
