# postgresql_restore

Postgresql Restore role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/postgresql/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `postgresql_version` | `15` | No | defaults file for postgresql_restore |
| `postgresql_bin_path` | `"/usr/pgsql-{{ postgresql_version }}/bin"` | No | — |
| `postgresql_data_directory` | `"/var/lib/pgsql/{{ postgresql_version }}/data"` | No | — |
| `postgresql_config_directory` | `"{{ postgresql_data_directory }}"` | No | — |
| `postgresql_backup_directory` | `"/var/lib/pgsql/backups"` | No | — |
| `postgresql_wal_archive_directory` | `"/var/lib/pgsql/wal_archive"` | No | — |
| `postgresql_port` | `5432` | No | — |
| `postgresql_home_directory` | `"/var/lib/pgsql"` | No | — |
| `postgresql_recovery_target_action` | `promote` | No | PITR settings postgresql_recovery_target_time: '2025-01-15 14:30:00' postgresql_recovery_target_xid: '12345' pause, promote, shutdown |
| `postgresql_restore_run_analyze` | `true` | No | Post-restore options |
| `postgresql_restore_analyze_databases` | `[]` | No | — |

## Example Playbook

```yaml
---
- name: Postgresql Restore
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/postgresql/roles/postgresql_restore
```

## License

MIT
