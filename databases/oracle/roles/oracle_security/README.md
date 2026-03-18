# oracle_security

Oracle Security role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/oracle/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Oracle Security
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/oracle/roles/oracle_security
```

## License

MIT
