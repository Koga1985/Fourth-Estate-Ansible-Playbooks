# aci_fabric_deploy

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

## Requirements
- Ansible >= 2.15
- Collections: `cisco.aci >= 2.8.0`, `ansible.utils >= 2.10.0`
- Python packages: `acicobra`, `acimodel`, `requests`
- Network reachability to APIC management interface

## Role Variables

### Connection Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `aci_host` | `{{ vault_aci_apic_hostname }}` | APIC hostname or IP address |
| `aci_username` | `{{ vault_aci_apic_username }}` | APIC admin username |
| `aci_password` | `{{ vault_aci_apic_password }}` | APIC admin password (vault-encrypted) |
| `aci_verify_ssl` | `true` | Validate APIC TLS certificate |
| `aci_timeout` | `30` | APIC API request timeout (seconds) |

### Deployment Control
`apply_changes: false` — The role defaults to **dry-run mode**. No configuration changes are written to the APIC unless `apply_changes: true` is explicitly passed. In dry-run mode, all tasks execute `state: query` instead of `state: present`.

### Fabric Configuration
| Variable | Default | Description |
|----------|---------|-------------|
| `aci_fabric_name` | `FourthEstate-ACI` | Fabric instance name |
| `aci_pod_id` | `1` | Default pod ID |
| `aci_infra_vlan` | `4093` | Infrastructure VLAN ID |
| `aci_multicast_gipo` | `225.0.0.0/15` | Multicast GIPo address range |
| `aci_ntp_servers` | NIST servers | List of NTP server objects |
| `aci_dns_servers` | 8.8.8.8, 8.8.4.4 | List of DNS server objects |

### Feature Toggles
| Variable | Default | Description |
|----------|---------|-------------|
| `enable_apic_config` | `true` | Configure APIC system settings |
| `enable_node_registration` | `true` | Register fabric nodes |
| `enable_fabric_policies` | `true` | Configure fabric-wide policies |
| `enable_access_policies` | `true` | Configure VLAN pools, domains, AEP |
| `enable_interface_profiles` | `true` | Configure switch and interface profiles |
| `enable_vpc_protection` | `true` | Configure vPC protection groups |

### Node Registration
`aci_nodes` is a list of node objects. Each entry must include:
```yaml
aci_nodes:
  - node_id: 101          # ACI node ID (101-4000)
    name: "spine-101"     # Node hostname in fabric
    role: "spine"         # spine or leaf
    pod_id: 1             # Pod ID (default: aci_pod_id)
    serial: "TEP-1-101"   # Serial number for auto-discovery
    description: "..."    # Optional description
```

## Dependencies
None

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
