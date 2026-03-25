# fortigate_firewall_policy

Fortigate Firewall Policy role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/fortinet/README.md`

## Requirements

- Ansible 2.15+
- Collection: `fortinet.fortios`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Fortigate Firewall Policy
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/fortinet/roles/fortigate_firewall_policy
```

## License

MIT
