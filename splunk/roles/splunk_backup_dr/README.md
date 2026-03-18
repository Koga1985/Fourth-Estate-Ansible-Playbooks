# splunk_backup_dr

Configures Splunk Enterprise backup and disaster recovery: scheduled backups of `$SPLUNK_HOME/etc` and KVStore, optional offsite replication, encrypted archives, and DR runbook automation.

## Requirements

- Ansible 2.15+
- Sufficient disk space at `backup_path` (default `/backup/splunk`)
- `vault_splunk_admin_password` and `vault_backup_encryption_key` in vault.yml

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `backup_enabled` | `true` | No | Enable scheduled backups |
| `backup_path` | `"/backup/splunk"` | No | Local backup destination directory |
| `backup_retention_days` | `90` | No | Days to retain local backups |
| `backup_schedule` | `"0 2 * * 0"` | No | Cron schedule (default: weekly at 2 AM Sunday) |
| `backup_encryption_enabled` | `true` | No | Encrypt backup archives (STIG requirement) |
| `backup_encryption_key` | `{{ vault_backup_encryption_key }}` | **Yes** | Encryption key for backup archives |
| `backup_include_etc` | `true` | No | Back up `$SPLUNK_HOME/etc` (configs) |
| `backup_include_kvstore` | `true` | No | Back up KVStore (lookup tables, saved searches) |
| `backup_include_indexes` | `false` | No | Back up raw indexes (very large — use snapshots instead) |
| `dr_enabled` | `true` | No | Enable DR configuration |
| `archive_retention_years` | `7` | No | Long-term archive retention (compliance requirement) |

## Example Playbook

```yaml
---
- name: Configure Splunk Backup and DR
  hosts: splunk_servers
  become: true
  roles:
    - role: splunk/roles/splunk_backup_dr
      vars:
        backup_path: "/nfs/backups/splunk"
        backup_retention_days: 90
        backup_encryption_enabled: true
        archive_retention_years: 7
```

## License

MIT
