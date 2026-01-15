# Fabric Interconnects and Service Profile Association

Comprehensive guide for configuring Fabric Interconnects and associating service profiles with physical servers in Cisco UCS.

## Overview

This guide covers two critical UCS operations:

1. **Fabric Interconnect Configuration** - Configure FI-A and FI-B clustering, ports, and uplinks
2. **Service Profile Association** - Bind service profiles to physical servers in the cluster

## Table of Contents

- [Fabric Interconnect Configuration](#fabric-interconnect-configuration)
  - [Architecture](#fabric-interconnect-architecture)
  - [Configuration Options](#fabric-interconnect-configuration-options)
  - [Usage Examples](#fabric-interconnect-usage)
- [Service Profile Association](#service-profile-association)
  - [Association Modes](#association-modes)
  - [Configuration Options](#association-configuration-options)
  - [Usage Examples](#association-usage)
- [Playbooks](#playbooks)
- [Troubleshooting](#troubleshooting)

---

## Fabric Interconnect Configuration

### Fabric Interconnect Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     UCS Manager (UCSM)                      │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
            ┌───────▼────────┐  ┌──────▼────────┐
            │  Fabric         │  │  Fabric       │
            │  Interconnect A │  │  Interconnect B│
            │  (Primary)      │  │  (Secondary)  │
            │                 │  │                │
            │  Mgmt: .10      │  │  Mgmt: .11    │
            │  Ports: 1-30    │  │  Ports: 1-30  │
            │  Uplinks: 31-32 │  │  Uplinks: 31-32│
            └───────┬─────────┘  └──────┬────────┘
                    │                   │
        Server Ports (1-30)         Server Ports (1-30)
        Uplink Ports (31-32)        Uplink Ports (31-32)
```

### Fabric Interconnect Components

#### Port Types

1. **Server Ports** - Connect to blade servers or I/O modules
   - Typically ports 1-30 (varies by model)
   - Automatically discovered when chassis is connected
   - Configured as unified ports (Ethernet/FCoE)

2. **Uplink Ports** - Connect to upstream network switches
   - Typically ports 31-48 (varies by model)
   - Support Ethernet and Fibre Channel
   - Can be configured as individual ports or port channels

3. **Management Ports** - Out-of-band management
   - Dedicated mgmt0 interface
   - Used for initial configuration and remote access

#### Clustering

- **HA Cluster (Recommended)** - Two FIs in active/active for redundancy
- **Standalone** - Single FI (not recommended for production)

### Fabric Interconnect Configuration Options

Configure via `defaults/main.yml` or playbook variables:

```yaml
# Enable Fabric Interconnect configuration
ucs_enable_fabric_interconnects: true

# Cluster mode: 'ha' or 'standalone'
fi_cluster_mode: "ha"

# Management IP addresses
fi_a_mgmt_ip: "192.168.1.10"
fi_b_mgmt_ip: "192.168.1.11"
fi_mgmt_subnet: "255.255.255.0"
fi_mgmt_gateway: "192.168.1.1"

# Fabric Interconnect A - Server Ports
fi_a_server_ports:
  - name: "server-port-1-1"
    slot: 1
    port: 1
  - name: "server-port-1-2"
    slot: 1
    port: 2

# Fabric Interconnect A - Uplink Ports
fi_a_uplink_ports:
  - slot: 1
    port: 31
    type: "ethernet"
  - slot: 1
    port: 32
    type: "ethernet"

# Fabric Interconnect A - Port Channels
fi_a_port_channels:
  - id: 10
    name: "uplink-pc-a"
    ports:
      - "1/31"
      - "1/32"

# Repeat configuration for Fabric Interconnect B
fi_b_server_ports: [...]
fi_b_uplink_ports: [...]
fi_b_port_channels: [...]
```

### Fabric Interconnect Usage

#### Using the Dedicated Playbook

```bash
# Dry run (validation only)
ansible-playbook cisco/playbooks/40_ucs_fabric_interconnect_config.yml

# Apply configuration
ansible-playbook cisco/playbooks/40_ucs_fabric_interconnect_config.yml \
  -e "apply_changes=true"

# Custom management IPs
ansible-playbook cisco/playbooks/40_ucs_fabric_interconnect_config.yml \
  -e "apply_changes=true" \
  -e "fi_a_mgmt_ip=10.0.1.10" \
  -e "fi_b_mgmt_ip=10.0.1.11" \
  -e "fi_mgmt_gateway=10.0.1.1"
```

#### Using Ansible Role Directly

```yaml
- name: Configure Fabric Interconnects
  hosts: localhost
  roles:
    - role: ucs_prod_infrastructure
      tasks_from: fabric_interconnects
  vars:
    apply_changes: true
    fi_a_mgmt_ip: "192.168.1.10"
    fi_b_mgmt_ip: "192.168.1.11"
```

---

## Service Profile Association

### Association Modes

#### Auto-Association (Recommended)

Service profiles automatically bind to servers from a server pool based on qualifications.

**Advantages:**
- Automatic server assignment
- Consistent server selection criteria
- Faster deployment for multiple servers
- Pool-based management

**Use Cases:**
- Large deployments (10+ servers)
- Dynamic server provisioning
- Template-based deployments

#### Manual Association

Explicitly bind specific service profiles to specific physical servers.

**Advantages:**
- Precise control over server assignment
- Required for specific hardware requirements
- Easier to track specific server assignments

**Use Cases:**
- Small deployments (<10 servers)
- Servers with specific requirements (GPU, storage, etc.)
- Legacy or migration scenarios

### Association Architecture

```
┌────────────────────────────────────────────────────────────┐
│              Service Profile Templates                      │
│  (FourthEstate-Web-Template, FourthEstate-App-Template)   │
└────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
            ┌───────▼────────┐  ┌──────▼────────┐
            │ Auto Association│  │Manual Association│
            │   (Pool-Based) │  │  (Explicit)    │
            └───────┬─────────┘  └──────┬────────┘
                    │                   │
            ┌───────▼────────┐  ┌──────▼────────┐
            │  Server Pool   │  │ Specific Server│
            │  (Qualified)   │  │  (By DN)       │
            └───────┬─────────┘  └──────┬────────┘
                    │                   │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │ Physical Servers  │
                    │  (Blade/Rack)     │
                    └───────────────────┘
```

### Association Configuration Options

```yaml
# Enable service profile association
ucs_enable_sp_association: true

# Association mode: 'auto' or 'manual'
sp_association_mode: "auto"

# Manual Association Configuration
sp_manual_associations:
  - service_profile: "SP-Web-01"
    server_dn: "sys/chassis-1/blade-1"
  - service_profile: "SP-App-01"
    server_dn: "sys/chassis-1/blade-2"
  - service_profile: "SP-DB-01"
    server_dn: "sys/rack-unit-1"

# Auto Association Configuration
sp_server_pool_name: "FourthEstate-Pool"
sp_pool_servers:
  - server_dn: "sys/chassis-1/blade-1"
  - server_dn: "sys/chassis-1/blade-2"
  - server_dn: "sys/chassis-1/blade-3"
  - server_dn: "sys/chassis-1/blade-4"

# Templates to enable for auto-association
sp_templates_for_auto_assoc:
  - "FourthEstate-Web-Template"
  - "FourthEstate-App-Template"
```

### Association Usage

#### Using the Dedicated Playbook

```bash
# Dry run - check server inventory
ansible-playbook cisco/playbooks/41_ucs_service_profile_association.yml

# Auto-association (pool-based)
ansible-playbook cisco/playbooks/41_ucs_service_profile_association.yml \
  -e "apply_changes=true" \
  -e "sp_association_mode=auto"

# Manual association (explicit binding)
ansible-playbook cisco/playbooks/41_ucs_service_profile_association.yml \
  -e "apply_changes=true" \
  -e "sp_association_mode=manual" \
  -e '{"sp_manual_associations": [{"service_profile": "SP-Web-01", "server_dn": "sys/chassis-1/blade-1"}]}'
```

#### Using Ansible Role Directly

```yaml
- name: Associate Service Profiles
  hosts: localhost
  roles:
    - role: ucs_prod_infrastructure
      tasks_from: service_profile_association
  vars:
    apply_changes: true
    sp_association_mode: "auto"
    sp_server_pool_name: "Production-Pool"
```

---

## Playbooks

### 40_ucs_fabric_interconnect_config.yml

**Purpose:** Configure Fabric Interconnects A and B

**Features:**
- Management IP configuration
- Server port configuration
- Uplink port configuration
- Port channel configuration
- Cluster health verification
- Fault detection and reporting

**Usage:**
```bash
ansible-playbook cisco/playbooks/40_ucs_fabric_interconnect_config.yml -e "apply_changes=true"
```

### 41_ucs_service_profile_association.yml

**Purpose:** Associate service profiles with physical servers

**Features:**
- Server inventory discovery
- Service profile status checking
- Manual and auto association support
- Association health monitoring
- Detailed association reporting

**Usage:**
```bash
ansible-playbook cisco/playbooks/41_ucs_service_profile_association.yml -e "apply_changes=true"
```

---

## Complete Deployment Workflow

### Step 1: Configure Fabric Interconnects

```bash
# Configure FI clustering and ports
ansible-playbook cisco/playbooks/40_ucs_fabric_interconnect_config.yml \
  -e "apply_changes=true"
```

### Step 2: Deploy Infrastructure

```bash
# Deploy organizations, service profiles, pools
ansible-playbook cisco/playbooks/02_ucs_phase1_infrastructure.yml \
  -e "apply_changes=true"
```

### Step 3: Associate Service Profiles

```bash
# Bind service profiles to servers
ansible-playbook cisco/playbooks/41_ucs_service_profile_association.yml \
  -e "apply_changes=true" \
  -e "sp_association_mode=auto"
```

### Step 4: Validate

```bash
# Verify all configurations
ansible-playbook cisco/playbooks/10_ucs_validation.yml
```

---

## Troubleshooting

### Fabric Interconnect Issues

#### Cluster Not Forming

**Symptoms:**
- Only one FI visible in UCS Manager
- Cluster status shows "standalone"

**Resolution:**
1. Verify both FIs are powered on
2. Check management network connectivity
3. Verify cluster configuration:
   ```bash
   connect nxos a
   show cluster state
   ```
4. Check HA ports are connected between FIs

#### Port Configuration Fails

**Symptoms:**
- Ports remain in "down" state
- Configuration rejected by UCS Manager

**Resolution:**
1. Verify port is not already in use
2. Check port licensing
3. Verify port type (Ethernet vs FC)
4. Review UCS Manager faults:
   ```bash
   scope fabric-interconnect a
   show fault
   ```

### Service Profile Association Issues

#### Association Fails

**Symptoms:**
- Service profile stuck in "associating" state
- Association state shows "failed"

**Resolution:**
1. Check server discovery status
2. Verify server pool membership
3. Check service profile policies are valid
4. Review association faults:
   ```bash
   scope org FourthEstate
   scope service-profile SP-Name
   show fsm status
   ```

#### Server Not Available

**Symptoms:**
- Server doesn't appear in pool
- Server shows as "unavailable"

**Resolution:**
1. Verify server is discovered:
   ```bash
   show server status
   ```
2. Check server operational state
3. Verify server meets pool qualifications
4. Check for hardware faults on server

#### Association Takes Too Long

**Expected Times:**
- Blade server: 5-10 minutes
- Rack server: 3-5 minutes

**If Longer:**
1. Check for firmware mismatches
2. Review boot policy (PXE can add time)
3. Verify storage controller initialization
4. Check for BIOS POST errors

### Common Server DN Formats

```yaml
# Blade Servers
server_dn: "sys/chassis-1/blade-1"    # Chassis 1, Blade 1
server_dn: "sys/chassis-2/blade-8"    # Chassis 2, Blade 8

# Rack Servers
server_dn: "sys/rack-unit-1"          # Rack server 1
server_dn: "sys/rack-unit-10"         # Rack server 10
```

### Getting Server DNs

Query all available servers:

```bash
ansible-playbook -i localhost, cisco/playbooks/41_ucs_service_profile_association.yml --tags never
```

Or use UCS Manager CLI:

```bash
# Blade servers
show server status

# Rack servers
show server status detail
```

---

## Best Practices

### Fabric Interconnect Configuration

1. **Always configure both FIs** - Never run standalone in production
2. **Use port channels for uplinks** - Redundancy and bandwidth
3. **Document port assignments** - Maintain port maps
4. **Test failover** - Verify HA functionality quarterly
5. **Monitor faults** - Regular health checks

### Service Profile Association

1. **Use auto-association for scale** - Easier to manage 10+ servers
2. **Use manual association for special requirements** - GPU, storage, etc.
3. **Verify before associating** - Check server discovery and health
4. **Monitor association progress** - Can take 5-10 minutes per server
5. **Backup before association** - Always have rollback option
6. **Test in non-production first** - Validate process and timing

### General

1. **Always dry-run first** - Review changes before applying
2. **Review artifacts** - Check generated reports
3. **Monitor during deployment** - Watch UCS Manager for faults
4. **Document changes** - Maintain change records
5. **Test recovery procedures** - Ensure you can rollback

---

## Additional Resources

- **Role README**: `roles/ucs_prod_infrastructure/README.md`
- **Playbooks README**: `playbooks/README.md`
- **Main Documentation**: `README.md`
- **Cisco UCS Documentation**: https://www.cisco.com/c/en/us/support/servers-unified-computing/index.html

---

## Support

For issues or questions:

1. Review troubleshooting section above
2. Check generated artifacts in `/tmp/ucs-*/`
3. Review UCS Manager faults and logs
4. Consult Cisco TAC for hardware issues

## License

MIT

## Author

Created for Fourth Estate Cisco UCS deployments.
