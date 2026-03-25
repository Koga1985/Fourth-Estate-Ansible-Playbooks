# fortigate_security_profiles

Fortigate Security Profiles role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `databases/fortinet/README.md`

## Requirements

- Ansible 2.15+
- Collection: `fortinet.fortios`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Fortigate Security Profiles
  hosts: localhost
  gather_facts: false
  roles:
    - role: databases/fortinet/roles/fortigate_security_profiles
```

## License

MIT
