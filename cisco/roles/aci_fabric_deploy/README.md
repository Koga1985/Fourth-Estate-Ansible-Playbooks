# aci_fabric_deploy

## Requirements
- Ansible >= 2.15
- Collections: `cisco.aci >= 2.8.0`, `ansible.utils >= 2.10.0`
- Python packages: `acicobra`, `acimodel`, `requests`
- Network reachability to APIC management interface

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
| `enable_apic_config` | `true` | No | Feature Toggles |
| `enable_node_registration` | `true` | No | — |
| `enable_fabric_policies` | `true` | No | — |
| `enable_access_policies` | `true` | No | — |
| `enable_interface_profiles` | `true` | No | — |
| `enable_vpc_protection` | `true` | No | — |
| `aci_fabric_name` | `"FourthEstate-ACI"` | No | Fabric Global Settings |
| `aci_pod_id` | `1` | No | — |
| `aci_infra_vlan` | `4093` | No | — |
| `aci_multicast_gipo` | `"225.0.0.0/15"` | No | — |
| `aci_ntp_servers` | `(see defaults/main.yml)` | No | NTP Servers (DoD Approved) |
| `aci_dns_servers` | `(see defaults/main.yml)` | No | DNS Servers |
| `aci_dns_search_domains` | `(see defaults/main.yml)` | No | — |
| `aci_nodes` | `(see defaults/main.yml)` | No | Fabric Node Registration |
| `aci_node_discovery_retries` | `10` | No | Node registration wait settings |
| `aci_node_discovery_delay` | `30` | No | — |
| `aci_leaf_switch_profiles` | `(see defaults/main.yml)` | No | Leaf Switch Profiles |
| `aci_spine_switch_profiles` | `(see defaults/main.yml)` | No | Spine Switch Profiles |
| `aci_interface_policy_groups` | `(see defaults/main.yml)` | No | Interface Policy Groups |
| `aci_vpc_protection_groups` | `(see defaults/main.yml)` | No | VPC Protection Groups |
| `aci_vlan_pools` | `(see defaults/main.yml)` | No | VLAN Pools |
| `aci_physical_domains` | `(see defaults/main.yml)` | No | Physical Domains |
| `aci_l3_domains` | `(see defaults/main.yml)` | No | L3 Domains |
| `aci_vmm_domains` | `[]` | No | VMM Domains (empty by default - configure per environment) |
| `aci_syslog_enabled` | `true` | No | Syslog Settings |
| `aci_syslog_server` | `"{{ vault_syslog_server }}"` | No | — |
| `aci_syslog_port` | `514` | No | — |
| `aci_syslog_severity` | `"warnings"` | No | — |
| `aci_syslog_facility` | `"local0"` | No | — |
| `aci_snmp_enabled` | `true` | No | SNMP Settings |
| `aci_snmp_community` | `"{{ vault_aci_snmp_community }}"` | No | — |
| `aci_snmp_location` | `"Fourth Estate Primary Data Center"` | No | — |
| `aci_snmp_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

## Example Playbook
```yaml
---
- name: Phase 1 - ACI Fabric Deployment
  hosts: localhost
  connection: local
  gather_facts: true

  vars:
    apply_changes: false
    artifacts_dir: "/tmp/aci-artifacts"

  roles:
    - role: aci_fabric_deploy
```

To apply changes:
```bash
ansible-playbook -i inventory site.yml -e "apply_changes=true" --ask-vault-pass
```

## Tags
| Tag | Description |
|-----|-------------|
| `always` | Prerequisites and validation (always executes) |
| `prerequisites` | Connectivity checks and variable validation |
| `phase1` | All Phase 1 fabric deployment tasks |
| `aci` | All ACI tasks |
| `apic` | APIC cluster configuration |
| `cluster` | APIC system, NTP, DNS, syslog |
| `fabric` | Fabric node and policy tasks |
| `nodes` | Node registration tasks |
| `registration` | Node discovery and registration |
| `policies` | Fabric and access policy tasks |
| `access` | Access policy tasks (VLAN, domains, AEP) |
| `interface` | Interface profile tasks |
| `profiles` | Switch and interface profile tasks |
| `vpc` | vPC protection group tasks |
| `validation` | Validation and verification tasks |

## Overview
This role automates the initial deployment of a Cisco ACI fabric for Fourth Estate infrastructure, covering APIC cluster configuration, spine and leaf node registration, fabric-wide policies, access policies (VLAN pools, domains, AEP), and interface/switch profiles. It is designed as Phase 1 of the ACI platform deployment pipeline and defaults to dry-run mode to prevent unintended changes.

## Features
- APIC cluster configuration: system name, OOB management, NTP, DNS, and syslog
- Fabric node registration for spine and leaf nodes with discovery wait/retry logic
- Fabric-wide policies: node control (MACsec/analytics), link level, ISIS redistribution, COOP group
- Endpoint security policies: loop protection and rogue endpoint control
- VLAN pool creation with encapsulation block ranges
- Physical domain and L3 domain creation with VLAN pool associations
- Attachable Entity Profile (AEP) configuration with domain bindings
- Leaf and spine switch profile creation with node selectors
- Interface policy group creation (access, port-channel, vPC)
- vPC protection group configuration for dual-homed leaf pairs
- JSON artifact generation for every configuration stage

## Dependencies
None

## Compliance

### DoD STIG Controls
- **Category I (Critical):** vPC protection groups prevent split-brain scenarios; endpoint loop protection prevents network disruption
- **Category II (High):** NTP synchronization with DoD-approved NIST servers; syslog forwarding to centralized logging; CDP/LLDP policy enforcement
- **Category III (Medium):** APIC OOB management IP restriction; DNS server configuration for name resolution integrity; fabric node identity verification via serial number

### NIST 800-53 Controls
- **AU-2, AU-3, AU-12:** Syslog forwarding and fabric audit logging configuration
- **CM-6, CM-7:** Baseline configuration enforcement via fabric policies and interface policy groups
- **IA-3:** Fabric node authentication via serial number registration
- **SC-5:** Endpoint loop protection and rogue endpoint control prevent DoS
- **SC-28:** Configuration artifacts stored with restricted permissions (mode 0640)
- **SI-2, SI-3:** Rogue endpoint control and loop protection for network integrity

## Artifacts Generated
| File | Description |
|------|-------------|
| `aci_fabric_deploy_metadata.json` | Deployment metadata, timestamps, and configuration summary |
| `aci_apic_cluster_config.json` | APIC cluster, NTP, DNS, and syslog configuration record |
| `aci_fabric_nodes.json` | Node registration details and fabric inventory snapshot |
| `aci_fabric_policies.json` | Fabric-wide policy configuration record |
| `aci_access_policies.json` | VLAN pools, domains, AEP, and policy group configuration |
| `aci_interface_profiles.json` | Switch profiles, interface profiles, and vPC groups |
| `aci_fabric_validation_report.json` | Post-deployment validation results and fault summary |

## Author
Fourth Estate Infrastructure Team

## License

MIT
