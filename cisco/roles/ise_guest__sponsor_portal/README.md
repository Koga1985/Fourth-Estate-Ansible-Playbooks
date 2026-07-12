# ise_guest__sponsor_portal

Configures the Cisco ISE sponsor portal and sponsor groups. The sponsor portal allows authorized internal users (sponsors) to create, manage, and approve guest accounts on behalf of visiting guests. This role provisions the portal settings, certificate bindings, password-change permissions, and the sponsor groups that define which guest types and locations a sponsor can manage.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE 3.x or later with Guest Services licensed and enabled
- ISE admin credentials with ERS API access
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
| `ise_guest__sponsor_portal_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_guest__sponsor_portal_log_level` | `"INFO"` | No | Logging |
| `ise_guest__sponsor_portal_log_to_syslog` | `true` | No | — |
| `ise_guest__sponsor_portal_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_guest__sponsor_portal_notify_on_completion` | `false` | No | Notification Settings |
| `ise_guest__sponsor_portal_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_guest__sponsor_portal_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Configure ISE sponsor portal
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    sponsor_portal_name: "Sponsor-Portal"
    sponsor_portal_cert_group: "Default Portal Certificate Group"
    sponsor_allow_password_change: true
    sponsor_groups:
      - name: "ALL_ACCOUNTS"
        is_default: true
        guest_types:
          - "Contractor"
          - "Daily"
          - "Weekly"
        locations:
          - "San Jose"
          - "Washington DC"
      - name: "LIMITED_SPONSORS"
        is_default: false
        guest_types:
          - "Daily"
  roles:
    - role: cisco/roles/ise_guest__sponsor_portal
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `guest` | All guest service tasks |
| `sponsor` | Sponsor-specific tasks |
| `portal` | Sponsor portal configuration tasks |
| `groups` | Sponsor group configuration tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Sponsor groups reference guest types by name; those guest types must already exist in ISE.
- All credentials must be stored in Ansible Vault.

## License

MIT
