# f5_bigip_node

F5 Bigip Node role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `f5_bigip_nodes` | `[]` |  |
| `f5_bigip_fqdn_nodes` | `[]` |  |
| `f5_bigip_node_discovery_enabled` | `false` |  |
| `f5_bigip_node_connection_limit` | `0` | 0 = unlimited |
| `f5_bigip_node_rate_limit` | `0` | 0 = unlimited |
| `f5_bigip_node_monitor_default` | `"/Common/icmp"` |  |
| `f5_bigip_node_session_default` | `"user-enabled"` |  |
| `f5_bigip_node_state_default` | `"user-up"` |  |
| `f5_bigip_node_ratio_default` | `1` |  |
| `f5_bigip_save_config` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: F5 Bigip Node
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_node
```

## License

MIT
