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

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `arista_apply_changes` | `false` | No | — |
| `arista_artifacts_dir` | `"/tmp/arista-artifacts"` | No | — |
| `routing_loopbacks` | `(see defaults/main.yml)` | No | Loopback interfaces |
| `static_routes` | `(see defaults/main.yml)` | No | Static routes |
| `prefix_lists` | `(see defaults/main.yml)` | No | Prefix lists |
| `route_maps` | `(see defaults/main.yml)` | No | Route maps |
| `bgp_config` | `(see defaults/main.yml)` | No | BGP Configuration |
| `bgp_address_families` | `(see defaults/main.yml)` | No | BGP Address Families |
| `bgp_neighbors` | `[]` | No | BGP Neighbors |
| `bgp_peer_groups` | `(see defaults/main.yml)` | No | BGP Peer Groups |
| `bgp_evpn` | `(see defaults/main.yml)` | No | BGP EVPN Configuration |
| `bgp_vrfs` | `[]` | No | BGP VRFs |
| `ospf_config` | `(see defaults/main.yml)` | No | OSPF Configuration |
| `ospf_interfaces` | `[]` | No | OSPF Interfaces |
| `ospf_areas` | `[]` | No | OSPF Areas |
| `isis_config` | `(see defaults/main.yml)` | No | ISIS Configuration |
| `isis_interfaces` | `[]` | No | ISIS Interfaces |
| `bfd_config` | `(see defaults/main.yml)` | No | BFD Configuration |
| `routing_config` | `(see defaults/main.yml)` | No | Routing configuration composite |

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

## License

MIT
