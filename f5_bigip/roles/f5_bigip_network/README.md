# f5_bigip_network

F5 Bigip Network role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `f5_bigip_provider` | `(see defaults/main.yml)` | No | F5 BIG-IP Connection Details (inherited from system role) |
| `f5_bigip_vlans` | `[]` | No | VLANs Configuration |
| `f5_bigip_selfips` | `[]` | No | Self IPs Configuration |
| `f5_bigip_static_routes` | `[]` | No | Static Routes Configuration |
| `f5_bigip_route_domains` | `[]` | No | Route Domains |
| `f5_bigip_trunks` | `[]` | No | Trunk Configuration (Link Aggregation) |
| `f5_bigip_port_lockdown_default` | `"allow-default"` | No | Port Lockdown Settings |
| `f5_bigip_mac_masquerade_enabled` | `false` | No | MAC Masquerading |
| `f5_bigip_mac_masquerade_addresses` | `[]` | No | — |
| `f5_bigip_tunnels` | `[]` | No | Network Tunnels |
| `f5_bigip_interfaces` | `[]` | No | Network Interface Settings |
| `f5_bigip_management_route` | `(see defaults/main.yml)` | No | Management Route |
| `f5_bigip_default_mtu` | `1500` | No | MTU Settings |
| `f5_bigip_arp_enabled` | `true` | No | ARP Configuration |
| `f5_bigip_icmp_echo_enabled` | `true` | No | ICMP Echo (Ping) Response |
| `f5_bigip_save_config` | `true` | No | Save Configuration |

## Example Playbook

```yaml
---
- name: F5 Bigip Network
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_network
```

## Tags

| Tag | Description |
|-----|-------------|
| `f5_ha` | Tasks tagged `f5_ha` |
| `f5_interfaces` | Tasks tagged `f5_interfaces` |
| `f5_mac_masquerade` | Tasks tagged `f5_mac_masquerade` |
| `f5_management_route` | Tasks tagged `f5_management_route` |
| `f5_network` | Tasks tagged `f5_network` |
| `f5_route_domains` | Tasks tagged `f5_route_domains` |
| `f5_routes` | Tasks tagged `f5_routes` |
| `f5_save` | Tasks tagged `f5_save` |
| `f5_selfips` | Tasks tagged `f5_selfips` |
| `f5_trunks` | Tasks tagged `f5_trunks` |
| `f5_tunnels` | Tasks tagged `f5_tunnels` |
| `f5_verify` | Tasks tagged `f5_verify` |
| `f5_vlans` | Tasks tagged `f5_vlans` |

## License

MIT
