# oracle_flashback

Oracle Flashback role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/oracle/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Oracle Flashback
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/oracle/roles/oracle_flashback
```

## License

MIT
