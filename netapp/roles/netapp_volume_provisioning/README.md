# netapp_volume_provisioning

Netapp Volume Provisioning role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `netapp/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `netapp_volume_hostname` | `"{{ vault_netapp_cluster_hostname | default('ne...` |  |
| `netapp_volume_username` | `"{{ vault_netapp_cluster_username | default('ad...` |  |
| `netapp_volume_password` | `"{{ vault_netapp_cluster_password }}"` |  |
| `netapp_volume_validate_certs` | `true` |  |
| `netapp_volume_svm` | `"svm_prod"` |  |
| `netapp_volume_default_aggregate` | `"aggr1_netapp01_SAS"` |  |
| `netapp_volume_security_style` | `"unix"` |  |
| `netapp_volume_space_guarantee` | `"none"` | Thin provisioning |
| `netapp_volume_snapshot_reserve` | `5` | Percentage |
| `netapp_volume_snapshot_policy` | `"default"` |  |
| `netapp_volume_tiering_policy` | `"none"` | Options: none, snapshot-only, auto, all |
| `netapp_volume_encryption` | `true` | Enable NVE |
| `netapp_volume_create_flexvols` | `true` |  |
| `netapp_volume_create_flexgroups` | `false` |  |
| `netapp_volume_create_qos_policies` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `netapp.ontap`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Netapp Volume Provisioning
  hosts: localhost
  gather_facts: false
  roles:
    - role: netapp/roles/netapp_volume_provisioning
```

## License

MIT
