# win_wsus

Win Wsus role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `windows/README.md`

## Requirements

- Ansible 2.15+
- Collection: `ansible.windows community.windows`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Win Wsus
  hosts: localhost
  gather_facts: false
  roles:
    - role: windows/roles/win_wsus
```

## License

MIT
