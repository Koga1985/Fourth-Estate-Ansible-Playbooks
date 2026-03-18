# ise_endpoints__register_bulk

Registers endpoints in Cisco ISE in bulk, either from a CSV file or from a variable list. This role is used to pre-populate the ISE endpoint database with known devices — such as managed workstations, printers, or IoT devices — including static group assignment. It supports both CSV-driven import workflows and inline variable definitions.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- `community.general` collection (for `from_csv` filter)
- ISE admin credentials with ERS API access
- Ansible Vault for credential management

## Role Variables

### ISE Connection

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hostname` | `{{ vault_ise_hostname }}` | **Yes** | ISE primary PAN hostname or IP |
| `ise_username` | `{{ vault_ise_username }}` | **Yes** | ISE admin username |
| `ise_password` | `{{ vault_ise_password }}` | **Yes** | ISE admin password (vault-protected) |
| `ise_verify_ssl` | `true` | No | Validate ISE TLS certificate |
| `ise_use_proxy` | `false` | No | Route ISE API calls through a proxy |
| `ise_debug` | `false` | No | Enable verbose debug logging |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` runs in plan/audit mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Endpoint Input

| Variable | Default | Required | Description |
|---|---|---|
| `endpoint_csv_file` | (optional) | No | Absolute path to a CSV file; columns should include `mac` (or `MAC`), optional `description`, and optional `group_id` |
| `endpoints` | `[]` | No | Fallback list of endpoint dicts when `endpoint_csv_file` is not provided |
| `default_endpoint_group` | (required when group not in CSV) | No | Default endpoint identity group ID for endpoints without an explicit `group_id` |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_endpoints__register_bulk_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_endpoints__register_bulk_log_level` | `INFO` | No | Log verbosity level |
| `ise_endpoints__register_bulk_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_endpoints__register_bulk_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_endpoints__register_bulk_notify_on_completion` | `false` | No | Send email on completion |
| `ise_endpoints__register_bulk_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_endpoints__register_bulk_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

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
