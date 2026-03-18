# aci_network_config

Ansible role for Cisco ACI Network Connectivity configuration - L3Out, L2Out, external EPG, static route, BGP, and OSPF configuration for tenant external connectivity.

## Overview

This role automates the configuration of ACI external network connectivity objects within the Fourth Estate ACI fabric. It supports L3Out and L2Out configurations with associated external EPGs, static routing, and dynamic routing protocols (BGP and OSPF). All tasks default to dry-run (query) mode and must be explicitly enabled for live changes.

**Deployment Phase:** Phase 3 (requires Phase 1 fabric deploy and Phase 2 tenant config to be complete)

## Features

- L3Out configuration with logical node profiles, interface profiles, and routed sub-interfaces
- L2Out bridged external connectivity with external EPGs
- External EPG creation with subnet scope configuration and contract bindings
- Static route configuration with primary and backup next-hops
- BGP peer configuration with MD5 authentication support
- OSPF interface policy and area configuration
- Dry-run mode by default (`apply_changes: false`) - safe for pre-change validation
- JSON artifact generation for all configured objects
- DoD STIG and NIST 800-53 compliant configuration patterns
- Compliance framework tracking

## Requirements

- Ansible >= 2.15
- Collection: `cisco.aci` >= 2.7.0
- Collection: `ansible.utils` >= 2.10.0
- APIC reachability from Ansible control node (TCP/443)
- Vault-encrypted credentials for APIC access and BGP peer passwords

## Role Variables

### APIC Connection Parameters

| Variable | Default | Required | Description |
|---|---|---|
| `aci_host` | `{{ vault_aci_apic_hostname }}` | **Yes** | APIC hostname or IP address |
| `aci_username` | `{{ vault_aci_apic_username }}` | **Yes** | APIC username |
| `aci_password` | `{{ vault_aci_apic_password }}` | **Yes** | APIC password (vault-encrypted) |
| `aci_verify_ssl` | `true` | No | Verify SSL/TLS certificate |
| `aci_use_proxy` | `false` | No | Use HTTP proxy for APIC connections |
| `aci_timeout` | `30` | No | Connection timeout in seconds |
| `aci_port` | `443` | No | APIC HTTPS port |

### Deployment Control

| Variable | Default | Required | Description |
|---|---|---|
| `apply_changes` | `false` | No | Set to `true` to apply changes; `false` for dry-run query mode |
| `artifacts_dir` | `/tmp/aci-artifacts` | No | Directory for JSON configuration artifacts |

### Feature Toggles

| Variable | Default | Required | Description |
|---|---|---|
| `enable_l3out` | `true` | No | Enable L3Out configuration |
| `enable_l2out` | `false` | No | Enable L2Out configuration |
| `enable_external_epgs` | `true` | No | Enable external EPG configuration |
| `enable_static_routes` | `true` | No | Enable static route configuration |
| `enable_bgp_peers` | `true` | No | Enable BGP peer configuration |
| `enable_ospf_peers` | `false` | No | Enable OSPF interface policy configuration |

### L3Out Configuration Structure

The `aci_l3outs` list defines all L3Out objects. Each entry supports:

```yaml
aci_l3outs:
  - name: "L3Out-Core-Routing"        # L3Out name
    tenant: "FourthEstate-Prod"        # Parent tenant
    vrf: "Prod-VRF"                    # Associated VRF
    domain: "L3Dom-External"           # L3 domain
    description: "Core routing L3Out"
    ospf_area: "0.0.0.0"              # OSPF area ID
    ospf_area_type: "regular"          # regular, stub, nssa
    bgp_enabled: true                  # Enable BGP external policy
    ospf_enabled: false                # Enable OSPF external policy
    node_profile: "NodeProfile-Core"   # Logical node profile name
    interface_profile: "IntProfile-Core"  # Logical interface profile name
    nodes:
      - node_dn: "topology/pod-1/node-201"
        router_id: "10.0.0.201"
        loopback: true                 # Use router-id as loopback
    paths:
      - path_dn: "topology/pod-1/paths-201/pathep-[eth1/1]"
        encap: "vlan-100"
        addr: "10.10.100.1/30"
        description: "Uplink to core router"
    bgp_peers:
      - peer_ip: "10.10.100.2"
        remote_asn: 65000
        local_asn: 65100
        password: "{{ vault_aci_bgp_peer_password }}"
        description: "Core router BGP peer"
        path_dn: "topology/pod-1/paths-201/pathep-[eth1/1]"
    external_epgs:
      - name: "ExtEPG-Internet"
        description: "Internet external EPG"
        subnets:
          - prefix: "0.0.0.0/0"
            scope: "import-security"
        provided_contracts: []
        consumed_contracts:
          - "Contract-Internet-Access"
```

