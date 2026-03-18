# netapp_backup

Netapp Backup role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/netapp/README.md`

## Requirements

- Ansible 2.15+
- Collection: `netapp.ontap`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Netapp Backup
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/netapp/roles/netapp_backup
```

## License

MIT
