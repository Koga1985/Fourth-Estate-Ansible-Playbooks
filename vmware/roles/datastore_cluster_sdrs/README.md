# datastore_cluster_sdrs

Datastore Cluster Sdrs role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vmware/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vcenter_hostname` | `""` |  |
| `vcenter_username` | `""` |  |
| `vcenter_password` | `""` |  |
| `vcenter_validate_certs` | `false` |  |
| `vcenter_datacenter` | `""` |  |
| `target_folder` | `""` |  |
| `apply_recommendations` | `false` |  |
| `report_path` | `"/tmp/{{ sdrs.name | No | default('datastore-cluster...` |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.vmware`
- See platform `requirements.yml` for install instructions

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
