# infoblox_dhcp_failover

Infoblox Dhcp Failover role for Fourth Estate infrastructure automation.

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
| `artifact_dir` | `"/tmp/infoblox-dhcp-failover"` |  |
| `dhcp_failover_pairs` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Infoblox Dhcp Failover
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/day0_deploy_config/roles/infoblox_dhcp_failover
```

## License

MIT
