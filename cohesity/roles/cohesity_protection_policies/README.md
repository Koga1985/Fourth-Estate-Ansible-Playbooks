# cohesity_protection_policies

Cohesity Protection Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `cohesity/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Cohesity Protection Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: cohesity/roles/cohesity_protection_policies
```

## License

MIT
