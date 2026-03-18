# infoblox_dns_config

Infoblox Dns Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `infoblox_grid_master` | `"infoblox-master.example.com"` |  |
| `infoblox_username` | `"admin"` |  |
| `infoblox_password` | `"{{ vault_infoblox_password }}"` |  |
| `infoblox_wapi_version` | `"2.12"` |  |
| `infoblox_validate_certs` | `true` |  |
| `infoblox_forwarder_group_name` | `"fourth-estate-forwarders"` |  |
| `infoblox_configure_root_hints` | `false` |  |
| `infoblox_root_hints` | `[]` |  |
| `infoblox_enable_dnssec` | `true` |  |
| `infoblox_enable_dnssec_validation` | `true` |  |
| `infoblox_dnssec_validation_policy` | `"strict"` |  |
| `infoblox_dnssec_key_algorithm` | `"RSASHA256"` |  |
| `infoblox_dnssec_ksk_size` | `2048` |  |
| `infoblox_dnssec_zsk_size` | `1024` |  |
| `infoblox_dnssec_ksk_rollover` | `"AUTO"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Infoblox Dns Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/roles/infoblox_dns_config
```

## License

MIT
