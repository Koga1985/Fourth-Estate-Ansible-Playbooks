# postgresql_install

Postgresql Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/postgresql/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `postgresql_version` | `15` | No | PostgreSQL version |
| `postgresql_major_version` | `"{{ postgresql_version }}"` | No | — |
| `postgresql_bin_path` | `"/usr/pgsql-{{ postgresql_version }}/bin"` | No | Installation paths |
| `postgresql_home_directory` | `"/var/lib/pgsql"` | No | — |
| `postgresql_data_directory` | `"/var/lib/pgsql/{{ postgresql_version }}/data"` | No | — |
| `postgresql_config_directory` | `"{{ postgresql_data_directory }}"` | No | — |
| `postgresql_log_directory` | `"/var/log/postgresql"` | No | — |
| `postgresql_backup_directory` | `"/var/lib/pgsql/backups"` | No | — |
| `postgresql_wal_archive_directory` | `"/var/lib/pgsql/wal_archive"` | No | — |
| `postgresql_tablespace_directories` | `[]` | No | Optional tablespace directories |
| `postgresql_packages` | `(see defaults/main.yml)` | No | PostgreSQL packages (OS-specific, can be overridden in vars/) |
| `postgresql_contrib_packages` | `(see defaults/main.yml)` | No | — |
| `postgresql_pgaudit_package` | `"pgaudit{{ postgresql_version }}_{{ postgresql_version }}"` | No | — |
| `postgresql_python_package` | `"python3-psycopg2"` | No | — |
| `postgresql_encoding` | `UTF8` | No | Database initialization parameters |
| `postgresql_locale` | `en_US.UTF-8` | No | — |
| `postgresql_initial_password` | `"{{ vault_postgresql_superuser_password \| default('ChangeMe123!') }}"` | **Yes** | — |
| `postgresql_port` | `5432` | No | Network configuration |
| `postgresql_listen_addresses` | `"localhost"` | No | — |
| `postgresql_max_connections` | `200` | No | — |
| `postgresql_service_enabled` | `true` | No | Service configuration |
| `postgresql_configure_firewall` | `true` | No | — |
| `postgresql_configure_kernel_parameters` | `true` | No | — |
| `postgresql_shared_buffers_mb` | `"{{ (ansible_memtotal_mb * 0.25) \| int }}"` | No | Kernel and system tuning |
| `postgresql_effective_cache_size_mb` | `"{{ (ansible_memtotal_mb * 0.75) \| int }}"` | No | — |
| `postgresql_maintenance_work_mem_mb` | `"{{ [2048, (ansible_memtotal_mb * 0.05) \| int] \| min }}"` | No | — |
| `postgresql_work_mem_mb` | `"{{ ((ansible_memtotal_mb * 0.25) / postgresql_max_connections) \| i...` | No | — |
| `postgresql_ssl_enabled` | `true` | No | Security settings |
| `postgresql_ssl_cert_file` | `"/etc/pki/tls/certs/postgresql.crt"` | No | — |
| `postgresql_ssl_key_file` | `"/etc/pki/tls/private/postgresql.key"` | No | — |
| `postgresql_ssl_ca_file` | `"/etc/pki/tls/certs/ca-bundle.crt"` | No | — |
| `postgresql_auth_method` | `scram-sha-256` | No | — |
| `postgresql_wal_level` | `replica` | No | WAL and replication settings |
| `postgresql_max_wal_senders` | `10` | No | — |
| `postgresql_wal_keep_size_mb` | `1024` | No | — |
| `postgresql_log_destination` | `stderr` | No | Logging configuration |
| `postgresql_logging_collector` | `"on"` | No | — |
| `postgresql_log_filename` | `"postgresql-%Y-%m-%d_%H%M%S.log"` | No | — |
| `postgresql_log_rotation_age` | `1d` | No | — |
| `postgresql_log_rotation_size` | `100MB` | No | — |
| `postgresql_log_min_duration_statement` | `1000` | No | — |
| `postgresql_log_line_prefix` | `"%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h "` | No | — |
| `postgresql_log_connections` | `"on"` | No | — |
| `postgresql_log_disconnections` | `"on"` | No | — |
| `postgresql_log_lock_waits` | `"on"` | No | — |
| `postgresql_log_checkpoints` | `"on"` | No | — |
| `postgresql_checkpoint_completion_target` | `0.9` | No | Performance and optimization |
| `postgresql_max_wal_size_gb` | `4` | No | — |
| `postgresql_min_wal_size_gb` | `1` | No | — |
| `postgresql_random_page_cost` | `1.1` | No | — |
| `postgresql_effective_io_concurrency` | `200` | No | — |
| `postgresql_autovacuum` | `"on"` | No | Autovacuum settings |
| `postgresql_autovacuum_max_workers` | `3` | No | — |
| `postgresql_autovacuum_naptime` | `60` | No | — |
| `postgresql_default_statistics_target` | `100` | No | Query planner |
| `postgresql_pgaudit_enabled` | `true` | No | Compliance and auditing |
| `postgresql_pgaudit_log` | `"ddl, role, read, write"` | No | — |
| `postgresql_pgaudit_log_catalog` | `"off"` | No | — |
| `postgresql_pgaudit_log_parameter` | `"on"` | No | — |
| `postgresql_pgaudit_log_relation` | `"on"` | No | — |
| `postgresql_pgaudit_log_statement_once` | `"off"` | No | — |
| `postgresql_stig_mode` | `true` | No | DISA STIG compliance settings |
| `postgresql_fips_mode` | `false` | No | — |
| `postgresql_health_check_enabled` | `true` | No | Monitoring and health checks |
| `postgresql_health_check_interval` | `60` | No | — |
| `postgresql_archive_mode` | `"on"` | No | Backup integration |
| `postgresql_archive_command` | `"test ! -f {{ postgresql_wal_archive_directory }}/%f && cp %p {{ po...` | No | — |
| `postgresql_shared_preload_libraries` | `(see defaults/main.yml)` | No | Extensions to preload |
| `postgresql_timezone` | `UTC` | No | Timezone |
| `postgresql_statement_timeout` | `0` | No | Connection pooling |
| `postgresql_idle_in_transaction_session_timeout` | `0` | No | — |
| `postgresql_custom_config` | `{}` | No | Custom configuration snippets |

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
