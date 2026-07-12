# panos_network_config

Panos Network Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `palo_alto/README.md`

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `panos_provider` | `(see defaults/main.yml)` | No | PAN-OS provider connection details |
| `panos_mgmt_profiles` | `(see defaults/main.yml)` | No | Management profiles |
| `panos_l3_interfaces` | `(see defaults/main.yml)` | No | Layer 3 interfaces (typical Fourth Estate deployment) |
| `panos_l2_interfaces` | `[]` | No | Layer 2 interfaces |
| `panos_virtual_wire_interfaces` | `[]` | No | Virtual wire interfaces |
| `panos_vlan_interfaces` | `(see defaults/main.yml)` | No | VLAN interfaces |
| `panos_zones` | `(see defaults/main.yml)` | No | Security zones (Fourth Estate architecture) |
| `panos_zone_interfaces` | `(see defaults/main.yml)` | No | Zone interface assignments |
| `panos_virtual_routers` | `(see defaults/main.yml)` | No | Virtual routers |
| `panos_static_routes` | `(see defaults/main.yml)` | No | Static routes |
| `panos_bgp_configs` | `[]` | No | BGP configuration (optional) |
| `panos_bgp_peer_groups` | `[]` | No | — |
| `panos_bgp_peers` | `[]` | No | — |
| `panos_ospf_configs` | `[]` | No | OSPF configuration |
| `panos_ospf_areas` | `[]` | No | — |
| `panos_ospf_interfaces` | `[]` | No | — |
| `panos_multicast_configs` | `[]` | No | Multicast (PIM) configuration |
| `panos_pim_interfaces` | `[]` | No | — |
| `panos_qos_profiles` | `(see defaults/main.yml)` | No | QoS profiles (prioritize critical traffic) |
| `panos_lag_interfaces` | `[]` | No | Link aggregation groups (LAG) |
| `panos_lag_members` | `[]` | No | — |
| `panos_enable_lldp` | `true` | No | LLDP |
| `panos_tunnel_interfaces` | `(see defaults/main.yml)` | No | Tunnel interfaces |

## Example Playbook

```yaml
---
- name: Panos Network Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: palo_alto/roles/panos_network_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `bgp` | Tasks tagged `bgp` |
| `interfaces` | Tasks tagged `interfaces` |
| `lag` | Tasks tagged `lag` |
| `layer2` | Tasks tagged `layer2` |
| `layer3` | Tasks tagged `layer3` |
| `lldp` | Tasks tagged `lldp` |
| `management` | Tasks tagged `management` |
| `multicast` | Tasks tagged `multicast` |
| `network` | Tasks tagged `network` |
| `ospf` | Tasks tagged `ospf` |
| `pim` | Tasks tagged `pim` |
| `qos` | Tasks tagged `qos` |
| `routing` | Tasks tagged `routing` |
| `static` | Tasks tagged `static` |
| `tunnel` | Tasks tagged `tunnel` |
| `virtualwire` | Tasks tagged `virtualwire` |
| `vlan` | Tasks tagged `vlan` |
| `vr` | Tasks tagged `vr` |
| `zones` | Tasks tagged `zones` |

## License

MIT
