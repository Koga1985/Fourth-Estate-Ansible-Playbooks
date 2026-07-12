# fortigate_interfaces

Configures FortiGate network interfaces — physical, VLAN, loopback, and LAG
interfaces, zones, secondary IPs, DHCP servers, and interface-level monitoring/BFD
settings — via the FortiGate API.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `fortigate_host` | `"{{ ansible_host }}"` | No | FortiGate connection parameters |
| `fortigate_username` | `"{{ vault_fortigate_username \| default('admin') }}"` | No | — |
| `fortigate_password` | `"{{ vault_fortigate_password }}"` | No | — |
| `fortigate_api_token` | `"{{ vault_fortigate_api_token \| default('') }}"` | No | — |
| `fortigate_vdom` | `"root"` | No | — |
| `fortigate_https` | `true` | No | — |
| `fortigate_validate_certs` | `true` | No | — |
| `fortigate_physical_interfaces` | `(see defaults/main.yml)` | No | Physical interfaces configuration |
| `fortigate_vlan_interfaces` | `(see defaults/main.yml)` | No | VLAN interfaces |
| `fortigate_loopback_interfaces` | `(see defaults/main.yml)` | No | Loopback interfaces |
| `fortigate_lag_interfaces` | `[]` | No | Link aggregation (LAG) interfaces |
| `fortigate_dhcp_servers` | `(see defaults/main.yml)` | No | DHCP server configuration for interfaces |
| `fortigate_zones` | `(see defaults/main.yml)` | No | Interface zones configuration |
| `fortigate_ipv6_enabled` | `false` | No | IPv6 configuration |
| `fortigate_ipv6_interfaces` | `[]` | No | — |
| `fortigate_secondary_ips` | `[]` | No | Secondary IP addresses |
| `fortigate_interface_monitoring` | `(see defaults/main.yml)` | No | Interface monitoring |
| `fortigate_mac_override` | `[]` | No | MAC address override |
| `fortigate_bfd_interfaces` | `[]` | No | BFD (Bidirectional Forwarding Detection) on interfaces |
| `fortigate_interface_policy` | `[]` | No | Interface policy configuration |
| `fortigate_speed_duplex_settings` | `(see defaults/main.yml)` | No | Speed and duplex settings |
| `fortigate_mtu_settings` | `(see defaults/main.yml)` | No | MTU settings per interface type |
| `fortigate_lldp_enabled` | `true` | No | LLDP configuration |
| `fortigate_lldp_network_policy` | `[]` | No | — |
| `fortigate_sflow_enabled` | `false` | No | sFlow configuration |
| `fortigate_sflow_collectors` | `[]` | No | — |
| `fortigate_netflow_enabled` | `false` | No | NetFlow configuration |
| `fortigate_netflow_collectors` | `[]` | No | — |
| `fortigate_preserve_existing` | `false` | No | Preserve interface settings on role application |
| `fortigate_wccp_enabled` | `false` | No | WCCP (Web Cache Communication Protocol) |
| `fortigate_explicit_proxy` | `false` | No | Explicit proxy settings |
| `fortigate_device_identification` | `true` | No | Device identification |

## Example Playbook

```yaml
- name: Use fortigate_interfaces
  hosts: all
  gather_facts: false
  roles:
    - role: fortigate_interfaces
```

## License

MIT
