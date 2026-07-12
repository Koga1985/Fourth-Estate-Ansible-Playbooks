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

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ise_hostname` | `"{{ vault_ise_hostname }}"` | No | ISE Connection Parameters |
| `ise_username` | `"{{ vault_ise_username }}"` | No | — |
| `ise_password` | `"{{ vault_ise_password }}"` | No | — |
| `ise_verify_ssl` | `true` | No | — |
| `ise_use_proxy` | `false` | No | — |
| `ise_debug` | `false` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `ise_artifacts_dir` | `"/tmp/ise-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Configuration |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `audit_start_date` | `"{{ (ansible_date_time.epoch \| int - 86400) \| int }}"` | No | Audit Configuration Last 24 hours |
| `audit_end_date` | `"{{ ansible_date_time.epoch }}"` | No | — |
| `audit_lookback_minutes` | `1440` | No | 24 hours |
| `audit_change_categories` | `(see defaults/main.yml)` | No | Audit Categories |
| `ise_enable_api_audit` | `true` | No | API Audit |
| `authorized_admin_users` | `(see defaults/main.yml)` | No | Authorized Admin Users |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `stig_restricted_actions` | `(see defaults/main.yml)` | No | — |
| `audit_siem_integration_enabled` | `true` | No | SIEM Integration |
| `siem_endpoint` | `"{{ vault_siem_endpoint }}"` | No | — |
| `siem_api_token` | `"{{ vault_siem_api_token }}"` | No | — |
| `audit_notify_on_completion` | `true` | No | Notification Settings |
| `audit_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `audit_export_zip` | `"{{ ise_artifacts_dir }}/ise_config_audit_{{ ansible_date_time.epoc...` | No | Export Settings |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `audit_log_level` | `"INFO"` | No | Logging |
| `audit_log_to_syslog` | `true` | No | — |
| `audit_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `audit_retention_days` | `90` | No | Retention |
| `audit_archive_old_reports` | `true` | No | — |
| `audit_detect_unauthorized_changes` | `true` | No | Change Detection |
| `audit_alert_on_violations` | `true` | No | — |
| `audit_report_formats` | `(see defaults/main.yml)` | No | Reporting Format |
| `smtp_host` | `"{{ vault_smtp_host \| default('localhost') }}"` | No | Email Configuration |
| `smtp_port` | `25` | No | — |

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

## License

MIT
