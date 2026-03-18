# infoblox_grid_bootstrap

Infoblox Grid Bootstrap role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/day0_deploy_config/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nios_host` | `""` |  |
| `nios_username` | `""` |  |
| `nios_password` | `""` |  |
| `nios_validate_certs` | `false` |  |
| `nios_wapi_version` | `"v2.12"` |  |
| `grid_name` | `"PROD-GRID"` |  |
| `grid_master_vip` | `""` |  |
| `grid_members` | `[]` |  |
| `ntp_servers` | `[]` |  |
| `syslog_targets` | `[]` |  |
| `smtp_relay` | `""` |  |
| `snmp_trap_receivers` | `[]` |  |
| `artifact_dir` | `"/tmp/infoblox-grid-bootstrap"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Infoblox Grid Bootstrap
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/day0_deploy_config/roles/infoblox_grid_bootstrap
```

## License

MIT
