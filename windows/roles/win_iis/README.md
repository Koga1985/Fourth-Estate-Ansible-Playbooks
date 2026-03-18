# win_iis

Win Iis role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `windows/README.md`

## Requirements

- Ansible 2.15+
- Collection: `ansible.windows community.windows`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Win Iis
  hosts: localhost
  gather_facts: false
  roles:
    - role: windows/roles/win_iis
```

## License

MIT
