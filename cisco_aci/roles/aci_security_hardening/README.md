# aci_security_hardening

Ansible role for DoD STIG and NIST 800-53 security hardening of Cisco ACI fabrics. Implements all applicable DISA STIG findings for Cisco network devices in ACI environments.

## Quick Start

```bash
# Dry-run (default) — no changes applied
ansible-playbook -i inventory site.yml --tags security --ask-vault-pass

# Apply hardening
ansible-playbook -i inventory site.yml --tags security -e "apply_changes=true" --ask-vault-pass

# Apply only CAT I (critical) controls
ansible-playbook -i inventory site.yml --tags stig_cat1 -e "apply_changes=true" --ask-vault-pass
```

## Role Execution Order

This role is **Phase 4** of the full deployment and should run after fabric and tenant configuration:

```
Phase 1: aci_fabric_deploy        (fabric infrastructure)
Phase 2: aci_tenant_config        (tenant policies)
Phase 3: aci_network_config       (L3Out/L2Out connectivity)
Phase 4: aci_security_hardening   ← this role
Phase 5: aci_monitoring           (SNMP, syslog, Call Home)
```

> The role can be run independently on an existing fabric — it does not depend on the other roles completing first.

## Requirements

- `cisco.aci` collection >= 2.8.0
- ACI APIC version 5.x or later
- Admin credentials stored in Ansible Vault
- Network access to APIC on port 443

## STIG Controls Implemented

### Category I — High Severity

| STIG ID | Control | Task File |
|---------|---------|-----------|
| CISC-ND-001440 | Enforce HTTPS, disable HTTP | `crypto_tls.yml` |
| CISC-ND-000530 | Password encryption and strength policy | `authentication.yml` |
| CISC-ND-000570 | Minimum password length (15 characters) | `authentication.yml` |
| CISC-ND-001190 | Centralized authentication (LDAP/RADIUS/TACACS+) | `authentication.yml` |

### Category II — Medium Severity

| STIG ID | Control | Task File |
|---------|---------|-----------|
| CISC-ND-000370 | Account lockout after 3 failures | `authentication.yml` |
| CISC-ND-000390 | Session idle timeout (10 minutes) | `session_management.yml` |
| CISC-ND-000360 | Concurrent session limits | `session_management.yml` |
| CISC-ND-000700 | Audit logging with timestamps | `audit_logging.yml` |
| CISC-ND-000710 | Audit logging with user identity | `audit_logging.yml` |
| CISC-ND-000720 | Audit log protection | `audit_logging.yml` |
| CISC-ND-000090 | SNMPv3 required, disable SNMPv1/v2 | `snmp_security.yml` |
| CISC-ND-001400 | SSH enforcement, disable Telnet | `crypto_tls.yml` |
| CISC-ND-001420 | NTP with authentication | `ntp_dns.yml` |

### Category III — Low Severity

| STIG ID | Control | Task File |
|---------|---------|-----------|
| CISC-ND-000080 | DoD mandatory login banner | `banners.yml` |
| CISC-ND-001290 | NTP configuration | `ntp_dns.yml` |
| CISC-ND-001470 | System contact and location | `banners.yml` |

## NIST 800-53 Mapping

| Control Family | Controls | Task Files |
|---------------|----------|-----------|
| AC — Access Control | AC-2, AC-3, AC-6, AC-7, AC-8, AC-11, AC-12, AC-17 | `access_control.yml`, `session_management.yml`, `banners.yml` |
| IA — Identification & Authentication | IA-2, IA-5 | `authentication.yml` |
| AU — Audit & Accountability | AU-2, AU-3, AU-8, AU-9, AU-12 | `audit_logging.yml`, `ntp_dns.yml` |
| SC — System & Comms Protection | SC-8, SC-28 | `crypto_tls.yml`, `snmp_security.yml` |

## Variables

### Feature Toggles

```yaml
# Enable/disable entire STIG categories
stig_cat1_enabled: true       # Category I (High) — authentication, TLS
stig_cat2_enabled: true       # Category II (Medium) — sessions, audit, SNMP
stig_cat3_enabled: true       # Category III (Low) — banners, NTP

# Enable/disable individual modules
enable_auth_hardening: true      # LDAP/RADIUS/TACACS+ + password policy
enable_access_control: true      # RBAC, security domains, local users
enable_audit_logging: true       # Syslog destinations, audit policy
enable_crypto_tls: true          # TLS 1.2+, cipher suites, SSH, disable Telnet/HTTP
enable_session_management: true  # Idle/session timeouts, concurrent session limits
enable_banners: true             # DoD login banner, system contact/location
enable_ntp_dns: true             # NTP with auth, DNS servers
enable_snmp_security: true       # SNMPv3 users, disable v1/v2
enable_compliance_report: true   # Generate JSON + text compliance report artifacts
```

### Authentication

```yaml
aci_auth_realm_type: "ldap"      # Options: ldap, radius, tacacs, local
aci_auth_login_domain: "FourthEstate-LDAP"

# LDAP servers (list — primary and secondary)
aci_ldap_servers:
  - host: "{{ vault_aci_ldap_host_1 }}"
    port: 636
    use_ssl: true
    base_dn: "{{ vault_aci_ldap_base_dn }}"
    bind_dn: "{{ vault_aci_ldap_bind_dn }}"
    bind_password: "{{ vault_aci_ldap_bind_password }}"
```

### Password Policy

```yaml
aci_password_min_length: 15          # DoD minimum
aci_password_min_uppercase: 1
aci_password_min_lowercase: 1
aci_password_min_digits: 1
aci_password_min_special: 1
aci_password_history_count: 5        # Prevent reuse
aci_password_expiry_days: 60
aci_lockout_max_attempts: 3          # Account lockout threshold
aci_lockout_duration_seconds: 1800   # 30-minute lockout
```

### Session Management

```yaml
aci_session_timeout: 600     # 10-minute maximum session duration
aci_idle_timeout: 300        # 5-minute idle timeout
aci_max_concurrent_sessions: 10
```

### SNMPv3

```yaml
aci_snmp_v1_enabled: false   # Disabled per STIG
aci_snmp_v2_enabled: false   # Disabled per STIG
aci_snmp_v3_enabled: true

aci_snmp_v3_users:
  - username: "snmpv3-monitor"
    auth_type: "SHA"
    auth_password: "{{ vault_aci_snmp_auth_password }}"
    priv_type: "AES128"
    priv_password: "{{ vault_aci_snmp_priv_password }}"

aci_snmp_trap_destinations:
  - host: "{{ vault_snmp_trap_host }}"
    version: "v3"
    security_level: "auth-priv"

aci_snmp_allowed_clients:
  - "{{ vault_snmp_management_subnet }}"   # e.g., "10.0.10.0/24"
```

## Required Vault Variables

All sensitive values must be stored in `group_vars/all/vault.yml`:

```yaml
# APIC connection
vault_aci_apic_hostname: "apic.example.com"
vault_aci_apic_username: "admin"
vault_aci_apic_password: "your-secure-password"

# LDAP authentication
vault_aci_ldap_host_1: "ldap1.example.com"
vault_aci_ldap_host_2: "ldap2.example.com"
vault_aci_ldap_base_dn: "dc=example,dc=com"
vault_aci_ldap_bind_dn: "cn=ansible-svc,ou=svc,dc=example,dc=com"
vault_aci_ldap_bind_password: "ldap-bind-password"

# SNMPv3
vault_aci_snmp_auth_password: "snmp-auth-password-min-8-chars"
vault_aci_snmp_priv_password: "snmp-priv-password-min-8-chars"
vault_snmp_trap_host: "10.0.10.100"
vault_snmp_management_subnet: "10.0.10.0/24"

# Syslog / audit
vault_syslog_server_primary: "siem.example.com"
vault_syslog_server_secondary: "siem-backup.example.com"

# NTP authentication key
vault_aci_ntp_key: "ntp-hmac-key-string"

# DNS servers
vault_dns_server_primary: "8.8.8.8"
vault_dns_server_secondary: "8.8.4.4"

# System identification (STIG CISC-ND-001470)
vault_aci_system_contact: "NOC Team - noc@example.com"
vault_aci_system_location: "Building A, DC Row 3, Rack 12"

# Organization
vault_fourth_estate_contact: "it@fourthestate.gov"
```

### Optional Vault Variables (if using RADIUS or TACACS+)

```yaml
vault_aci_radius_host_1: "radius.example.com"
vault_aci_radius_key: "radius-shared-secret"
vault_aci_tacacs_host_1: "tacacs.example.com"
vault_aci_tacacs_key: "tacacs-shared-secret"
```

## Generated Artifacts

When `enable_compliance_report: true`, the role writes to `{{ artifacts_dir }}`:

| Artifact | Description |
|----------|-------------|
| `aci_stig_compliance_report.json` | Full pass/fail status per STIG control |
| `aci_stig_compliance_summary.txt` | Human-readable summary with CAT I/II/III breakdown |

## Tags Reference

```bash
# Run all security hardening
--tags security

# Run only specific STIG categories
--tags stig_cat1
--tags stig_cat2
--tags stig_cat3

# Run specific controls
--tags authentication
--tags crypto,tls
--tags rbac
--tags sessions
--tags audit,logging
--tags snmp
--tags ntp,dns
--tags banners
```

## Troubleshooting

**LDAP authentication not working after applying:**
- Verify `vault_aci_ldap_host_1` is reachable from the APIC on port 636
- Check LDAP bind DN and password are correct
- Ensure the LDAP server certificate is trusted by APIC (or set `use_ssl: false` for testing only)

**SNMPv3 passwords rejected:**
- Auth and priv passwords must be at least 8 characters
- SHA auth and AES128 priv are required — MD5 and DES are not STIG-compliant

**Compliance report not generated:**
- Set `enable_compliance_report: true` (default)
- Ensure `artifacts_dir` directory is writable: `mkdir -p /tmp/aci-artifacts`

**NTP authentication failures:**
- The NTP key must match exactly what is configured on the NTP server
- `aci_ntp_key_id` must match the key ID on the NTP server

## Author

Created for Fourth Estate DoD STIG-compliant ACI deployments.
