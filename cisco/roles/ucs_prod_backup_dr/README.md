# ucs_prod_backup_dr

Cisco UCS production backup and disaster recovery role.

## Description

Configures automated backups and disaster recovery procedures for Cisco UCS infrastructure.

## Features

- Full-state backups
- Configuration-only backups
- Scheduled and immediate backups
- Disaster recovery documentation
- Backup verification scripts
- RTO/RPO tracking

## Requirements

- Ansible >= 2.9
- Cisco UCS Ansible collection
- SCP/FTP/TFTP server for backup storage

## Variables

See `defaults/main.yml` for configuration options.

## Example Playbook

```yaml
- name: Configure UCS Backup and DR
  hosts: localhost
  roles:
    - role: ucs_prod_backup_dr
      vars:
        apply_changes: true
        backup_type: "full-state"
        backup_schedule: "daily"
```

## Backup Types

- **full-state**: Complete system backup (recommended)
- **config-all**: All configuration
- **config-logical**: Logical configuration only

## License

MIT
