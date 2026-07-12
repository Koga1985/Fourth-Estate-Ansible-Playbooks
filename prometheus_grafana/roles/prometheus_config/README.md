# prometheus_config

Prometheus Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `prometheus_grafana/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `prometheus_config_dir` | `"/etc/prometheus"` | No | Prometheus configuration directory |
| `prometheus_install_dir` | `"/opt/prometheus"` | No | — |
| `prometheus_global_scrape_interval` | `"15s"` | No | Global configuration |
| `prometheus_global_scrape_timeout` | `"10s"` | No | — |
| `prometheus_global_evaluation_interval` | `"15s"` | No | — |
| `prometheus_external_labels` | `(see defaults/main.yml)` | No | External labels |
| `prometheus_alertmanager_enabled` | `true` | No | Alertmanager configuration |
| `prometheus_alertmanagers` | `(see defaults/main.yml)` | No | — |
| `prometheus_scrape_configs` | `(see defaults/main.yml)` | No | Scrape configurations |
| `prometheus_kubernetes_sd_enabled` | `false` | No | Kubernetes/OpenShift service discovery |
| `prometheus_kubernetes_api_server` | `"https://kubernetes.default.svc"` | No | — |
| `prometheus_kubernetes_sd_role` | `"node"` | No | node, pod, service, endpoints |
| `prometheus_consul_sd_enabled` | `false` | No | Consul service discovery |
| `prometheus_consul_server` | `"localhost:8500"` | No | — |
| `prometheus_consul_datacenter` | `"dc1"` | No | — |
| `prometheus_recording_rules_enabled` | `true` | No | Recording rules |
| `prometheus_recording_rules_files` | `(see defaults/main.yml)` | No | — |
| `prometheus_alert_rules_enabled` | `true` | No | Alert rules for Fourth Estate |
| `prometheus_alert_rules_files` | `(see defaults/main.yml)` | No | — |
| `prometheus_remote_write_enabled` | `false` | No | Remote write configuration |
| `prometheus_remote_write_configs` | `[]` | No | — |
| `prometheus_remote_read_enabled` | `false` | No | Remote read configuration |
| `prometheus_remote_read_configs` | `[]` | No | — |

## Example Playbook

```yaml
---
- name: Prometheus Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: prometheus_grafana/roles/prometheus_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `alert_rules` | Tasks tagged `alert_rules` |
| `prometheus` | Tasks tagged `prometheus` |
| `prometheus_config` | Tasks tagged `prometheus_config` |
| `recording_rules` | Tasks tagged `recording_rules` |
| `service` | Tasks tagged `service` |
| `service_discovery` | Tasks tagged `service_discovery` |
| `testing` | Tasks tagged `testing` |
| `validation` | Tasks tagged `validation` |

## License

MIT
