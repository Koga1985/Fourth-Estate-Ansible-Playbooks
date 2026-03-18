# dns_views_zones

Dns Views Zones role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/day0_deploy_config/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `nios_host` | `""` |  |
| `nios_username` | `""` |  |
| `nios_password` | `""` |  |
| `nios_validate_certs` | `false` |  |
| `nios_wapi_version` | `"v2.12"` |  |
| `network_views` | `[]` |  |
| `dns_views` | `[]` |  |
| `network_containers_v4` | `[]` |  |
| `network_containers_v6` | `[]` |  |
| `zones_auth` | `[]` |  |
| `artifact_dir` | `"/tmp/infoblox-inventory"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

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
