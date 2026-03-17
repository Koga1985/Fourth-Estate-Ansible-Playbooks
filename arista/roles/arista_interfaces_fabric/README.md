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

All variables are defined in `defaults/main.yml`. Device-specific variables must be set in `host_vars`.

| Variable | Default | Description |
|---|---|---|
| `arista_apply_changes` | `false` | Safety gate. Set to `true` to push configuration; otherwise only a plan artifact is written. |
| `arista_artifacts_dir` | `/tmp/arista-artifacts` | Directory on the Ansible controller for plan and state artifacts. |
| `fabric_vlans` | USERS(10), SERVERS(20), DMZ(30), GUEST(40), VOICE(100), L3VNI transit VLANs 3001/3002 | List of VLAN definitions (`vlan_id`, `name`, `state`) in `arista.eos.eos_vlans` format. |
| `fabric_vrfs` | TENANT_A, TENANT_B | VRF instances with route-distinguisher and import/export route-targets. |
| `mlag_config.enabled` | `false` | Enables MLAG configuration. Must be `true` for any MLAG tasks to run. |
| `mlag_config.domain_id` | `MLAG_DOMAIN_1` | MLAG domain identifier shared between the peer pair. |
| `mlag_config.peer_link` | `Port-Channel1` | Interface used as the MLAG peer-link (configured as a trunk). |
| `mlag_config.peer_vlan` | `4094` | VLAN for MLAG peer communication SVI. |
| `mlag_config.peer_address` | `169.254.255.1` | Peer switch MLAG IP address. |
| `mlag_config.local_peer_ip` | `169.254.255.0` | This switch's MLAG IP address. |
| `vxlan_config.enabled` | `false` | Enables the VXLAN tunnel interface (Vxlan1). |
| `vxlan_config.source_interface` | `Loopback1` | VTEP source loopback interface. |
| `vxlan_config.udp_port` | `4789` | VXLAN UDP encapsulation port. |
| `vxlan_config.anycast_mac` | `00:1c:73:00:dc:01` | Virtual-router MAC for VXLAN anycast gateway. |
| `vxlan_vni_mappings` | VLANs 10/20/30/40/100 → VNIs 10010/10020/10030/10040/10100 | L2VNI-to-VLAN mappings. |
| `vxlan_vrf_mappings` | TENANT_A→13001, TENANT_B→13002 | L3VNI-to-VRF mappings. |
| `fabric_loopbacks` | Loopback0 (router-id), Loopback1 (VTEP) | Loopback interface definitions with IP addresses. |
| `fabric_uplinks` | Ethernet49 (SPINE1), Ethernet50 (SPINE2) | Physical uplink interface definitions (description, MTU). |
| `fabric_uplinks_l3` | Ethernet49, Ethernet50 | L3 IP address assignments for fabric uplinks (uses `fabric_uplink_1_ip`/`fabric_uplink_2_ip`). |
| `fabric_access_ports` | Ethernet1 (VLAN10), Ethernet2 (VLAN20) | Access-mode downlink port definitions. |
| `fabric_trunk_ports` | Ethernet3, Ethernet4 (VLANs 10,20,30,40,100) | Trunk-mode downlink port definitions. |
| `mlag_port_channels` | `[]` | MLAG port-channel definitions (`name`, `description`, `mode`, `vlans`, `mlag_id`). |
| `fabric_svis` | Vlan10–Vlan100 with anycast gateway IPs | SVI definitions with IP address and virtual-router address for anycast gateway. |
| `fabric_spanning_tree.mode` | `mstp` | Spanning-tree mode applied globally. |
| `fabric_spanning_tree.priority` | `16384` | MST instance 0 bridge priority. |
| `fabric_mac_aging_time` | `300` | MAC address-table aging time in seconds. |

### Required host_vars

| Variable | Description |
|---|---|
| `fabric_router_id` | Unique /32 loopback IP used as BGP/OSPF router ID (e.g. `10.255.255.1`). |
| `fabric_vtep_ip` | Unique /32 loopback IP used as the VXLAN VTEP source (e.g. `10.255.254.1`). |
| `fabric_uplink_1_ip` | /31 IP for the first fabric uplink point-to-point link. |
| `fabric_uplink_2_ip` | /31 IP for the second fabric uplink point-to-point link. |

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
