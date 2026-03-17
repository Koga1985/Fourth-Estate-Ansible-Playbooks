# ise_audit__config_changes

Retrieves, parses, and reports on Cisco ISE configuration change audit logs. This role pulls change records from the ISE Monitoring and Troubleshooting (MnT) API, detects changes made by unauthorized administrators, flags DISA STIG compliance violations, exports events to a SIEM, archives reports, and optionally sends email notifications. It is designed for continuous compliance monitoring under DoD/FISMA frameworks.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- `community.general` collection (for archive module)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
- SMTP server available if email notification is enabled
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
| `apply_changes` | `false` | Not used for mutation in this role; controls report archiving behavior |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports |

### Audit Window

| Variable | Default | Description |
|---|---|---|
| `audit_start_date` | Last 24 hours (epoch) | Start of audit window (Unix epoch) |
| `audit_end_date` | Current time (epoch) | End of audit window (Unix epoch) |
| `audit_lookback_minutes` | `1440` | Convenience variable: lookback window in minutes |
| `audit_change_categories` | See `defaults/main.yml` | ISE change categories to include in the audit query |
| `ise_enable_api_audit` | `true` | Enable MnT API audit log retrieval |

### Authorization and Compliance

| Variable | Default | Description |
|---|---|---|
| `authorized_admin_users` | `[admin, automation_user, fourth_estate_admin, ...]` | Usernames considered authorized; changes by others trigger an alert |
| `enable_disa_stig_compliance` | `true` | Check for STIG restricted action violations |
| `stig_restricted_actions` | `[DISABLE_AUDIT, DELETE_BACKUP, ...]` | Actions flagged as STIG violations |

### SIEM Integration

| Variable | Default | Description |
|---|---|---|
| `audit_siem_integration_enabled` | `true` | Forward parsed events to SIEM |
| `siem_endpoint` | `{{ vault_siem_endpoint }}` | SIEM ingest endpoint URL |
| `siem_api_token` | `{{ vault_siem_api_token }}` | Bearer token for SIEM API |

### Notifications and Retention

| Variable | Default | Description |
|---|---|---|
| `audit_notify_on_completion` | `true` | Send email report when audit completes |
| `audit_notification_email` | `{{ vault_security_team_email }}` | Recipient address |
| `smtp_host` | `{{ vault_smtp_host \| default('localhost') }}` | SMTP relay hostname |
| `smtp_port` | `25` | SMTP port |
| `audit_export_zip` | `{{ ise_artifacts_dir }}/ise_config_audit_<epoch>.zip` | Path for archived report bundle |
| `audit_retention_days` | `90` | How many days to retain audit artifacts |
| `audit_archive_old_reports` | `true` | Archive reports older than retention period |

### Reporting

| Variable | Default | Description |
|---|---|---|
| `audit_report_formats` | `[json, csv, html]` | Output formats for audit reports |
| `audit_detect_unauthorized_changes` | `true` | Flag changes by non-authorized users |
| `audit_alert_on_violations` | `true` | Emit warnings for detected violations |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Run ISE configuration change audit
  hosts: localhost
  gather_facts: true
  vars:
    audit_lookback_minutes: 2880   # 48-hour lookback
    audit_notify_on_completion: true
    authorized_admin_users:
      - admin
      - automation_user
      - jane.doe
  roles:
    - role: cisco/roles/ise_audit__config_changes
```

### STIG Compliance Audit Only

```yaml
- name: STIG compliance audit
  hosts: localhost
  gather_facts: true
  vars:
    enable_disa_stig_compliance: true
    audit_siem_integration_enabled: false
  roles:
    - role: cisco/roles/ise_audit__config_changes
  tags: [compliance, stig]
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `audit` | All audit-related tasks |
| `logs` | Log retrieval tasks |
| `parsing` | Log parsing and fact-setting tasks |
| `security` | Unauthorized-change detection tasks |
| `compliance` | Compliance framework checks |
| `stig` | DISA STIG violation checks |
| `siem` | SIEM forwarding tasks |
| `reporting` | Report generation tasks |
| `archive` | Report archiving tasks |
| `notification` | Email notification tasks |

## Notes

- This role is primarily read-only; it does not modify ISE configuration.
- All credentials must be stored in Ansible Vault.
- SIEM and email notification failures use `ignore_errors: true` to prevent blocking the audit run.
- Reports are generated in both JSON and CSV format for downstream processing.
