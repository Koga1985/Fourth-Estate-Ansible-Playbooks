# pure_flasharray_performance

Pure Flasharray Performance role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` |  |
| `flasharray_monitoring_interval_seconds` | `60` |  |
| `flasharray_performance_history_days` | `90` |  |
| `flasharray_detailed_monitoring_enabled` | `true` |  |
| `flasharray_nvme_enabled` | `true` |  |
| `flasharray_nvme_queue_depth` | `1024` |  |
| `flasharray_nvme_io_queues` | `128` |  |
| `flasharray_nvme_performance_boost` | `true` |  |
| `flasharray_inline_deduplication` | `true` |  |
| `flasharray_inline_compression` | `true` |  |
| `flasharray_pattern_removal` | `true` |  |
| `flasharray_expected_reduction_ratio` | `"5:1"` |  |
| `flasharray_reduction_monitoring` | `true` |  |
| `flasharray_intelligent_caching` | `true` |  |
| `flasharray_write_coalescing` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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
