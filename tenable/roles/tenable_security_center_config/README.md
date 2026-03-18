# tenable_security_center_config

Tenable Security Center Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `tsc_host` | `"{{ ansible_fqdn }}"` |  |
| `tsc_port` | `443` |  |
| `tsc_username` | `"admin"` |  |
| `tsc_password` | `"{{ vault_tsc_password }}"` |  |
| `tsc_validate_certs` | `true` |  |
| `tsc_session_timeout` | `3600` |  |
| `tsc_idle_timeout` | `1800` |  |
| `tsc_banner_text` | `"AUTHORIZED USE ONLY - Fourth Estate Agency Sec...` |  |
| `tsc_allow_post` | `false` |  |
| `tsc_enable_syslog` | `true` |  |
| `tsc_syslog_host` | `"syslog.agency.gov"` |  |
| `tsc_syslog_port` | `514` |  |
| `tsc_syslog_protocol` | `"tcp"` |  |
| `tsc_configure_smtp` | `true` |  |
| `tsc_smtp_host` | `"smtp.agency.gov"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Tenable Security Center Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: tenable/roles/tenable_security_center_config
```

## License

MIT
