# arista_interfaces_fabric

Configures the full data-plane fabric on Arista EOS devices: VLANs, VRFs, MLAG peer-link and port-channels, VXLAN tunnel interface with L2VNI and L3VNI mappings, loopback interfaces, fabric uplinks (physical and L3 addressing), access/trunk downlink ports, SVI anycast gateways, spanning-tree mode and priority, and MAC address-table aging. The role is the primary tool for building and maintaining VXLAN/EVPN leaf-spine fabrics with optional MLAG redundancy.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- EOS user with `network-admin` privilege
- `ansible_network_os: eos` and `ansible_connection: network_cli` (or `httpapi`) set for target hosts
- Per-device variables `fabric_router_id`, `fabric_vtep_ip`, `fabric_uplink_1_ip`, and `fabric_uplink_2_ip` must be defined in `host_vars`

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `arista_apply_changes` | `false` | No | Control whether changes are applied or just planned |
| `arista_artifacts_dir` | `"/tmp/arista-artifacts"` | No | Artifacts directory |
| `fabric_vlans` | `(see defaults/main.yml)` | No | VLAN Configuration |
| `fabric_vrfs` | `(see defaults/main.yml)` | No | VRF Configuration for multi-tenancy |
| `mlag_config` | `(see defaults/main.yml)` | No | MLAG Configuration |
| `vxlan_config` | `(see defaults/main.yml)` | No | VXLAN Configuration |
| `vxlan_vni_mappings` | `(see defaults/main.yml)` | No | VXLAN VNI to VLAN Mappings (L2VNI) |
| `vxlan_vrf_mappings` | `(see defaults/main.yml)` | No | VXLAN VRF to VNI Mappings (L3VNI) |
| `fabric_loopbacks` | `(see defaults/main.yml)` | No | Loopback Interfaces |
| `fabric_uplinks` | `(see defaults/main.yml)` | No | Fabric uplink interfaces (to spines) - Physical attributes |
| `fabric_uplinks_l3` | `(see defaults/main.yml)` | No | Fabric uplink L3 configuration |
| `fabric_access_ports` | `(see defaults/main.yml)` | No | Access ports configuration |
| `fabric_trunk_ports` | `(see defaults/main.yml)` | No | Trunk ports configuration |
| `mlag_port_channels` | `[]` | No | MLAG port-channels |
| `fabric_svis` | `(see defaults/main.yml)` | No | SVIs for VXLAN anycast gateway |
| `fabric_spanning_tree` | `(see defaults/main.yml)` | No | Spanning Tree Configuration |
| `fabric_mac_aging_time` | `300` | No | MAC address-table aging time (seconds) |
| `fabric_config` | `(see defaults/main.yml)` | No | Fabric configuration composite |

## Example Playbook

```yaml
- name: Configure VXLAN/EVPN leaf fabric
  hosts: arista_leafs
  gather_facts: false
  roles:
    - role: arista_interfaces_fabric
      vars:
        arista_apply_changes: true
        vxlan_config:
          enabled: true
          source_interface: Loopback1
          udp_port: 4789
          anycast_mac: "00:1c:73:00:dc:01"
        mlag_config:
          enabled: true
          domain_id: MLAG_DOMAIN_1
          peer_link: Port-Channel1
          peer_vlan: 4094
          peer_address: "169.254.255.1"
          local_peer_ip: "169.254.255.0"
```

## Notes and Dependencies

- `arista_apply_changes` defaults to `false`. A JSON fabric plan (`<hostname>_fabric_plan.json`) is always written regardless of this setting.
- When changes are applied, a post-run state artifact (`<hostname>_fabric_state.json`) captures output from `show vlan`, `show mlag`, `show vxlan vtep`, `show vxlan vni`, and `show bgp evpn summary`.
- VXLAN and MLAG are both disabled by default (`enabled: false`). Enable each feature explicitly in `group_vars` or `host_vars`.
- Spanning-tree is automatically disabled on the VXLAN interface (`no spanning-tree vlan-id 1-4094`) when VXLAN is enabled.
- This role configures the data-plane fabric. Routing protocols (BGP EVPN underlay/overlay) are configured by the `arista_routing_baseline` role.
- The handler `save eos configuration` is notified by all configuration tasks and saves the running configuration to startup at play completion.

## License

MIT
