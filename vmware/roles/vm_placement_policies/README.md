# vm_placement_policies

Vm Placement Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vcenter_hostname` | `""` | No | vCenter connection |
| `vcenter_username` | `""` | No | — |
| `vcenter_password` | `""` | No | — |
| `vcenter_validate_certs` | `false` | No | — |
| `cluster_name` | `""` | No | Scope default cluster for rules/RPs (can be overridden per item) |
| `affinity_policies` | `[]` | No | VM-VM (anti-)affinity by tag |
| `host_affinity_policies` | `[]` | No | VM↔Host affinity by groups (pin to host groups, or avoid certain hosts) |
| `resource_pools` | `[]` | No | Resource pool policies (reservations/limits/shares) + tag-based placement |
| `report_path` | `"/tmp/vm-placement-policies-report.json"` | No | Report |

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
