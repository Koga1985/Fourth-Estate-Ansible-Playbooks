# ise_policy__policy_sets_scaffold

Creates the Cisco ISE Network Access policy set containers that serve as the top-level organizational structure for authentication and authorization rules. Policy sets group related rules together and are matched against incoming RADIUS requests based on configurable conditions (e.g., NAS type, protocol, network device group). This role scaffolds the policy set structure as a prerequisite before rules are applied by `ise_policy__apply_rules`.

The role includes a wrapper playbook pattern: it plans by default and mutates only when `apply_changes: true` is set, making it safe to use in a review-then-apply workflow.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API access and Network Access policy management permissions
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
| `apply_changes` | `false` | No | Set to `true` to write changes; `false` generates a plan document only |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Policy Sets

| Variable | Default | Required | Description |
|---|---|---|
| `policy_sets` | (required) | No | List of policy set definitions. Each entry has: `name` (required), optional `description`, optional `condition` (a condition expression that determines when this policy set is matched), `is_proxy` (default `false`), and `service_name` (default `Default Network Access`) |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_policy__policy_sets_scaffold_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_policy__policy_sets_scaffold_log_level` | `INFO` | No | Log verbosity level |
| `ise_policy__policy_sets_scaffold_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_policy__policy_sets_scaffold_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_policy__policy_sets_scaffold_notify_on_completion` | `false` | No | Send email on completion |
| `ise_policy__policy_sets_scaffold_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_policy__policy_sets_scaffold_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

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
