# veeam_backup_server_install

Veeam Backup Server Install role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `veeam_install_dir` | `"C:\\Temp\\Veeam"` |  |
| `veeam_log_dir` | `"C:\\VeeamLogs"` |  |
| `veeam_install_source` | `"D:\\"` | No | CD/DVD drive or network path |
| `veeam_installer_url` | `""` | No | Optional: URL to download Veeam ISO |
| `veeam_install_catalog_path` | `"C:\\VBRCatalog"` |  |
| `veeam_install_logs_path` | `"C:\\ProgramData\\Veeam\\Backup"` |  |
| `veeam_license_file` | `""` | No | Leave empty for trial license |
| `veeam_sql_edition` | `"express"` | No | express or standard |
| `veeam_sql_instance_name` | `"VEEAMSQL2019"` |  |
| `veeam_sql_service_account` | `"NT AUTHORITY\\SYSTEM"` |  |
| `veeam_sql_service_password` | `""` |  |
| `veeam_sql_admin_account` | `"{{ ansible_hostname }}\\Administrator"` |  |
| `veeam_sql_sa_password` | `"{{ lookup('password', '/dev/null length=32 cha...` |  |
| `veeam_sql_express_url` | `"https://download.microsoft.com/download/7/c/1/...` |  |
| `veeam_database_name` | `"VeeamBackup"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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
