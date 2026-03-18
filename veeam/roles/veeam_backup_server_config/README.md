# veeam_backup_server_config

Veeam Backup Server Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `veeam_use_change_tracking` | `true` |  |
| `veeam_vmware_tools_quiescence` | `true` |  |
| `veeam_set_results_to_vm_notes` | `true` |  |
| `veeam_email_notifications` | `true` |  |
| `veeam_smtp_server` | `"smtp.example.com"` |  |
| `veeam_smtp_port` | `587` |  |
| `veeam_smtp_use_ssl` | `true` |  |
| `veeam_smtp_username` | `""` |  |
| `veeam_smtp_password` | `""` |  |
| `veeam_smtp_from` | `"veeam@example.com"` |  |
| `veeam_smtp_to` | `"backup-team@example.com"` |  |
| `veeam_email_subject` | `"Veeam Backup: %JOB_NAME% - %JOB_STATUS%"` |  |
| `veeam_notify_on_success` | `false` |  |
| `veeam_notify_on_warning` | `true` |  |
| `veeam_notify_on_error` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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
