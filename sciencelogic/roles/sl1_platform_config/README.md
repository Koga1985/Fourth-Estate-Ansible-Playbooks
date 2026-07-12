# sl1_platform_config

Sl1 Platform Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `sciencelogic/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sl1` | `(see defaults/main.yml)` | No | SL1 Connection |
| `sl1_system_settings` | `(see defaults/main.yml)` | No | System Settings |
| `sl1_smtp` | `(see defaults/main.yml)` | No | SMTP Configuration |
| `sl1_snmp_trap` | `(see defaults/main.yml)` | No | SNMP Trap Receiver |
| `sl1_syslog` | `(see defaults/main.yml)` | No | Syslog Receiver |
| `sl1_authentication` | `(see defaults/main.yml)` | No | Authentication Configuration |
| `sl1_users` | `(see defaults/main.yml)` | No | User Accounts and Roles |
| `sl1_organizations` | `(see defaults/main.yml)` | No | Organizations (Multi-Tenancy) |
| `sl1_api` | `(see defaults/main.yml)` | No | API Access Configuration |
| `sl1_branding` | `(see defaults/main.yml)` | No | Branding Customization |
| `sl1_backup` | `(see defaults/main.yml)` | No | Backup Configuration |
| `sl1_log_retention` | `(see defaults/main.yml)` | No | Log Retention Policies |
| `sl1_performance` | `(see defaults/main.yml)` | No | Performance Tuning |
| `sl1_database_maintenance` | `(see defaults/main.yml)` | No | Database Maintenance |
| `fourth_estate` | `(see defaults/main.yml)` | No | Fourth Estate Specific |
| `artifacts_dir` | `"/tmp/sl1-config-artifacts"` | No | Artifacts and Logging |
| `log_level` | `"info"` | No | — |
| `dry_run` | `false` | No | — |

## Example Playbook

```yaml
---
- name: Sl1 Platform Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: sciencelogic/roles/sl1_platform_config
```

## License

MIT
