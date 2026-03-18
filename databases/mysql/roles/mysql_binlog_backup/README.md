# mysql_binlog_backup

Mysql Binlog Backup role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/mysql/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Mysql Binlog Backup
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/mysql/roles/mysql_binlog_backup
```

## License

MIT
