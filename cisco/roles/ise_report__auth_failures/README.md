# ise_report__auth_failures

Retrieves and analyzes Cisco ISE authentication failure records from the MnT API for a specified time window. This role parses failure events, groups them by failure reason and identity store, generates a timestamped JSON report, and is used for security monitoring, troubleshooting, and compliance reporting. It helps identify authentication misconfigurations, brute-force attempts, and systemic identity store issues.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
- Ansible Vault for credential management

## Role Variables

### ISE Connection

| Variable | Default | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | Route ISE API calls through a proxy |
| `ise_debug` | `false` | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Description |
|---|---|---|
| `apply_changes` | `false` | Not used for mutation; reserved |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports |

### Report Window

| Variable | Default | Description |
|---|---|---|
| `report_start_date` | (required) | Start of the authentication failure query window |
| `report_end_date` | (required) | End of the authentication failure query window |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_report__auth_failures_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_report__auth_failures_log_level` | `INFO` | Log verbosity level |
| `ise_report__auth_failures_log_to_syslog` | `true` | Forward events to syslog |
| `ise_report__auth_failures_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_report__auth_failures_notify_on_completion` | `false` | Send email on completion |
| `ise_report__auth_failures_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_report__auth_failures_auto_backup` | `true` | Reserved |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Generate ISE authentication failure report
  hosts: localhost
  gather_facts: true
  vars:
    report_start_date: "2026-03-16T00:00:00"
    report_end_date: "2026-03-17T00:00:00"
  roles:
    - role: cisco/roles/ise_report__auth_failures
```

### Daily Scheduled Report

```yaml
- name: Daily ISE auth failure report
  hosts: localhost
  gather_facts: true
  vars:
    report_start_date: "{{ (ansible_date_time.epoch | int - 86400) | string }}"
    report_end_date: "{{ ansible_date_time.epoch }}"
    ise_report__auth_failures_notify_on_completion: true
  roles:
    - role: cisco/roles/ise_report__auth_failures
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `reporting` | All report generation tasks |
| `failures` | Authentication failure retrieval tasks |
| `analysis` | Failure analysis and grouping tasks |

## Output

The role produces a JSON report at:

```
{{ ise_artifacts_dir }}/auth_failures_<epoch>.json
```

The report includes:
- Total failure count
- Failures grouped by failure reason
- Failures grouped by identity store

## Notes

- This role is read-only with respect to ISE; it does not modify any configuration.
- All credentials must be stored in Ansible Vault.
