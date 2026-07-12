# dns_views_zones

Dns Views Zones role for Fourth Estate infrastructure automation.

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
| `network_views` | `[]` | No | — |
| `dns_views` | `[]` | No | — |
| `network_containers_v4` | `[]` | No | — |
| `network_containers_v6` | `[]` | No | — |
| `zones_auth` | `[]` | No | — |
| `artifact_dir` | `"/tmp/infoblox-inventory"` | No | — |

## Example Playbook

```yaml
---
- name: Dns Views Zones
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/day0_deploy_config/roles/dns_views_zones
```

## License

MIT
