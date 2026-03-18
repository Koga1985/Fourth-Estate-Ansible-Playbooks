# postgresql_install

Postgresql Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/postgresql/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `postgresql_version` | `15` |  |
| `postgresql_major_version` | `"{{ postgresql_version }}"` |  |
| `postgresql_bin_path` | `"/usr/pgsql-{{ postgresql_version }}/bin"` |  |
| `postgresql_home_directory` | `"/var/lib/pgsql"` |  |
| `postgresql_data_directory` | `"/var/lib/pgsql/{{ postgresql_version }}/data"` |  |
| `postgresql_config_directory` | `"{{ postgresql_data_directory }}"` |  |
| `postgresql_log_directory` | `"/var/log/postgresql"` |  |
| `postgresql_backup_directory` | `"/var/lib/pgsql/backups"` |  |
| `postgresql_wal_archive_directory` | `"/var/lib/pgsql/wal_archive"` |  |
| `postgresql_tablespace_directories` | `[]` |  |
| `postgresql_pgaudit_package` | `"pgaudit{{ postgresql_version }}_{{ postgresql_...` |  |
| `postgresql_python_package` | `"python3-psycopg2"` |  |
| `postgresql_encoding` | `UTF8` |  |
| `postgresql_locale` | `en_US.UTF-8` |  |
| `postgresql_initial_password` | `"{{ vault_postgresql_superuser_password | No | defau...` |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Postgresql Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/postgresql/roles/postgresql_install
```

## License

MIT
