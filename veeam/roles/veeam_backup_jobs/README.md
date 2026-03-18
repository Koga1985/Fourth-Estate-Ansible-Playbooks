# veeam_backup_jobs

Veeam Backup Jobs role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Veeam Backup Jobs
  hosts: localhost
  gather_facts: false
  roles:
    - role: veeam/roles/veeam_backup_jobs
```

## License

MIT
