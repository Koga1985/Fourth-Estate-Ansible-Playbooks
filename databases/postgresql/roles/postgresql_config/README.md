# postgresql_config

Postgresql Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/postgresql/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `postgresql_version` | `15` |  |
| `postgresql_bin_path` | `"/usr/pgsql-{{ postgresql_version }}/bin"` |  |
| `postgresql_data_directory` | `"/var/lib/pgsql/{{ postgresql_version }}/data"` |  |
| `postgresql_config_directory` | `"{{ postgresql_data_directory }}"` |  |
| `postgresql_log_directory` | `"/var/log/postgresql"` |  |
| `postgresql_port` | `5432` |  |
| `postgresql_listen_addresses` | `"*"` |  |
| `postgresql_max_connections` | `200` |  |
| `postgresql_superuser_reserved_connections` | `3` |  |
| `postgresql_shared_buffers` | `"{{ (ansible_memtotal_mb * 0.25) | No | int }}MB"` |
| `postgresql_effective_cache_size` | `"{{ (ansible_memtotal_mb * 0.75) | No | int }}MB"` |
| `postgresql_maintenance_work_mem` | `"{{ [2048, (ansible_memtotal_mb * 0.05) | No | int] ...` |
| `postgresql_work_mem` | `"{{ ((ansible_memtotal_mb * 1024 * 0.25) / post...` |  |
| `postgresql_shared_preload_libraries` | `"pgaudit,pg_stat_statements"` |  |
| `postgresql_wal_level` | `replica` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Postgresql Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/postgresql/roles/postgresql_config
```

## License

MIT
