# ise_guest__accounts_bulk

Creates Cisco ISE guest user accounts in bulk, either from a CSV file or from an inline variable list. This role is used when large numbers of temporary guest credentials must be provisioned at once — for example, for an event, conference, or scheduled contractor access — without manually creating each account through the ISE GUI or sponsor portal.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- `community.general` collection (for `from_csv` filter)
- ISE admin credentials with ERS API access and Guest Services enabled
- A guest type and portal configured in ISE
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
| `ise_guest__accounts_bulk_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_guest__accounts_bulk_log_level` | `"INFO"` | No | Logging |
| `ise_guest__accounts_bulk_log_to_syslog` | `true` | No | — |
| `ise_guest__accounts_bulk_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_guest__accounts_bulk_notify_on_completion` | `false` | No | Notification Settings |
| `ise_guest__accounts_bulk_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_guest__accounts_bulk_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

### CSV Import

```yaml
- name: Bulk create guest accounts from CSV
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    guest_csv_file: "/data/event_guests.csv"
    default_guest_type: "Contractor"
    default_portal_id: "portal-uuid-here"
  roles:
    - role: cisco/roles/ise_guest__accounts_bulk
```

CSV format example:
```csv
username,first_name,last_name,email,company
jsmith,John,Smith,jsmith@example.com,Acme Corp
ajones,Alice,Jones,ajones@vendor.com,Vendor Inc
```

### Variable List Import

```yaml
- name: Bulk create guest accounts from variable list
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    default_guest_type: "Daily"
    default_portal_id: "portal-uuid-here"
    guest_accounts:
      - name: "event_guest_001"
        first_name: "Event"
        last_name: "Guest"
        email: "guest001@example.com"
        company: "Conference Attendee"
  roles:
    - role: cisco/roles/ise_guest__accounts_bulk
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `bulk` | All bulk operation tasks |
| `import` | CSV file reading tasks |
| `parsing` | CSV data parsing tasks |
| `guest` | Guest account creation tasks |
| `reporting` | Report and credential document generation |

## Notes

- A credential report is written to `ise_artifacts_dir` for distribution; protect this file appropriately.
- When both `guest_csv_file` and `guest_accounts` are provided, the CSV takes precedence.
- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- All credentials must be stored in Ansible Vault.

## License

MIT
