# nsx_t_networking

Nsx T Networking role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Nsx T Networking
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/nsx_t_networking
```

## License

MIT
