# win_user_management

Win User Management role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `windows/README.md`

## Requirements

- Ansible 2.15+
- Collection: `ansible.windows community.windows`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Win User Management
  hosts: localhost
  gather_facts: false
  roles:
    - role: windows/roles/win_user_management
```

## License

MIT
