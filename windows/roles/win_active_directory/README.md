# win_active_directory

Win Active Directory role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `windows/README.md`

## Requirements

- Ansible 2.15+
- Collection: `ansible.windows community.windows`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Win Active Directory
  hosts: localhost
  gather_facts: false
  roles:
    - role: windows/roles/win_active_directory
```

## License

MIT
