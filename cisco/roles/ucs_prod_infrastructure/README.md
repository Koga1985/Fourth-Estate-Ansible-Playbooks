# ucs_prod_infrastructure

Cisco UCS Production Infrastructure deployment role for Fourth Estate organizations.

## Requirements

- Ansible >= 2.9
- Cisco UCS Python SDK (`pip install ucsmsdk`)
- Cisco UCS Ansible collection (`ansible-galaxy collection install cisco.ucs`)
- Access to UCS Manager with administrative credentials
- Network connectivity to UCS Manager

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ucs_hostname` | `"{{ vault_ucs_hostname }}"` | No | UCS Manager Connection |
| `ucs_username` | `"{{ vault_ucs_username }}"` | No | — |
| `ucs_password` | `"{{ vault_ucs_password }}"` | No | — |
| `ucs_use_ssl` | `true` | No | — |
| `ucs_validate_certs` | `true` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `ucs_artifacts_dir` | `"/tmp/ucs-artifacts"` | No | — |
| `fourth_estate_org_name` | `"FourthEstate"` | No | Fourth Estate Configuration |
| `fourth_estate_description` | `"Fourth Estate Organization - Free Press and Media"` | No | — |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `fourth_estate_phone` | `"{{ vault_fourth_estate_phone }}"` | No | — |
| `fourth_estate_email` | `"{{ vault_fourth_estate_email }}"` | No | — |
| `fourth_estate_address` | `"{{ vault_fourth_estate_address }}"` | No | — |
| `fourth_estate_sub_orgs` | `(see defaults/main.yml)` | No | Sub-organizations |
| `ucs_system_name` | `"UCS-FourthEstate"` | No | UCS System Configuration |
| `ucs_system_description` | `"Fourth Estate UCS Domain"` | No | — |
| `ucs_timezone` | `"America/New_York"` | No | — |
| `ucs_enable_ucsm_config` | `true` | No | Feature Toggles |
| `ucs_enable_org_setup` | `true` | No | — |
| `ucs_enable_service_profiles` | `true` | No | — |
| `ucs_enable_vnic_vhba` | `true` | No | — |
| `ucs_enable_server_pools` | `true` | No | — |
| `ucs_enable_address_pools` | `true` | No | — |
| `ucs_enable_firmware_mgmt` | `true` | No | — |
| `ucs_enable_chassis_discovery` | `true` | No | — |
| `ucs_enable_server_config` | `true` | No | — |
| `ucs_enable_ha` | `true` | No | — |
| `ucs_enable_san` | `true` | No | — |
| `ucs_enable_iscsi` | `false` | No | — |
| `ucs_enable_snmp` | `true` | No | — |
| `ucs_enable_firmware_updates` | `false` | No | — |
| `ucs_auto_associate_servers` | `false` | No | — |
| `ucs_dns_servers` | `(see defaults/main.yml)` | No | DNS Servers |
| `ucs_ntp_servers` | `(see defaults/main.yml)` | No | NTP Servers (DoD approved) |
| `ucs_callhome_enabled` | `true` | No | Call Home Configuration |
| `ucs_snmp_communities` | `(see defaults/main.yml)` | No | SNMP Configuration |
| `ucs_server_pools` | `(see defaults/main.yml)` | No | Server Pools |
| `ucs_server_pool_qualifications` | `[]` | No | Server Pool Qualifications |
| `ucs_power_groups` | `(see defaults/main.yml)` | No | Power Groups |
| `ucs_uuid_pools` | `(see defaults/main.yml)` | No | UUID Pools |
| `ucs_mac_pools` | `(see defaults/main.yml)` | No | MAC Address Pools |
| `ucs_wwnn_pools` | `(see defaults/main.yml)` | No | WWNN Pools |
| `ucs_wwpn_pools_a` | `(see defaults/main.yml)` | No | WWPN Pools (Fabric A) |
| `ucs_wwpn_pools_b` | `(see defaults/main.yml)` | No | WWPN Pools (Fabric B) |
| `ucs_iqn_pools` | `(see defaults/main.yml)` | No | IQN Pools |
| `ucs_service_profile_templates` | `(see defaults/main.yml)` | No | Service Profile Templates |
| `ucs_bios_policies` | `(see defaults/main.yml)` | No | BIOS Policies |
| `ucs_boot_policies` | `(see defaults/main.yml)` | No | Boot Policies |
| `ucs_maintenance_policies` | `(see defaults/main.yml)` | No | Maintenance Policies |
| `ucs_vnic_templates` | `(see defaults/main.yml)` | No | vNIC Templates |
| `ucs_vhba_templates` | `(see defaults/main.yml)` | No | vHBA Templates |
| `ucs_lan_connectivity_policies` | `(see defaults/main.yml)` | No | LAN Connectivity Policies |
| `ucs_san_connectivity_policies` | `(see defaults/main.yml)` | No | SAN Connectivity Policies |
| `ucs_host_firmware_packages` | `(see defaults/main.yml)` | No | Host Firmware Packages |
| `ucs_service_profile_instances` | `[]` | No | Service Profile Instances |
| `ucs_power_policies` | `(see defaults/main.yml)` | No | Power Policies |
| `ucs_disk_group_policies` | `(see defaults/main.yml)` | No | Disk Group Policies |
| `ucs_chassis_link_aggregation` | `"port-channel"` | No | Chassis Discovery |
| `ucs_chassis_num_links` | `"2"` | No | — |
| `ucs_backup_enabled` | `true` | No | High Availability |
| `ucs_backup_type` | `"full-state"` | No | — |
| `ucs_backup_protocol` | `"scp"` | No | — |
| `ucs_backup_path` | `"/backups/ucs/{{ fourth_estate_org_name }}"` | No | — |
| `ucs_backup_server` | `"{{ vault_backup_server }}"` | No | — |
| `ucs_backup_username` | `"{{ vault_backup_username }}"` | No | — |
| `ucs_backup_password` | `"{{ vault_backup_password }}"` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `ucs_enable_fabric_interconnects` | `true` | No | Fabric Interconnect Configuration |
| `fi_cluster_mode` | `"ha"` | No | ha or standalone |
| `fi_a_mgmt_ip` | `"{{ vault_fi_a_mgmt_ip \| default('192.168.1.10') }}"` | No | — |
| `fi_b_mgmt_ip` | `"{{ vault_fi_b_mgmt_ip \| default('192.168.1.11') }}"` | No | — |
| `fi_mgmt_subnet` | `"255.255.255.0"` | No | — |
| `fi_mgmt_gateway` | `"{{ vault_fi_mgmt_gateway \| default('192.168.1.1') }}"` | No | — |
| `fi_a_server_ports` | `(see defaults/main.yml)` | No | Fabric Interconnect A - Server Ports (ports connected to servers) |
| `fi_b_server_ports` | `(see defaults/main.yml)` | No | Fabric Interconnect B - Server Ports |
| `fi_a_uplink_ports` | `(see defaults/main.yml)` | No | Fabric Interconnect A - Uplink Ports (ports connected to network) |
| `fi_b_uplink_ports` | `(see defaults/main.yml)` | No | Fabric Interconnect B - Uplink Ports |
| `fi_a_port_channels` | `(see defaults/main.yml)` | No | Fabric Interconnect A - Port Channels |
| `fi_b_port_channels` | `(see defaults/main.yml)` | No | Fabric Interconnect B - Port Channels |
| `ucs_enable_sp_association` | `true` | No | Service Profile Association Configuration |
| `sp_association_mode` | `"auto"` | No | auto or manual |
| `sp_manual_associations` | `[]` | No | Manual Association (when sp_association_mode is 'manual') |
| `sp_server_pool_name` | `"FourthEstate-Pool"` | No | Auto Association (when sp_association_mode is 'auto') |
| `sp_pool_servers` | `[]` | No | — |
| `sp_templates_for_auto_assoc` | `[]` | No | Service profile templates to enable for auto-association |

## Example Playbook

```yaml
---
- name: Deploy UCS Infrastructure for Fourth Estate
  hosts: localhost
  gather_facts: yes

  vars:
    apply_changes: true
    ucs_hostname: "ucs-manager.example.com"
    fourth_estate_org_name: "NewsOrg"

  roles:
    - role: ucs_prod_infrastructure
