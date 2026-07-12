# ise_policy__apply_rules

Creates and updates authentication and authorization rules within Cisco ISE policy sets. This role is used to apply a defined set of policy rules — specifying identity sources, conditions, and authorization profiles — to one or more policy sets. It is the enforcement step after policy sets and profiles have been scaffolded and is designed to be idempotent.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access and Network Access policy management permissions
- Policy sets must already exist (use `ise_policy__policy_sets_scaffold` first)
- Authorization profiles must already exist (use `ise_policy__authz_profiles` first)
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
| `ise_policy__apply_rules_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_policy__apply_rules_log_level` | `"INFO"` | No | Logging |
| `ise_policy__apply_rules_log_to_syslog` | `true` | No | — |
| `ise_policy__apply_rules_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_policy__apply_rules_notify_on_completion` | `false` | No | Notification Settings |
| `ise_policy__apply_rules_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_policy__apply_rules_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Apply ISE policy rules
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    authentication_rules:
      - policy_set_id: "policy-set-uuid"
        name: "Dot1X-Authentication"
        identity_source: "AD-Domain"
        rank: 1
    authorization_rules:
      - policy_set_id: "policy-set-uuid"
        name: "Employee-Full-Access"
        authorization_profile: "EMPLOYEE_VLAN10"
        rank: 1
      - policy_set_id: "policy-set-uuid"
        name: "Default-Deny"
        authorization_profile: "DenyAccess"
        is_default: true
  roles:
    - role: cisco/roles/ise_policy__apply_rules
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `discovery` | Retrieve existing policy sets |
| `policy` | All policy configuration tasks |
| `authentication` | Authentication rule tasks |
| `authorization` | Authorization rule tasks |
| `reporting` | Report generation tasks |

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in discovery/plan mode.
- `policy_set_id` values must be valid UUIDs of existing policy sets in ISE.
- Rule `rank` values determine evaluation order; lower numbers are evaluated first.
- All credentials must be stored in Ansible Vault.

## License

MIT
