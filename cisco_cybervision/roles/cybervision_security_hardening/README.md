# cybervision_security_hardening

Ansible role for DoD STIG and NIST 800-53 security hardening of Cisco Cyber Vision Center. Applies authentication, TLS, access control, session management, audit logging, NTP, and DoD login banner controls via the Cyber Vision REST API.

## Quick Start

```bash
# Dry-run (no changes, shows what would apply)
ansible-playbook -i inventory site.yml --tags security --ask-vault-pass

# Apply all STIG controls
ansible-playbook -i inventory site.yml --tags security -e "apply_changes=true" --ask-vault-pass

# Apply only CAT I (critical) controls
ansible-playbook -i inventory site.yml --tags stig_cat1 -e "apply_changes=true" --ask-vault-pass
```

## Role Execution Order

```
Phase 1: cybervision_center_deploy        (center infrastructure)
Phase 2: cybervision_sensor_config        (sensor enrollment)
Phase 3: cybervision_asset_management     (OT asset management)
Phase 4: cybervision_security_hardening   ← this role
Phase 5: cybervision_monitoring           (SIEM, SNMP, ISE)
```

## STIG Controls Implemented

### Category I — High Severity

| STIG ID | Control | Task File |
|---------|---------|-----------|
| CISC-ND-001440 | HTTPS enforced, HTTP disabled | `crypto_tls.yml` |
| CISC-ND-000530 | Password strength policy | `authentication.yml` |
| CISC-ND-000570 | Minimum password length (15 chars) | `authentication.yml` |
| CISC-ND-001190 | Centralized authentication (LDAP) | `authentication.yml` |

### Category II — Medium Severity

| STIG ID | Control | Task File |
|---------|---------|-----------|
| CISC-ND-000370 | Account lockout after 3 failures | `authentication.yml` |
| CISC-ND-000390 | Session idle timeout <= 10 min | `session_management.yml` |
| CISC-ND-000360 | Concurrent session limits | `access_control.yml` |
| CISC-ND-000700 | Audit logging with timestamps | `audit_logging.yml` |
| CISC-ND-000710 | Audit logging with user identity | `audit_logging.yml` |
| CISC-ND-000720 | Audit log protection | `audit_logging.yml` |
| CISC-ND-001420 | NTP configured | `ntp_dns.yml` |

### Category III — Low Severity

| STIG ID | Control | Task File |
|---------|---------|-----------|
| CISC-ND-000080 | DoD mandatory login banner | `banners.yml` |
| CISC-ND-001290 | NTP configuration | `ntp_dns.yml` |
| CISC-ND-001470 | System contact and location | `banners.yml` |

## Feature Toggles

```yaml
stig_cat1_enabled: true       # CAT I (High) — auth, TLS
stig_cat2_enabled: true       # CAT II (Medium) — sessions, audit, NTP
stig_cat3_enabled: true       # CAT III (Low) — banners, system ID

enable_auth_hardening: true      # LDAP + password policy + lockout
enable_access_control: true      # RBAC, session limits
enable_audit_logging: true       # Auth events, config changes, admin actions
enable_crypto_tls: true          # TLS 1.2+, HTTPS only
enable_session_management: true  # Idle/session timeouts
enable_banners: true             # DoD banner + system contact/location
enable_ntp_dns: true             # NTP and DNS servers
enable_compliance_report: true   # JSON + text STIG report artifacts
```

## Required Vault Variables

```yaml
vault_cv_center_hostname: "cybervision.example.com"
vault_cv_api_token: "your-api-bearer-token"

# LDAP authentication
vault_cv_ldap_host_1: "ldap1.example.com"
vault_cv_ldap_host_2: "ldap2.example.com"
vault_cv_ldap_base_dn: "dc=example,dc=com"
vault_cv_ldap_bind_dn: "cn=svc-cybervision,ou=svc,dc=example,dc=com"
vault_cv_ldap_bind_password: "ldap-bind-password"

# System identification (STIG CISC-ND-001470)
vault_cv_system_contact: "NOC Team - noc@example.com"
vault_cv_system_location: "Building A, DC Row 3"

# DNS/NTP
vault_dns_server_primary: "8.8.8.8"
vault_dns_server_secondary: "8.8.4.4"
vault_fourth_estate_contact: "it@fourthestate.gov"
```

## Generated Artifacts

| Artifact | Description |
|----------|-------------|
| `cv_stig_compliance_report.json` | Full pass/fail per STIG control |
| `cv_stig_compliance_summary.txt` | Human-readable CAT I/II/III summary |
| `cv_authentication.json` | Auth config and STIG control status |
| `cv_crypto_tls.json` | TLS settings |
| `cv_session_management.json` | Session/idle timeout values |
| `cv_audit_logging.json` | Audit policy settings |

## Tags

```bash
--tags security          # All security hardening
--tags stig_cat1         # CAT I controls only
--tags stig_cat2         # CAT II controls only
--tags stig_cat3         # CAT III controls only
--tags authentication    # Auth hardening
--tags tls               # TLS/crypto controls
--tags audit,logging     # Audit logging
--tags sessions          # Session management
--tags banners           # Login banner and system ID
```