```

## Tags

Available tags for selective execution:
- `prerequisites`: Run prerequisite checks only
- `organizations`: Configure organizations only
- `service_profiles`: Configure service profiles only
- `vnic_vhba`: Configure vNIC/vHBA templates only
- `pools`: Configure address pools only
- `policies`: Configure server policies only
- `ha`: Configure high availability only

**Example:**
```bash
# Deploy only organizations and pools
ansible-playbook playbooks/deploy_ucs.yml --tags "organizations,pools"

# Skip service profiles
ansible-playbook playbooks/deploy_ucs.yml --skip-tags "service_profiles"
```

## Description

This role automates the deployment of Cisco UCS infrastructure for production environments with a focus on Fourth Estate (free press and media) organizations. It includes comprehensive configuration management for:

- UCS Manager initial setup
- Organization hierarchy
- Service profile templates
- Network and storage connectivity
- Server pools and policies
- High availability configuration
- DoD STIG and NIST 800-53 compliance

## Dependencies

None

## Usage

### Dry Run (Validation Only)
```bash
ansible-playbook playbooks/deploy_ucs.yml
```

### Apply Changes
```bash
ansible-playbook playbooks/deploy_ucs.yml -e "apply_changes=true"
```

### Specific Tags
```bash
ansible-playbook playbooks/deploy_ucs.yml --tags "organizations,service_profiles"
```

### Infrastructure Only (No Service Profiles)
```bash
ansible-playbook playbooks/deploy_ucs.yml \
  -e "apply_changes=true" \
  -e "ucs_enable_service_profiles=false"
