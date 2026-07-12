# cybervision_security_hardening

Ansible role for DoD STIG and NIST 800-53 security hardening of Cisco Cyber Vision Center. Applies authentication, TLS, access control, session management, audit logging, NTP, and DoD login banner controls via the Cyber Vision REST API.

## Requirements

- Ansible 2.15+
- Collection: `community.general` (`ansible-galaxy collection install community.general`)
- Collection: `ansible.utils` (`ansible-galaxy collection install ansible.utils`)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cv_center_host` | `"{{ vault_cv_center_hostname }}"` | No | Cyber Vision Center API Connection |
| `cv_api_url` | `"https://{{ cv_center_host }}/api/3.0"` | No | — |
| `cv_api_token` | `"{{ vault_cv_api_token }}"` | No | — |
| `cv_validate_certs` | `true` | No | — |
| `cv_use_proxy` | `false` | No | — |
| `cv_timeout` | `60` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `artifacts_dir` | `"/tmp/cv-artifacts"` | No | — |
| `cv_org_name` | `"FourthEstate"` | No | Fourth Estate Organization |
| `cv_org_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `cv_environment` | `"production"` | No | — |
| `stig_cat1_enabled` | `true` | No | STIG Category Feature Toggles |
| `stig_cat2_enabled` | `true` | No | — |
| `stig_cat3_enabled` | `true` | No | — |
| `enable_auth_hardening` | `true` | No | Module Feature Toggles |
| `enable_access_control` | `true` | No | — |
| `enable_audit_logging` | `true` | No | — |
| `enable_crypto_tls` | `true` | No | — |
| `enable_session_management` | `true` | No | — |
| `enable_banners` | `true` | No | — |
| `enable_ntp_dns` | `true` | No | — |
| `enable_compliance_report` | `true` | No | — |
| `cv_auth_type` | `"ldap"` | No | Authentication Configuration NIST IA-2, IA-5 \| STIG CISC-ND-001190 Options: local, ldap, radius, tacacs |
| `cv_ldap_enabled` | `true` | No | LDAP Configuration |
| `cv_ldap_servers` | `(see defaults/main.yml)` | No | — |
| `cv_ldap_group_mappings` | `(see defaults/main.yml)` | No | — |
| `cv_radius_enabled` | `false` | No | RADIUS (optional) |
| `cv_radius_servers` | `[]` | No | — |
| `cv_tacacs_enabled` | `false` | No | TACACS+ (optional) |
| `cv_tacacs_servers` | `[]` | No | — |
| `cv_password_min_length` | `15` | No | Password Policy (STIG CAT I) NIST IA-5 \| STIG CISC-ND-000530, CISC-ND-000570 |
| `cv_password_min_uppercase` | `1` | No | — |
| `cv_password_min_lowercase` | `1` | No | — |
| `cv_password_min_digits` | `1` | No | — |
| `cv_password_min_special` | `1` | No | — |
| `cv_password_history_count` | `5` | No | — |
| `cv_password_expiry_days` | `60` | No | — |
| `cv_password_strength_check` | `true` | No | — |
| `cv_lockout_enabled` | `true` | No | Account Lockout Policy (STIG CAT II) NIST AC-7 \| STIG CISC-ND-000370 |
| `cv_lockout_max_attempts` | `3` | No | — |
| `cv_lockout_window_seconds` | `300` | No | — |
| `cv_lockout_duration_seconds` | `1800` | No | — |
| `cv_session_timeout` | `600` | No | Session Management (STIG CAT II) NIST AC-11, AC-12 \| STIG CISC-ND-000390 10 minutes — maximum session duration |
| `cv_idle_timeout` | `300` | No | 5 minutes — idle/inactivity timeout |
| `cv_max_concurrent_sessions` | `10` | No | — |
| `cv_https_only` | `true` | No | TLS Configuration (STIG CAT I) NIST SC-8 \| STIG CISC-ND-001440 Disable HTTP — enforce HTTPS only |
| `cv_min_tls_version` | `"TLSv1.2"` | No | — |
| `cv_allowed_ciphers` | `(see defaults/main.yml)` | No | — |
| `cv_audit_enabled` | `true` | No | Audit Logging (STIG CAT II) NIST AU-2, AU-3, AU-9, AU-12 \| STIG CISC-ND-000700/710/720 |
| `cv_audit_log_auth_events` | `true` | No | — |
| `cv_audit_log_config_changes` | `true` | No | — |
| `cv_audit_log_admin_actions` | `true` | No | — |
| `cv_audit_log_retention_days` | `90` | No | — |
| `cv_ntp_servers` | `(see defaults/main.yml)` | No | NTP Configuration (STIG CAT II/III) NIST AU-8 \| STIG CISC-ND-001290, CISC-ND-001420 |
| `cv_dns_servers` | `(see defaults/main.yml)` | No | DNS |
| `cv_login_banner` | `(multi-line text — see defaults/main.yml)` | No | DoD Login Banner (STIG CAT III) NIST AC-8 \| STIG CISC-ND-000080 |
| `cv_system_contact` | `"{{ vault_cv_system_contact }}"` | No | System Identification (STIG CAT III) NIST CM-8 \| STIG CISC-ND-001470 |
| `cv_system_location` | `"{{ vault_cv_system_location }}"` | No | — |
| `cv_system_description` | `"Fourth Estate OT Security Platform - DoD STIG Compliant"` | No | — |
| `cv_roles` | `(see defaults/main.yml)` | No | RBAC Roles NIST AC-2, AC-3, AC-6 \| STIG CISC-ND-000360 |

## Example Playbook

```yaml
- name: Use cybervision_security_hardening
  hosts: all
  gather_facts: false
  roles:
    - role: cybervision_security_hardening
      vars:
        apply_changes: false   # set true to apply
```

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

## License

MIT
