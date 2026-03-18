# pure_flasharray_replication

Pure Flasharray Replication role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `pure_storage/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `flasharray_url` | `"https://{{ inventory_hostname }}"` |  |
| `flasharray_default_rpo_minutes` | `15` |  |
| `flasharray_critical_rpo_minutes` | `5` |  |
| `flasharray_standard_rpo_minutes` | `60` |  |
| `flasharray_activecluster_enabled` | `false` |  |
| `flasharray_activecluster_rpo` | `0` | Synchronous (zero RPO) |
| `flasharray_activecluster_auto_failover` | `true` |  |
| `flasharray_activecluster_witness` | `true` |  |
| `flasharray_activedr_enabled` | `true` |  |
| `flasharray_activedr_compression` | `true` |  |
| `flasharray_activedr_dedupe` | `true` |  |
| `flasharray_replication_use_jumbo_frames` | `true` |  |
| `flasharray_replication_mtu` | `9000` |  |
| `flasharray_replication_compression` | `true` |  |
| `flasharray_replication_bandwidth_unlimited` | `false` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Pure Flasharray Replication
  hosts: localhost
  gather_facts: false
  roles:
    - role: pure_storage/roles/pure_flasharray_replication
```

## License

MIT
