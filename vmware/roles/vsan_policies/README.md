# vsan_policies

Vsan Policies role for Fourth Estate infrastructure automation.

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
| `policies` | `[]` | No | — |
| `assignments` | `[]` | No | — |
| `report_path` | `"/tmp/vsan-policies-report.json"` | No | — |
| `run_compliance_checks` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Vsan Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/vsan_policies
```

## License

MIT
