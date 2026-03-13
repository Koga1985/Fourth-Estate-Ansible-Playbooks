# aci_tenant_config

## Overview
This role automates Cisco ACI tenant configuration for Fourth Estate infrastructure, including tenant creation, VRF provisioning, bridge domain and subnet definition, application profile and EPG setup, filter and contract configuration, and optional static path bindings. It is designed as Phase 2 of the ACI platform deployment pipeline and defaults to dry-run mode to prevent unintended changes.

## Features
- Tenant creation for production, development, management, and DMZ security domains
- VRF provisioning per tenant with configurable policy enforcement and preferred group settings
- Bridge domain creation with unicast routing, ARP flooding, and L2/L3 flooding controls
- Bridge domain subnet (gateway IP) configuration with public/private scope
- Application profile creation per tenant
- Endpoint group (EPG) creation with bridge domain association and intra-EPG isolation
- EPG-to-contract binding for provider and consumer roles
- Filter and filter entry creation with protocol, port, and stateful options
- Contract and contract subject creation with filter bindings and directional scope
- Optional static path bindings to physical ports, port-channels, and vPC interfaces
- JSON artifact generation for every configuration stage

## Requirements
- Ansible >= 2.15
- Collections: `cisco.aci >= 2.8.0`, `ansible.utils >= 2.10.0`
- Python packages: `acicobra`, `acimodel`, `requests`
- Network reachability to APIC management interface
- `aci_fabric_deploy` role should be run first (Phase 1)

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
`apply_changes: false` — The role defaults to **dry-run mode**. No configuration changes are written to the APIC unless `apply_changes: true` is explicitly passed. In dry-run mode all tasks execute `state: query` instead of `state: present`.

### Feature Toggles
| Variable | Default | Description |
|----------|---------|-------------|
| `enable_tenants` | `true` | Create/manage tenants |
| `enable_vrfs` | `true` | Configure VRFs |
| `enable_bridge_domains` | `true` | Configure bridge domains and subnets |
| `enable_app_profiles` | `true` | Configure application profiles |
| `enable_epgs` | `true` | Configure EPGs and contract bindings |
| `enable_filters` | `true` | Configure filters and filter entries |
| `enable_contracts` | `true` | Configure contracts and subjects |
| `enable_static_paths` | `false` | Configure static path bindings (disabled by default) |

### Fabric Configuration
Key variables and their structures:

**Tenants (`aci_tenants`):**
```yaml
aci_tenants:
  - name: "FourthEstate-Prod"
    description: "Production Tenant"
    security_domain: "all"
    enabled: true
```

**VRFs (`aci_vrfs`):**
```yaml
aci_vrfs:
  - name: "Prod-VRF"
    tenant: "FourthEstate-Prod"
    policy_control_preference: enforced
    policy_control_direction: ingress
    preferred_group: false
```

**Bridge Domains (`aci_bridge_domains`):**
```yaml
aci_bridge_domains:
  - name: "Prod-App-BD"
    tenant: "FourthEstate-Prod"
    vrf: "Prod-VRF"
    gateway_ip: "10.10.10.1/24"
    scope: "private"
    unicast_routing: true
    arp_flooding: false
```

**EPGs (`aci_epgs`):**
```yaml
aci_epgs:
  - name: "Web-EPG"
    app_profile: "Prod-App"
    tenant: "FourthEstate-Prod"
    bridge_domain: "Prod-App-BD"
    preferred_group: false
    intra_epg_isolation: "unenforced"
```

### Node Registration
Not applicable to this role. See `aci_fabric_deploy` for node registration.

## Dependencies
None

## Example Playbook
```yaml
---
- name: Phase 2 - ACI Tenant Configuration
  hosts: localhost
  connection: local
  gather_facts: true

  vars:
    apply_changes: false
    artifacts_dir: "/tmp/aci-artifacts"

  roles:
    - role: aci_tenant_config
```

To apply changes:
```bash
ansible-playbook -i inventory site.yml -e "apply_changes=true" --ask-vault-pass
```

To configure only tenants and VRFs:
```bash
ansible-playbook -i inventory site.yml --tags "tenants,vrfs" --ask-vault-pass
```

## Tags
| Tag | Description |
|-----|-------------|
| `always` | Prerequisites and validation (always executes) |
| `prerequisites` | Connectivity checks and variable validation |
| `phase2` | All Phase 2 tenant configuration tasks |
| `aci` | All ACI tasks |
| `tenants` | Tenant creation tasks |
| `vrfs` | VRF configuration tasks |
| `bridge_domains` | Bridge domain and subnet tasks |
| `subnets` | Bridge domain subnet tasks |
| `app_profiles` | Application profile tasks |
| `epgs` | EPG creation and contract binding tasks |
| `filters` | Filter and filter entry tasks |
| `contracts` | Contract and subject tasks |
| `static_paths` | Static path binding tasks |
| `validation` | Validation and verification tasks |

## Compliance

### DoD STIG Controls
- **Category I (Critical):** Contract enforcement between EPGs prevents unauthorized lateral movement; VRF policy enforcement mode set to `enforced` by default
- **Category II (High):** Intra-EPG isolation for sensitive EPGs (e.g., database tier); bridge domain limit-IP-learn prevents IP spoofing; tenant-scoped contracts limit blast radius
- **Category III (Medium):** Descriptive tenant and EPG naming for audit traceability; artifact logging of all configuration changes with timestamps and compliance framework references

### NIST 800-53 Controls
- **AC-3, AC-4:** Contract and filter enforcement implements mandatory access controls between application tiers
- **AU-2, AU-12:** Configuration artifacts capture all tenant changes with ISO8601 timestamps for audit trails
- **CM-6, CM-7:** Baseline tenant configurations enforce least-privilege network access via contracts
- **SC-7:** EPG segmentation implements boundary protection between security zones (Prod, Dev, Mgmt, DMZ)
- **SC-28:** Artifacts stored with restricted file permissions (mode 0640)
- **SI-3, SI-4:** Intra-EPG isolation and contract enforcement support threat containment

## Artifacts Generated
| File | Description |
|------|-------------|
| `aci_tenant_config_metadata.json` | Deployment metadata, timestamps, and configuration summary |
| `aci_tenants.json` | Tenant creation details and query results |
| `aci_vrfs.json` | VRF configuration record per tenant |
| `aci_bridge_domains.json` | Bridge domain and subnet configuration record |
| `aci_app_profiles.json` | Application profile configuration record |
| `aci_epgs.json` | EPG configuration and contract binding record |
| `aci_filters.json` | Filter and filter entry configuration record |
| `aci_contracts.json` | Contract, subject, and filter binding record |
| `aci_static_paths.json` | Static path binding configuration record |
| `aci_tenant_validation_report.json` | Post-deployment validation results and fault summary |

## Author
Fourth Estate Infrastructure Team
