# vast_backup_dr

Vast Backup Dr role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vast/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vast_mgmt_host` | `"{{ vault_vast_mgmt_host }}"` |  |
| `vast_mgmt_port` | `443` |  |
| `vast_mgmt_user` | `"{{ vault_vast_mgmt_user }}"` |  |
| `vast_mgmt_password` | `"{{ vault_vast_mgmt_password }}"` |  |
| `vast_api_version` | `"v1"` |  |
| `vast_verify_ssl` | `true` |  |
| `vast_snapshot_enabled` | `true` |  |
| `vast_snapshot_schedule` | `"daily"` |  |
| `vast_snapshot_retention_days` | `30` |  |
| `vast_snapshot_prefix` | `"auto"` |  |
| `vast_replication_enabled` | `false` |  |
| `vast_replication_type` | `"async"` | No | Options: sync, async |
| `vast_replication_target_cluster` | `"{{ vault_vast_dr_cluster | No | default('') }}"` |
| `vast_replication_target_user` | `"{{ vault_vast_dr_user | No | default('') }}"` |
| `vast_replication_target_password` | `"{{ vault_vast_dr_password | No | default('') }}"` |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vast Backup Dr
  hosts: localhost
  gather_facts: false
  roles:
    - role: vast/roles/vast_backup_dr
```

## License

MIT
