# veeam_backup_server_install

Veeam Backup Server Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `veeam_install_dir` | `"C:\\Temp\\Veeam"` | No | Installation paths |
| `veeam_log_dir` | `"C:\\VeeamLogs"` | No | — |
| `veeam_install_source` | `"D:\\"` | No | CD/DVD drive or network path |
| `veeam_installer_url` | `""` | No | Optional: URL to download Veeam ISO |
| `veeam_install_catalog_path` | `"C:\\VBRCatalog"` | No | Veeam installation paths |
| `veeam_install_logs_path` | `"C:\\ProgramData\\Veeam\\Backup"` | No | — |
| `veeam_license_file` | `""` | No | License Leave empty for trial license |
| `veeam_sql_edition` | `"express"` | No | SQL Server configuration express or standard |
| `veeam_sql_instance_name` | `"VEEAMSQL2019"` | No | — |
| `veeam_sql_service_account` | `"NT AUTHORITY\\SYSTEM"` | No | — |
| `veeam_sql_service_password` | `""` | No | — |
| `veeam_sql_admin_account` | `"{{ ansible_hostname }}\\Administrator"` | No | — |
| `veeam_sql_sa_password` | `"{{ lookup('password', '/dev/null length=32 chars=ascii_letters,dig...` | No | — |
| `veeam_sql_express_url` | `"https://download.microsoft.com/download/7/c/1/7c14e92e-bdcb-4f89-b...` | No | — |
| `veeam_database_name` | `"VeeamBackup"` | No | — |
| `veeam_create_service_account` | `true` | No | Service account configuration |
| `veeam_service_account_name` | `"veeam_svc"` | No | — |
| `veeam_service_account_password` | `"{{ lookup('password', '/dev/null length=32 chars=ascii_letters,dig...` | No | — |
| `veeam_service_account_domain` | `"{{ ansible_hostname }}"` | No | — |
| `veeam_enable_tls` | `true` | No | TLS/SSL configuration |
| `veeam_tls_cert_path` | `""` | No | Path to PFX certificate file |
| `veeam_tls_cert_password` | `""` | No | — |
| `fourth_estate_mode` | `true` | No | Fourth Estate specific settings |
| `enable_audit_logging` | `true` | No | — |
| `require_mfa` | `true` | No | — |
| `immutable_backups` | `true` | No | — |
| `encryption_required` | `true` | No | — |
| `veeam_configure_firewall` | `true` | No | Firewall configuration |
| `veeam_force_reinstall` | `false` | No | Installation behavior |

## Example Playbook

```yaml
---
- name: Veeam Backup Server Install
  hosts: localhost
  gather_facts: false
  roles:
    - role: veeam/roles/veeam_backup_server_install
```

## License

MIT
