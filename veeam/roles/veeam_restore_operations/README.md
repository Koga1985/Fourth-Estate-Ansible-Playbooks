# veeam_restore_operations

Veeam Restore Operations role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `veeam/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Veeam Restore Operations
  hosts: localhost
  gather_facts: false
  roles:
    - role: veeam/roles/veeam_restore_operations
```

## License

MIT
