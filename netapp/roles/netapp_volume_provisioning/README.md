# netapp_volume_provisioning

Netapp Volume Provisioning role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `netapp/README.md`

## Requirements

- Ansible 2.15+
- Collection: `netapp.ontap`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `netapp_volume_hostname` | `"{{ vault_netapp_cluster_hostname \| default('netapp-cluster.example...` | No | Connection settings |
| `netapp_volume_username` | `"{{ vault_netapp_cluster_username \| default('admin') }}"` | No | — |
| `netapp_volume_password` | `"{{ vault_netapp_cluster_password }}"` | No | — |
| `netapp_volume_validate_certs` | `true` | No | — |
| `netapp_volume_svm` | `"svm_prod"` | No | SVM configuration |
| `netapp_volume_default_aggregate` | `"aggr1_netapp01_SAS"` | No | Default volume settings |
| `netapp_volume_security_style` | `"unix"` | No | — |
| `netapp_volume_space_guarantee` | `"none"` | No | Thin provisioning |
| `netapp_volume_snapshot_reserve` | `5` | No | Percentage |
| `netapp_volume_snapshot_policy` | `"default"` | No | — |
| `netapp_volume_tiering_policy` | `"none"` | No | Options: none, snapshot-only, auto, all |
| `netapp_volume_encryption` | `true` | No | Enable NVE |
| `netapp_volume_create_flexvols` | `true` | No | FlexVol provisioning |
| `netapp_volume_flexvols` | `(see defaults/main.yml)` | No | — |
| `netapp_volume_create_flexgroups` | `false` | No | FlexGroup provisioning (for scale-out workloads) |
| `netapp_volume_flexgroups` | `(see defaults/main.yml)` | No | — |
| `netapp_volume_create_qos_policies` | `true` | No | QoS policies |
| `netapp_volume_qos_policies` | `(see defaults/main.yml)` | No | — |
| `netapp_volume_enable_efficiency` | `true` | No | Volume efficiency (deduplication and compression) |
| `netapp_volume_efficiency_schedule` | `"daily@0"` | No | — |
| `netapp_volume_efficiency_policy` | `"default"` | No | — |
| `netapp_volume_enable_compression` | `true` | No | — |
| `netapp_volume_enable_inline_compression` | `true` | No | — |
| `netapp_volume_enable_inline_dedupe` | `true` | No | — |
| `netapp_volume_enable_data_compaction` | `true` | No | — |
| `netapp_volume_enable_autosize` | `true` | No | Volume autosize configuration |
| `netapp_volume_autosize_mode` | `"grow_shrink"` | No | — |
| `netapp_volume_autosize_grow_threshold` | `85` | No | — |
| `netapp_volume_autosize_shrink_threshold` | `50` | No | — |
| `netapp_volume_create_clones` | `false` | No | Volume cloning |
| `netapp_volume_clones` | `[]` | No | — |
| `netapp_volume_enable_snaplock` | `false` | No | SnapLock configuration (compliance/governance) |
| `netapp_volume_snaplock_volumes` | `[]` | No | — |
| `netapp_volume_enable_anti_ransomware` | `true` | No | Anti-ransomware protection (Autonomous Ransomware Protection) |
| `netapp_volume_enable_analytics` | `false` | No | Volume analytics |
| `netapp_volume_enable_quotas` | `false` | No | Quotas |
| `netapp_volume_quotas` | `[]` | No | — |
| `netapp_volume_set_options` | `true` | No | Volume options |
| `netapp_volume_verify_provisioning` | `true` | No | Verification |
| `netapp_volume_debug` | `false` | No | Debug mode |

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
