# ise_policy__conditions_library

Creates and manages reusable network access policy conditions in the Cisco ISE conditions library. Library conditions are named, shareable condition objects (attribute-value comparisons) that can be referenced by name across multiple policy rules and policy sets rather than duplicating condition logic inline. This role builds the condition library as a prerequisite step before creating policy rules.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access and Network Access policy management permissions
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
| `ise_policy__conditions_library_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_policy__conditions_library_log_level` | `"INFO"` | No | Logging |
| `ise_policy__conditions_library_log_to_syslog` | `true` | No | — |
| `ise_policy__conditions_library_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_policy__conditions_library_notify_on_completion` | `false` | No | Notification Settings |
| `ise_policy__conditions_library_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_policy__conditions_library_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

```yaml
- name: Build ISE policy conditions library
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    policy_conditions:
      - name: "Wired-802.1X"
        type: "LibraryConditionAttributes"
        attribute_name: "Radius:NAS-Port-Type"
        attribute_value: "Ethernet"
        operator: "EQUALS"
      - name: "Wireless-802.1X"
        type: "LibraryConditionAttributes"
        attribute_name: "Radius:NAS-Port-Type"
        attribute_value: "Wireless - IEEE 802.11"
        operator: "EQUALS"
      - name: "AD-Domain-Joined"
        type: "LibraryConditionAttributes"
        attribute_name: "AD:ExternalGroups"
        attribute_value: "Domain Computers"
        operator: "CONTAINS"
      - name: "Compliant-Posture"
        type: "LibraryConditionAttributes"
        attribute_name: "Session:PostureStatus"
        attribute_value: "Compliant"
        operator: "EQUALS"
  roles:
    - role: cisco/roles/ise_policy__conditions_library
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `conditions` | All conditions library tasks |
| `reporting` | Report generation tasks |

## Recommended Role Execution Order

For a full policy deployment, run roles in this sequence:

1. `ise_policy__conditions_library` — build reusable conditions
2. `ise_policy__radius_dacls` — create downloadable ACLs
3. `ise_policy__authz_profiles` — create authorization profiles
4. `ise_policy__policy_sets_scaffold` — create policy set containers
5. `ise_policy__apply_rules` — apply authentication and authorization rules

## Notes

- `apply_changes` defaults to `false`; the role is safe to run in plan mode.
- Conditions created here can be referenced by name in `ise_policy__apply_rules` rule conditions.
- All credentials must be stored in Ansible Vault.

## License

MIT
