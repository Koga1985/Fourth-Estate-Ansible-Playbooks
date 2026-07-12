# ise_policy__authz_profiles

Creates and manages Cisco ISE authorization profiles. Authorization profiles define the network access attributes — VLAN assignment, downloadable ACL (dACL), Security Group Tag (SGT), and access type — that are returned to network access devices when a policy rule matches. This role is typically run before `ise_policy__apply_rules` to ensure profiles exist before rules reference them.

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
| `ise_policy__authz_profiles_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_policy__authz_profiles_log_level` | `"INFO"` | No | Logging |
| `ise_policy__authz_profiles_log_to_syslog` | `true` | No | — |
| `ise_policy__authz_profiles_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_policy__authz_profiles_notify_on_completion` | `false` | No | Notification Settings |
| `ise_policy__authz_profiles_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_policy__authz_profiles_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Configure ISE authorization profiles
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    authz_profiles:
      - name: "EMPLOYEE_VLAN10"
        access_type: "ACCESS_ACCEPT"
        vlan: 10
        dacl: "PERMIT_ALL_TRAFFIC"
        sgt: "Employees"
      - name: "CONTRACTOR_VLAN20"
        access_type: "ACCESS_ACCEPT"
        vlan: 20
        dacl: "PERMIT_INTERNET_ONLY"
      - name: "QUARANTINE_VLAN99"
        access_type: "ACCESS_ACCEPT"
        vlan: 99
        dacl: "DENY_ALL"
      - name: "DenyAccess"
        access_type: "ACCESS_REJECT"
  roles:
    - role: cisco/roles/ise_policy__authz_profiles
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `authz` | All authorization profile tasks |
| `profiles` | Profile creation and update tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Referenced `dacl` names must exist in ISE; use `ise_policy__radius_dacls` to create them first.
- Referenced `sgt` (Security Group Tag) names must exist in ISE TrustSec configuration.
- All credentials must be stored in Ansible Vault.

## License

MIT
