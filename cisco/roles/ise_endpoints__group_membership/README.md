# ise_endpoints__group_membership

Creates and manages Cisco ISE endpoint identity groups and assigns endpoints to those groups with static group membership. This role is used to establish a structured endpoint inventory where devices are categorized by group (e.g., by device type, department, or trust level) to enable group-based authorization policy decisions.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access
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

### Endpoint Identity Groups

| Variable | Default | Description |
|---|---|---|
| `endpoint_groups` | (required) | List of group definitions; each entry has `name` and optional `description` |

### Endpoint Assignments

| Variable | Default | Description |
|---|---|---|
| `endpoint_group_assignments` | (required) | List of endpoint-to-group mappings; each entry has `mac_address` and `group_id` |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_endpoints__group_membership_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_endpoints__group_membership_log_level` | `INFO` | Log verbosity level |
| `ise_endpoints__group_membership_log_to_syslog` | `true` | Forward events to syslog |
| `ise_endpoints__group_membership_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_endpoints__group_membership_notify_on_completion` | `false` | Send email on completion |
| `ise_endpoints__group_membership_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_endpoints__group_membership_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

## Example Playbook

```yaml
- name: Manage ISE endpoint group membership
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    endpoint_groups:
      - name: "Workstations"
        description: "Corporate workstations"
      - name: "Printers"
        description: "Network-attached printers"
      - name: "IoT-Devices"
        description: "IoT and OT devices"
    endpoint_group_assignments:
      - mac_address: "AA:BB:CC:11:22:33"
        group_id: "workstations-group-uuid"
      - mac_address: "AA:BB:CC:44:55:66"
        group_id: "printers-group-uuid"
  roles:
    - role: cisco/roles/ise_endpoints__group_membership
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `discovery` | Retrieve existing endpoint groups |
| `endpoints` | All endpoint-related tasks |
| `groups` | Group creation tasks |
| `assignment` | Endpoint-to-group assignment tasks |
| `reporting` | Report generation tasks |

## Notes

- Group IDs (`group_id`) must reference either pre-existing group UUIDs or groups created earlier in the same play.
- Assignments use `staticGroupAssignment: true`, which overrides profiler-assigned groups.
- `apply_changes` defaults to `false`; the role is safe to run in discovery/plan mode.
- All credentials must be stored in Ansible Vault.
