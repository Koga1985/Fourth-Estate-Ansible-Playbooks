# f5_bigip_network

F5 Bigip Network role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `f5_bigip/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `f5_bigip_vlans` | `[]` |  |
| `f5_bigip_selfips` | `[]` |  |
| `f5_bigip_static_routes` | `[]` |  |
| `f5_bigip_route_domains` | `[]` |  |
| `f5_bigip_trunks` | `[]` |  |
| `f5_bigip_port_lockdown_default` | `"allow-default"` |  |
| `f5_bigip_mac_masquerade_enabled` | `false` |  |
| `f5_bigip_mac_masquerade_addresses` | `[]` |  |
| `f5_bigip_tunnels` | `[]` |  |
| `f5_bigip_interfaces` | `[]` |  |
| `f5_bigip_default_mtu` | `1500` |  |
| `f5_bigip_arp_enabled` | `true` |  |
| `f5_bigip_icmp_echo_enabled` | `true` |  |
| `f5_bigip_save_config` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `f5networks.f5_modules`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: F5 Bigip Network
  hosts: localhost
  gather_facts: false
  roles:
    - role: f5_bigip/roles/f5_bigip_network
```

## License

MIT
