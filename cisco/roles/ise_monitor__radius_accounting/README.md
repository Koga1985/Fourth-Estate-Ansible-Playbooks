# ise_monitor__radius_accounting

Retrieves and analyzes RADIUS accounting data from Cisco ISE, including active session lists and historical accounting logs. This role computes session statistics (total sessions, unique authenticated users, NAS device count), exports data to a SIEM, and generates timestamped JSON reports. It is used for network access visibility, capacity planning, and compliance auditing.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
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
| `apply_changes` | `false` | No | Not used for mutation in this role; reserved for future use |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Accounting Window

| Variable | Default | Required | Description |
|---|---|---|
| `accounting_start_date` | (required) | No | Start of accounting log query window |
| `accounting_end_date` | (required) | No | End of accounting log query window |

### SIEM Integration

| Variable | Default | Required | Description |
|---|---|---|
| `siem_integration_enabled` | (required) | No | Forward session data to SIEM |
| `siem_endpoint` | (required when enabled) | No | SIEM ingest endpoint URL |
| `siem_api_token` | `{{ vault_siem_api_token }}` | **Yes** | Bearer token for SIEM API |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_monitor__radius_accounting_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_monitor__radius_accounting_log_level` | `INFO` | No | Log verbosity level |
| `ise_monitor__radius_accounting_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_monitor__radius_accounting_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_monitor__radius_accounting_notify_on_completion` | `false` | No | Send email on completion |
| `ise_monitor__radius_accounting_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_monitor__radius_accounting_auto_backup` | `true` | No | Reserved; no destructive changes are made |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Monitor ISE RADIUS accounting
  hosts: localhost
  gather_facts: true
  vars:
    accounting_start_date: "2026-03-16T00:00:00"
    accounting_end_date: "2026-03-17T00:00:00"
    siem_integration_enabled: true
    siem_endpoint: "https://siem.example.com"
  roles:
    - role: cisco/roles/ise_monitor__radius_accounting
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `monitoring` | All monitoring and data retrieval tasks |
| `radius` | RADIUS session retrieval tasks |
| `accounting` | Accounting log retrieval tasks |
| `analysis` | Session statistics computation tasks |
| `siem` | SIEM data forwarding tasks |
| `integration` | External integration tasks |
| `reporting` | Report generation tasks |

## Notes

- This role is read-only with respect to ISE; it does not modify any ISE configuration.
- SIEM forwarding failures use `ignore_errors: true` to prevent blocking report generation.
- All credentials must be stored in Ansible Vault.
