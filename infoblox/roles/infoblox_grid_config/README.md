# infoblox_grid_config

Infoblox Grid Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `infoblox/README.md`

## Requirements

- Ansible 2.15+
- Collection: `infoblox.nios_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `infoblox_grid_master` | `"infoblox-master.example.com"` | No | Grid connection settings |
| `infoblox_username` | `"admin"` | No | — |
| `infoblox_password` | `"{{ vault_infoblox_password }}"` | No | — |
| `infoblox_wapi_version` | `"2.12"` | No | — |
| `infoblox_max_retries` | `5` | No | — |
| `infoblox_validate_certs` | `true` | No | — |
| `infoblox_grid_name` | `"fourth-estate-grid"` | No | Grid properties |
| `infoblox_grid_comment` | `"Fourth Estate Infoblox DDI Grid"` | No | — |
| `infoblox_configure_ntp` | `true` | No | NTP configuration |
| `infoblox_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `infoblox_time_zone` | `"America/New_York"` | No | — |
| `infoblox_enable_snmp` | `true` | No | SNMP configuration |
| `infoblox_snmp_version` | `"v3"` | No | — |
| `infoblox_snmp_community` | `"{{ vault_infoblox_snmp_community }}"` | No | — |
| `infoblox_snmp_contact` | `"netops@fourthestate.example.com"` | No | — |
| `infoblox_snmp_location` | `"Fourth Estate Data Center - Primary"` | No | — |
| `infoblox_snmp_engine_id` | `""` | No | — |
| `infoblox_snmp_trap_destinations` | `(see defaults/main.yml)` | No | SNMP trap destinations |
| `infoblox_grid_members` | `(see defaults/main.yml)` | No | Grid members (examples - customize per deployment) |
| `infoblox_admin_users` | `(see defaults/main.yml)` | No | Admin users |
| `infoblox_upload_certificate` | `false` | No | Certificate management |
| `infoblox_certificate_path` | `""` | No | — |
| `infoblox_private_key_path` | `""` | No | — |
| `infoblox_certificate_usage` | `"ADMIN_HTTPS"` | No | — |
| `infoblox_syslog_servers` | `(see defaults/main.yml)` | No | Syslog servers for audit logging (365+ day retention) |
| `infoblox_configure_smtp` | `true` | No | Email notification settings |
| `infoblox_smtp_server` | `"smtp.example.com"` | No | — |
| `infoblox_smtp_port` | `587` | No | — |
| `infoblox_smtp_auth_enable` | `true` | No | — |
| `infoblox_smtp_username` | `"infoblox@example.com"` | No | — |
| `infoblox_smtp_password` | `"{{ vault_infoblox_smtp_password }}"` | No | — |
| `infoblox_smtp_from_address` | `"infoblox-noreply@example.com"` | No | — |
| `infoblox_audit_log_format` | `"extended"` | No | Grid properties |
| `infoblox_admin_lockout_threshold` | `5` | No | Security settings |
| `infoblox_admin_lockout_duration` | `30` | No | minutes |
| `infoblox_min_password_length` | `15` | No | — |
| `infoblox_password_expiry_days` | `90` | No | — |
| `infoblox_min_tls_version` | `"TLSv1.2"` | No | — |
| `infoblox_cipher_suites` | `(see defaults/main.yml)` | No | — |
| `infoblox_configure_backup` | `true` | No | Backup configuration |
| `infoblox_backup_server` | `"backup.example.com"` | No | — |
| `infoblox_backup_protocol` | `"sftp"` | No | — |
| `infoblox_backup_path` | `"/backups/infoblox"` | No | — |
| `infoblox_backup_username` | `"infoblox_backup"` | No | — |
| `infoblox_backup_password` | `"{{ vault_infoblox_backup_password }}"` | No | — |
| `infoblox_backup_schedule` | `"0 2 * * *"` | No | Daily at 2 AM |
| `infoblox_backup_retention_days` | `90` | No | — |
| `infoblox_source_protection_enabled` | `true` | No | Fourth Estate specific settings Source protection network isolation |
| `infoblox_zone_separation` | `true` | No | Separate grid members for different security zones |

## Example Playbook

```yaml
---
- name: Infoblox Grid Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: infoblox/roles/infoblox_grid_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `backup` | Tasks tagged `backup` |
| `certificates` | Tasks tagged `certificates` |
| `config` | Tasks tagged `config` |
| `dhcp` | Tasks tagged `dhcp` |
| `dns` | Tasks tagged `dns` |
| `email` | Tasks tagged `email` |
| `grid` | Tasks tagged `grid` |
| `infoblox` | Tasks tagged `infoblox` |
| `logging` | Tasks tagged `logging` |
| `members` | Tasks tagged `members` |
| `ntp` | Tasks tagged `ntp` |
| `properties` | Tasks tagged `properties` |
| `security` | Tasks tagged `security` |
| `snmp` | Tasks tagged `snmp` |
| `syslog` | Tasks tagged `syslog` |
| `users` | Tasks tagged `users` |

## License

MIT
