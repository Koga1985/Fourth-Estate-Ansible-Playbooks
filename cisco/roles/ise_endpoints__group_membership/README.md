# ise_endpoints__group_membership

Creates and manages Cisco ISE endpoint identity groups and assigns endpoints to those groups with static group membership. This role is used to establish a structured endpoint inventory where devices are categorized by group (e.g., by device type, department, or trust level) to enable group-based authorization policy decisions.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
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
| `ise_endpoints__group_membership_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_endpoints__group_membership_log_level` | `"INFO"` | No | Logging |
| `ise_endpoints__group_membership_log_to_syslog` | `true` | No | — |
| `ise_endpoints__group_membership_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_endpoints__group_membership_notify_on_completion` | `false` | No | Notification Settings |
| `ise_endpoints__group_membership_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_endpoints__group_membership_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT
