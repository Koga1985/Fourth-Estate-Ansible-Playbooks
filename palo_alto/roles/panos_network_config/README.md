# panos_network_config

Panos Network Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `palo_alto/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `panos_l2_interfaces` | `[]` |  |
| `panos_virtual_wire_interfaces` | `[]` |  |
| `panos_bgp_configs` | `[]` |  |
| `panos_bgp_peer_groups` | `[]` |  |
| `panos_bgp_peers` | `[]` |  |
| `panos_ospf_configs` | `[]` |  |
| `panos_ospf_areas` | `[]` |  |
| `panos_ospf_interfaces` | `[]` |  |
| `panos_multicast_configs` | `[]` |  |
| `panos_pim_interfaces` | `[]` |  |
| `panos_lag_interfaces` | `[]` |  |
| `panos_lag_members` | `[]` |  |
| `panos_enable_lldp` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `paloaltonetworks.panos`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Panos Network Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: palo_alto/roles/panos_network_config
```

## License

MIT
