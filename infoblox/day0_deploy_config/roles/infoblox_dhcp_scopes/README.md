# infoblox_dhcp_scopes

Infoblox Dhcp Scopes role for Fourth Estate infrastructure automation.

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
| `network_view` | `"default"` | No | — |
| `artifact_dir` | `"/tmp/infoblox-dhcp-scopes"` | No | — |
| `dhcp_networks` | `[]` | No | — |
| `dhcp_ranges` | `[]` | No | — |

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
