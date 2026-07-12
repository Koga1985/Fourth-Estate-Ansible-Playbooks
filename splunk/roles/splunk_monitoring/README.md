# splunk_monitoring

Configures Splunk health monitoring, alerting thresholds, and compliance checks. Monitors Splunk services, index performance, and internal error rates. Sends alerts via email when thresholds are exceeded.

## Requirements

- Ansible 2.15+
- Splunk Enterprise installed and running

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_home` | `"/opt/splunk"` | No | — |
| `splunk_user` | `"splunk"` | No | — |
| `splunk_admin_password` | `"{{ vault_splunk_admin_password }}"` | No | — |
| `monitoring_enable_health_checks` | `true` | No | Monitoring Configuration |
| `monitoring_health_check_interval` | `300` | No | seconds |
| `monitoring_enable_alerting` | `true` | No | — |
| `monitoring_alert_email` | `"{{ vault_monitoring_email \| default('') }}"` | No | — |
| `monitoring_cpu_threshold` | `80` | No | Performance Monitoring |
| `monitoring_memory_threshold` | `90` | No | — |
| `monitoring_disk_threshold` | `85` | No | — |
| `monitoring_index_lag_threshold` | `300` | No | seconds |
| `monitoring_check_splunkd` | `true` | No | Service Monitoring |
| `monitoring_check_web` | `true` | No | — |
| `monitoring_check_indexers` | `true` | No | — |
| `monitoring_check_search_heads` | `true` | No | — |
| `monitoring_check_internal_errors` | `true` | No | Log Monitoring |
| `monitoring_error_threshold` | `10` | No | errors per hour |
| `monitoring_fips_compliance_check` | `true` | No | Compliance Monitoring |
| `monitoring_tls_compliance_check` | `true` | No | — |
| `monitoring_audit_log_check` | `true` | No | — |

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

## Tags

| Tag | Description |
|-----|-------------|
| `alerting` | Tasks tagged `alerting` |
| `compliance` | Tasks tagged `compliance` |
| `health` | Tasks tagged `health` |
| `monitoring` | Tasks tagged `monitoring` |
| `performance` | Tasks tagged `performance` |

## License

MIT
