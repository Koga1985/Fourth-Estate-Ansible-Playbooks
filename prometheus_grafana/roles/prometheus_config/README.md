# prometheus_config

Prometheus Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `prometheus_grafana/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `prometheus_config_dir` | `"/etc/prometheus"` |  |
| `prometheus_install_dir` | `"/opt/prometheus"` |  |
| `prometheus_global_scrape_interval` | `"15s"` |  |
| `prometheus_global_scrape_timeout` | `"10s"` |  |
| `prometheus_global_evaluation_interval` | `"15s"` |  |
| `prometheus_alertmanager_enabled` | `true` |  |
| `prometheus_kubernetes_sd_enabled` | `false` |  |
| `prometheus_kubernetes_api_server` | `"https://kubernetes.default.svc"` |  |
| `prometheus_kubernetes_sd_role` | `"node"` | No | node, pod, service, endpoints |
| `prometheus_consul_sd_enabled` | `false` |  |
| `prometheus_consul_server` | `"localhost:8500"` |  |
| `prometheus_consul_datacenter` | `"dc1"` |  |
| `prometheus_recording_rules_enabled` | `true` |  |
| `prometheus_alert_rules_enabled` | `true` |  |
| `prometheus_remote_write_enabled` | `false` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Prometheus Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: prometheus_grafana/roles/prometheus_config
```

## License

MIT
