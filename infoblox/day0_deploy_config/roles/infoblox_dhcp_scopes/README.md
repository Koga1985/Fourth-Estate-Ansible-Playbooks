# infoblox_dhcp_scopes

Infoblox Dhcp Scopes role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/day0_deploy_config/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `nios_host` | `""` |  |
| `nios_username` | `""` |  |
| `nios_password` | `""` |  |
| `nios_validate_certs` | `false` |  |
| `nios_wapi_version` | `"v2.12"` |  |
| `network_view` | `"default"` |  |
| `artifact_dir` | `"/tmp/infoblox-dhcp-scopes"` |  |
| `dhcp_networks` | `[]` |  |
| `dhcp_ranges` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Infoblox Dhcp Scopes
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/day0_deploy_config/roles/infoblox_dhcp_scopes
```

## License

MIT
