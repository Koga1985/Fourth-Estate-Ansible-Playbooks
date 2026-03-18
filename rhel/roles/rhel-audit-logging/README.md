# rhel-audit-logging

Configures auditd and rsyslog on RHEL servers to meet DoD STIG (V-204494 through V-204644) and NIST 800-53 AU family requirements. Implements audit rules for privileged commands, file system mounts, user/group changes, and security events.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `rhel_audit_enabled` | `true` | No | Enable and start auditd |
| `rhel_audit_log_retention_days` | `365` | No | Days to retain audit logs |
| `rhel_audit_max_log_file` | `10` | No | Max size per log file (MB) |
| `rhel_audit_num_logs` | `40` | No | Number of log files to rotate through |
| `rhel_audit_max_log_file_action` | `"rotate"` | No | Action when log is full: `rotate`, `syslog`, `suspend`, `halt` |
| `rhel_audit_space_left` | `75` | No | MB of disk space to trigger low-space warning |
| `rhel_audit_space_left_action` | `"email"` | No | Action when space is low |
| `rhel_remote_logging_enabled` | `false` | No | Forward logs to remote syslog server |
| `rhel_syslog_server` | `""` | No | Remote syslog server address (if remote logging enabled) |

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

## License

MIT
