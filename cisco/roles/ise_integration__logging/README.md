# ise_integration__logging

Configures Cisco ISE remote syslog targets, logging category settings, and SIEM integration. This role ensures that ISE sends the correct event streams — authentication, authorization, posture, guest, and system events — to the appropriate external logging infrastructure. It is a foundational role for meeting DISA STIG audit logging requirements and enabling real-time security monitoring.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access
- A reachable syslog server and/or SIEM endpoint
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
| `ise_integration__logging_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_integration__logging_log_level` | `"INFO"` | No | Logging |
| `ise_integration__logging_log_to_syslog` | `true` | No | — |
| `ise_integration__logging_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_integration__logging_notify_on_completion` | `false` | No | Notification Settings |
| `ise_integration__logging_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_integration__logging_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT
