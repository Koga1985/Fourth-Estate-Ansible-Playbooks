# Cisco Cyber Vision Ansible Automation

Comprehensive Ansible roles and playbooks for Cisco Cyber Vision OT security visibility platform automation, including Center deployment, sensor configuration, OT asset management, DoD STIG/NIST 800-53 security hardening, and monitoring integrations (SIEM, SNMP, ISE pxGrid).

## Quick Start

```bash
# 1. Install dependencies
ansible-galaxy collection install -r requirements.yml
pip install requests

# 2. Configure inventory
cp inventory.example inventory
# Edit with your Center IP/hostname

# 3. Create vault for credentials
ansible-vault create group_vars/all/vault.yml
# Add: vault_cv_center_hostname, vault_cv_api_token, etc.

# 4. Deploy (dry-run by default — no changes applied)
ansible-playbook -i inventory site.yml --ask-vault-pass

# 5. Apply changes when ready
ansible-playbook -i inventory site.yml -e "apply_changes=true" --ask-vault-pass
```

### Targeted Deployments

```bash
# Security hardening only
ansible-playbook -i inventory site.yml --tags security --ask-vault-pass

# Monitoring and integrations only
ansible-playbook -i inventory site.yml --tags monitoring --ask-vault-pass

# Specific phase
ansible-playbook -i inventory playbooks/05_cv_phase4_security.yml \
  -e "apply_changes=true" --ask-vault-pass

# CAT I STIG controls only
ansible-playbook -i inventory site.yml \
  --tags stig_cat1 -e "apply_changes=true" --ask-vault-pass
```

## Role Execution Order

Roles are designed to run in this order, though each can be run independently:

```
Phase 1: cybervision_center_deploy     — Center setup, DNS/NTP, license, local users
Phase 2: cybervision_sensor_config     — Sensor enrollment, zones, protocols, capture
Phase 3: cybervision_asset_management  — OT asset groups, vulnerability tracking, baseline
Phase 4: cybervision_security_hardening — DoD STIG/NIST 800-53 hardening
Phase 5: cybervision_monitoring        — SIEM/syslog, SNMP, alerts, ISE pxGrid
```

**Dependencies:**
- Phase 2 (sensors) requires Phase 1 (Center must be operational)
- Phase 3 (assets) requires Phase 2 (sensors must be enrolling/reporting assets)
- Phases 4 and 5 are independent and can run in any order after Phase 1

## Role Descriptions

### 1. cybervision_center_deploy

**Purpose:** Cisco Cyber Vision Center initial deployment and base configuration

**Features:**
- System name, timezone, and language configuration
- DNS and NTP server configuration
- License key activation
- Local admin and break-glass account management
- HTTPS certificate management
- Post-deployment API validation

**Documentation:** `roles/cybervision_center_deploy/README.md`

### 2. cybervision_sensor_config

**Purpose:** Sensor enrollment and capture configuration

**Features:**
- Enrollment token generation
- Sensor zone (group) creation (plant_floor, control_room, dmz, substation)
- Reporting policy configuration (OT protocol decoders: Modbus, DNP3, S7, BACnet, EtherNet/IP, PROFINET, IEC 61850, OPC-UA)
- Capture mode configuration per sensor type (SPAN, TAP, IOx)
- Online/offline sensor status validation

**Documentation:** `roles/cybervision_sensor_config/README.md`

### 3. cybervision_asset_management

**Purpose:** OT asset discovery, inventory, and risk management

**Features:**
- Passive and active OT asset discovery configuration
- Criticality level labels (critical, high, medium, low)
- Pre-configured OT device groups (Safety-Systems, SCADA-Controllers, HMI-Systems, etc.)
- CVE/vulnerability tracking with CVSS threshold alerting
- Network baseline ("known-good") configuration with deviation alerting
- Full asset inventory export artifact

**Documentation:** `roles/cybervision_asset_management/README.md`

### 4. cybervision_security_hardening

**Purpose:** DoD STIG and NIST 800-53 security hardening

**Features:**
- **STIG CAT I:** HTTPS enforcement, TLS 1.2+ minimum, centralized LDAP auth, 15-char minimum passwords
- **STIG CAT II:** Account lockout (3 failures), session/idle timeout, concurrent session limits, full audit logging, NTP
- **STIG CAT III:** DoD mandatory login banner, system contact and location
- JSON + text STIG compliance report artifact generation

**Documentation:** `roles/cybervision_security_hardening/README.md`

### 5. cybervision_monitoring

**Purpose:** Monitoring integrations and operational visibility

**Features:**
- Syslog/SIEM integration in CEF format (recommended for Splunk, QRadar, etc.)
- SNMPv3 monitoring users and trap destinations
- OT-specific alert policies (new device, SIS boundary crossing, critical CVE, auth failures, sensor offline)
- Cisco ISE pxGrid integration for OT asset context publishing (TrustSec segmentation)
- Center and sensor health metrics with configurable thresholds

**Documentation:** `roles/cybervision_monitoring/README.md`

## Directory Structure

```
cisco_cybervision/
├── README.md                   # This file
├── site.yml                    # Main entry-point playbook
├── requirements.yml            # Ansible collection dependencies
├── inventory.example           # Example inventory file
├── playbooks/                  # Phase-specific playbooks
│   ├── README.md
│   ├── 01_cv_full_deployment.yml     # Full end-to-end deployment
│   ├── 02_cv_phase1_center.yml       # Phase 1: Center setup
│   ├── 03_cv_phase2_sensors.yml      # Phase 2: Sensor config
│   ├── 04_cv_phase3_assets.yml       # Phase 3: Asset management
│   ├── 05_cv_phase4_security.yml     # Phase 4: STIG/NIST hardening
│   └── 06_cv_phase5_monitoring.yml   # Phase 5: Monitoring
└── roles/
    ├── cybervision_center_deploy/     # Center initial deployment
    ├── cybervision_sensor_config/     # Sensor enrollment and config
    ├── cybervision_asset_management/  # OT asset management
    ├── cybervision_security_hardening/ # DoD STIG/NIST hardening
    └── cybervision_monitoring/        # SIEM, SNMP, ISE, alerts
```

## Prerequisites

### Ansible Requirements

```bash
ansible-galaxy collection install -r requirements.yml
```

Required collections:
- `community.general` >= 8.0.0
- `ansible.posix` >= 1.5.0
- `ansible.utils` >= 2.10.0

> No dedicated `cisco.cybervision` collection is required. All Cyber Vision
> API calls use `ansible.builtin.uri` against the Center REST API (`/api/3.0/`).

### Python Requirements

```bash
pip install requests urllib3
```

### Access Requirements

- Cyber Vision Center reachable from Ansible controller on port 443
- Admin API token or admin credentials stored in Ansible Vault
- Ansible 2.15+

## Vault Variables

Create a vault file at `group_vars/all/vault.yml`:

```bash
ansible-vault create group_vars/all/vault.yml
```

### Required Variables

```yaml
# Center connection
vault_cv_center_hostname: "cybervision.example.com"
vault_cv_api_token: "your-api-bearer-token"       # Preferred — generate in CV UI

# Initial admin auth (only if API token not yet generated)
vault_cv_admin_username: "admin"
vault_cv_admin_password: "your-admin-password"

# Local accounts (Phase 1)
vault_cv_admin_email: "admin@example.com"
vault_cv_breakglass_email: "security@example.com"
vault_cv_breakglass_password: "break-glass-password"
vault_cv_license_key: "XXXX-XXXX-XXXX-XXXX"

# LDAP authentication (Phase 4)
vault_cv_ldap_host_1: "ldap1.example.com"
vault_cv_ldap_host_2: "ldap2.example.com"
vault_cv_ldap_base_dn: "dc=example,dc=com"
vault_cv_ldap_bind_dn: "cn=svc-cv,ou=svc,dc=example,dc=com"
vault_cv_ldap_bind_password: "ldap-bind-password"

# SNMPv3 (Phase 5)
vault_cv_snmp_auth_password: "snmp-auth-min-8-chars"
vault_cv_snmp_priv_password: "snmp-priv-min-8-chars"
vault_snmp_trap_host: "10.0.10.100"
vault_snmp_management_subnet: "10.0.10.0/24"

# Syslog/SIEM (Phase 5)
vault_syslog_server_primary: "siem.example.com"
vault_syslog_server_secondary: "siem-backup.example.com"

# Alert notifications (Phase 5)
vault_cv_smtp_server: "smtp.example.com"
vault_cv_alert_email_primary: "soc@example.com"
vault_cv_alert_email_secondary: "noc@example.com"

# Cisco ISE pxGrid (Phase 5)
vault_cv_ise_hostname: "ise.example.com"
vault_cv_ise_pxgrid_node: "ise-pxgrid.example.com"
vault_cv_ise_client_cert: "{{ lookup('file', 'files/cv-pxgrid.crt') }}"
vault_cv_ise_client_key: "{{ lookup('file', 'files/cv-pxgrid.key') }}"
vault_cv_ise_ca_cert: "{{ lookup('file', 'files/ise-ca.crt') }}"

# System identification (Phase 4 — STIG CISC-ND-001470)
vault_cv_system_contact: "NOC Team - noc@example.com"
vault_cv_system_location: "Building A, Data Center Row 3"

# DNS and organization
vault_dns_server_primary: "8.8.8.8"
vault_dns_server_secondary: "8.8.4.4"
vault_fourth_estate_contact: "it@fourthestate.gov"
```

## Compliance

### DoD STIG Controls

| Category | STIG ID | Description | Role |
|----------|---------|-------------|------|
| CAT I | CISC-ND-001440 | HTTPS enforced, HTTP disabled | cybervision_security_hardening |
| CAT I | CISC-ND-000530 | Password strength policy | cybervision_security_hardening |
| CAT I | CISC-ND-000570 | Min password length (15 chars) | cybervision_security_hardening |
| CAT I | CISC-ND-001190 | Centralized authentication | cybervision_security_hardening |
| CAT II | CISC-ND-000370 | Account lockout (3 failures) | cybervision_security_hardening |
| CAT II | CISC-ND-000390 | Session idle timeout (10 min) | cybervision_security_hardening |
| CAT II | CISC-ND-000360 | Concurrent session limits | cybervision_security_hardening |
| CAT II | CISC-ND-000700/710/720 | Comprehensive audit logging | cybervision_security_hardening |
| CAT II | CISC-ND-001420 | NTP with authentication | cybervision_security_hardening |
| CAT III | CISC-ND-000080 | DoD mandatory login banner | cybervision_security_hardening |
| CAT III | CISC-ND-001290 | NTP configuration | cybervision_security_hardening |
| CAT III | CISC-ND-001470 | System contact and location | cybervision_security_hardening |

### NIST 800-53 Control Families

| Family | Description | Roles |
|--------|-------------|-------|
| AC | Access Control | cybervision_security_hardening |
| IA | Identification and Authentication | cybervision_security_hardening |
| AU | Audit and Accountability | cybervision_security_hardening, cybervision_monitoring |
| SC | System and Communications Protection | cybervision_security_hardening |
| CM | Configuration Management | cybervision_center_deploy |
| SI | System and Information Integrity | cybervision_asset_management, cybervision_monitoring |
| CA | Security Assessment | cybervision_security_hardening (compliance report) |

## Artifacts

All deployments generate artifacts in `{{ artifacts_dir }}` (default: `/tmp/cv-artifacts/`):

| Artifact | Phase | Description |
|----------|-------|-------------|
| `cv_initial_setup.json` | 1 | Center name, timezone, language |
| `cv_network_config.json` | 1 | DNS and NTP configuration |
| `cv_license.json` | 1 | License type and status |
| `cv_center_validation.json` | 1 | API health check results |
| `cv_enrollment_token.json` | 2 | Sensor enrollment token (mode 0600) |
| `cv_sensor_enrollment.json` | 2 | Zone and sensor counts |
| `cv_sensor_policies.json` | 2 | Protocol decoder policy |
| `cv_sensor_validation.json` | 2 | Online/offline sensor status |
| `cv_asset_inventory.json` | 3 | Full OT device inventory |
| `cv_vulnerability_report.json` | 3 | CVE findings |
| `cv_baseline_config.json` | 3 | Baseline configuration |
| `cv_stig_compliance_report.json` | 4 | Full STIG compliance report |
| `cv_stig_compliance_summary.txt` | 4 | Human-readable STIG summary |
| `cv_syslog_config.json` | 5 | Syslog/SIEM settings |
| `cv_snmp_config.json` | 5 | SNMP configuration |
| `cv_alert_policies.json` | 5 | Alert policy definitions |
| `cv_ise_integration.json` | 5 | ISE pxGrid settings |
| `cv_health_report.json` | 5 | Center and sensor health |

## Testing

### Pre-Production Testing

```bash
# 1. Dry-run — no changes, exports current state
ansible-playbook -i inventory site.yml --ask-vault-pass

# 2. Review artifacts
ls -la /tmp/cv-artifacts/

# 3. Review STIG compliance report
cat /tmp/cv-artifacts/cv_stig_compliance_summary.txt

# 4. Test in lab Center before production
```

### Applying to Production

```bash
# Full deployment
ansible-playbook -i inventory site.yml -e "apply_changes=true" --ask-vault-pass

# Single phase
ansible-playbook -i inventory playbooks/05_cv_phase4_security.yml \
  -e "apply_changes=true" --ask-vault-pass
```

## Troubleshooting

**API authentication fails:**
- Generate an API token in Cyber Vision UI: Settings → Users → API Tokens
- Store as `vault_cv_api_token` in vault
- Set `cv_validate_certs: false` for self-signed certificates in lab

**LDAP integration not working:**
- Verify LDAP server is reachable from Center on port 636
- Check bind DN format matches your directory (AD vs OpenLDAP syntax differs)
- Confirm the bind account has read access to the `base_dn` subtree

**ISE pxGrid integration fails:**
- pxGrid must be enabled in ISE Administration → pxGrid Services
- Cyber Vision pxGrid client account must be approved in ISE UI
- Certificate CN must match what ISE expects for the pxGrid client

**Active discovery causing OT device issues:**
- Set `cv_discovery_active: false` immediately
- Consult OT engineers before re-enabling
- Always use `cv_active_discovery_rate: "low"` in production

## References

- [Cisco Cyber Vision Documentation](https://www.cisco.com/c/en/us/products/security/cyber-vision/index.html)
- [Cyber Vision REST API Guide](https://www.cisco.com/c/en/us/td/docs/security/cyber_vision/api/)
- [DISA STIG for Cisco Network Devices](https://public.cyber.mil/stigs/)
- [NIST 800-53 Rev 5 Controls](https://nvd.nist.gov/800-53)
- [Cisco ISE pxGrid Integration](https://developer.cisco.com/docs/pxgrid/)
- [ICS-CERT OT Security Guidance](https://www.cisa.gov/ics)

## Author

Created for Fourth Estate DoD OT security deployments.

---

**Last Updated:** 2026-03-16
**Maintained By:** Fourth Estate Infrastructure Team
