# Cisco ACI Ansible Automation

Comprehensive Ansible roles and playbooks for Cisco Application Centric Infrastructure (ACI) automation, including fabric deployment, tenant configuration, network connectivity, DoD STIG/NIST 800-53 security hardening, and monitoring.

## 🚀 Quick Start (Drop-In Deployment)

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml
pip install acicobra acimodel requests

# 2. Configure your inventory
cp inventory.example inventory
# Edit inventory with your APIC hostname and credentials

# 3. Create vault for credentials
ansible-vault create group_vars/all/vault.yml
# Add: vault_aci_username, vault_aci_password, vault_aci_apic_hostname

# 4. Deploy (dry-run by default - no changes applied)
ansible-playbook -i inventory site.yml --ask-vault-pass

# 5. Apply changes when ready
ansible-playbook -i inventory site.yml -e "apply_changes=true" --ask-vault-pass
```

### Deployment Options

```bash
# Deploy full ACI fabric
ansible-playbook -i inventory site.yml --tags fabric,tenants,network

# Apply DoD STIG and NIST security hardening only
ansible-playbook -i inventory site.yml --tags security --ask-vault-pass

# Configure monitoring only
ansible-playbook -i inventory site.yml --tags monitoring --ask-vault-pass

# Run specific phase
ansible-playbook -i inventory playbooks/02_aci_phase1_fabric.yml --ask-vault-pass

# Production deployment
ansible-playbook -i inventory playbooks/aci_fourth_estate_production.yml \
  -e "apply_changes=true" --ask-vault-pass
```

## 📋 Role Categories

### Fabric Infrastructure
| Role | Purpose |
|------|---------|
| `aci_fabric_deploy` | APIC cluster registration, spine/leaf node discovery, fabric policies, access policies, interface profiles |

### Tenant Configuration
| Role | Purpose |
|------|---------|
| `aci_tenant_config` | Tenant, VRF, Bridge Domain, Application Profile, EPG, Contract, and Filter management |

### Network Connectivity
| Role | Purpose |
|------|---------|
| `aci_network_config` | L3Out, L2Out, external EPGs, static routes, BGP peers, OSPF configuration |

### Security & Compliance
| Role | Purpose |
|------|---------|
| `aci_security_hardening` | DoD STIG and NIST 800-53 hardening - authentication, TLS, access control, session management, audit logging, SNMPv3, NTP, DoD banners |

### Monitoring & Observability
| Role | Purpose |
|------|---------|
| `aci_monitoring` | SNMP, syslog, Call Home, fabric health monitoring, fault management |

## Directory Structure

```
cisco_aci/
├── README.md               # This file
├── site.yml                # Main entry-point playbook
├── requirements.yml        # Ansible collection dependencies
├── inventory.example       # Example inventory file
├── playbooks/              # Production-ready phased playbooks
│   ├── README.md
│   ├── 01_aci_full_deployment.yml        # Full end-to-end deployment
│   ├── 02_aci_phase1_fabric.yml          # Phase 1: Fabric infrastructure
│   ├── 03_aci_phase2_tenants.yml         # Phase 2: Tenant configuration
│   ├── 04_aci_phase3_network.yml         # Phase 3: Network connectivity
│   ├── 05_aci_phase4_security.yml        # Phase 4: STIG/NIST hardening
│   ├── 06_aci_phase5_monitoring.yml      # Phase 5: Monitoring
│   └── aci_fourth_estate_production.yml  # Production deployment
├── roles/                  # Ansible roles
│   ├── aci_fabric_deploy/       # Fabric infrastructure deployment
│   ├── aci_tenant_config/       # Tenant and network policy configuration
│   ├── aci_network_config/      # L3Out/L2Out external connectivity
│   ├── aci_security_hardening/  # DoD STIG and NIST 800-53 hardening
│   └── aci_monitoring/          # Monitoring and observability
└── tasks/                  # Reusable standalone task files
    └── aci_fourth_estate_deploy.yml
```

## Role Descriptions

### 1. aci_fabric_deploy

**Purpose:** Complete ACI fabric infrastructure deployment

**Features:**
- APIC cluster OOB management configuration
- NTP and DNS policy configuration
- Spine and leaf node registration and discovery
- Fabric-wide node control and link level policies
- ISIS redistribution and COOP group policies
- Rogue endpoint and loop protection policies
- VLAN pool, physical domain, L3 domain, and AEP creation
- Leaf and spine switch profile management
- Interface policy group configuration
- VPC protection group setup

**Documentation:** `roles/aci_fabric_deploy/README.md`

### 2. aci_tenant_config

**Purpose:** ACI tenant and network policy configuration

**Features:**
- Tenant creation with security domain assignment
- VRF configuration with policy enforcement mode
- Bridge domain setup with gateway IP and unicast routing
- Application profile management
- Endpoint Group (EPG) configuration with preferred group membership
- Filter and contract creation (consumer/provider)
- Static path binding for server connectivity
- Pre-configured Fourth Estate tenant structure (Prod, Dev, Mgmt, DMZ)

**Documentation:** `roles/aci_tenant_config/README.md`

### 3. aci_network_config

**Purpose:** External network connectivity and routing

**Features:**
- L3Out configuration for external Layer 3 connectivity
- Logical node and interface profile management
- L2Out for external Layer 2 connectivity
- External EPG creation with subnet scope configuration
- Static route configuration per node
- BGP peer configuration with authentication
- OSPF area and interface policy configuration
- Contract binding to external EPGs

**Documentation:** `roles/aci_network_config/README.md`

### 4. aci_security_hardening

**Purpose:** DoD STIG and NIST 800-53 security hardening

**Features:**
- **STIG Category I:** HTTPS enforcement (disable HTTP), TLS 1.2+ minimum, centralized authentication, password encryption, 15-character minimum password length
- **STIG Category II:** Account lockout (3 failures), session/idle timeout (10 min), comprehensive audit logging, SNMPv3 required (disable v1/v2), SSH enforcement (disable Telnet), NTP authentication, concurrent session limits
- **STIG Category III:** DoD mandatory login banner, system contact and location, NTP configuration
- LDAP, RADIUS, and TACACS+ authentication provider configuration
- Role-based access control (RBAC) and security domain management
- Compliance report generation (JSON + text summary)
- Full STIG finding to NIST control mapping

**Documentation:** `roles/aci_security_hardening/README.md`

### 5. aci_monitoring

**Purpose:** Monitoring, observability, and health management

**Features:**
- SNMP policy configuration (v3 users with auth+priv)
- SNMP trap destination configuration
- Syslog remote destination configuration with severity filtering
- Call Home setup with SMTP integration
- Fabric health score monitoring (pod, node, tenant level)
- Fault collection and reporting by severity
- Health threshold alerting (configurable warn/critical)

**Documentation:** `roles/aci_monitoring/README.md`

## Prerequisites

### Ansible Requirements
```bash
ansible-galaxy collection install -r requirements.yml
```

Required collections:
- `cisco.aci` >= 2.8.0
- `community.general` >= 8.0.0
- `ansible.posix` >= 1.5.0
- `ansible.utils` >= 2.10.0

### Python Requirements
```bash
pip install acicobra acimodel requests
```

### Access Requirements
- APIC admin credentials (stored in Ansible Vault)
- Network access to APIC on port 443
- Ansible 2.15+

## Vault Variables

Create a vault file at `group_vars/all/vault.yml`:

```bash
ansible-vault create group_vars/all/vault.yml
```

Required vault variables:

```yaml
# APIC Connection
vault_aci_apic_hostname: "apic.example.com"
vault_aci_username: "admin"
vault_aci_password: "your-secure-password"

# Authentication providers
vault_aci_ldap_bind_dn: "cn=ansible-svc,ou=svc,dc=example,dc=com"
vault_aci_ldap_bind_password: "ldap-bind-password"
vault_aci_radius_key: "radius-shared-secret"
vault_aci_tacacs_key: "tacacs-shared-secret"

# SNMPv3
vault_aci_snmpv3_auth_password: "snmp-auth-password"
vault_aci_snmpv3_priv_password: "snmp-priv-password"

# Monitoring
vault_aci_snmp_community: "monitoring-community"
vault_aci_callhome_email: "noc@example.com"

# System info (STIG requirement)
vault_aci_system_contact: "NOC Team - noc@example.com"
vault_aci_system_location: "Building A, Data Center Row 3"

# NTP Authentication
vault_aci_ntp_key: "ntp-authentication-key"

# Organization contacts
vault_aci_org_contact: "IT Team"
vault_aci_org_email: "it@example.com"
```

## Compliance

### DoD STIG

All ACI security roles implement DISA STIG findings remediation:

- **Category I (High):**
  - CISC-ND-001440: HTTPS enforcement, disable HTTP
  - CISC-ND-000530: Password encryption and strength policy
  - CISC-ND-000570: Minimum password length (15 characters)
  - CISC-ND-001190: Centralized authentication (LDAP/RADIUS/TACACS+)

- **Category II (Medium):**
  - CISC-ND-000370: Account lockout after 3 consecutive failures
  - CISC-ND-000390: Session idle timeout (10 minutes)
  - CISC-ND-000700/710/720: Comprehensive audit logging with timestamps and user identity
  - CISC-ND-000090: SNMPv3 required, disable SNMPv1/v2
  - CISC-ND-001400: SSH enforcement, disable Telnet
  - CISC-ND-001420: NTP with authentication
  - CISC-ND-000360: Concurrent session limits

- **Category III (Low):**
  - CISC-ND-000080: DoD mandatory login banner
  - CISC-ND-001290: NTP configuration
  - CISC-ND-001470: System contact and location

### NIST 800-53 Control Families

| Control Family | Description | Roles |
|---------------|-------------|-------|
| AC | Access Control | aci_security_hardening |
| IA | Identification and Authentication | aci_security_hardening |
| AU | Audit and Accountability | aci_security_hardening, aci_monitoring |
| SC | System and Communications Protection | aci_security_hardening, aci_network_config |
| CM | Configuration Management | aci_fabric_deploy, aci_tenant_config |
| SI | System and Information Integrity | aci_monitoring |
| SA | System and Services Acquisition | aci_fabric_deploy |

### Additional Frameworks
- NIST 800-171 (CUI protection)
- FISMA Moderate baseline
- FISMA High baseline

## Configuration

### Key Variables

**Connection:**
```yaml
aci_host: "apic.example.com"          # APIC hostname or IP
aci_username: "admin"                  # Admin username (use vault)
aci_password: "password"               # Admin password (use vault)
aci_validate_certs: true               # SSL certificate validation
aci_use_ssl: true                      # Use HTTPS
```

**Deployment Control:**
```yaml
apply_changes: false                   # false = dry-run, true = apply
artifacts_dir: "/tmp/aci-artifacts"    # Artifact output directory
```

**Organization:**
```yaml
aci_fabric_name: "FourthEstate-ACI"    # ACI fabric name
aci_pod_id: 1                          # ACI pod ID
aci_org_name: "FourthEstate"           # Organization name
```

**Security:**
```yaml
stig_cat1_enabled: true                # Apply STIG Category I controls
stig_cat2_enabled: true                # Apply STIG Category II controls
stig_cat3_enabled: true                # Apply STIG Category III controls
aci_password_min_length: 15            # DoD minimum password length
aci_lockout_max_attempts: 3            # Account lockout threshold
aci_idle_timeout: 300                  # Session idle timeout (seconds)
aci_session_timeout: 600               # Maximum session timeout (seconds)
```

See individual role `defaults/main.yml` files for complete variable documentation.

## Artifacts

All deployments generate artifacts in `{{ artifacts_dir }}` (default: `/tmp/aci-artifacts/`):

- `aci_deployment_metadata.json` - Deployment metadata (hostname, user, timestamp, mode)
- `aci_fabric_config.json` - Fabric deployment configuration details
- `aci_tenant_config.json` - Tenant and policy configuration details
- `aci_network_config.json` - L3Out and connectivity configuration details
- `aci_stig_compliance_report.json` - Full STIG compliance report (pass/fail per control)
- `aci_stig_compliance_summary.txt` - Human-readable compliance summary
- `aci_monitoring_config.json` - SNMP, syslog, Call Home configuration
- `aci_health_report.json` - Fabric health scores
- `aci_fault_report.json` - Current faults by severity
- `aci_validation_report.json` - Post-deployment validation results

## Testing

### Pre-Production Testing

1. Run in dry-run mode (default) to verify planned changes:
```bash
ansible-playbook -i inventory site.yml --ask-vault-pass
```

2. Review all artifacts in `/tmp/aci-artifacts/`

3. Verify STIG compliance report for any gaps

4. Test in lab/dev APIC before production

### Applying to Production

```bash
# Apply all phases
ansible-playbook -i inventory site.yml -e "apply_changes=true" --ask-vault-pass

# Apply specific phase
ansible-playbook -i inventory playbooks/05_aci_phase4_security.yml \
  -e "apply_changes=true" --ask-vault-pass
```

## Support and Troubleshooting

### Common Issues

**APIC connection failures:**
- Verify APIC accessibility from Ansible controller on port 443
- Check `aci_validate_certs` setting (set to `false` for self-signed certs in lab)
- Verify credentials are correct in vault

**Module not found errors:**
- Run `ansible-galaxy collection install -r requirements.yml`
- Run `pip install acicobra acimodel requests`

**Dry-run shows no changes:**
- Expected behavior - set `apply_changes=true` to apply changes

**STIG findings not remediated:**
- Check `stig_cat1_enabled`, `stig_cat2_enabled`, `stig_cat3_enabled` variables
- Review individual task files for feature-specific toggles
- Verify ACI version supports the specific control

### Logging

- Ansible output shows all actions taken
- APIC audit logs record all API calls when apply_changes is true
- All artifacts contain detailed configuration records

## Contributing

When adding new ACI functionality:

1. Follow existing role structure (meta, defaults, tasks, handlers, README)
2. Include STIG/NIST compliance mapping in task names
3. Generate JSON artifacts for all configuration changes
4. Add `when: apply_changes | bool` guards on all write operations
5. Include `state: query` path for dry-run validation
6. Test against ACI simulator before submitting

## License

MIT

## References

- [Cisco ACI Documentation](https://www.cisco.com/c/en/us/support/cloud-systems-management/application-policy-infrastructure-controller-apic/index.html)
- [Cisco ACI Ansible Collection](https://galaxy.ansible.com/cisco/aci)
- [DISA STIG for Cisco NX-OS/ACI](https://public.cyber.mil/stigs/)
- [NIST 800-53 Rev 5 Controls](https://nvd.nist.gov/800-53)
- [ACI APIC REST API Guide](https://developer.cisco.com/docs/aci/)

## Author

Created for Fourth Estate production deployments.

---

**Last Updated:** 2026-03-12
**Maintained By:** Fourth Estate Infrastructure Team
