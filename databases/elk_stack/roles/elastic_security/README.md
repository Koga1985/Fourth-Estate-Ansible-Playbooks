# elastic_security

Elastic Security role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/elk_stack/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Elastic Security
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/elk_stack/roles/elastic_security
```

## License

MIT
