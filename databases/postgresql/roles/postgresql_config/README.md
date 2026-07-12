# postgresql_config

Postgresql Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/postgresql/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `postgresql_version` | `15` | No | PostgreSQL version and paths |
| `postgresql_bin_path` | `"/usr/pgsql-{{ postgresql_version }}/bin"` | No | — |
| `postgresql_data_directory` | `"/var/lib/pgsql/{{ postgresql_version }}/data"` | No | — |
| `postgresql_config_directory` | `"{{ postgresql_data_directory }}"` | No | — |
| `postgresql_log_directory` | `"/var/log/postgresql"` | No | — |
| `postgresql_port` | `5432` | No | Network settings |
| `postgresql_listen_addresses` | `"*"` | No | — |
| `postgresql_max_connections` | `200` | No | — |
| `postgresql_superuser_reserved_connections` | `3` | No | — |
| `postgresql_shared_buffers` | `"{{ (ansible_memtotal_mb * 0.25) \| int }}MB"` | No | Memory settings (calculated from system RAM) |
| `postgresql_effective_cache_size` | `"{{ (ansible_memtotal_mb * 0.75) \| int }}MB"` | No | — |
| `postgresql_maintenance_work_mem` | `"{{ [2048, (ansible_memtotal_mb * 0.05) \| int] \| min }}MB"` | No | — |
| `postgresql_work_mem` | `"{{ ((ansible_memtotal_mb * 1024 * 0.25) / postgresql_max_connectio...` | No | — |
| `postgresql_shared_preload_libraries` | `"pgaudit,pg_stat_statements"` | No | — |
| `postgresql_wal_level` | `replica` | No | WAL settings |
| `postgresql_wal_buffers` | `16MB` | No | — |
| `postgresql_min_wal_size` | `1GB` | No | — |
| `postgresql_max_wal_size` | `4GB` | No | — |
| `postgresql_wal_keep_size` | `1GB` | No | — |
| `postgresql_archive_mode` | `"on"` | No | — |
| `postgresql_archive_command` | `"/bin/true"` | No | — |
| `postgresql_max_wal_senders` | `10` | No | — |
| `postgresql_wal_sender_timeout` | `60s` | No | — |
| `postgresql_checkpoint_timeout` | `15min` | No | Checkpoints |
| `postgresql_checkpoint_completion_target` | `0.9` | No | — |
| `postgresql_checkpoint_warning` | `30s` | No | — |
| `postgresql_log_destination` | `stderr` | No | Logging |
| `postgresql_logging_collector` | `"on"` | No | — |
| `postgresql_log_filename` | `"postgresql-%Y-%m-%d_%H%M%S.log"` | No | — |
| `postgresql_log_file_mode` | `"0640"` | No | — |
| `postgresql_log_rotation_age` | `1d` | No | — |
| `postgresql_log_rotation_size` | `100MB` | No | — |
| `postgresql_log_min_duration_statement` | `1000` | No | — |
| `postgresql_log_checkpoints` | `"on"` | No | — |
| `postgresql_log_connections` | `"on"` | No | — |
| `postgresql_log_disconnections` | `"on"` | No | — |
| `postgresql_log_duration` | `"off"` | No | — |
| `postgresql_log_line_prefix` | `"%m [%p] %q%u@%d "` | No | — |
| `postgresql_log_lock_waits` | `"on"` | No | — |
| `postgresql_log_statement` | `"ddl"` | No | — |
| `postgresql_log_temp_files` | `0` | No | — |
| `postgresql_random_page_cost` | `1.1` | No | Query planner |
| `postgresql_effective_io_concurrency` | `200` | No | — |
| `postgresql_default_statistics_target` | `100` | No | — |
| `postgresql_ssl_enabled` | `true` | No | SSL/TLS configuration |
| `postgresql_ssl_cert_directory` | `"{{ postgresql_data_directory }}"` | No | — |
| `postgresql_ssl_cert_file` | `"{{ postgresql_ssl_cert_directory }}/server.crt"` | No | — |
| `postgresql_ssl_key_file` | `"{{ postgresql_ssl_cert_directory }}/server.key"` | No | — |
| `postgresql_ssl_ca_file` | `"{{ postgresql_ssl_cert_directory }}/root.crt"` | No | — |
| `postgresql_ssl_ciphers` | `"HIGH:MEDIUM:+3DES:!aNULL"` | No | — |
| `postgresql_ssl_prefer_server_ciphers` | `"on"` | No | — |
| `postgresql_ssl_min_protocol_version` | `TLSv1.2` | No | — |
| `postgresql_ssl_generate_self_signed` | `true` | No | — |
| `postgresql_password_encryption` | `scram-sha-256` | No | Authentication and security |
| `postgresql_db_user_namespace` | `"off"` | No | — |
| `postgresql_pgaudit_enabled` | `true` | No | pgAudit configuration |
| `postgresql_pgaudit_log` | `"ddl, role, read, write"` | No | — |
| `postgresql_pgaudit_log_catalog` | `"off"` | No | — |
| `postgresql_pgaudit_log_level` | `log` | No | — |
| `postgresql_pgaudit_log_parameter` | `"on"` | No | — |
| `postgresql_pgaudit_log_relation` | `"on"` | No | — |
| `postgresql_pgaudit_log_statement_once` | `"off"` | No | — |
| `postgresql_pg_stat_statements_enabled` | `true` | No | pg_stat_statements configuration |
| `postgresql_pg_stat_statements_max` | `10000` | No | — |
| `postgresql_pg_stat_statements_track` | `all` | No | — |
| `postgresql_pg_stat_statements_track_utility` | `"on"` | No | — |
| `postgresql_autovacuum` | `"on"` | No | Autovacuum |
| `postgresql_autovacuum_max_workers` | `3` | No | — |
| `postgresql_autovacuum_naptime` | `1min` | No | — |
| `postgresql_autovacuum_vacuum_threshold` | `50` | No | — |
| `postgresql_autovacuum_analyze_threshold` | `50` | No | — |
| `postgresql_autovacuum_vacuum_scale_factor` | `0.2` | No | — |
| `postgresql_autovacuum_analyze_scale_factor` | `0.1` | No | — |
| `postgresql_timezone` | `UTC` | No | Client connection defaults |
| `postgresql_lc_messages` | `en_US.UTF-8` | No | — |
| `postgresql_lc_monetary` | `en_US.UTF-8` | No | — |
| `postgresql_lc_numeric` | `en_US.UTF-8` | No | — |
| `postgresql_lc_time` | `en_US.UTF-8` | No | — |
| `postgresql_default_text_search_config` | `pg_catalog.english` | No | — |
| `postgresql_deadlock_timeout` | `1s` | No | Lock management |
| `postgresql_max_locks_per_transaction` | `64` | No | — |
| `postgresql_exit_on_error` | `"off"` | No | Error handling |
| `postgresql_restart_after_crash` | `"on"` | No | — |
| `postgresql_bgwriter_delay` | `200ms` | No | Background writer |
| `postgresql_bgwriter_lru_maxpages` | `100` | No | — |
| `postgresql_bgwriter_lru_multiplier` | `2.0` | No | — |
| `postgresql_hba_entries` | `(see defaults/main.yml)` | No | pg_hba.conf rules |
| `postgresql_ident_mappings` | `[]` | No | pg_ident.conf mappings |
| `postgresql_custom_configs` | `{}` | No | Custom configuration snippets |
| `postgresql_databases` | `[]` | No | Database and user management |
| `postgresql_users` | `[]` | No | — |
| `postgresql_extensions` | `[]` | No | — |
| `postgresql_privileges` | `[]` | No | — |
| `postgresql_encoding` | `UTF8` | No | Encoding |
| `postgresql_locale` | `en_US.UTF-8` | No | — |

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
