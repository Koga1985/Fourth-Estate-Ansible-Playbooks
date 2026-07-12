# datastore_cluster_sdrs

Datastore Cluster Sdrs role for Fourth Estate infrastructure automation.

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
| `vcenter_datacenter` | `""` | No | — |
| `target_folder` | `""` | No | — |
| `sdrs` | `(see defaults/main.yml)` | No | — |
| `membership` | `(see defaults/main.yml)` | No | — |
| `apply_recommendations` | `false` | No | — |
| `report_path` | `"/tmp/{{ sdrs.name \| default('datastore-cluster') }}-sdrs-report.json"` | No | — |

## Example Playbook

```yaml
---
- name: Datastore Cluster Sdrs
  hosts: localhost
  gather_facts: false
  roles:
    - role: vmware/roles/datastore_cluster_sdrs
```

## License

MIT
