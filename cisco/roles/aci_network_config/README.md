# aci_network_config

Ansible role for Cisco ACI Network Connectivity configuration - L3Out, L2Out, external EPG, static route, BGP, and OSPF configuration for tenant external connectivity.

## Requirements

- Ansible >= 2.15
- Collection: `cisco.aci` >= 2.7.0
- Collection: `ansible.utils` >= 2.10.0
- APIC reachability from Ansible control node (TCP/443)
- Vault-encrypted credentials for APIC access and BGP peer passwords

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aci_host` | `"{{ vault_aci_apic_hostname }}"` | No | APIC Connection Parameters |
| `aci_username` | `"{{ vault_aci_apic_username }}"` | No | — |
| `aci_password` | `"{{ vault_aci_apic_password }}"` | No | — |
| `aci_verify_ssl` | `true` | No | — |
| `aci_use_proxy` | `false` | No | — |
| `aci_timeout` | `30` | No | — |
| `aci_port` | `443` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `artifacts_dir` | `"/tmp/aci-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Organization |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `fourth_estate_environment` | `"production"` | No | — |
| `fourth_estate_region` | `"primary"` | No | — |
| `enable_l3out` | `true` | No | Feature Toggles |
| `enable_l2out` | `false` | No | — |
| `enable_external_epgs` | `true` | No | — |
| `enable_static_routes` | `true` | No | — |
| `enable_bgp_peers` | `true` | No | — |
| `enable_ospf_peers` | `false` | No | — |
| `aci_l3outs` | `(see defaults/main.yml)` | No | L3Out Configurations |
| `aci_l2outs` | `(see defaults/main.yml)` | No | L2Out Configurations |
| `aci_external_epgs` | `[]` | No | Standalone External EPG Configurations (for external EPGs not defined inline with L3Out) |
| `aci_static_routes` | `(see defaults/main.yml)` | No | Static Route Configurations |
| `aci_ospf_interface_policies` | `(see defaults/main.yml)` | No | OSPF Interface Policy Settings |
| `aci_ospf_configs` | `(see defaults/main.yml)` | No | OSPF Area Configurations (per L3Out requiring OSPF) |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

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

## License

MIT
