# pure_flasharray_volumes

Pure Flasharray Volumes role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` | No | Array connection |
| `flasharray_production_volumes` | `(see defaults/main.yml)` | No | Fourth Estate production volumes |
| `flasharray_default_qos` | `(see defaults/main.yml)` | No | Default QoS settings |
| `flasharray_snapshot_retention` | `(see defaults/main.yml)` | No | Snapshot retention defaults |
| `flasharray_volume_prefix` | `"vol"` | No | Volume naming convention |
| `flasharray_volume_naming_pattern` | `"{{ flasharray_volume_prefix }}-{{ application }}-{{ environment }}...` | No | — |
| `flasharray_thin_provisioning` | `true` | No | Thin provisioning (always enabled on Pure) |
| `flasharray_inline_reduction` | `true` | No | Data reduction (inline dedup and compression) |
| `flasharray_expected_reduction_ratio` | `"5:1"` | No | Typical for Fourth Estate workloads |
| `flasharray_volume_encryption` | `true` | No | Encryption (always enabled) AES-256 |
| `flasharray_default_block_size` | `"4K"` | No | Performance settings For databases and VMs |
| `flasharray_sequential_workload_hint` | `false` | No | — |
| `flasharray_volume_overprovisioning_ratio` | `3` | No | Capacity management Thin provisioning ratio |
| `flasharray_capacity_alert_threshold` | `80` | No | percent |
| `flasharray_capacity_critical_threshold` | `90` | No | percent |
| `flasharray_evidence_volumes_immutable` | `true` | No | Fourth Estate specific |
| `flasharray_source_protection_enabled` | `true` | No | — |
| `flasharray_ransomware_protection` | `true` | No | SafeMode snapshots |

## Example Playbook

```yaml
---
- name: Pure Flasharray Volumes
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_volumes
```

## Tags

| Tag | Description |
|-----|-------------|
| `production` | Tasks tagged `production` |
| `volumes` | Tasks tagged `volumes` |

## License

MIT
