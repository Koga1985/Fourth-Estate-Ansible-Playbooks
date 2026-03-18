# veeam_replication

Veeam Replication role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Veeam Replication
  hosts: localhost
  gather_facts: false
  roles:
    - role: veeam/roles/veeam_replication
```

## License

MIT
