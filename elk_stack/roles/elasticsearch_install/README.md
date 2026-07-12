# elasticsearch_install

Elasticsearch Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `elk_stack/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `elasticsearch_version` | `"8.11.3"` | No | Elasticsearch version |
| `elasticsearch_major_version` | `"8.x"` | No | — |
| `elasticsearch_install_method` | `"package"` | No | Installation method package, archive |
| `elasticsearch_use_official_repo` | `true` | No | Repository configuration |
| `elasticsearch_repo_gpg_key` | `"https://artifacts.elastic.co/GPG-KEY-elasticsearch"` | No | — |
| `elasticsearch_user` | `"elasticsearch"` | No | System configuration |
| `elasticsearch_group` | `"elasticsearch"` | No | — |
| `elasticsearch_home` | `"/usr/share/elasticsearch"` | No | — |
| `elasticsearch_config_dir` | `"/etc/elasticsearch"` | No | — |
| `elasticsearch_data_dir` | `"/var/lib/elasticsearch"` | No | — |
| `elasticsearch_log_dir` | `"/var/log/elasticsearch"` | No | — |
| `elasticsearch_pid_dir` | `"/var/run/elasticsearch"` | No | — |
| `elasticsearch_data_paths` | `(see defaults/main.yml)` | No | Additional data paths for multi-disk setups |
| `elasticsearch_java_home` | `""` | No | Java/JVM configuration Auto-detect if empty |
| `elasticsearch_heap_size` | `"{{ (ansible_memtotal_mb * 0.5) \| int \| min(32768) }}m"` | No | — |
| `elasticsearch_heap_size_min` | `"{{ elasticsearch_heap_size }}"` | No | — |
| `elasticsearch_heap_size_max` | `"{{ elasticsearch_heap_size }}"` | No | — |
| `elasticsearch_jvm_options` | `(see defaults/main.yml)` | No | JVM options |
| `elasticsearch_max_open_files` | `65536` | No | System limits |
| `elasticsearch_max_locked_memory` | `"unlimited"` | No | — |
| `elasticsearch_max_map_count` | `262144` | No | — |
| `elasticsearch_max_threads` | `4096` | No | — |
| `elasticsearch_http_port` | `9200` | No | Network configuration |
| `elasticsearch_transport_port` | `9300` | No | — |
| `elasticsearch_configure_firewall` | `true` | No | Firewall configuration |
| `elasticsearch_firewall_zone` | `"public"` | No | — |
| `elasticsearch_allowed_ips` | `[]` | No | Empty = allow all |
| `elasticsearch_service_enabled` | `true` | No | Service configuration |
| `elasticsearch_service_state` | `"started"` | No | — |
| `elasticsearch_restart_on_upgrade` | `false` | No | — |
| `elasticsearch_perform_bootstrap_checks` | `true` | No | Bootstrap configuration |
| `elasticsearch_plugins` | `[]` | No | Plugin installation |
| `elasticsearch_backup_dir` | `"/var/backups/elasticsearch"` | No | Backup directories |
| `elasticsearch_snapshot_dir` | `"/mnt/elasticsearch/snapshots"` | No | — |
| `elasticsearch_security_enabled` | `true` | No | Security (basic setup, detailed in elasticsearch_security role) |
| `elasticsearch_security_enrollment_token` | `""` | No | — |
| `elasticsearch_fourth_estate_mode` | `true` | No | Fourth Estate specific |
| `elasticsearch_retention_days` | `365` | No | Compliance requirement |
| `elasticsearch_audit_logging` | `true` | No | — |
| `elasticsearch_disable_swap` | `true` | No | Performance tuning |
| `elasticsearch_bootstrap_memory_lock` | `true` | No | — |
| `elasticsearch_monitoring_enabled` | `true` | No | Monitoring |
| `elasticsearch_monitoring_collection_interval` | `"10s"` | No | — |

## Example Playbook

```yaml
---
- name: Elasticsearch Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: elk_stack/roles/elasticsearch_install
```

## License

MIT
