# vm_placement_policies

Vm Placement Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `vcenter_hostname` | `""` |  |
| `vcenter_username` | `""` |  |
| `vcenter_password` | `""` |  |
| `vcenter_validate_certs` | `false` |  |
| `cluster_name` | `""` | default cluster for rules/RPs (can be overridden per item) |
| `affinity_policies` | `[]` |  |
| `host_affinity_policies` | `[]` |  |
| `resource_pools` | `[]` |  |
| `report_path` | `"/tmp/vm-placement-policies-report.json"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vm Placement Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/vm_placement_policies
```

## License

MIT
