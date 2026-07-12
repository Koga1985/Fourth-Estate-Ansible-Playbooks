# infoblox_grid_bootstrap

Infoblox Grid Bootstrap role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/day0_deploy_config/README.md`

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nios_host` | `""` | No | — |
| `nios_username` | `""` | No | — |
| `nios_password` | `""` | No | — |
| `nios_validate_certs` | `false` | No | — |
| `nios_wapi_version` | `"v2.12"` | No | — |
| `grid_name` | `"PROD-GRID"` | No | — |
| `grid_master_vip` | `""` | No | — |
| `grid_members` | `[]` | No | — |
| `ntp_servers` | `[]` | No | — |
| `syslog_targets` | `[]` | No | — |
| `smtp_relay` | `""` | No | — |
| `snmp_trap_receivers` | `[]` | No | — |
| `artifact_dir` | `"/tmp/infoblox-grid-bootstrap"` | No | — |

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
