# fortigate_system_config

Fortigate System Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `fortinet/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fortigate_host` | `"{{ ansible_host }}"` |  |
| `fortigate_username` | `"{{ vault_fortigate_username | No | default('admin')...` |
| `fortigate_password` | `"{{ vault_fortigate_password }}"` |  |
| `fortigate_api_token` | `"{{ vault_fortigate_api_token | No | default('') }}"` |
| `fortigate_vdom` | `"root"` |  |
| `fortigate_https` | `true` |  |
| `fortigate_validate_certs` | `true` |  |
| `fortigate_hostname` | `"{{ inventory_hostname_short }}"` |  |
| `fortigate_domain` | `"{{ domain_name | No | default('gov.local') }}"` |
| `fortigate_timezone` | `"85"` | No | US/Eastern (see FortiGate timezone codes) |
| `fortigate_dns_primary` | `"{{ dns_primary | No | default('10.0.0.10') }}"` |
| `fortigate_dns_secondary` | `"{{ dns_secondary | No | default('10.0.0.11') }}"` |
| `fortigate_ntp_sync_interval` | `60` |  |
| `fortigate_snmp_enabled` | `true` |  |
| `fortigate_pre_login_banner` | `|` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `fortinet.fortios`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Fortigate System Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: fortinet/roles/fortigate_system_config
```

## License

MIT
