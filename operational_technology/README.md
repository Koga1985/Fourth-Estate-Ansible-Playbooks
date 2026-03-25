# Operational Technology (OT/ICS) Security

This directory contains **24 Ansible roles** for securing **Operational Technology (OT)** and **Industrial Control Systems (ICS)** with emphasis on **NIST 800-82**, **ISA/IEC 62443**, and **DoD STIG** compliance for Fourth Estate critical infrastructure.

## Overview

Comprehensive OT/ICS security automation covering network segmentation, firewall management, intrusion detection/prevention, secure remote access, firmware management, and compliance monitoring.

## 📋 Role Categories

### Zone & Topology (3 roles)
- **ot_zone_model** - Purdue model zone definition and segmentation
- **ot_topology_baseline** - Network topology baselining and change detection
- **ot_inventory_model** - OT asset inventory and CMDB synchronization

### Asset Management (3 roles)
- **ot_asset_lifecycle** - OT asset lifecycle and classification
- **ot_firmware_register** - Firmware version tracking and registration
- **ot_windows_hmi_patching** - Windows HMI and workstation patching

### Firewall & Network (5 roles)
- **ot_firewall_backup** - OT firewall configuration backup
- **ot_firewall_policy_checkpoint** - Check Point firewall policy management
- **ot_firewall_policy_panos** - Palo Alto PAN-OS firewall policy management
- **ot_network_backup** - Network device configuration backup
- **ot_nac_visibility** - NAC/network access control visibility

### Security Monitoring (4 roles)
- **ot_sensor_ops** - OT sensor deployment and health monitoring
- **ot_idps_baseline** - IDS/IPS baseline configuration
- **ot_allowlist_assist** - Protocol and traffic allowlist management
- **ot_remote_access_bastion** - Secure remote access bastion

### Communications & Trust (3 roles)
- **ot_pki_trust** - PKI certificate trust management
- **ot_timesync_baseline** - Time synchronization baseline (NTP/PTP)
- **ot_logging_pipeline** - Security log pipeline configuration

### SCADA & ICS (2 roles)
- **ot_scada_historians_backup** - SCADA/historian backup operations
- **ot_emergency_freeze** - Emergency change freeze enforcement

### Compliance & Governance (4 roles)
- **ot_compliance_pack** - OT compliance reporting and governance
- **ot_vuln_pipeline** - OT vulnerability tracking pipeline
- **ot_metrics_reporting** - KPI dashboards and metrics reporting
- **ot_change_window_guard** - Change window enforcement guard

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your OT/ICS network details

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Configure zone model
ansible-playbook -i inventory site.yml --tags zones

# Configure asset inventory
ansible-playbook -i inventory site.yml --tags inventory

# Configure security monitoring
ansible-playbook -i inventory site.yml --tags security

# Configure compliance
ansible-playbook -i inventory site.yml --tags compliance
```

### Prerequisites

- Ansible 2.12.0+
- Network access to OT environment (with proper authorization)
- OT-specific modules: `cisco.ios`, `paloaltonetworks.panos`
- Change control approval for OT modifications

### Basic Configuration

```yaml
# group_vars/ot_environment.yml
ot_network_zones:
  - name: "zone_0_safety"
    vlan: 10
    description: "Safety Instrumented Systems"
    criticality: "critical"

  - name: "zone_1_control"
    vlan: 20
    description: "Process Control Systems"
    criticality: "high"

  - name: "zone_2_supervision"
    vlan: 30
    description: "Supervisory HMI/SCADA"
    criticality: "medium"

ot_firewall_default_deny: true
ot_change_window_enforcement: true
```

## 📖 Common Use Cases

### Define OT Zone Model

```bash
ansible-playbook -i inventory site.yml --tags zones
```

### Configure Asset Inventory

```bash
ansible-playbook -i inventory site.yml --tags inventory
```

### Run Compliance Pack

```bash
ansible-playbook -i inventory site.yml --tags compliance \
  -e "ot_compliance_framework=IEC62443"
```

## 🛡️ Security Standards

### NIST 800-82 Rev 2 (ICS Security)
- Network Architecture (segregation, DMZ, defense-in-depth)
- Access Control (least privilege, authentication)
- Audit and Accountability
- Configuration Management
- Incident Response

### ISA/IEC 62443 (Industrial Automation Security)
- **SL 1** - Protection against casual or coincidental violation
- **SL 2** - Protection against intentional violation using simple means
- **SL 3** - Protection against sophisticated means
- **SL 4** - Protection against sophisticated means with extended resources

### DoD STIG for OT
- Network device hardening
- Secure remote access
- Audit logging
- Firmware integrity
- Vulnerability management

## ⚠️ OT-Specific Considerations

1. **Change Control** - All changes require maintenance window approval
2. **Testing First** - Always test in non-production OT test bed
3. **Rollback Plan** - Document and test rollback procedures
4. **Safety Systems** - Never automate changes to Safety Instrumented Systems (SIS)
5. **Availability Priority** - OT prioritizes availability over confidentiality
6. **Legacy Systems** - Handle systems that cannot be patched/upgraded
7. **Vendor Support** - Maintain vendor relationships for critical systems

## 🔧 Troubleshooting

### Issue: Connectivity Loss to OT Devices

**Prevention:**
- Always maintain out-of-band management
- Test changes in lab environment first
- Use maintenance windows
- Have rollback plan ready

### Issue: IDS False Positives

**Resolution:**
- Baseline normal OT traffic patterns
- Tune signatures for OT protocols (Modbus, DNP3, etc.)
- Create allowlists for known-good traffic

## 📚 Additional Resources

- [NIST 800-82 Rev 2](https://csrc.nist.gov/publications/detail/sp/800-82/rev-2/final)
- [ISA/IEC 62443 Standards](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)
- [CISA ICS Advisories](https://www.cisa.gov/uscert/ics/advisories)

---

**Last Updated:** 2026-02-06
**Maintained By:** Fourth Estate Infrastructure Team
**⚠️ CRITICAL: All OT changes require change control approval**
