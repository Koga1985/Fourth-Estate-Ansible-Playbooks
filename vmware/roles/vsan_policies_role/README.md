# vsan_policies_role

VMware vSAN Storage Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Configure vSAN Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/vsan_policies_role
```

## License

MIT
