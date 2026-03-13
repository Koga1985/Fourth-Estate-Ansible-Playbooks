# Cisco Ansible Automation

Comprehensive Ansible roles and playbooks for Cisco infrastructure automation, including Application Centric Infrastructure (ACI), Identity Services Engine (ISE), and Unified Computing System (UCS).

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your Cisco devices

# 3. Deploy
ansible-playbook -i inventory site.yml --ask-vault-pass
```

### Deployment Options

```bash
# Deploy ACI fabric
ansible-playbook -i inventory site.yml --tags aci,fabric

# Deploy ACI tenant configuration
ansible-playbook -i inventory site.yml --tags aci,tenant

# Apply ACI security hardening
ansible-playbook -i inventory site.yml --tags aci,security

# Deploy ISE policy configuration
ansible-playbook -i inventory site.yml --tags ise,policy

# Deploy UCS infrastructure
ansible-playbook -i inventory site.yml --tags ucs,infrastructure

# Apply UCS security hardening
ansible-playbook -i inventory site.yml --tags ucs,security
```

## Directory Structure

```
cisco/
├── playbooks/          # Production-ready playbooks
│   ├── ucs_fourth_estate_production.yml
│   └── README.md
├── roles/              # Ansible roles
│   ├── aci_fabric_deploy/             # ACI fabric initial deployment
│   ├── aci_tenant_config/             # ACI tenant, VRF, BD, EPG, contracts
│   ├── aci_network_config/            # ACI L3Out/L2Out external connectivity
│   ├── aci_security_hardening/        # ACI security hardening (DoD STIG)
│   ├── aci_monitoring/                # ACI SNMP, syslog, Call Home, health
│   ├── ise_*/                         # ISE roles (28 roles)
│   ├── ucs_prod_infrastructure/       # UCS infrastructure deployment
│   ├── ucs_security_hardening/        # UCS security hardening (DoD STIG)
│   ├── ucs_prod_networking/           # UCS networking configuration
│   ├── ucs_prod_monitoring/           # UCS monitoring and compliance
│   └── ucs_prod_backup_dr/            # UCS backup and disaster recovery
└── tasks/              # Reusable task files
    └── ucs_fourth_estate_deploy.yml
```

## ACI Roles for Fourth Estate

### Overview

The ACI roles provide production-ready automation for deploying Cisco Application Centric Infrastructure (ACI) fabric for Fourth Estate organizations. All roles implement a phased deployment pipeline and include DoD STIG and NIST 800-53 compliance controls. All roles default to dry-run mode (`apply_changes: false`).

### Roles

#### 1. aci_fabric_deploy

**Purpose:** Phase 1 — ACI fabric initial deployment

**Features:**
- APIC cluster configuration (system name, OOB management, NTP, DNS, syslog)
- Spine and leaf node registration with discovery retry logic
- Fabric-wide policies (node control, link level, ISIS redistribution, COOP group)
- Endpoint security (loop protection, rogue endpoint control)
- VLAN pools, physical/L3 domains, and Attachable Entity Profiles (AEP)
- Leaf/spine switch profiles, interface policy groups, and vPC protection groups

**Documentation:** `roles/aci_fabric_deploy/README.md`

#### 2. aci_tenant_config

**Purpose:** Phase 2 — Tenant, VRF, bridge domain, EPG, and contract configuration

**Features:**
- Tenant creation for production, development, management, and DMZ domains
- VRF provisioning with policy enforcement and preferred group settings
- Bridge domain and subnet (gateway) configuration
- Application profile and EPG creation with intra-EPG isolation
- Filter, contract, and contract subject creation
- Optional static path bindings to physical ports, port-channels, and vPC interfaces

**Documentation:** `roles/aci_tenant_config/README.md`

#### 3. aci_network_config

**Purpose:** Phase 3 — L3Out/L2Out external network connectivity

**Features:**
- L3Out with logical node/interface profiles and routed sub-interfaces
- L2Out bridged external connectivity with external EPGs
- Static route configuration with primary and backup next-hops
- BGP peer configuration with MD5 authentication
- OSPF interface policy and area configuration

**Documentation:** `roles/aci_network_config/README.md`

#### 4. aci_security_hardening

**Purpose:** Phase 4 — DoD STIG and NIST 800-53 security hardening

**Features:**
- STIG Category I, II, III controls for Cisco ACI
- Password complexity and session timeout enforcement
- Insecure protocol disabling (Telnet, SNMPv1/v2c)
- RBAC configuration and privilege separation
- Audit logging and syslog forwarding
- TLS 1.2+ enforcement and FIPS-mode settings
- Compliance reporting

**Documentation:** `roles/aci_security_hardening/README.md`

#### 5. aci_monitoring

**Purpose:** Phase 5 — SNMP, syslog, Call Home, health, and fault management

**Features:**
- SNMPv3 policy with SHA authentication and AES-128 privacy
- SNMP trap destinations and client group source-IP restrictions
- Syslog remote destinations with severity filtering
- Cisco Call Home smart notification configuration
- Fabric health score monitoring with configurable thresholds
- Fault management with severity-based reporting (critical, major, minor, warning)

**Documentation:** `roles/aci_monitoring/README.md`

---

## UCS Roles for Fourth Estate

### Overview

The UCS roles provide production-ready automation for deploying Cisco UCS infrastructure for Fourth Estate organizations (free press and media). All roles include DoD STIG and NIST 800-53 compliance controls.

### Roles

#### 1. ucs_prod_infrastructure

**Purpose:** Complete UCS infrastructure deployment

**Features:**
- UCS Manager initial configuration
- Organization hierarchy setup
- Service profile templates
- Network and storage connectivity (vNIC/vHBA)
- Server pools and policies
- UUID and MAC address pools
- Firmware management
- High availability configuration

**Documentation:** `roles/ucs_prod_infrastructure/README.md`

#### 2. ucs_security_hardening

**Purpose:** Security hardening with compliance

**Features:**
- DoD STIG Category I, II, III remediation
- NIST 800-53 controls (AC, IA, AU, SC, CM, SI, PE)
- Access control and RBAC
- Authentication hardening (LDAP/RADIUS/TACACS+)
- Comprehensive audit logging
- Cryptographic controls (TLS 1.2+)
- Network security controls
- DoD banner configuration
- Compliance reporting

**Documentation:** `roles/ucs_security_hardening/README.md`

#### 3. ucs_prod_networking

**Purpose:** Network infrastructure configuration

**Features:**
- VLAN configuration
- VSAN configuration (SAN)
- QoS policies
- Network control policies (CDP/LLDP)
- Multicast policies
- Uplink port channels

**Documentation:** `roles/ucs_prod_networking/README.md`

#### 4. ucs_prod_monitoring

**Purpose:** Monitoring and health checks

**Features:**
- SNMP v2c/v3 configuration
- SNMP trap destinations
- Call Home configuration
- System health monitoring
- Power and thermal monitoring
- Compliance monitoring checklists

**Documentation:** `roles/ucs_prod_monitoring/README.md`

#### 5. ucs_prod_backup_dr

**Purpose:** Backup and disaster recovery

**Features:**
- Full-state backups
- Configuration backups
- Scheduled and immediate backups
- Disaster recovery procedures
- RTO/RPO tracking
- Backup verification scripts

**Documentation:** `roles/ucs_prod_backup_dr/README.md`

## Quick Start

### Prerequisites

1. Install required collections:
```bash
ansible-galaxy collection install -r requirements.yml
pip install acicobra acimodel ciscoisesdk ucsmsdk intersight requests
```

2. Create vault for credentials:
```bash
ansible-vault create group_vars/all/vault.yml
```

Add the following variables:
```yaml
# ACI
vault_aci_apic_hostname: "apic.example.com"
vault_aci_apic_username: "admin"
vault_aci_apic_password: "your-password"

# UCS
vault_ucs_hostname: "ucs-manager.example.com"
vault_ucs_username: "admin"
vault_ucs_password: "your-password"

# Shared
vault_fourth_estate_contact: "Contact Name"
vault_fourth_estate_email: "contact@example.com"
vault_backup_server: "backup.example.com"
vault_backup_username: "backup"
vault_backup_password: "backup-password"
```

### Deployment

#### Dry Run (Planning Phase)

```bash
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml \
  -e "ucs_hostname=ucs-manager.example.com" \
  --ask-vault-pass
```

This will:
- Validate connectivity
- Generate configuration plans
- Create compliance reports
- **NOT apply any changes**

Review artifacts in `/tmp/ucs-fourth-estate-artifacts/`

#### Production Deployment

```bash
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml \
  -e "ucs_hostname=ucs-manager.example.com" \
  -e "apply_changes=true" \
  --ask-vault-pass
```

#### Selective Deployment

Deploy specific components:

```bash
# Infrastructure only
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml \
  --tags infrastructure

# Security hardening only
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml \
  --tags security

# Networking only
ansible-playbook cisco/playbooks/ucs_fourth_estate_production.yml \
  --tags networking
```

## Compliance

### DoD STIG

All UCS roles implement DoD STIG findings remediation:

- **Category I (High):** Password policies, TLS enforcement, session management
- **Category II (Medium):** Account lockout, audit logging, NTP, SNMPv3
- **Category III (Low):** System documentation, contact information, backups

### NIST 800-53

Implemented control families:

- **AC:** Access Control
- **IA:** Identification and Authentication
- **AU:** Audit and Accountability
- **SC:** System and Communications Protection
- **CM:** Configuration Management
- **SI:** System and Information Integrity
- **PE:** Physical and Environmental Protection

### Additional Frameworks

- NIST 800-171 (CUI protection)
- FISMA Moderate baseline
- FISMA High baseline

## Configuration

### Key Variables

**Connection:**
- `ucs_hostname`: UCS Manager hostname/IP
- `ucs_username`: Administrative username
- `ucs_password`: Administrative password

**Deployment Control:**
- `apply_changes`: Set to `true` to apply configurations (default: `false`)
- `ucs_artifacts_dir`: Directory for deployment artifacts

**Organization:**
- `fourth_estate_org_name`: Organization name
- `fourth_estate_description`: Organization description
- `fourth_estate_sub_orgs`: Sub-organization list

**Security:**
- `stig_cat1_enabled`: Apply STIG Category I (default: `true`)
- `stig_cat2_enabled`: Apply STIG Category II (default: `true`)
- `stig_cat3_enabled`: Apply STIG Category III (default: `true`)
- `ia_password_min_length`: Minimum password length (default: 15)
- `ac_session_timeout_minutes`: Session timeout (default: 15)

See individual role `defaults/main.yml` files for complete variable documentation.

## Artifacts

All deployments generate artifacts in the artifacts directory (default: `/tmp/ucs-fourth-estate-artifacts/`):

- `deployment_metadata.json`: Deployment information
- `deployment_summary.txt`: Human-readable summary
- `compliance_report.txt`: Compliance status
- `stig_cat[1-3]_remediation.txt`: STIG remediation details
- `disaster_recovery_plan.txt`: DR procedures
- `network_topology.txt`: Network documentation
- And more...

## Testing

### Pre-Production Testing

1. Test in lab environment
2. Run with `apply_changes=false` (dry-run)
3. Review all artifacts
4. Verify configurations meet requirements
5. Test backup/restore procedures

### Validation

After deployment:
1. Review fault reports
2. Verify service profile associations
3. Test network connectivity
4. Verify security controls
5. Test monitoring integrations
6. Validate backup functionality

## Support and Troubleshooting

### Common Issues

**Connection failures:**
- Verify UCS Manager accessibility
- Check credentials
- Verify SSL/TLS settings

**Dry-run shows no changes:**
- This is expected - set `apply_changes=true` to apply

**STIG findings not remediated:**
- Check role variable settings
- Review individual STIG task files
- Verify UCS platform support for controls

### Logging

All roles use comprehensive logging:
- Ansible output shows all actions
- UCS Manager audit logs track changes
- Artifacts contain detailed reports

## Contributing

When adding new UCS functionality:

1. Follow existing role structure
2. Include comprehensive documentation
3. Add compliance mapping
4. Create example playbooks
5. Generate artifacts for verification
6. Test in lab environment

## License

MIT

## References

- [Cisco ACI Documentation](https://www.cisco.com/c/en/us/support/cloud-systems-management/application-policy-infrastructure-controller-apic/index.html)
- [Cisco ACI Ansible Collection](https://galaxy.ansible.com/cisco/aci)
- [Cisco UCS Documentation](https://www.cisco.com/c/en/us/support/servers-unified-computing/index.html)
- [Cisco UCS Ansible Collection](https://galaxy.ansible.com/cisco/ucs)
- [DoD STIG for Cisco Devices](https://public.cyber.mil/stigs/)
- [NIST 800-53 Controls](https://nvd.nist.gov/800-53)

## Author

Created for Fourth Estate production deployments.

---

**Last Updated:** 2026-03-13
**Maintained By:** Fourth Estate Infrastructure Team
