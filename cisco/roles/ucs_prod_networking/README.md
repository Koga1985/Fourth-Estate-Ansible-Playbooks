# ucs_prod_networking

Cisco UCS production networking configuration role for Fourth Estate deployments.

## Description

This role configures comprehensive networking for Cisco UCS production environments including VLANs, VSANs, QoS policies, network control policies, and multicast policies. It provides network segmentation, SAN connectivity, and quality of service management for fourth estate organizations.

## Features

- **VLAN Management**: Network segmentation for management, production, development, and DMZ
- **VSAN Configuration**: Fibre Channel over Ethernet (FCoE) for SAN connectivity
- **QoS Policies**: Traffic prioritization (Platinum, Gold, Best-Effort)
- **Network Control**: CDP and LLDP discovery protocol management
- **Multicast Policies**: IGMP snooping and querier configuration
- **Uplink Port Channels**: Redundant uplink connectivity
- **Network Security**: Network isolation and traffic control

## Requirements

- Ansible >= 2.9
- Cisco UCS Python SDK (`pip install ucsmsdk`)
- Cisco UCS Ansible collection (`ansible-galaxy collection install cisco.ucs`)
- Administrative access to UCS Manager
- Network connectivity to UCS fabric interconnects

## Role Variables

### Connection Variables (Required)
```yaml
ucs_hostname: "ucs-manager.example.com"
ucs_username: "admin"
ucs_password: "secure_password"
```

### Deployment Control
```yaml
apply_changes: false                    # Set to true to apply changes
ucs_artifacts_dir: "/tmp/ucs-artifacts" # Artifacts output directory
ucs_enable_san: true                    # Enable SAN/VSAN configuration
```

### VLAN Configuration
```yaml
ucs_vlans:
  - name: "Management-VLAN"
    id: 100
    fabric: "common"                    # Options: common, A, B
  - name: "Production-VLAN"
    id: 200
    fabric: "common"
  - name: "Development-VLAN"
    id: 300
    fabric: "common"
  - name: "DMZ-VLAN"
    id: 400
    fabric: "common"
```

**VLAN Best Practices:**
- Management: VLAN 100 (isolated management traffic)
- Production: VLAN 200 (production workloads)
- Development: VLAN 300 (development/test environments)
- DMZ: VLAN 400 (external-facing services)

### VSAN Configuration
```yaml
ucs_vsans:
  - name: "VSAN-A"
    id: 100
    fabric: "A"                         # Fabric A
    fcoe_vlan_id: 1000                  # FCoE VLAN for Fabric A
  - name: "VSAN-B"
    id: 200
    fabric: "B"                         # Fabric B
    fcoe_vlan_id: 2000                  # FCoE VLAN for Fabric B
```

**VSAN Best Practices:**
- Use separate VSANs for each fabric (A/B)
- FCoE VLAN IDs should be in dedicated range (1000+)
- Maintain redundant paths for high availability

### QoS Policies
```yaml
ucs_qos_policies:
  - name: "QoS-Platinum"
    priority: "platinum"                # Highest priority
    rate: "line-rate"
  - name: "QoS-Gold"
    priority: "gold"                    # Medium-high priority
    rate: "line-rate"
  - name: "QoS-Best-Effort"
    priority: "best-effort"             # Default priority
    rate: "line-rate"
```

**QoS Priority Levels:**
- **Platinum**: Critical applications (databases, real-time systems)
- **Gold**: Business-critical applications
- **Best-Effort**: General purpose traffic

### Network Control Policies
```yaml
ucs_network_control_policies:
  - name: "NetCtrl-CDP-LLDP"
    cdp: "enabled"                      # Cisco Discovery Protocol
    lldp_transmit: "enabled"            # Link Layer Discovery Protocol
    lldp_receive: "enabled"
```

### Multicast Policies
```yaml
ucs_multicast_policies:
  - name: "Multicast-Policy"
    querier_state: "disabled"           # IGMP querier
    snooping_state: "enabled"           # IGMP snooping
```

See `defaults/main.yml` for complete variable documentation.

## Dependencies

