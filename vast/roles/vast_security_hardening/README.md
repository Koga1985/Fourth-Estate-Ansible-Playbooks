# vast_security_hardening

## Overview

This role applies DoD STIG and NIST 800-53 security hardening to VAST Data
cluster management interfaces. It configures access control, authentication,
encryption, audit logging, protocol security, network security, and compliance
reporting — bringing the VAST management plane into alignment with federal
security requirements.

## Features

- LDAP / Active Directory integration for centralized authentication (STIG V-238197)
- Password policy enforcement — length, complexity, history, lockout (STIG V-238199)
- Session management — inactivity timeout and concurrent session limits (STIG V-238201)
- FIPS 140-2 mode and TLS 1.2+ enforcement with approved cipher suites (STIG V-238203)
- Audit logging of all admin actions, access events, and configuration changes (STIG V-238205)
- SMB signing and encryption enforcement; NFS secure port requirement (STIG V-238207)
- Access-based enumeration and Unix permission enforcement (STIG V-238209)
- Management network firewall restrictions (STIG V-238211)
- Vulnerability scanning schedule configuration (STIG V-238213)
- Backup and DR encryption enforcement (STIG V-238215)
- Automated compliance report generation — NIST 800-53, NIST 800-171, DoD STIG (STIG V-238217)
- DoD PKI certificate validation enforcement (STIG V-238219)
- Multi-factor authentication configuration (NIST 800-63B)
- SIEM integration for centralized log forwarding

## Requirements

- Ansible >= 2.15
- Collections: `ansible.builtin`
- Python packages: `requests >= 2.28`
- Network reachability to the VAST management interface (TCP 443)
- VAST cluster running VAST OS 4.x or later
- LDAP/AD server accessible from the VAST cluster (if `vast_enable_ldap: true`)

## Role Variables

### Connection Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `vast_mgmt_host` | `{{ vault_vast_mgmt_host }}` | VAST cluster management IP or FQDN |
| `vast_mgmt_port` | `443` | Management API port |
| `vast_mgmt_user` | `{{ vault_vast_mgmt_user }}` | Admin username |
| `vast_mgmt_password` | `{{ vault_vast_mgmt_password }}` | Admin password (vault-encrypted) |
| `vast_api_version` | `v1` | VAST REST API version |
| `vast_verify_ssl` | `true` | Validate TLS certificate |

### Access Control

| Variable | Default | Description |
|----------|---------|-------------|
| `vast_enable_ldap` | `true` | Enable LDAP authentication |
| `vast_ldap_server` | `{{ vault_ldap_server }}` | LDAP server FQDN |
| `vast_ldap_port` | `636` | LDAP port (636 = LDAPS) |
| `vast_ldap_use_ssl` | `true` | Require LDAPS |
| `vast_ldap_base_dn` | `{{ vault_ldap_base_dn }}` | LDAP base DN |
| `vast_enable_active_directory` | `true` | Enable AD integration |
| `vast_ad_domain` | `{{ vault_ad_domain }}` | Active Directory domain |
| `vast_require_kerberos` | `true` | Require Kerberos for AD auth |

### Password Policy

| Variable | Default | Description |
|----------|---------|-------------|
| `vast_password_min_length` | `15` | Minimum password length (STIG requirement) |
| `vast_password_complexity_required` | `true` | Enforce complexity rules |
| `vast_password_max_age_days` | `60` | Maximum password age in days |
| `vast_password_history_count` | `24` | Number of previous passwords to remember |
| `vast_account_lockout_threshold` | `3` | Failed attempts before lockout |
| `vast_account_lockout_duration_minutes` | `15` | Lockout duration |

### Encryption

| Variable | Default | Description |
|----------|---------|-------------|
| `vast_enforce_encryption_at_rest` | `true` | Require data-at-rest encryption |
| `vast_enforce_encryption_in_transit` | `true` | Require TLS for all data transfers |
| `vast_fips_140_2_mode` | `true` | Enable FIPS 140-2 mode |
| `vast_tls_min_version` | `1.2` | Minimum TLS version |
| `vast_disable_weak_ciphers` | `true` | Disable weak cipher suites |
| `vast_allowed_cipher_suites` | See defaults | Approved cipher suite list |

### Protocol Security

| Variable | Default | Description |
|----------|---------|-------------|
| `vast_disable_smb1` | `true` | Disable SMBv1 (required by STIG) |
| `vast_smb_signing_required` | `true` | Require SMB packet signing |
| `vast_smb_encryption_required` | `true` | Require SMB encryption |
| `vast_nfs_require_secure_port` | `true` | Restrict NFS to privileged ports |
| `vast_disable_anonymous_access` | `true` | Block anonymous share access |

### Audit Logging

| Variable | Default | Description |
|----------|---------|-------------|
| `vast_audit_all_access` | `true` | Audit all file/share access |
| `vast_audit_admin_actions` | `true` | Audit all admin operations |
| `vast_audit_failed_logins` | `true` | Audit failed authentication |
| `vast_audit_config_changes` | `true` | Audit configuration changes |
| `vast_audit_log_retention_days` | `365` | Log retention period |
| `vast_send_logs_to_siem` | `true` | Forward logs to SIEM |
| `vast_siem_server` | `{{ vault_siem_server }}` | SIEM server address |

## Dependencies

None. This role can be run independently or as part of the VAST full deployment pipeline.

## Example Playbook

```yaml
---
- name: VAST Security Hardening
  hosts: localhost
  connection: local
  gather_facts: false
  any_errors_fatal: true

  vars:
    apply_changes: false    # Default: dry-run mode

  roles:
    - role: vast_security_hardening
```

Apply changes:
```bash
ansible-playbook vast/site.yml -i vast/inventory \
  -e "apply_changes=true" \
  --tags security \
  --ask-vault-pass
```

Run only encryption hardening:
```bash
ansible-playbook vast/site.yml -i vast/inventory \
  -e "apply_changes=true" \
  --tags encryption \
  --ask-vault-pass
```

## Tags

| Tag | Description |
|-----|-------------|
| `security` | All hardening tasks |
| `access_control` | LDAP/AD integration and user restrictions |
| `authentication` | Password policy and MFA configuration |
| `encryption` | TLS, FIPS, cipher suite configuration |
| `audit` | Audit logging and SIEM forwarding |
| `protocol_security` | SMB, NFS, and anonymous access settings |
| `network_security` | Management network firewall rules |
| `compliance` | Compliance report generation |

## Compliance Mapping

### DoD STIG Controls

| STIG ID | Control | Implementation |
|---------|---------|----------------|
| V-238197 | AC-2, AC-3 | LDAP/AD integration enforces centralized identity management |
| V-238199 | IA-5 | Password policy enforces length, complexity, history, and age |
| V-238201 | AC-11, AC-12 | Session timeout and concurrent session limits |
| V-238203 | SC-8, SC-28 | FIPS 140-2, TLS 1.2+, approved cipher suites |
| V-238205 | AU-2, AU-9, AU-12 | Comprehensive audit logging with integrity protection |
| V-238207 | SC-8 | SMB signing, SMB encryption, NFS secure port |
| V-238209 | AC-3, AC-6 | Access-based enumeration, Unix permission enforcement |
| V-238211 | SC-7 | Management interface restricted to defined networks |
| V-238213 | RA-5, SI-2 | Scheduled vulnerability scanning |
| V-238215 | CP-9, SC-28 | Backup encryption and integrity verification |
| V-238217 | CA-7 | Automated compliance report generation |
| V-238219 | IA-5, SC-17 | DoD PKI certificate enforcement |

### NIST 800-53 Rev 5 Controls

| Control Family | Controls | Implementation |
|---------------|---------|----------------|
| Access Control (AC) | AC-2, AC-3, AC-6, AC-11, AC-12 | LDAP/AD, session management, least privilege |
| Audit & Accountability (AU) | AU-2, AU-9, AU-12 | Comprehensive audit logging, log integrity, SIEM forwarding |
| Identification & Auth (IA) | IA-2, IA-5 | MFA support, strong password policy |
| System & Comm Protection (SC) | SC-7, SC-8, SC-17, SC-28 | Network boundary, TLS, PKI, encryption at rest |
| System & Info Integrity (SI) | SI-2 | Vulnerability scanning schedule |
| Risk Assessment (RA) | RA-5 | Vulnerability management configuration |
| Contingency Planning (CP) | CP-9 | Backup encryption enforcement |

## Vault Variables Required

Add these to your encrypted vault file before running:

```yaml
# Required
vault_vast_mgmt_host: "vast-cluster.yourdomain.com"
vault_vast_mgmt_user: "admin"
vault_vast_mgmt_password: "your-password"

# Required if vast_enable_ldap: true
vault_ldap_server: "ldap.yourdomain.com"
vault_ldap_base_dn: "DC=yourdomain,DC=com"

# Required if vast_enable_active_directory: true
vault_ad_domain: "yourdomain.com"

# Required if vast_send_logs_to_siem: true
vault_siem_server: "siem.yourdomain.com"
```

## Author

Fourth Estate Infrastructure Team
