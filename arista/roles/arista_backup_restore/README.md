# arista_backup_restore

Backs up, restores, and compares Arista EOS device configurations. The role captures running configuration, startup configuration, and a full operational-state snapshot per device, enforces a configurable retention policy with archive compression, and can optionally integrate with Git for version-controlled configuration storage.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- Write access to `backup_dir` and `backup_archive_dir` on the Ansible controller
- EOS user with at minimum read access (`network-operator`) for backup; `network-admin` for restore

## Role Variables

All variables are defined in `defaults/main.yml`.

| Variable | Default | Description |
|---|---|---|
| `backup_dir` | `/tmp/arista-backups` | Root directory for device backup files on the controller. A per-device subdirectory is created automatically. |
| `backup_archive_dir` | `/tmp/arista-backups/archives` | Directory where compressed `.tar.gz` archives of aged-out backups are stored. |
| `backup_operation` | `backup` | Operational mode. Valid values: `backup`, `restore`, `compare`, `both`. |
| `backup_startup` | `true` | When `true`, the startup configuration is also captured in addition to the running configuration. |
| `backup_snapshots` | `true` | When `true`, collects operational-state outputs (version, inventory, VLANs, interfaces, routes, BGP). |
| `backup_retention_days` | `30` | Files older than this many days are archived and removed from the active backup directory. |
| `restore_file` | `""` | Absolute path to the configuration file used during a restore operation. Required when `backup_operation` is `restore` or `both`. |
| `restore_mode` | `replace` | How the configuration is applied during restore. Valid values: `replace` (full replacement), `merge` (additive). |
| `pre_restore_backup` | `true` | Creates a timestamped backup immediately before any restore so the previous state can be recovered. |
| `save_after_restore` | `true` | Saves the running configuration to startup after a successful restore. |
| `verify_after_restore` | `true` | Runs a brief verification (hostname, software version, connected interfaces) after restore completes. |
| `baseline_config` | `""` | Path to a baseline configuration file used when `backup_operation` is `compare`. |
| `backup_git.enabled` | `false` | Enables Git commit of backup files after each run. |
| `backup_encryption.enabled` | `false` | Enables GPG or Ansible Vault encryption of backup files. |
| `backup_compliance.enabled` | `true` | Enables post-backup compliance checks (STIG and baseline deviation reporting). |

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
