# ise_policy__conditions_library

Creates and manages reusable network access policy conditions in the Cisco ISE conditions library. Library conditions are named, shareable condition objects (attribute-value comparisons) that can be referenced by name across multiple policy rules and policy sets rather than duplicating condition logic inline. This role builds the condition library as a prerequisite step before creating policy rules.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access and Network Access policy management permissions
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
| `apply_changes` | `false` | Set to `true` to write changes; `false` runs in plan mode |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | Local directory for generated reports |

### Policy Conditions

| Variable | Default | Description |
|---|---|---|
| `policy_conditions` | (required) | List of condition definitions. Each entry has: `name` (required), `type` (condition type, e.g., `LibraryConditionAttributes`), `attribute_name` (the ISE attribute to evaluate), `attribute_value` (the expected value), and `operator` (comparison operator, e.g., `EQUALS`, `CONTAINS`, `STARTS_WITH`) |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_policy__conditions_library_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_policy__conditions_library_log_level` | `INFO` | Log verbosity level |
| `ise_policy__conditions_library_log_to_syslog` | `true` | Forward events to syslog |
| `ise_policy__conditions_library_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_policy__conditions_library_notify_on_completion` | `false` | Send email on completion |
| `ise_policy__conditions_library_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_policy__conditions_library_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

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