```

### With Custom Organization
```bash
ansible-playbook playbooks/deploy_ucs.yml \
  -e "apply_changes=true" \
  -e "fourth_estate_org_name=CustomOrg"
```

## Infrastructure Architecture

### Fourth Estate UCS Deployment Structure

```
┌─────────────────────────────────────────────────────────────┐
│                   UCS Manager (UCSM)                        │
│             Centralized Management Platform                  │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
            ┌───────▼────────┐  ┌──────▼────────┐
            │  Fabric         │  │  Fabric       │
            │  Interconnect A │  │  Interconnect B│
            │  (Primary)      │  │  (Secondary)  │
            └───────┬─────────┘  └──────┬────────┘
                    │                   │
        ┌───────────┼───────────────────┼──────────┐
        │           │                   │          │
   ┌────▼────┐ ┌───▼────┐         ┌───▼────┐ ┌───▼────┐
   │ Blade   │ │ Blade  │         │ Rack   │ │ Rack   │
   │ Server 1│ │ Server 2│  ...   │ Server 1│ │ Server 2│
   └─────────┘ └────────┘         └────────┘ └────────┘

Organization: FourthEstate
  ├── Sub-Org: Production
  ├── Sub-Org: Development
  └── Sub-Org: Management

Service Profiles → Server Pools → Physical Servers
```

## Infrastructure Components

### Organizations
- **Root Organization**: FourthEstate
- **Sub-Organizations**: Production, Development, Management
- **Purpose**: Logical separation and multi-tenancy
- **Benefits**: Isolation, RBAC, policy inheritance

### Service Profile Templates
- **Updating Templates**: Changes propagate to all instances
- **Initial Templates**: Static configuration, no propagation
- **Use Cases**:
  - Updating: Production workloads (standardization)
  - Initial: Development/test (flexibility)

### Server Pools
- **Purpose**: Grouping servers for assignment
- **Qualification**: Criteria-based server selection
- **Auto-Association**: Automatic service profile binding
- **Manual Association**: Explicit server selection

### Address Pools
- **UUID Pools**: Server identifiers
- **MAC Pools**: Network adapter addresses
- **WWN Pools**: Fibre Channel addresses (WWNN/WWPN)
- **IQN Pools**: iSCSI qualified names

### vNIC/vHBA Templates
- **vNIC**: Virtual network interface cards (Ethernet)
- **vHBA**: Virtual host bus adapters (Fibre Channel)
- **Redundancy**: Fabric A/B for high availability
- **QoS**: Traffic prioritization

## Troubleshooting

### Service Profile Association Failures
- **Check Server Pool**: Verify servers available in pool
- **Review Qualifications**: Ensure server meets criteria
- **Check Policies**: Validate boot policy, power policy
- **View Faults**: Check UCS Manager faults for errors
- **Verify Hardware**: Ensure server is discovered and operational

### Address Pool Exhaustion
- **Expand Pools**: Increase pool size
- **Review Assignments**: Check for duplicate assignments
- **Clean Unused**: Remove decommissioned service profiles
- **Monitor Usage**: Set alerts for pool utilization

### Template Binding Issues
- **Check Template Type**: Verify updating vs initial
- **Review Policies**: Ensure all referenced policies exist
- **Check Hierarchy**: Verify organization inheritance
- **Validate Syntax**: Check for configuration errors

### High Availability Issues
- **Verify Fabric Interconnects**: Both A and B operational
- **Check Uplinks**: Verify uplink connectivity
- **Review Failover**: Test failover mechanisms
- **Monitor Heartbeat**: Check cluster state

## Artifacts Generated

The role creates the following artifacts in `ucs_artifacts_dir`:
- `infrastructure_plan.json`: Complete deployment plan
- `organization_structure.txt`: Organization hierarchy
- `service_profile_templates.txt`: Template configurations
- `address_pools.txt`: Pool allocations (UUID, MAC, WWN, IQN)
- `server_pool_assignments.txt`: Server pool memberships
- `vnic_vhba_templates.txt`: Network/storage template configs
- `deployment_report.txt`: Complete deployment summary
- `deployment_metadata.json`: Deployment tracking information

## Best Practices

### Organization Design
1. **Hierarchical Structure**: Use sub-organizations for separation
2. **Naming Convention**: Consistent, descriptive names
3. **Policy Inheritance**: Leverage parent-child relationships
4. **RBAC Integration**: Align with access control requirements

### Service Profile Strategy
1. **Template-Based**: Always use templates, not individual profiles
2. **Updating Templates**: For production (ensure standardization)
3. **Initial Templates**: For development/test (allow customization)
4. **Versioning**: Document template changes
5. **Testing**: Validate in non-production first

### Server Pool Management
1. **Qualification Criteria**: Use server qualifications for consistency
2. **Pool Sizing**: Right-size pools for workload requirements
3. **Segregation**: Separate blade and rack server pools
4. **Documentation**: Maintain pool assignment records

### Address Pool Planning
1. **Size Appropriately**: Plan for growth (50% headroom)
2. **Non-Overlapping**: Ensure pools don't overlap with physical network
3. **Standardization**: Use consistent address schemes
4. **Monitoring**: Alert on pool utilization thresholds (80%)

### High Availability
1. **Fabric Redundancy**: Always configure both fabrics (A/B)
2. **Uplink Redundancy**: Multiple uplinks per fabric
3. **Power Redundancy**: Dual power supplies
4. **Regular Testing**: Test failover scenarios quarterly

## Deployment Phases

This role supports phased deployment for large environments:

### Phase 1: Core Infrastructure
- UCS Manager initial configuration
- Organization hierarchy
- Server pools

### Phase 2: Networking Foundation
- vNIC templates
- Network policies
- MAC/WWN/IQN pools

### Phase 3: Service Profiles
- Service profile templates
- Boot policies
- Power policies

### Phase 4: Server Association
- Pool qualifications
- Auto-association (if enabled)
- Manual server binding

### Phase 5: Validation
- Service profile status
- Server association verification
- Policy compliance check

## Performance Considerations

- **Template Creation**: ~5-10 seconds per template
- **Service Profile Instantiation**: ~30-60 seconds per profile
- **Server Association**: ~2-5 minutes per server
- **Pool Creation**: ~2-5 seconds per pool
- **Large Deployments**: Consider running in batches

## Integration

### Integration with Other Roles
- **ucs_prod_networking**: Provides VLAN/VSAN configuration
- **ucs_security_hardening**: Applies security policies
- **ucs_prod_monitoring**: Sets up monitoring
- **ucs_prod_backup_dr**: Configures backups

### Workflow Order
```
1. ucs_prod_infrastructure  (this role - foundation)
2. ucs_prod_networking      (network configuration)
3. ucs_security_hardening   (security policies)
4. ucs_prod_monitoring      (monitoring setup)
5. ucs_prod_backup_dr       (backup configuration)
```

## Security Considerations

- Store sensitive credentials in Ansible Vault
- Enable `ucs_validate_certs: true` for production
- Review all configurations before setting `apply_changes: true`
- Follow DoD STIG guidelines for UCS hardening
- Implement NIST 800-53 controls as required
- Use service accounts with least privilege
- Enable audit logging for all configuration changes
- Regular security reviews of service profile templates

## Compliance

This role supports the following compliance frameworks:
- **DoD STIG for Cisco UCS**: Infrastructure security requirements
- **NIST 800-53**: CM-2 (Baseline Configuration), CM-6 (Configuration Settings)
- **NIST 800-171**: Configuration management for CUI
- **FISMA**: System inventory and configuration management

## Common Deployment Scenarios

### Scenario 1: New Greenfield Deployment
```bash
# Full deployment with all features
ansible-playbook playbooks/deploy_ucs.yml \
  -e "apply_changes=true" \
  -e "ucs_enable_ha=true" \
  -e "ucs_enable_san=true"
```

### Scenario 2: Expand Existing Deployment
```bash
# Add new service profiles only
ansible-playbook playbooks/deploy_ucs.yml \
  -e "apply_changes=true" \
  --tags "service_profiles"
```

### Scenario 3: LAN-Only Environment
```bash
# Deploy without SAN connectivity
ansible-playbook playbooks/deploy_ucs.yml \
  -e "apply_changes=true" \
  -e "ucs_enable_san=false"
```

### Scenario 4: Development Environment
```bash
# Minimal deployment for testing
ansible-playbook playbooks/deploy_ucs.yml \
  -e "apply_changes=true" \
  -e "fourth_estate_org_name=Dev" \
  -e "ucs_enable_ha=false"
```

## Author Information

Created for Fourth Estate production deployments.

## License

MIT
