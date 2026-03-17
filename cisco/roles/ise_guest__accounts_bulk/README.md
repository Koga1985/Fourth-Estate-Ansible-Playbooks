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
| `apply_changes` | `false` | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports |

### Guest Account Input

| Variable | Default | Description |
|---|---|---|
| `guest_csv_file` | (optional) | Absolute path to a CSV file with guest account data |
| `guest_accounts` | `[]` | Fallback list of guest account dicts when `guest_csv_file` is not provided |
| `default_guest_type` | (required) | ISE guest type name applied to accounts without an explicit `guest_type` |
| `default_portal_id` | (required) | ISE portal ID applied to accounts without an explicit `portal_id` |

CSV / list fields per guest entry: `username` (or `name`), `first_name`, `last_name`, `email`, `phone`, `company`, `guest_type`, `portal_id`.

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_guest__accounts_bulk_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_guest__accounts_bulk_log_level` | `INFO` | Log verbosity level |
| `ise_guest__accounts_bulk_log_to_syslog` | `true` | Forward events to syslog |
| `ise_guest__accounts_bulk_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_guest__accounts_bulk_notify_on_completion` | `false` | Send email on completion |
| `ise_guest__accounts_bulk_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_guest__accounts_bulk_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

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
