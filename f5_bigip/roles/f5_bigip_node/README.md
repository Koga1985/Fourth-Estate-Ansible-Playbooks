# f5_bigip_node

F5 Bigip Node role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `f5_bigip_provider` | `(see defaults/main.yml)` | No | F5 BIG-IP Connection Details |
| `f5_bigip_nodes` | `[]` | No | Node Configuration |
| `f5_bigip_fqdn_nodes` | `[]` | No | FQDN Nodes Configuration |
| `f5_bigip_node_discovery_enabled` | `false` | No | Dynamic Node Discovery |
| `f5_bigip_node_connection_limit` | `0` | No | Connection Limits 0 = unlimited |
| `f5_bigip_node_rate_limit` | `0` | No | 0 = unlimited |
| `f5_bigip_node_monitor_default` | `"/Common/icmp"` | No | Node Monitoring |
| `f5_bigip_node_session_default` | `"user-enabled"` | No | Session State |
| `f5_bigip_node_state_default` | `"user-up"` | No | — |
| `f5_bigip_node_ratio_default` | `1` | No | Node Ratio (for ratio-based load balancing) |
| `f5_bigip_save_config` | `true` | No | Save Configuration |

## Example Playbook

```yaml
---
- name: F5 Bigip Node
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_node
```

## Tags

| Tag | Description |
|-----|-------------|
| `f5_backend` | Tasks tagged `f5_backend` |
| `f5_fqdn_nodes` | Tasks tagged `f5_fqdn_nodes` |
| `f5_node_state` | Tasks tagged `f5_node_state` |
| `f5_nodes` | Tasks tagged `f5_nodes` |
| `f5_save` | Tasks tagged `f5_save` |
| `f5_verify` | Tasks tagged `f5_verify` |

## License

MIT
