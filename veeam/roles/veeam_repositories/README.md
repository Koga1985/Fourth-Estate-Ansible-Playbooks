# veeam_repositories

Veeam Repositories role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `veeam_debug` | `false` | No | General settings |
| `veeam_no_log` | `true` | No | — |
| `veeam_generate_documentation` | `true` | No | — |
| `veeam_documentation_path` | `"C:\\VeeamConfig\\Docs"` | No | — |
| `veeam_enable_capacity_alerts` | `true` | No | Capacity planning alerts |
| `veeam_capacity_warning_threshold` | `80` | No | — |
| `veeam_capacity_critical_threshold` | `90` | No | — |
| `veeam_capacity_alert_email` | `"backup-admin@news-agency.example.com"` | No | — |
| `veeam_repositories` | `(see defaults/main.yml)` | No | Standard backup repositories |
| `veeam_sobr_repositories` | `(see defaults/main.yml)` | No | Scale-Out Backup Repository (SOBR) configurations |
| `veeam_object_storage_repositories` | `(see defaults/main.yml)` | No | Object storage repositories |
| `veeam_fourth_estate_retention_days` | `365` | No | Fourth Estate specific repository settings |
| `veeam_source_protection_retention_days` | `730` | No | — |
| `veeam_compliance_retention_years` | `7` | No | — |
| `veeam_repository_block_size` | `"1024KB"` | No | Repository performance tuning 1MB, 512KB, 256KB, 128KB |
| `veeam_repository_cache_size_gb` | `4` | No | — |
| `veeam_default_immutability_enabled` | `true` | No | Immutability settings for ransomware protection |
| `veeam_default_immutability_period_days` | `14` | No | — |
| `veeam_immutability_compliance_mode` | `false` | No | Set to true for SEC compliance |
| `veeam_enable_storage_optimization` | `true` | No | Deduplication settings |
| `veeam_deduplication_block_size` | `"1024KB"` | No | — |
| `veeam_default_encryption_enabled` | `true` | No | Encryption defaults |
| `veeam_encryption_algorithm` | `"AES256"` | No | — |
| `veeam_maintenance_window_start` | `"22:00"` | No | Maintenance windows |
| `veeam_maintenance_window_end` | `"06:00"` | No | — |
| `veeam_maintenance_days` | `["Saturday", "Sunday"]` | No | — |
| `veeam_repository_monitor_enabled` | `true` | No | Monitoring thresholds |
| `veeam_repository_latency_threshold_ms` | `100` | No | — |
| `veeam_repository_iops_threshold` | `1000` | No | — |
| `veeam_use_per_vm_backup_files` | `true` | No | Backup file settings |
| `veeam_enable_inline_deduplication` | `false` | No | — |
| `veeam_enable_inline_compression` | `true` | No | — |
| `veeam_default_compression_level` | `5` | No | 0 (None) to 9 (Extreme) |
| `veeam_enable_repository_rotation` | `true` | No | Repository rotation |
| `veeam_rotation_schedule` | `"Monthly"` | No | — |
| `veeam_health_check_enabled` | `true` | No | Health check settings |
| `veeam_health_check_schedule` | `"Weekly"` | No | — |
| `veeam_health_check_day` | `"Sunday"` | No | — |
| `veeam_health_check_time` | `"03:00"` | No | — |
| `veeam_capacity_tier_offload_window_hours` | `168` | No | Capacity tier offload settings 7 days |
| `veeam_capacity_tier_transfer_window_start` | `"20:00"` | No | — |
| `veeam_capacity_tier_transfer_window_end` | `"08:00"` | No | — |
| `veeam_archive_tier_enabled` | `true` | No | Archive tier settings |
| `veeam_archive_tier_after_days` | `365` | No | — |
| `veeam_archive_tier_cost_optimized` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Veeam Repositories
  hosts: localhost
  gather_facts: false
  roles:
    - role: veeam/roles/veeam_repositories
```

## Tags

| Tag | Description |
|-----|-------------|
| `alerts` | Tasks tagged `alerts` |
| `documentation` | Tasks tagged `documentation` |
| `encryption` | Tasks tagged `encryption` |
| `hardened` | Tasks tagged `hardened` |
| `immutable` | Tasks tagged `immutable` |
| `maintenance` | Tasks tagged `maintenance` |
| `object-storage` | Tasks tagged `object-storage` |
| `ransomware-protection` | Tasks tagged `ransomware-protection` |
| `repositories` | Tasks tagged `repositories` |
| `sobr` | Tasks tagged `sobr` |
| `test` | Tasks tagged `test` |
| `veeam` | Tasks tagged `veeam` |
| `verify` | Tasks tagged `verify` |

## License

MIT
