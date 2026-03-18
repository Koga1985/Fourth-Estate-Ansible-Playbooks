# win_dhcp_dns

Win Dhcp Dns role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `windows/README.md`

## Requirements

- Ansible 2.15+
- Collection: `ansible.windows community.windows`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Win Dhcp Dns
  hosts: localhost
  gather_facts: false
  roles:
    - role: windows/roles/win_dhcp_dns
```

## License

MIT
