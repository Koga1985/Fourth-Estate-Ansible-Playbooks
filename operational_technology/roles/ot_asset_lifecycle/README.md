# ot_asset_lifecycle

Ot Asset Lifecycle role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `operational_technology/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ot_asset_api_url` | `"https://cmdb.agency.gov/api/v1"` |  |
| `ot_asset_api_token` | `""` |  |
| `ot_asset_verify_ssl` | `true` |  |
| `ot_asset_api_timeout` | `30` |  |
| `ot_asset_state` | `present` | present, absent, maintenance, retired |
| `ot_asset_operation` | `register` | register, update, decommission, dispose |
| `ot_asset_id` | `""` |  |
| `ot_asset_name` | `""` |  |
| `ot_asset_type` | `""` | plc, hmi, rtu, ied, scada_server, historian, switch, firewall, sensor |
| `ot_asset_vendor` | `""` |  |
| `ot_asset_model` | `""` |  |
| `ot_asset_serial_number` | `""` |  |
| `ot_asset_firmware_version` | `""` |  |
| `ot_asset_ip_address` | `""` |  |
| `ot_asset_mac_address` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Ot Asset Lifecycle
  hosts: localhost
  gather_facts: false
  roles:
    - role: operational_technology/roles/ot_asset_lifecycle
```

## License

MIT
