# ise_policy__authz_profiles

Creates and manages Cisco ISE authorization profiles. Authorization profiles define the network access attributes — VLAN assignment, downloadable ACL (dACL), Security Group Tag (SGT), and access type — that are returned to network access devices when a policy rule matches. This role is typically run before `ise_policy__apply_rules` to ensure profiles exist before rules reference them.

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

### Authorization Profiles

| Variable | Default | Description |
|---|---|---|
| `authz_profiles` | (required) | List of authorization profile definitions. Each entry supports: `name` (required), `access_type` (default `ACCESS_ACCEPT`), `vlan` (optional), `dacl` (optional dACL name), and `sgt` (optional Security Group Tag name) |

### Feature Flags

| Variable | Default | Description |
|---|---|---|
| `ise_policy__authz_profiles_enabled` | `true` | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Description |
|---|---|---|
| `ise_policy__authz_profiles_log_level` | `INFO` | Log verbosity level |
| `ise_policy__authz_profiles_log_to_syslog` | `true` | Forward events to syslog |
| `ise_policy__authz_profiles_syslog_server` | `{{ vault_syslog_server }}` | Syslog server address |
| `ise_policy__authz_profiles_notify_on_completion` | `false` | Send email on completion |
| `ise_policy__authz_profiles_notification_email` | `{{ vault_security_team_email }}` | Notification recipient |
| `ise_policy__authz_profiles_auto_backup` | `true` | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | Frameworks referenced in generated reports |

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
