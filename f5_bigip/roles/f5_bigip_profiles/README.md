# f5_bigip_profiles

F5 Bigip Profiles role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: F5 Bigip Profiles
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_profiles
```

## License

MIT
