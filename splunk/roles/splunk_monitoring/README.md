# splunk_monitoring

Configures Splunk health monitoring, alerting thresholds, and compliance checks. Monitors Splunk services, index performance, and internal error rates. Sends alerts via email when thresholds are exceeded.

## Requirements

- Ansible 2.15+
- Splunk Enterprise installed and running

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `monitoring_enable_health_checks` | `true` | No | Enable periodic health checks |
| `monitoring_enable_alerting` | `true` | No | Enable email alerting |
| `monitoring_alert_email` | `{{ vault_monitoring_email }}` | **Yes** | Alert recipient email address |
| `monitoring_cpu_threshold` | `80` | No | CPU usage alert threshold (%) |
| `monitoring_memory_threshold` | `90` | No | Memory usage alert threshold (%) |
| `monitoring_disk_threshold` | `85` | No | Disk usage alert threshold (%) |
| `monitoring_index_lag_threshold` | `300` | No | Indexing lag alert threshold (seconds) |
| `monitoring_fips_compliance_check` | `true` | No | Verify FIPS mode is active |
| `monitoring_tls_compliance_check` | `true` | No | Verify TLS configuration |

## Example Playbook

```yaml
---
- name: Configure Splunk Monitoring
  hosts: splunk_servers
  become: true
  roles:
    - role: splunk/roles/splunk_monitoring
      vars:
        monitoring_alert_email: "ops@example.com"
        monitoring_cpu_threshold: 80
        monitoring_disk_threshold: 85
```

## License

MIT
