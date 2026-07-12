# tenable_security_center_config

Tenable Security Center Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `tsc_host` | `"{{ ansible_fqdn }}"` | No | Connection Settings |
| `tsc_port` | `443` | No | — |
| `tsc_username` | `"admin"` | No | — |
| `tsc_password` | `"{{ vault_tsc_password }}"` | No | — |
| `tsc_validate_certs` | `true` | No | — |
| `tsc_session_timeout` | `3600` | No | System Settings |
| `tsc_idle_timeout` | `1800` | No | — |
| `tsc_banner_text` | `"AUTHORIZED USE ONLY - Fourth Estate Agency Security System"` | No | — |
| `tsc_allow_post` | `false` | No | — |
| `tsc_enable_syslog` | `true` | No | Syslog Configuration |
| `tsc_syslog_host` | `"syslog.agency.gov"` | No | — |
| `tsc_syslog_port` | `514` | No | — |
| `tsc_syslog_protocol` | `"tcp"` | No | — |
| `tsc_configure_smtp` | `true` | No | SMTP Configuration |
| `tsc_smtp_host` | `"smtp.agency.gov"` | No | — |
| `tsc_smtp_port` | `587` | No | — |
| `tsc_smtp_from` | `"noreply-tenable@agency.gov"` | No | — |
| `tsc_smtp_auth_type` | `"login"` | No | — |
| `tsc_smtp_username` | `""` | No | — |
| `tsc_smtp_password` | `""` | No | — |
| `tsc_smtp_encryption` | `"tls"` | No | — |
| `tsc_configure_ldap` | `false` | No | LDAP/AD Configuration |
| `tsc_ldap_servers` | `[]` | No | — |
| `tsc_ldap_test_user` | `""` | No | — |
| `tsc_ldap_test_password` | `""` | No | — |
| `tsc_organizations` | `[]` | No | Organizations |
| `tsc_users` | `[]` | No | User Management |
| `tsc_custom_roles` | `[]` | No | Custom Roles |
| `tsc_repositories` | `[]` | No | Repositories |
| `tsc_scanners` | `[]` | No | Scanners |
| `tsc_credentials` | `[]` | No | Credentials |
| `tsc_assets` | `[]` | No | Asset Lists |
| `tsc_api_keys` | `[]` | No | API Keys |
| `tsc_api_key_file` | `"/root/.tenable/api_keys.yml"` | No | — |
| `tsc_configure_audit` | `true` | No | Audit Configuration |
| `tsc_audit_level` | `"high"` | No | — |
| `tsc_audit_retention_days` | `365` | No | — |
| `tsc_detailed_logging` | `true` | No | — |
| `tsc_password_min_length` | `15` | No | Security Settings |
| `tsc_password_complexity` | `"high"` | No | — |
| `tsc_password_expiration` | `90` | No | — |
| `tsc_max_login_attempts` | `5` | No | — |
| `tsc_lockout_duration` | `1800` | No | — |
| `tsc_enable_mfa` | `false` | No | — |
| `tsc_mfa_type` | `"totp"` | No | — |
| `tsc_update_plugins_now` | `false` | No | Plugin Feed |

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
