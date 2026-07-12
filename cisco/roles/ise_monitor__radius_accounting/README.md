# ise_monitor__radius_accounting

Retrieves and analyzes RADIUS accounting data from Cisco ISE, including active session lists and historical accounting logs. This role computes session statistics (total sessions, unique authenticated users, NAS device count), exports data to a SIEM, and generates timestamped JSON reports. It is used for network access visibility, capacity planning, and compliance auditing.

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
| `ise_monitor__radius_accounting_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_monitor__radius_accounting_log_level` | `"INFO"` | No | Logging |
| `ise_monitor__radius_accounting_log_to_syslog` | `true` | No | — |
| `ise_monitor__radius_accounting_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_monitor__radius_accounting_notify_on_completion` | `false` | No | Notification Settings |
| `ise_monitor__radius_accounting_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_monitor__radius_accounting_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT
