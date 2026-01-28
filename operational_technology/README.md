# Operational Technology (OT/ICS) Security

This directory contains **24 Ansible roles** for securing **Operational Technology (OT)** and **Industrial Control Systems (ICS)** with emphasis on **NIST 800-82**, **ISA/IEC 62443**, and **DoD STIG** compliance for Fourth Estate critical infrastructure.

## Overview

Comprehensive OT/ICS security automation covering network segmentation, firewall management, intrusion detection/prevention, secure remote access, firmware management, and compliance monitoring.

## 📋 Role Categories

### Network Security (8 roles)
- **ot_firewall_baseline** - OT firewall configuration
- **ot_network_segmentation** - Zone-based architecture
- **ot_dmz_configuration** - DMZ setup for IT/OT boundary
- **ot_vlan_isolation** - VLAN-based isolation
- **ot_acl_management** - Access control lists
- **ot_nat_rules** - Network address translation
- **ot_vpn_config** - Secure remote access VPN
- **ot_port_security** - Switch port security

### Intrusion Detection (5 roles)
- **ot_idps_deployment** - IDS/IPS deployment
- **ot_snort_config** - Snort IDS configuration
- **ot_suricata_config** - Suricata IDS setup
- **ot_signature_management** - Signature updates
- **ot_anomaly_detection** - Baseline anomaly detection

### Asset Management (4 roles)
- **ot_asset_inventory** - Device discovery and inventory
- **ot_asset_classification** - Criticality classification
- **ot_vulnerability_scanning** - OT-safe scanning
- **ot_patch_management** - Firmware/patch lifecycle

### Monitoring & Logging (4 roles)
- **ot_syslog_aggregation** - Centralized logging
- **ot_metrics_reporting** - KPI dashboards
- **ot_event_correlation** - Security event correlation
- **ot_audit_logging** - Compliance audit logs

### Compliance & Hardening (3 roles)
- **ot_stig_hardening** - DoD STIG for OT systems
- **ot_isa62443_compliance** - ISA/IEC 62443 controls
- **ot_nist80082_compliance** - NIST 800-82 Rev 2

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

### Deploy OT Network Segmentation

```bash
ansible-playbook playbooks/ot_network_segmentation.yml \
  -i inventory/ot_production.yml \
  -e "apply_changes=false" \
  --check
```

### Configure IDPS

```bash
ansible-playbook playbooks/ot_idps_deployment.yml \
  -i inventory/ot_production.yml \
  -e "idps_mode=inline" \
  -e "signature_update=true"
```

### Apply ISA 62443 Controls

```bash
ansible-playbook playbooks/ot_isa62443_compliance.yml \
  -i inventory/ot_production.yml \
  -e "security_level=3"  # SL 1-4
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

**Last Updated:** 2026-01-15
**Maintained By:** Fourth Estate Infrastructure Team
**⚠️ CRITICAL: All OT changes require change control approval**
