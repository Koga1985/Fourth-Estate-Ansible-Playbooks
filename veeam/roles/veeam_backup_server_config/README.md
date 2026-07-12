# veeam_backup_server_config

Veeam Backup Server Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `veeam_use_change_tracking` | `true` | No | Global backup settings |
| `veeam_vmware_tools_quiescence` | `true` | No | — |
| `veeam_set_results_to_vm_notes` | `true` | No | — |
| `veeam_email_notifications` | `true` | No | Email notification settings |
| `veeam_smtp_server` | `"smtp.example.com"` | No | — |
| `veeam_smtp_port` | `587` | No | — |
| `veeam_smtp_use_ssl` | `true` | No | — |
| `veeam_smtp_username` | `""` | No | — |
| `veeam_smtp_password` | `""` | No | — |
| `veeam_smtp_from` | `"veeam@example.com"` | No | — |
| `veeam_smtp_to` | `"backup-team@example.com"` | No | — |
| `veeam_email_subject` | `"Veeam Backup: %JOB_NAME% - %JOB_STATUS%"` | No | — |
| `veeam_notify_on_success` | `false` | No | — |
| `veeam_notify_on_warning` | `true` | No | — |
| `veeam_notify_on_error` | `true` | No | — |
| `veeam_notify_on_last_retry` | `true` | No | — |
| `veeam_vmware_credentials` | `[]` | No | Credentials (stored securely in Ansible Vault) |
| `veeam_windows_credentials` | `[]` | No | — |
| `veeam_linux_credentials` | `[]` | No | — |
| `veeam_backup_proxies` | `[]` | No | Backup proxies |
| `veeam_wan_accelerators` | `[]` | No | WAN accelerators |
| `veeam_network_traffic_rules` | `[]` | No | Network traffic rules (bandwidth throttling) |
| `veeam_encryption_passwords` | `[]` | No | Encryption passwords |
| `veeam_mount_server` | `""` | No | Backup infrastructure Hostname for mount server |
| `veeam_storage_corruption_guard` | `true` | No | Global settings |
| `veeam_backup_chain_length` | `14` | No | Days before creating new full backup |
| `veeam_enable_traffic_encryption` | `true` | No | — |
| `veeam_enable_auto_tape_scan` | `false` | No | Tape settings |
| `veeam_tape_scan_hour` | `2` | No | 2 AM daily scan |
| `veeam_enable_cloud_connect` | `false` | No | Cloud Connect settings |
| `veeam_cloud_connect_port` | `6180` | No | — |
| `veeam_config_backup_path` | `"C:\\VeeamConfigBackups"` | No | Configuration backup |
| `fourth_estate_mode` | `true` | No | Fourth Estate specific settings |
| `enable_audit_logging` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Veeam Backup Server Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: veeam/roles/veeam_backup_server_config
```

## License

MIT
