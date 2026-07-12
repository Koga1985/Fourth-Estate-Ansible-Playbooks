# arista_backup_restore

Backs up, restores, and compares Arista EOS device configurations. The role captures running configuration, startup configuration, and a full operational-state snapshot per device, enforces a configurable retention policy with archive compression, and can optionally integrate with Git for version-controlled configuration storage.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- Write access to `backup_dir` and `backup_archive_dir` on the Ansible controller
- EOS user with at minimum read access (`network-operator`) for backup; `network-admin` for restore

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `backup_dir` | `"/tmp/arista-backups"` | No | Backup directory |
| `backup_archive_dir` | `"/tmp/arista-backups/archives"` | No | — |
| `backup_operation` | `"backup"` | No | Backup operation mode: backup, restore, compare, both |
| `backup_startup` | `true` | No | Backup options |
| `backup_snapshots` | `true` | No | — |
| `backup_retention_days` | `30` | No | — |
| `restore_file` | `""` | No | Restore options |
| `restore_mode` | `"replace"` | No | Options: replace, merge |
| `pre_restore_backup` | `true` | No | — |
| `save_after_restore` | `true` | No | — |
| `verify_after_restore` | `true` | No | — |
| `baseline_config` | `""` | No | Compare options |
| `backup_schedule` | `(see defaults/main.yml)` | No | Backup schedule (for use with cron/scheduled jobs) |
| `backup_notification` | `(see defaults/main.yml)` | No | Backup notification |
| `backup_git` | `(see defaults/main.yml)` | No | Git integration for version control |
| `backup_encryption` | `(see defaults/main.yml)` | No | Encryption options |
| `backup_compliance` | `(see defaults/main.yml)` | No | Backup compliance |

## Example Playbook

### Back up all devices

```yaml
- name: Back up Arista EOS configurations
  hosts: arista_switches
  gather_facts: false
  roles:
    - role: arista_backup_restore
      vars:
        backup_operation: backup
        backup_dir: /opt/network-backups/arista
        backup_retention_days: 60
```

### Restore a specific device from a backup file

```yaml
- name: Restore configuration from backup
  hosts: leaf-01
  gather_facts: false
  roles:
    - role: arista_backup_restore
      vars:
        backup_operation: restore
        restore_file: /opt/network-backups/arista/leaf-01/leaf-01_2026-03-01_02-00-00.cfg
        restore_mode: replace
```

### Compare running configuration against a baseline

```yaml
- name: Diff running config against baseline
  hosts: arista_switches
  gather_facts: false
  roles:
    - role: arista_backup_restore
      vars:
        backup_operation: compare
        baseline_config: /opt/baselines/arista_standard.cfg
```

## Notes and Dependencies

- Backup files are placed in `<backup_dir>/<inventory_hostname>/` and timestamped with the execution date and time.
- A per-device JSON metadata file containing full device facts is written alongside each backup.
- An HTML backup report is rendered from the `backup_report.j2` template; this template must be present in the role's `templates/` directory.
- When `backup_retention_days` is set, files older than the threshold are archived to `backup_archive_dir` before deletion. The archive step uses `ignore_errors: true` so a missing archive directory does not abort the play.
- Notification (`backup_notification`) and Git integration (`backup_git`) options are available but require additional site-specific configuration such as an SMTP server and a Git remote URL.
- Sensitive variables such as GPG recipients and email addresses should be stored in Ansible Vault.

## License

MIT
