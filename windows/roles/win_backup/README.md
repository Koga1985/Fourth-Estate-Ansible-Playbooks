# win_backup

Win Backup role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `windows/README.md`

## Requirements

- Ansible 2.15+
- Collection: `ansible.windows community.windows`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Win Backup
  hosts: localhost
  gather_facts: false
  roles:
    - role: windows/roles/win_backup
```

## License

MIT
