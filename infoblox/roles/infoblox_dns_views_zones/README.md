# infoblox_dns_views_zones

Infoblox Dns Views Zones role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nios_host` | `""` | No | Connection (Infoblox NIOS WAPI) |
| `nios_username` | `""` | No | — |
| `nios_password` | `""` | No | — |
| `nios_validate_certs` | `false` | No | — |
| `nios_wapi_version` | `"v2.12"` | No | — |
| `dns_views` | `(see defaults/main.yml)` | No | — |
| `zones_auth` | `[]` | No | — |
| `zones_forward` | `[]` | No | — |
| `zones_stub` | `[]` | No | — |

## Example Playbook

```yaml
---
- name: Infoblox Dns Views Zones
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/roles/infoblox_dns_views_zones
```

## License

MIT
