# ise_policy__policy_sets_scaffold

Creates the Cisco ISE Network Access policy set containers that serve as the top-level organizational structure for authentication and authorization rules. Policy sets group related rules together and are matched against incoming RADIUS requests based on configurable conditions (e.g., NAS type, protocol, network device group). This role scaffolds the policy set structure as a prerequisite before rules are applied by `ise_policy__apply_rules`.

The role includes a wrapper playbook pattern: it plans by default and mutates only when `apply_changes: true` is set, making it safe to use in a review-then-apply workflow.

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
| `ise_policy__policy_sets_scaffold_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_policy__policy_sets_scaffold_log_level` | `"INFO"` | No | Logging |
| `ise_policy__policy_sets_scaffold_log_to_syslog` | `true` | No | — |
| `ise_policy__policy_sets_scaffold_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_policy__policy_sets_scaffold_notify_on_completion` | `false` | No | Notification Settings |
| `ise_policy__policy_sets_scaffold_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_policy__policy_sets_scaffold_auto_backup` | `true` | No | Backup Settings |

## Example Playbook

### Plan Mode (review what will be created)

```yaml
- name: Plan ISE policy set scaffold
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: false
    policy_sets:
      - name: "Wired-Dot1X"
        description: "Wired 802.1X Network Access"
        service_name: "Default Network Access"
      - name: "Wireless-Dot1X"
        description: "Wireless 802.1X Network Access"
        service_name: "Default Network Access"
      - name: "Device-Admin"
        description: "TACACS Device Administration"
        service_name: "Default Device Admin"
  roles:
    - role: cisco/roles/ise_policy__policy_sets_scaffold
```

### Apply Changes

```yaml
- name: Scaffold ISE policy sets
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    policy_sets:
      - name: "Wired-Dot1X"
        description: "Wired 802.1X Network Access"
        condition:
          conditionType: "ConditionAttributes"
          attributeName: "Radius:NAS-Port-Type"
          attributeValue: "Ethernet"
          operator: "EQUALS"
        service_name: "Default Network Access"
      - name: "Wireless-Dot1X"
        description: "Wireless 802.1X Network Access"
        condition:
          conditionType: "ConditionAttributes"
          attributeName: "Radius:NAS-Port-Type"
          attributeValue: "Wireless - IEEE 802.11"
          operator: "EQUALS"
        service_name: "Default Network Access"
  roles:
    - role: cisco/roles/ise_policy__policy_sets_scaffold
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `policy` | All policy configuration tasks |
| `sets` | Policy set creation tasks |
| `reporting` | Report generation tasks |

## Recommended Role Execution Order

For a full policy deployment, run roles in this sequence:

1. `ise_policy__conditions_library` — build reusable conditions
2. `ise_policy__radius_dacls` — create downloadable ACLs
3. `ise_policy__authz_profiles` — create authorization profiles
4. **`ise_policy__policy_sets_scaffold`** — create policy set containers (this role)
5. `ise_policy__apply_rules` — apply authentication and authorization rules

## Notes

- `apply_changes` defaults to `false`; the role is self-contained and safe to run in plan mode by default.
- Policy set UUIDs are needed by `ise_policy__apply_rules`; capture them from the ISE GUI or API after this role runs.
- All credentials must be stored in Ansible Vault.

## License

MIT
