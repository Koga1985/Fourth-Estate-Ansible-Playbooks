# prometheus_install

Prometheus Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `prometheus_grafana/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `prometheus_version` | `"2.48.0"` |  |
| `prometheus_download_url` | `"https://github.com/prometheus/prometheus/relea...` |  |
| `prometheus_install_dir` | `"/opt/prometheus"` |  |
| `prometheus_config_dir` | `"/etc/prometheus"` |  |
| `prometheus_data_dir` | `"/var/lib/prometheus"` |  |
| `prometheus_log_dir` | `"/var/log/prometheus"` |  |
| `prometheus_user` | `"prometheus"` |  |
| `prometheus_group` | `"prometheus"` |  |
| `prometheus_uid` | `9090` |  |
| `prometheus_gid` | `9090` |  |
| `prometheus_listen_address` | `"0.0.0.0:9090"` |  |
| `prometheus_web_external_url` | `"http://{{ ansible_fqdn }}:9090"` |  |
| `prometheus_enable_admin_api` | `false` |  |
| `prometheus_enable_lifecycle` | `true` |  |
| `prometheus_storage_retention_time` | `"15d"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Prometheus Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: prometheus_grafana/roles/prometheus_install
```

## License

MIT
