# ise_hygiene__stale_objects_prune

Identifies and removes stale objects from Cisco ISE to maintain database performance and policy accuracy. This role discovers endpoints that have not been seen within a configurable threshold, identifies expired guest accounts, and optionally deletes them. It generates a hygiene report documenting all objects reviewed and actions taken. Running in plan mode (the default) produces the report without deleting anything.

## Requirements

- Ansible 2.14 or later
- `cisco.ise` collection (install via `ansible-galaxy collection install cisco.ise`)
- ISE admin credentials with ERS API read/write access
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
| `ise_hygiene__stale_objects_prune_enabled` | `true` | No | Feature Configuration |
| `enable_disa_stig_compliance` | `true` | No | DISA STIG Compliance |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ise_hygiene__stale_objects_prune_log_level` | `"INFO"` | No | Logging |
| `ise_hygiene__stale_objects_prune_log_to_syslog` | `true` | No | — |
| `ise_hygiene__stale_objects_prune_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `ise_hygiene__stale_objects_prune_notify_on_completion` | `false` | No | Notification Settings |
| `ise_hygiene__stale_objects_prune_notification_email` | `"{{ vault_security_team_email }}"` | No | — |
| `ise_hygiene__stale_objects_prune_auto_backup` | `true` | No | Backup Settings |

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

## License

MIT