None

## Example Playbook

### Basic Networking Deployment
```yaml
---
- name: Configure UCS Networking
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    ucs_hostname: "ucs-manager.example.com"
    ucs_enable_san: true

  roles:
    - role: ucs_prod_networking
```

### LAN-Only Configuration (No SAN)
```yaml
---
- name: Configure UCS LAN Networking Only
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    ucs_enable_san: false               # Disable SAN/VSAN configuration

  roles:
    - role: ucs_prod_networking
```

### Custom VLAN Configuration
```yaml
---
- name: Configure Custom VLANs
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    ucs_vlans:
      - name: "Custom-VLAN-1"
        id: 500
        fabric: "common"
      - name: "Custom-VLAN-2"
        id: 600
        fabric: "A"

  roles:
    - role: ucs_prod_networking
```

## Usage

### Dry Run (Validation Only)
```bash
ansible-playbook playbooks/deploy_networking.yml
```

### Apply Changes
```bash
ansible-playbook playbooks/deploy_networking.yml -e "apply_changes=true"
```

### LAN-Only Deployment
```bash
ansible-playbook playbooks/deploy_networking.yml -e "apply_changes=true ucs_enable_san=false"
```

## Network Architecture

### Fourth Estate Network Segments

```
┌─────────────────────────────────────────────────────────────┐
│                     UCS Fabric Interconnects                │
│                         (Redundant A/B)                     │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼────┐          ┌────▼────┐          ┌────▼────┐
   │ VLAN 100│          │ VLAN 200│          │ VLAN 300│
   │Management│          │Production│         │  Dev    │
   └─────────┘          └─────────┘          └─────────┘

   ┌────────────────────┐          ┌────────────────────┐
   │   VSAN 100 (A)    │          │   VSAN 200 (B)    │
   │   FCoE VLAN 1000  │          │   FCoE VLAN 2000  │
   └────────────────────┘          └────────────────────┘
```

## Network Security Considerations

### VLAN Isolation
- Separate management traffic from production workloads
- Isolate development/test from production
- DMZ for external-facing services

### SAN Security
- Dedicated VSANs for storage traffic
- Separate FCoE VLANs to prevent cross-fabric traffic
- VSAN zoning for access control

### Discovery Protocols
- Enable CDP for Cisco device discovery
- Enable LLDP for multi-vendor environments
- Disable on untrusted ports

## Compliance

This role supports network security requirements from:
- **NIST 800-53**: SC-7 (Boundary Protection), SC-8 (Transmission Confidentiality)
- **DoD STIG**: Network segmentation requirements
- **NIST 800-171**: Network isolation for CUI

## Troubleshooting

### VLAN Not Appearing
- Verify VLAN ID is not already in use
- Check fabric assignment (common vs A/B)
- Review UCS Manager faults

### VSAN Issues
- Verify FCoE VLAN IDs don't overlap with standard VLANs
- Check fabric connectivity
- Ensure SAN boot policies reference correct VSAN

### QoS Not Applied
- Verify QoS policy is assigned to vNIC templates
- Check service profile association
- Review network adapter policies

## Artifacts Generated

The role creates the following artifacts in `ucs_artifacts_dir`:
- `networking_plan.json`: Planned networking configuration
- `vlan_configuration.txt`: VLAN deployment details
- `vsan_configuration.txt`: VSAN deployment details (if enabled)
- `qos_policies.txt`: QoS policy configuration
- `networking_report.txt`: Complete deployment report

## Tags

Available tags for selective execution:
- `vlans`: Configure VLANs only
- `vsans`: Configure VSANs only
- `qos`: Configure QoS policies only
- `network_control`: Configure network control policies only
- `multicast`: Configure multicast policies only

**Example:**
```bash
ansible-playbook playbooks/deploy_networking.yml --tags vlans,qos
```

## Security Considerations

- Store UCS credentials in Ansible Vault
- Review VLAN assignments before applying changes
- Test in non-production environment first
- Document all network changes
- Maintain network diagrams

## License

MIT

## Author Information

Created for Fourth Estate production networking deployments.
