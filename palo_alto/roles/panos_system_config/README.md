# panos_system_config

Panos System Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `palo_alto/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `panos_hostname` | `"fw01"` |  |
| `panos_domain` | `"example.local"` |  |
| `panos_timezone` | `"America/New_York"` |  |
| `panos_dns_primary` | `"8.8.8.8"` |  |
| `panos_dns_secondary` | `"8.8.4.4"` |  |
| `panos_ntp_primary` | `"time.nist.gov"` |  |
| `panos_ntp_secondary` | `"time.google.com"` |  |
| `panos_login_banner` | `|` |  |
| `panos_idle_timeout` | `10` |  |
| `panos_global_session_timeout` | `15` |  |
| `panos_password_min_length` | `15` |  |
| `panos_password_min_uppercase` | `1` |  |
| `panos_password_min_lowercase` | `1` |  |
| `panos_password_min_numeric` | `1` |  |
| `panos_password_min_special` | `1` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Panos System Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: palo_alto/roles/panos_system_config
```

## License

MIT