### Static Route Structure

```yaml
aci_static_routes:
  - tenant: "FourthEstate-Prod"
    vrf: "Prod-VRF"
    node_dn: "topology/pod-1/node-201"
    l3out_name: "L3Out-Core-Routing"
    node_profile: "NodeProfile-Core"
    prefix: "192.168.100.0/24"
    description: "Static route to remote site A"
    next_hops:
      - next_hop: "10.10.100.2"
        preference: 1
        description: "Primary next hop"
      - next_hop: "10.10.100.6"
        preference: 100
        description: "Backup next hop"
```

### OSPF Interface Policy Structure

```yaml
aci_ospf_interface_policies:
  - name: "OSPF-P2P-Policy"
    tenant: "FourthEstate-Prod"
    network_type: "p2p"       # p2p, bcast
    hello_interval: 10
    dead_interval: 40
    retransmit_interval: 5
    transmit_delay: 1
    priority: 1

aci_ospf_configs:
  - l3out_name: "L3Out-DMZ-Routing"
    tenant: "FourthEstate-DMZ"
    area_id: "0.0.0.0"
    area_type: "regular"
    area_cost: 1
    interface_policy: "OSPF-P2P-Policy"
```

### Compliance Frameworks

```yaml
compliance_frameworks:
  - "dod_stig"
  - "nist_800_53"
  - "nist_800_171"
  - "fisma_moderate"
  - "fisma_high"
```

## Example Playbook

### Dry-Run (Validation Mode - Default)

```yaml
---
- name: ACI Network Configuration - Dry Run
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: false

  roles:
    - role: aci_network_config
```

### Apply Mode (Live Changes)

```yaml
---
- name: ACI Network Configuration - Apply Changes
  hosts: localhost
  gather_facts: true
  vars:
    apply_changes: true
    enable_l3out: true
    enable_external_epgs: true
    enable_static_routes: true
    enable_bgp_peers: true

  roles:
    - role: aci_network_config
```

### Running Specific Components with Tags

```bash
# Run only L3Out configuration
ansible-playbook site.yml --tags "l3out"

# Run only BGP peer configuration
ansible-playbook site.yml --tags "bgp"

# Run validation only
ansible-playbook site.yml --tags "validation"

# Run all Phase 3 tasks
ansible-playbook site.yml --tags "phase3"

# Dry-run check of all network config
ansible-playbook site.yml --tags "phase3" -e "apply_changes=false"
```

## Tags

| Tag | Description |
|---|---|
| `always` | Prerequisites (always runs) |
| `prerequisites` | Prerequisite validation tasks |
| `aci` | All ACI-related tasks |
| `network` | All network configuration tasks |
| `l3out` | L3Out configuration tasks |
| `l2out` | L2Out configuration tasks |
| `external_epgs` | External EPG tasks |
| `routing` | Static route, BGP, and OSPF tasks |
| `bgp` | BGP peer configuration tasks |
| `ospf` | OSPF interface policy tasks |
| `validation` | Validation and verification tasks |
| `phase3` | All Phase 3 deployment tasks |

## Compliance

This role implements network connectivity patterns aligned with:

**DoD STIG (Cisco ACI):**
- CISC-ND-001290: Network time protocol (NTP) configuration
- CISC-ND-000366: Route filtering and prefix-list controls via external EPG subnet scopes

**NIST 800-53 Controls:**
- SC-7: Boundary Protection - L3Out and external EPG isolation
- SC-8: Transmission Confidentiality - BGP MD5 authentication
- AC-4: Information Flow Enforcement - contract-based connectivity control
- SI-3: Malware Protection - endpoint loop protection policies
- AU-12: Audit Record Generation - artifact generation for all changes

## Artifacts Generated

All artifacts are written to `artifacts_dir` (default: `/tmp/aci-artifacts`):

| File | Description |
|---|---|
| `aci_network_config_metadata.json` | Role execution metadata, feature toggles, timestamps |
| `aci_l3out_config.json` | L3Out names, tenants, BGP/OSPF configuration summary |
| `aci_l2out_config.json` | L2Out names and external EPG counts |
| `aci_external_epgs.json` | External EPG configuration summary |
| `aci_static_routes.json` | Static route prefixes and next-hop counts |
| `aci_bgp_peers.json` | BGP-enabled L3Outs and peer IP addresses |
| `aci_ospf_config.json` | OSPF interface policies and area configurations |
| `aci_network_validation_report.json` | Post-deployment validation with fault counts |

## Author

**Fourth Estate Infrastructure Team**
Company: Fourth Estate
License: MIT
Minimum Ansible Version: 2.15
