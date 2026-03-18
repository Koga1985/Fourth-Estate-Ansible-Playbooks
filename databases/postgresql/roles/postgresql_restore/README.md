# postgresql_restore

Postgresql Restore role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/postgresql/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `postgresql_version` | `15` |  |
| `postgresql_bin_path` | `"/usr/pgsql-{{ postgresql_version }}/bin"` |  |
| `postgresql_data_directory` | `"/var/lib/pgsql/{{ postgresql_version }}/data"` |  |
| `postgresql_config_directory` | `"{{ postgresql_data_directory }}"` |  |
| `postgresql_backup_directory` | `"/var/lib/pgsql/backups"` |  |
| `postgresql_wal_archive_directory` | `"/var/lib/pgsql/wal_archive"` |  |
| `postgresql_port` | `5432` |  |
| `postgresql_home_directory` | `"/var/lib/pgsql"` |  |
| `postgresql_recovery_target_action` | `promote` | No | pause, promote, shutdown |
| `postgresql_restore_run_analyze` | `true` |  |
| `postgresql_restore_analyze_databases` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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
