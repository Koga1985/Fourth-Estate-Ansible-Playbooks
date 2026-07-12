# prometheus_install

Prometheus Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `prometheus_grafana/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `prometheus_version` | `"2.48.0"` | No | Prometheus version |
| `prometheus_download_url` | `"https://github.com/prometheus/prometheus/releases/download/v{{ pro...` | No | — |
| `prometheus_install_dir` | `"/opt/prometheus"` | No | Installation paths |
| `prometheus_config_dir` | `"/etc/prometheus"` | No | — |
| `prometheus_data_dir` | `"/var/lib/prometheus"` | No | — |
| `prometheus_log_dir` | `"/var/log/prometheus"` | No | — |
| `prometheus_user` | `"prometheus"` | No | System user and group |
| `prometheus_group` | `"prometheus"` | No | — |
| `prometheus_uid` | `9090` | No | — |
| `prometheus_gid` | `9090` | No | — |
| `prometheus_listen_address` | `"0.0.0.0:9090"` | No | Service configuration |
| `prometheus_web_external_url` | `"http://{{ ansible_fqdn }}:9090"` | No | — |
| `prometheus_enable_admin_api` | `false` | No | — |
| `prometheus_enable_lifecycle` | `true` | No | — |
| `prometheus_storage_retention_time` | `"15d"` | No | Storage configuration |
| `prometheus_storage_retention_size` | `"50GB"` | No | — |
| `prometheus_storage_tsdb_path` | `"{{ prometheus_data_dir }}"` | No | — |
| `prometheus_storage_wal_compression` | `true` | No | — |
| `prometheus_max_samples_per_send` | `500` | No | Performance tuning |
| `prometheus_max_samples_per_query` | `50000000` | No | — |
| `prometheus_query_timeout` | `"2m"` | No | — |
| `prometheus_query_max_concurrency` | `20` | No | — |
| `prometheus_enable_tls` | `false` | No | Security configuration |
| `prometheus_tls_cert_file` | `"{{ prometheus_config_dir }}/tls/prometheus.crt"` | No | — |
| `prometheus_tls_key_file` | `"{{ prometheus_config_dir }}/tls/prometheus.key"` | No | — |
| `prometheus_enable_basic_auth` | `true` | No | — |
| `prometheus_basic_auth_users` | `(see defaults/main.yml)` | No | — |
| `prometheus_firewall_enabled` | `true` | No | Firewall configuration |
| `prometheus_firewall_zone` | `"public"` | No | — |
| `prometheus_firewall_ports` | `(see defaults/main.yml)` | No | — |
| `prometheus_selinux_enabled` | `true` | No | SELinux configuration |
| `prometheus_selinux_ports` | `(see defaults/main.yml)` | No | — |
| `prometheus_log_level` | `"info"` | No | Log configuration |
| `prometheus_log_format` | `"logfmt"` | No | — |
| `prometheus_service_enabled` | `true` | No | Systemd service configuration |
| `prometheus_service_state` | `started` | No | — |
| `prometheus_restart_on_change` | `true` | No | — |
| `prometheus_ha_enabled` | `false` | No | High availability |
| `prometheus_ha_replica_id` | `"{{ inventory_hostname }}"` | No | — |
| `prometheus_remote_write_enabled` | `false` | No | Remote write configuration (for long-term storage) |
| `prometheus_remote_write_url` | `""` | No | — |
| `prometheus_remote_write_basic_auth_username` | `""` | No | — |
| `prometheus_remote_write_basic_auth_password` | `""` | No | — |
| `prometheus_remote_read_enabled` | `false` | No | Remote read configuration |
| `prometheus_remote_read_url` | `""` | No | — |
| `prometheus_feature_flags` | `[]` | No | Feature flags |
| `prometheus_additional_args` | `[]` | No | Additional command line arguments |
| `prometheus_dependencies` | `(see defaults/main.yml)` | No | Package dependencies |
| `prometheus_backup_enabled` | `true` | No | Backup configuration |
| `prometheus_backup_dir` | `"/backup/prometheus"` | No | — |
| `prometheus_backup_retention_days` | `7` | No | — |
| `prometheus_audit_enabled` | `true` | No | Compliance and auditing |
| `prometheus_compliance_mode` | `"fips"` | No | fips, hipaa, or standard |
| `prometheus_organization` | `"fourth_estate"` | No | Fourth Estate specific settings |
| `prometheus_environment` | `"{{ environment \| default('production') }}"` | No | — |
| `prometheus_tags` | `(see defaults/main.yml)` | No | — |

## Example Playbook

```yaml
---
- name: Prometheus Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: prometheus_grafana/roles/prometheus_install
```

## Tags

| Tag | Description |
|-----|-------------|
| `backup` | Tasks tagged `backup` |
| `cleanup` | Tasks tagged `cleanup` |
| `config` | Tasks tagged `config` |
| `directories` | Tasks tagged `directories` |
| `download` | Tasks tagged `download` |
| `firewall` | Tasks tagged `firewall` |
| `packages` | Tasks tagged `packages` |
| `prometheus` | Tasks tagged `prometheus` |
| `prometheus_install` | Tasks tagged `prometheus_install` |
| `security` | Tasks tagged `security` |
| `selinux` | Tasks tagged `selinux` |
| `service` | Tasks tagged `service` |
| `systemd` | Tasks tagged `systemd` |
| `tls` | Tasks tagged `tls` |
| `users` | Tasks tagged `users` |
| `verification` | Tasks tagged `verification` |

## License

MIT
