# veeam_repositories

Veeam Repositories role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `veeam_debug` | `false` |  |
| `veeam_no_log` | `true` |  |
| `veeam_generate_documentation` | `true` |  |
| `veeam_documentation_path` | `"C:\\VeeamConfig\\Docs"` |  |
| `veeam_enable_capacity_alerts` | `true` |  |
| `veeam_capacity_warning_threshold` | `80` |  |
| `veeam_capacity_critical_threshold` | `90` |  |
| `veeam_capacity_alert_email` | `"backup-admin@news-agency.example.com"` |  |
| `veeam_fourth_estate_retention_days` | `365` |  |
| `veeam_source_protection_retention_days` | `730` |  |
| `veeam_compliance_retention_years` | `7` |  |
| `veeam_repository_block_size` | `"1024KB"` | 1MB, 512KB, 256KB, 128KB |
| `veeam_repository_cache_size_gb` | `4` |  |
| `veeam_default_immutability_enabled` | `true` |  |
| `veeam_default_immutability_period_days` | `14` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Veeam Repositories
  hosts: localhost
  gather_facts: false
  roles:
    - role: veeam/roles/veeam_repositories
```

## License

MIT
