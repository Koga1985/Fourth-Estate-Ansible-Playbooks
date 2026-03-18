# vsan_policies

Vsan Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vcenter_hostname` | `""` |  |
| `vcenter_username` | `""` |  |
| `vcenter_password` | `""` |  |
| `vcenter_validate_certs` | `false` |  |
| `policies` | `[]` |  |
| `assignments` | `[]` |  |
| `report_path` | `"/tmp/vsan-policies-report.json"` |  |
| `run_compliance_checks` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

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
