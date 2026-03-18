# ansible_tower_config

Ansible Tower Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `ansible_tower/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Ansible Tower Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: ansible_tower/roles/ansible_tower_config
```

## License

MIT
