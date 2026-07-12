# ise_report__auth_failures

Retrieves and analyzes Cisco ISE authentication failure records from the MnT API for a specified time window. This role parses failure events, groups them by failure reason and identity store, generates a timestamped JSON report, and is used for security monitoring, troubleshooting, and compliance reporting. It helps identify authentication misconfigurations, brute-force attempts, and systemic identity store issues.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE MnT API accessible from the Ansible control node
- ISE admin credentials with MnT API read access
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
| `ise_report__auth_failures_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_report__auth_failures_log_level` | `"INFO"` | No | Logging |
| `ise_report__auth_failures_log_to_syslog` | `true` | No | — |
| `ise_report__auth_failures_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_report__auth_failures_notify_on_completion` | `false` | No | Notification Settings |
| `ise_report__auth_failures_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_report__auth_failures_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT
