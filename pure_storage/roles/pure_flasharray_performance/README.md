# pure_flasharray_performance

Pure Flasharray Performance role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` | No | Array connection |
| `flasharray_performance_thresholds` | `(see defaults/main.yml)` | No | Performance thresholds |
| `flasharray_monitoring_interval_seconds` | `60` | No | Performance monitoring intervals |
| `flasharray_performance_history_days` | `90` | No | — |
| `flasharray_detailed_monitoring_enabled` | `true` | No | — |
| `flasharray_workload_profiles` | `(see defaults/main.yml)` | No | Workload optimization |
| `flasharray_nvme_enabled` | `true` | No | NVMe configuration |
| `flasharray_nvme_queue_depth` | `1024` | No | — |
| `flasharray_nvme_io_queues` | `128` | No | — |
| `flasharray_nvme_performance_boost` | `true` | No | — |
| `flasharray_inline_deduplication` | `true` | No | Data reduction |
| `flasharray_inline_compression` | `true` | No | — |
| `flasharray_pattern_removal` | `true` | No | — |
| `flasharray_expected_reduction_ratio` | `"5:1"` | No | — |
| `flasharray_reduction_monitoring` | `true` | No | — |
| `flasharray_intelligent_caching` | `true` | No | Cache and tiering (automatic on Pure) |
| `flasharray_write_coalescing` | `true` | No | — |
| `flasharray_read_ahead_enabled` | `true` | No | — |
| `flasharray_iscsi_queue_depth` | `128` | No | Queue depth optimization |
| `flasharray_fc_queue_depth` | `128` | No | — |
| `flasharray_enable_performance_tuning` | `true` | No | Performance tuning |
| `flasharray_auto_performance_optimization` | `true` | No | — |
| `flasharray_workload_balancing` | `"automatic"` | No | — |
| `flasharray_capacity_forecasting_enabled` | `true` | No | Capacity forecasting |
| `flasharray_forecast_period_days` | `180` | No | — |
| `flasharray_growth_rate_tracking` | `true` | No | — |
| `flasharray_fourth_estate_performance` | `(see defaults/main.yml)` | No | Fourth Estate performance requirements |
| `flasharray_performance_testing_enabled` | `true` | No | Performance testing |
| `flasharray_baseline_performance_tests` | `true` | No | — |
| `flasharray_test_frequency_days` | `90` | No | — |
| `flasharray_send_metrics_to_prometheus` | `true` | No | Monitoring integration |
| `flasharray_send_metrics_to_grafana` | `true` | No | — |
| `flasharray_send_metrics_to_splunk` | `false` | No | — |
| `flasharray_pure1_monitoring` | `true` | No | — |
| `flasharray_performance_alerting_enabled` | `true` | No | Alert configuration |
| `flasharray_latency_alerting` | `true` | No | — |
| `flasharray_iops_alerting` | `true` | No | — |
| `flasharray_throughput_alerting` | `true` | No | — |
| `flasharray_queue_depth_alerting` | `true` | No | — |
| `flasharray_generate_performance_reports` | `true` | No | Performance reports |
| `flasharray_report_frequency` | `"weekly"` | No | — |
| `flasharray_report_recipients` | `(see defaults/main.yml)` | No | — |
| `flasharray_directflash_modules` | `true` | No | DirectFlash architecture |
| `flasharray_directflash_performance` | `"maximum"` | No | — |
| `flasharray_sub_millisecond_latency` | `true` | No | All-flash performance characteristics |
| `flasharray_consistent_performance` | `true` | No | — |
| `flasharray_no_performance_degradation` | `true` | No | — |
| `flasharray_evergreen_performance_upgrades` | `true` | No | Evergreen optimization |
| `flasharray_non_disruptive_upgrades` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Pure Flasharray Performance
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_performance
```

## License

MIT
