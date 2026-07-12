# prometheus_exporters

Prometheus Exporters role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `prometheus_grafana/README.md`

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `node_exporter_enabled` | `true` | No | Node Exporter configuration |
| `node_exporter_version` | `"1.7.0"` | No | — |
| `node_exporter_download_url` | `"https://github.com/prometheus/node_exporter/releases/download/v{{ ...` | No | — |
| `node_exporter_install_dir` | `"/opt/node_exporter"` | No | — |
| `node_exporter_listen_address` | `"0.0.0.0:9100"` | No | — |
| `node_exporter_user` | `"node_exporter"` | No | — |
| `node_exporter_group` | `"node_exporter"` | No | — |
| `node_exporter_enabled_collectors` | `(see defaults/main.yml)` | No | — |
| `node_exporter_disabled_collectors` | `(see defaults/main.yml)` | No | — |
| `blackbox_exporter_enabled` | `true` | No | Blackbox Exporter configuration |
| `blackbox_exporter_version` | `"0.24.0"` | No | — |
| `blackbox_exporter_download_url` | `"https://github.com/prometheus/blackbox_exporter/releases/download/...` | No | — |
| `blackbox_exporter_install_dir` | `"/opt/blackbox_exporter"` | No | — |
| `blackbox_exporter_config_dir` | `"/etc/blackbox_exporter"` | No | — |
| `blackbox_exporter_listen_address` | `"0.0.0.0:9115"` | No | — |
| `blackbox_exporter_user` | `"blackbox_exporter"` | No | — |
| `blackbox_exporter_group` | `"blackbox_exporter"` | No | — |
| `blackbox_exporter_modules` | `(see defaults/main.yml)` | No | — |
| `postgres_exporter_enabled` | `false` | No | PostgreSQL Exporter configuration |
| `postgres_exporter_version` | `"0.15.0"` | No | — |
| `postgres_exporter_download_url` | `"https://github.com/prometheus-community/postgres_exporter/releases...` | No | — |
| `postgres_exporter_install_dir` | `"/opt/postgres_exporter"` | No | — |
| `postgres_exporter_listen_address` | `"0.0.0.0:9187"` | No | — |
| `postgres_exporter_user` | `"postgres_exporter"` | No | — |
| `postgres_exporter_group` | `"postgres_exporter"` | No | — |
| `postgres_exporter_data_source_name` | `"postgresql://postgres_exporter:{{ vault_postgres_exporter_password...` | **Yes** | — |
| `mysql_exporter_enabled` | `false` | No | MySQL Exporter configuration |
| `mysql_exporter_version` | `"0.15.1"` | No | — |
| `mysql_exporter_download_url` | `"https://github.com/prometheus/mysqld_exporter/releases/download/v{...` | No | — |
| `mysql_exporter_install_dir` | `"/opt/mysql_exporter"` | No | — |
| `mysql_exporter_listen_address` | `"0.0.0.0:9104"` | No | — |
| `mysql_exporter_user` | `"mysql_exporter"` | No | — |
| `mysql_exporter_group` | `"mysql_exporter"` | No | — |
| `mysql_exporter_data_source_name` | `"mysql_exporter:{{ vault_mysql_exporter_password \| default('changem...` | **Yes** | — |
| `redis_exporter_enabled` | `false` | No | Redis Exporter configuration |
| `redis_exporter_version` | `"1.55.0"` | No | — |
| `redis_exporter_download_url` | `"https://github.com/oliver006/redis_exporter/releases/download/v{{ ...` | No | — |
| `redis_exporter_install_dir` | `"/opt/redis_exporter"` | No | — |
| `redis_exporter_listen_address` | `"0.0.0.0:9121"` | No | — |
| `redis_exporter_user` | `"redis_exporter"` | No | — |
| `redis_exporter_group` | `"redis_exporter"` | No | — |
| `redis_exporter_redis_addr` | `"redis://localhost:6379"` | No | — |
| `nginx_exporter_enabled` | `false` | No | NGINX Exporter configuration |
| `nginx_exporter_version` | `"0.11.0"` | No | — |
| `nginx_exporter_download_url` | `"https://github.com/nginxinc/nginx-prometheus-exporter/releases/dow...` | No | — |
| `nginx_exporter_install_dir` | `"/opt/nginx_exporter"` | No | — |
| `nginx_exporter_listen_address` | `"0.0.0.0:9113"` | No | — |
| `nginx_exporter_user` | `"nginx_exporter"` | No | — |
| `nginx_exporter_group` | `"nginx_exporter"` | No | — |
| `nginx_exporter_scrape_uri` | `"http://localhost:80/stub_status"` | No | — |
| `exporters_firewall_enabled` | `true` | No | Firewall configuration |
| `exporters_firewall_zone` | `"public"` | No | — |
| `exporters_firewall_ports` | `(see defaults/main.yml)` | No | — |
| `exporters_selinux_enabled` | `true` | No | SELinux configuration |
| `exporters_service_enabled` | `true` | No | Service configuration |
| `exporters_service_state` | `started` | No | — |
| `exporters_restart_on_change` | `true` | No | — |
| `exporters_organization` | `"fourth_estate"` | No | Fourth Estate specific settings |
| `exporters_environment` | `"{{ environment \| default('production') }}"` | No | — |

## Example Playbook

```yaml
---
- name: Prometheus Exporters
  hosts: all
  become: true
  roles:
    - role: prometheus_grafana/roles/prometheus_exporters
```

## License

MIT
