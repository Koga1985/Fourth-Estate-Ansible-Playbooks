# rhel-audit-logging

Configures auditd and rsyslog on RHEL servers to meet DoD STIG (V-204494 through V-204644) and NIST 800-53 AU family requirements. Implements audit rules for privileged commands, file system mounts, user/group changes, and security events.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_audit_enabled` | `true` | No | Enable auditd service |
| `rhel_audit_log_retention_days` | `365` | No | Audit log retention days (365+ for Fourth Estate compliance) |
| `rhel_audit_max_log_file` | `10` | No | Audit log file size (MB) |
| `rhel_audit_num_logs` | `40` | No | Number of log files to keep (calculated for 365 day retention) With 10MB files and daily rotation, keep ~40 files for 1 year |
| `rhel_audit_max_log_file_action` | `rotate` | No | Action when audit log is full: ignore, syslog, suspend, single, halt |
| `rhel_audit_space_left` | `75` | No | Space left on disk (MB) |
| `rhel_audit_space_left_action` | `email` | No | Action when space is low: ignore, syslog, email, suspend, single, halt |
| `rhel_audit_action_mail_acct` | `root` | No | Admin to email when space is low |
| `rhel_audit_disk_full_action` | `suspend` | No | Disk full action |
| `rhel_audit_disk_error_action` | `suspend` | No | Disk error action |
| `rhel_audit_flush` | `incremental_async` | No | Flush audit logs to disk: none, incremental, incremental_async, data, sync |
| `rhel_configure_audit_rules` | `true` | No | Configure STIG-compliant audit rules |
| `rhel_custom_audit_rules` | `[]` | No | Custom audit rules |
| `rhel_rsyslog_enabled` | `true` | No | Enable rsyslog |
| `rhel_remote_logging_enabled` | `false` | No | Remote logging configuration |
| `rhel_remote_log_server` | `""` | No | — |
| `rhel_remote_log_port` | `514` | No | — |
| `rhel_remote_log_protocol` | `tcp` | No | — |
| `rhel_log_file_permissions` | `"0640"` | No | Log file permissions |
| `rhel_log_rotation_days` | `7` | No | Log rotation days |
| `rhel_configure_aide` | `true` | No | Configure AIDE for file integrity monitoring |
| `rhel_aide_db_path` | `/var/lib/aide/aide.db.gz` | No | AIDE database path |
| `rhel_aide_check_schedule` | `daily` | No | AIDE check schedule (cron) |

## Example Playbook

```yaml
---
- name: Configure RHEL Audit Logging
  hosts: rhel_servers
  become: true
  roles:
    - role: rhel/roles/rhel-audit-logging
      vars:
        rhel_audit_log_retention_days: 365
        rhel_remote_logging_enabled: true
        rhel_syslog_server: "syslog.example.com"
```

## Tags

| Tag | Description |
|-----|-------------|
| `aide` | Tasks tagged `aide` |
| `auditd` | Tasks tagged `auditd` |
| `packages` | Tasks tagged `packages` |
| `permissions` | Tasks tagged `permissions` |
| `rsyslog` | Tasks tagged `rsyslog` |
| `services` | Tasks tagged `services` |
| `validation` | Tasks tagged `validation` |

## License

MIT
