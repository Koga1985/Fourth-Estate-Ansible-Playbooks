# ise_hygiene__stale_objects_prune

Identifies and removes stale objects from Cisco ISE to maintain database performance and policy accuracy. This role discovers endpoints that have not been seen within a configurable threshold, identifies expired guest accounts, and optionally deletes them. It generates a hygiene report documenting all objects reviewed and actions taken. Running in plan mode (the default) produces the report without deleting anything.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API read/write access
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
| `apply_changes` | `false` | No | Set to `true` to delete stale objects; `false` identifies but does not delete |
| `ise_artifacts_dir` | `/tmp/ise-artifacts` | No | Local directory for generated reports |

### Stale Endpoint Pruning

| Variable | Default | Required | Description |
|---|---|---|
| `stale_days` | (required) | No | Number of days since last seen before an endpoint is considered stale |
| `hygiene_delete_stale_endpoints` | (required) | No | Set to `true` to delete identified stale endpoints (also requires `apply_changes: true`) |

### Guest Account Pruning

| Variable | Default | Required | Description |
|---|---|---|
| `expired_guest_accounts` | `[]` | No | List of expired guest account objects to purge (pre-populated by discovery tasks or external input) |
| `hygiene_purge_expired_guests` | (required) | No | Set to `true` to purge expired guest accounts (also requires `apply_changes: true`) |

### Feature Flags

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hygiene__stale_objects_prune_enabled` | `true` | No | Master toggle for this role |
| `enable_disa_stig_compliance` | `true` | No | Apply STIG-compliant settings |

### Logging and Notifications

| Variable | Default | Required | Description |
|---|---|---|
| `ise_hygiene__stale_objects_prune_log_level` | `INFO` | No | Log verbosity level |
| `ise_hygiene__stale_objects_prune_log_to_syslog` | `true` | No | Forward events to syslog |
| `ise_hygiene__stale_objects_prune_syslog_server` | `{{ vault_syslog_server }}` | **Yes** | Syslog server address |
| `ise_hygiene__stale_objects_prune_notify_on_completion` | `false` | No | Send email on completion |
| `ise_hygiene__stale_objects_prune_notification_email` | `{{ vault_security_team_email }}` | **Yes** | Notification recipient |
| `ise_hygiene__stale_objects_prune_auto_backup` | `true` | No | Trigger ISE backup after changes |

### Compliance Frameworks

| Variable | Default | Required | Description |
|---|---|---|
| `compliance_frameworks` | `[dod_stig, nist_800_53, nist_800_171, fisma_moderate]` | No | Frameworks referenced in generated reports |

## Example Playbook

### Plan Mode (identify only)

```yaml
- name: Identify stale ISE objects (plan mode)
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: false
    stale_days: 90
    hygiene_delete_stale_endpoints: false
    hygiene_purge_expired_guests: false
  roles:
    - role: cisco/roles/ise_hygiene__stale_objects_prune
```

### Cleanup Mode

```yaml
- name: Prune stale ISE objects
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    stale_days: 180
    hygiene_delete_stale_endpoints: true
    hygiene_purge_expired_guests: true
  roles:
    - role: cisco/roles/ise_hygiene__stale_objects_prune
```

## Tags

| Tag | Description |
|---|---|
| `validation` | Parameter assertion checks |
| `discovery` | Retrieve all endpoint objects |
| `hygiene` | All hygiene analysis and cleanup tasks |
| `analysis` | Stale endpoint identification tasks |
| `cleanup` | Endpoint deletion tasks |
| `guest` | Guest account pruning tasks |
| `reporting` | Report generation tasks |

## Notes

- Deletion is gated by BOTH `apply_changes: true` AND the specific `hygiene_delete_stale_endpoints` / `hygiene_purge_expired_guests` flags to prevent accidental data loss.
- Always run in plan mode first to review the stale object list before enabling deletion.
- All credentials must be stored in Ansible Vault.
