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

### Authentication Rules

| Variable | Default | Required | Description |
|---|---|---|
| `authentication_rules` | (required) | No | List of authentication rule definitions. Each entry has `policy_set_id`, `name`, `identity_source`, optional `condition`, optional `rank`, and optional `is_default` |

### Authorization Rules

| Variable | Default | Required | Description |
|---|---|---|
| `authorization_rules` | (required) | No | List of authorization rule definitions. Each entry has `policy_set_id`, `name`, `authorization_profile`, optional `condition`, optional `rank`, and optional `is_default` |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_policy__apply_rules_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_policy__apply_rules_log_level` | `INFO` | No | Log verbosity level |
| `ise_policy__apply_rules_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_policy__apply_rules_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_policy__apply_rules_notify_on_completion` | `false` | No | Send email on completion |
| `ise_policy__apply_rules_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_policy__apply_rules_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

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
