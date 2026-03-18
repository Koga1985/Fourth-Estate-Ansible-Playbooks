# infoblox_dns_views_zones

Infoblox Dns Views Zones role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nios_host` | `""` |  |
| `nios_username` | `""` |  |
| `nios_password` | `""` |  |
| `nios_validate_certs` | `false` |  |
| `nios_wapi_version` | `"v2.12"` |  |
| `zones_auth` | `[]` |  |
| `zones_forward` | `[]` |  |
| `zones_stub` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

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
