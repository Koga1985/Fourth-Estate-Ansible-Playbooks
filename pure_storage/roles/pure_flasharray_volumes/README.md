# pure_flasharray_volumes

Pure Flasharray Volumes role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` |  |
| `flasharray_volume_prefix` | `"vol"` |  |
| `flasharray_volume_naming_pattern` | `"{{ flasharray_volume_prefix }}-{{ application ...` |  |
| `flasharray_thin_provisioning` | `true` |  |
| `flasharray_inline_reduction` | `true` |  |
| `flasharray_expected_reduction_ratio` | `"5:1"` | No | Typical for Fourth Estate workloads |
| `flasharray_volume_encryption` | `true` | No | AES-256 |
| `flasharray_default_block_size` | `"4K"` | No | For databases and VMs |
| `flasharray_sequential_workload_hint` | `false` |  |
| `flasharray_volume_overprovisioning_ratio` | `3` | No | Thin provisioning ratio |
| `flasharray_capacity_alert_threshold` | `80` | No | percent |
| `flasharray_capacity_critical_threshold` | `90` | No | percent |
| `flasharray_evidence_volumes_immutable` | `true` |  |
| `flasharray_source_protection_enabled` | `true` |  |
| `flasharray_ransomware_protection` | `true` | No | SafeMode snapshots |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Flasharray Volumes
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_volumes
```

## License

MIT
