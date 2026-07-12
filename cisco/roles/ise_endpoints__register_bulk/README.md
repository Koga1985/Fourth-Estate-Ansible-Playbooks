# ise_endpoints__register_bulk

Registers endpoints in Cisco ISE in bulk, either from a CSV file or from a variable list. This role is used to pre-populate the ISE endpoint database with known devices — such as managed workstations, printers, or IoT devices — including static group assignment. It supports both CSV-driven import workflows and inline variable definitions.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- `community.general` collection (for `from_csv` filter)
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
| `ise_endpoints__register_bulk_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_endpoints__register_bulk_log_level` | `"INFO"` | No | Logging |
| `ise_endpoints__register_bulk_log_to_syslog` | `true` | No | — |
| `ise_endpoints__register_bulk_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_endpoints__register_bulk_notify_on_completion` | `false` | No | Notification Settings |
| `ise_endpoints__register_bulk_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_endpoints__register_bulk_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

### CSV Import

```yaml
- name: Bulk register endpoints from CSV
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    endpoint_csv_file: "/data/endpoints.csv"
    default_endpoint_group: "xxxxxxxx-yyyy-zzzz-aaaa-bbbbbbbbbbbb"
  roles:
    - role: cisco/roles/ise_endpoints__register_bulk
```

CSV format example:
```csv
mac,description,group_id
00:11:22:33:44:55,Finance Laptop,<group-uuid>
00:11:22:33:44:66,Reception Printer,<group-uuid>
```

### Variable List Import

```yaml
- name: Bulk register endpoints from variable list
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    default_endpoint_group: "xxxxxxxx-yyyy-zzzz-aaaa-bbbbbbbbbbbb"
    endpoints:
      - mac: "AA:BB:CC:DD:EE:FF"
        description: "Building access reader"
      - mac: "AA:BB:CC:DD:EE:00"
        description: "Conference room display"
  roles:
    - role: cisco/roles/ise_endpoints__register_bulk
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `bulk` | All bulk operation tasks |
| `import` | CSV file reading tasks |
| `parsing` | CSV data parsing tasks |
| `registration` | Endpoint registration tasks |
| `reporting` | Report generation tasks |

## Notes

- When both `endpoint_csv_file` and `endpoints` are provided, the CSV takes precedence.
- All registered endpoints use `staticGroupAssignment: true`.
- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- All credentials must be stored in Ansible Vault.

## License

MIT
