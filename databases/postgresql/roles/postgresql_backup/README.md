# postgresql_backup

Postgresql Backup role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/postgresql/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Postgresql Backup
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/postgresql/roles/postgresql_backup
```

## License

MIT
