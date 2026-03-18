# infoblox_dhcp_config

Infoblox Dhcp Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `infoblox_grid_master` | `"infoblox-master.example.com"` |  |
| `infoblox_username` | `"admin"` |  |
| `infoblox_password` | `"{{ vault_infoblox_password }}"` |  |
| `infoblox_wapi_version` | `"2.12"` |  |
| `infoblox_validate_certs` | `true` |  |
| `infoblox_enable_dhcp` | `true` |  |
| `infoblox_enable_dhcp_thresholds` | `true` |  |
| `infoblox_dhcp_authority` | `true` |  |
| `infoblox_enable_dhcp_email_warnings` | `true` |  |
| `infoblox_enable_dhcp_snmp_warnings` | `true` |  |
| `infoblox_configure_global_dhcp_options` | `true` |  |
| `infoblox_dhcp_domain_name` | `"fourthestate.example.com"` |  |
| `infoblox_dhcp_default_gateway` | `"10.100.10.1"` |  |
| `infoblox_dhcp_default_lease_time` | `86400` | 24 hours |
| `infoblox_dhcp_pxe_lease_time` | `300` | 5 minutes for PXE boot |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Infoblox Dhcp Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/roles/infoblox_dhcp_config
```

## License

MIT
