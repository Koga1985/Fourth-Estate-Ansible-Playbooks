# vast_monitoring

Vast Monitoring role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vast/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vast_mgmt_host` | `"{{ vault_vast_mgmt_host }}"` | No | — |
| `vast_mgmt_port` | `443` | No | — |
| `vast_mgmt_user` | `"{{ vault_vast_mgmt_user }}"` | No | — |
| `vast_mgmt_password` | `"{{ vault_vast_mgmt_password }}"` | No | — |
| `vast_api_version` | `"v1"` | No | — |
| `vast_verify_ssl` | `true` | No | — |
| `vast_enable_snmp` | `true` | No | SNMP Configuration (DoD STIG requirement for monitoring) |
| `vast_snmp_version` | `"3"` | No | Only SNMPv3 for DoD compliance |
| `vast_snmp_community` | `"{{ vault_vast_snmp_community }}"` | No | — |
| `vast_snmp_user` | `"{{ vault_vast_snmp_user \| default('vastmonitor') }}"` | No | — |
| `vast_snmp_auth_protocol` | `"SHA256"` | No | SHA256 for FIPS compliance |
| `vast_snmp_auth_password` | `"{{ vault_vast_snmp_auth_password \| default('') }}"` | No | — |
| `vast_snmp_priv_protocol` | `"AES256"` | No | AES256 for FIPS compliance |
| `vast_snmp_priv_password` | `"{{ vault_vast_snmp_priv_password \| default('') }}"` | No | — |
| `vast_snmp_trap_destinations` | `(see defaults/main.yml)` | No | — |
| `vast_enable_syslog` | `true` | No | Syslog Configuration (NIST 800-53 AU-4, AU-9) |
| `vast_syslog_servers` | `(see defaults/main.yml)` | No | — |
| `vast_syslog_facility` | `"local7"` | No | — |
| `vast_syslog_severity` | `"info"` | No | — |
| `vast_syslog_format` | `"rfc5424"` | No | — |
| `vast_enable_performance_monitoring` | `true` | No | Performance Monitoring |
| `vast_performance_metrics` | `(see defaults/main.yml)` | No | — |
| `vast_metric_collection_interval` | `60` | No | seconds |
| `vast_monitor_nfs_metrics` | `true` | No | Protocol-specific Monitoring |
| `vast_monitor_smb_metrics` | `true` | No | — |
| `vast_monitor_s3_metrics` | `true` | No | — |
| `vast_health_check_enabled` | `true` | No | Health Checks |
| `vast_health_check_interval` | `300` | No | 5 minutes |
| `vast_health_check_components` | `(see defaults/main.yml)` | No | — |
| `vast_capacity_monitoring_enabled` | `true` | No | Capacity Monitoring and Forecasting |
| `vast_capacity_check_interval` | `3600` | No | 1 hour |
| `vast_capacity_forecast_days` | `90` | No | — |
| `vast_capacity_trending_enabled` | `true` | No | — |
| `vast_performance_trending_enabled` | `true` | No | Performance Trending |
| `vast_performance_baseline_days` | `30` | No | — |
| `vast_performance_anomaly_detection` | `true` | No | — |
| `vast_alert_email_enabled` | `true` | No | Alerting Configuration |
| `vast_alert_email_recipients` | `(see defaults/main.yml)` | No | — |
| `vast_smtp_server` | `"{{ vault_smtp_server \| default('') }}"` | No | — |
| `vast_smtp_port` | `25` | No | — |
| `vast_smtp_from` | `"vast-alerts@fourthestate.local"` | No | — |
| `vast_alert_on_capacity_threshold` | `80` | No | Alert Thresholds percentage |
| `vast_alert_on_capacity_critical` | `90` | No | percentage |
| `vast_alert_on_performance_degradation` | `true` | No | — |
| `vast_alert_on_latency_threshold_ms` | `10` | No | milliseconds |
| `vast_alert_on_hardware_failure` | `true` | No | — |
| `vast_alert_on_security_events` | `true` | No | — |
| `vast_alert_on_node_failure` | `true` | No | — |
| `vast_alert_on_drive_failure` | `true` | No | — |
| `vast_alert_on_network_issues` | `true` | No | — |
| `vast_alert_on_replication_lag` | `true` | No | — |
| `vast_alert_on_snapshot_failures` | `true` | No | — |
| `vast_send_snmp_traps` | `true` | No | SNMP Traps |
| `vast_snmp_trap_severity_level` | `"warning"` | No | info, warning, error, critical |
| `vast_prometheus_enabled` | `false` | No | Integration with Monitoring Tools |
| `vast_prometheus_port` | `9090` | No | — |
| `vast_prometheus_retention_days` | `30` | No | — |
| `vast_prometheus_scrape_interval` | `60` | No | — |
| `vast_grafana_enabled` | `false` | No | — |
| `vast_grafana_url` | `"{{ vault_grafana_url \| default('') }}"` | No | — |
| `vast_grafana_api_key` | `"{{ vault_grafana_api_key \| default('') }}"` | No | — |
| `vast_grafana_dashboard_provisioning` | `true` | No | — |
| `vast_splunk_enabled` | `false` | No | — |
| `vast_splunk_hec_url` | `"{{ vault_splunk_hec_url \| default('') }}"` | No | — |
| `vast_splunk_hec_token` | `"{{ vault_splunk_hec_token \| default('') }}"` | No | — |
| `vast_splunk_index` | `"vast_storage"` | No | — |
| `vast_monitoring_script_dir` | `"/opt/vast/monitoring"` | No | Monitoring Scripts |
| `vast_monitoring_log_dir` | `"/var/log/vast"` | No | — |
| `vast_notification_channels` | `(see defaults/main.yml)` | No | Notification Settings |
| `vast_monitor_quota_usage` | `true` | No | Quota Monitoring |
| `vast_quota_warning_threshold` | `80` | No | — |
| `vast_quota_critical_threshold` | `95` | No | — |
| `vast_monitor_replication` | `true` | No | Replication Monitoring |
| `vast_replication_lag_warning_minutes` | `30` | No | — |
| `vast_replication_lag_critical_minutes` | `60` | No | — |
| `vast_monitor_snapshots` | `true` | No | Snapshot Monitoring |
| `vast_snapshot_failure_alert` | `true` | No | — |
| `vast_snapshot_retention_compliance_check` | `true` | No | — |
| `vast_node_cpu_threshold` | `90` | No | Node Health Monitoring |
| `vast_node_memory_threshold` | `90` | No | — |
| `vast_node_temperature_threshold` | `75` | No | Celsius |
| `vast_drive_smart_monitoring` | `true` | No | Drive Health Monitoring |
| `vast_drive_wear_level_threshold` | `80` | No | — |
| `vast_drive_read_errors_threshold` | `10` | No | — |
| `vast_drive_write_errors_threshold` | `10` | No | — |
| `vast_network_packet_loss_threshold` | `1` | No | Network Performance Monitoring percentage |
| `vast_network_bandwidth_utilization_threshold` | `80` | No | percentage |
| `vast_monitor_data_reduction` | `true` | No | Data Reduction Monitoring |
| `vast_data_reduction_ratio_expected` | `2.0` | No | 2:1 |
| `vast_create_custom_dashboards` | `true` | No | Custom Dashboards |
| `vast_dashboard_refresh_interval` | `60` | No | seconds |

## Example Playbook

```yaml
---
- name: Vast Monitoring
  hosts: localhost
  gather_facts: false
  roles:
    - role: vast/roles/vast_monitoring
```

## Tags

| Tag | Description |
|-----|-------------|
| `alerts` | Tasks tagged `alerts` |
| `check` | Tasks tagged `check` |
| `email` | Tasks tagged `email` |
| `health` | Tasks tagged `health` |
| `metrics` | Tasks tagged `metrics` |
| `monitoring` | Tasks tagged `monitoring` |
| `performance` | Tasks tagged `performance` |
| `snmp` | Tasks tagged `snmp` |
| `syslog` | Tasks tagged `syslog` |
| `thresholds` | Tasks tagged `thresholds` |
| `traps` | Tasks tagged `traps` |
| `verification` | Tasks tagged `verification` |

## License

MIT
