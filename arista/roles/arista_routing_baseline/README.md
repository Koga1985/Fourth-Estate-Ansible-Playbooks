# arista_routing_baseline

Configures the routing stack on Arista EOS devices: loopback interfaces, static routes, prefix lists, route maps, BGP (global settings, address families, neighbors, peer groups, EVPN overlay, and per-VRF instances), OSPFv2, IS-IS, and Bidirectional Forwarding Detection (BFD). The role is designed to work alongside `arista_interfaces_fabric` to provide the complete underlay and EVPN overlay for VXLAN leaf-spine fabrics.

## Requirements

- Ansible 2.12 or later
- `arista.eos` collection (`ansible-galaxy collection install arista.eos`)
- Network connectivity to Arista EOS devices
- EOS user with `network-admin` privilege
- `ansible_network_os: eos` and `ansible_connection: network_cli` (or `httpapi`) set for target hosts
- `fabric_router_id` must be defined per device (in `host_vars` or passed as an extra variable)

## Role Variables

All variables are defined in `defaults/main.yml`.

| Variable | Default | Required | Description |
|---|---|---|
| `arista_apply_changes` | `false` | No | Safety gate. Set to `true` to push configuration; otherwise only a plan artifact is written. |
| `arista_artifacts_dir` | `/tmp/arista-artifacts` | No | Directory on the Ansible controller for plan and state artifacts. |
| `routing_loopbacks` | Loopback0 with `fabric_router_id`/32 | No | Loopback interfaces used as router IDs. |
| `static_routes` | Default route `0.0.0.0/0` via `10.0.0.1` (AD 250) | No | Static route definitions in `arista.eos.eos_static_routes` format. |
| `prefix_lists` | `DEFAULT_ONLY`, `LOOPBACKS` | No | IPv4 prefix-list definitions (`name`, `afi`, `entries`). |
| `route_maps` | `RM_CONNECTED_TO_BGP` (permits LOOPBACKS) | No | Route-map definitions (`name`, `entries`). |
| `bgp_config.enabled` | `true` | No | Enables BGP configuration. |
| `bgp_config.asn` | `65000` | No | BGP autonomous system number. |
| `bgp_config.router_id` | `fabric_router_id` | No | BGP router ID. |
| `bgp_config.max_paths` | `4` | No | Maximum ECMP paths for BGP. |
| `bgp_config.max_paths_ibgp` | `4` | No | Maximum iBGP ECMP paths. |
| `bgp_address_families` | IPv4 (redistribute connected via RM_CONNECTED_TO_BGP), EVPN | No | BGP address-family configurations. |
| `bgp_neighbors` | `[]` | No | Individual BGP neighbor definitions (`neighbor`, `remote_as`, `description`, `update_source`, etc.). |
| `bgp_peer_groups` | `SPINE_UNDERLAY`, `SPINE_OVERLAY` | No | BGP peer-group definitions for spine peerings. |
| `bgp_evpn.enabled` | `true` | No | Enables the BGP EVPN address family for VXLAN overlay. |
| `bgp_evpn.peer_group` | `SPINE_OVERLAY` | No | Peer group activated in the EVPN address family. |
| `bgp_vrfs` | `[]` | No | Per-VRF BGP instances with RD and route-targets for L3VNI. |
| `ospf_config.enabled` | `false` | No | Enables OSPFv2 configuration. |
| `ospf_config.process_id` | `1` | No | OSPF process ID. |
| `ospf_config.passive_default` | `true` | No | Makes all interfaces passive by default (active interfaces must be explicitly enabled). |
| `ospf_interfaces` | `[]` | No | Per-interface OSPF settings (area, cost, network type). |
| `ospf_areas` | `[]` | No | OSPF area definitions (type, authentication). |
| `isis_config.enabled` | `false` | No | Enables IS-IS configuration. |
| `isis_config.instance` | `CORE` | No | IS-IS instance name. |
| `isis_config.is_type` | `level-2` | No | IS-IS level (level-1, level-2, or level-1-2). |
| `isis_config.auth_mode` | `md5` | No | IS-IS authentication mode. |
| `isis_interfaces` | `[]` | No | Per-interface IS-IS settings (circuit-type, network type, metric). |
| `bfd_config.enabled` | `true` | No | Enables BFD globally for fast failure detection. |
| `bfd_config.interval` | `300` | No | BFD transmit interval in milliseconds. |
| `bfd_config.min_rx` | `300` | No | BFD minimum receive interval in milliseconds. |
| `bfd_config.multiplier` | `3` | No | BFD detection multiplier. |

## Example Playbook

### BGP EVPN underlay and overlay (typical leaf)

```yaml
- name: Configure BGP EVPN routing
  hosts: arista_leafs
  gather_facts: false
  roles:
    - role: arista_routing_baseline
      vars:
        arista_apply_changes: true
        bgp_config:
          enabled: true
          asn: "65001"
          router_id: "{{ fabric_router_id }}"
          max_paths: 4
          max_paths_ibgp: 4
        bgp_neighbors:
          - neighbor: "10.1.1.0"
            remote_as: "65000"
            description: "SPINE1_UNDERLAY"
            update_source: "Loopback0"
            send_community: "extended"
          - neighbor: "10.1.1.2"
            remote_as: "65000"
            description: "SPINE2_UNDERLAY"
            update_source: "Loopback0"
            send_community: "extended"
        bgp_evpn:
          enabled: true
          peer_group: "SPINE_OVERLAY"
        bgp_vrfs:
          - name: "TENANT_A"
            rd: "{{ fabric_router_id }}:3001"
            rt_import: ["65000:3001"]
            rt_export: ["65000:3001"]
```

### Adding OSPF to the fabric underlay

```yaml
- name: Configure OSPF underlay
  hosts: arista_switches
  gather_facts: false
  roles:
    - role: arista_routing_baseline
      vars:
        arista_apply_changes: true
        bgp_config:
          enabled: false
        ospf_config:
          enabled: true
          process_id: 1
          router_id: "{{ fabric_router_id }}"
          passive_default: true
        ospf_interfaces:
          - name: "Ethernet49"
            address_family:
              - afi: "ipv4"
                area:
                  area_id: "0.0.0.0"
                network: "point-to-point"
```

## Notes and Dependencies

- `arista_apply_changes` defaults to `false`. A JSON routing plan (`<hostname>_routing_plan.json`) is always written. A post-run state artifact (`<hostname>_routing_state.json`) is written when changes are applied, capturing route summary, BGP summary, EVPN summary, OSPF neighbors, and IS-IS neighbors.
- Only one of BGP, OSPF, or IS-IS needs to be enabled; the others default to `disabled` and can be left unconfigured.
- `fabric_router_id` is used as the default value for BGP and OSPF router IDs and must be a unique /32 per device. Define it in `host_vars`.
- BGP EVPN (`bgp_evpn.enabled: true`) requires that the VXLAN interface be configured, which is handled by the `arista_interfaces_fabric` role. Both roles should be applied together for a complete fabric deployment.
- The handler `save eos configuration` is notified by all configuration tasks and writes the running configuration to startup at play completion.
