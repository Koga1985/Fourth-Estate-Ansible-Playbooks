# infoblox_grid_config

Infoblox Grid Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `infoblox_grid_master` | `"infoblox-master.example.com"` |  |
| `infoblox_username` | `"admin"` |  |
| `infoblox_password` | `"{{ vault_infoblox_password }}"` |  |
| `infoblox_wapi_version` | `"2.12"` |  |
| `infoblox_max_retries` | `5` |  |
| `infoblox_validate_certs` | `true` |  |
| `infoblox_grid_name` | `"fourth-estate-grid"` |  |
| `infoblox_grid_comment` | `"Fourth Estate Infoblox DDI Grid"` |  |
| `infoblox_configure_ntp` | `true` |  |
| `infoblox_time_zone` | `"America/New_York"` |  |
| `infoblox_enable_snmp` | `true` |  |
| `infoblox_snmp_version` | `"v3"` |  |
| `infoblox_snmp_community` | `"{{ vault_infoblox_snmp_community }}"` |  |
| `infoblox_snmp_contact` | `"netops@fourthestate.example.com"` |  |
| `infoblox_snmp_location` | `"Fourth Estate Data Center - Primary"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Infoblox Grid Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/roles/infoblox_grid_config
```

## License

MIT
