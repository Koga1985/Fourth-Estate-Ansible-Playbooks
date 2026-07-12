# aci_security_hardening

Ansible role for DoD STIG and NIST 800-53 security hardening of Cisco ACI fabrics. Implements all applicable DISA STIG findings for Cisco network devices in ACI environments.

## Requirements

- `cisco.aci` collection >= 2.8.0
- ACI APIC version 5.x or later
- Admin credentials stored in Ansible Vault
- Network access to APIC on port 443

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `aci_host` | `"{{ vault_aci_apic_hostname }}"` | No | APIC Connection Parameters |
| `aci_username` | `"{{ vault_aci_apic_username }}"` | No | — |
| `aci_password` | `"{{ vault_aci_apic_password }}"` | No | — |
| `aci_verify_ssl` | `true` | No | — |
| `aci_use_proxy` | `false` | No | — |
| `aci_timeout` | `30` | No | — |
| `aci_port` | `443` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `artifacts_dir` | `"/tmp/aci-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Organization |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `fourth_estate_environment` | `"production"` | No | — |
| `fourth_estate_region` | `"primary"` | No | — |
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
| `enable_snmp_security` | `true` | No | — |
| `enable_compliance_report` | `true` | No | — |
| `aci_auth_realm_type` | `"ldap"` | No | Authentication Configuration NIST IA-2, IA-5 \| STIG CISC-ND-001190, CISC-ND-000530 Options: ldap, radius, tacacs, local |
| `aci_ldap_servers` | `(see defaults/main.yml)` | No | LDAP Authentication Providers (STIG CISC-ND-001190) |
| `aci_radius_servers` | `[]` | No | RADIUS Authentication Providers (STIG CISC-ND-001190) |
| `aci_tacacs_servers` | `[]` | No | TACACS+ Authentication Providers (STIG CISC-ND-001190) |
| `aci_auth_login_domain` | `"FourthEstate-LDAP"` | No | Authentication Login Domain |
| `aci_auth_default_realm` | `"ldap"` | No | — |
| `aci_password_min_length` | `15` | No | Password Policy (STIG CAT I) NIST IA-5 \| STIG CISC-ND-000530, CISC-ND-000570 |
| `aci_password_min_uppercase` | `1` | No | — |
| `aci_password_min_lowercase` | `1` | No | — |
| `aci_password_min_digits` | `1` | No | — |
| `aci_password_min_special` | `1` | No | — |
| `aci_password_history_count` | `5` | No | — |
| `aci_password_expiry_days` | `60` | No | — |
| `aci_password_no_change_interval` | `24` | No | — |
| `aci_password_strength_check` | `true` | No | — |
| `aci_lockout_enabled` | `true` | No | Account Lockout Policy (STIG CAT II) NIST AC-7 \| STIG CISC-ND-000370 |
| `aci_lockout_max_attempts` | `3` | No | — |
| `aci_lockout_window_seconds` | `300` | No | — |
| `aci_lockout_duration_seconds` | `1800` | No | — |
| `aci_session_timeout` | `600` | No | Session Management (STIG CAT II) NIST AC-11, AC-12 \| STIG CISC-ND-000390 10 minutes - maximum session duration |
| `aci_idle_timeout` | `300` | No | 5 minutes - idle/inactivity timeout |
| `aci_max_concurrent_sessions` | `10` | No | — |
| `aci_https_enabled` | `true` | No | TLS and Cryptographic Controls (STIG CAT I) NIST SC-8, SC-28 \| STIG CISC-ND-001440, CISC-ND-001400 |
| `aci_http_enabled` | `false` | No | DISABLED per STIG CISC-ND-001440 |
| `aci_min_tls_version` | `"tls1.2"` | No | TLS 1.2 minimum per STIG CISC-ND-001440 |
| `aci_allowed_ciphers` | `(see defaults/main.yml)` | No | — |
| `aci_key_exchange_algos` | `(see defaults/main.yml)` | No | — |
| `aci_ssh_enabled` | `true` | No | SSH Configuration (STIG CAT II) NIST AC-17, SC-8 \| STIG CISC-ND-001400 |
| `aci_telnet_enabled` | `false` | No | DISABLED per STIG CISC-ND-001400 |
| `aci_ssh_ciphers` | `(see defaults/main.yml)` | No | — |
| `aci_ssh_kex_algos` | `(see defaults/main.yml)` | No | — |
| `aci_ssh_macs` | `(see defaults/main.yml)` | No | — |
| `aci_snmp_v1_enabled` | `false` | No | SNMP Configuration (STIG CAT II) NIST SC-8 \| STIG CISC-ND-000090 DISABLED per STIG CISC-ND-000090 |
| `aci_snmp_v2_enabled` | `false` | No | DISABLED per STIG CISC-ND-000090 |
| `aci_snmp_v3_enabled` | `true` | No | REQUIRED per STIG CISC-ND-000090 |
| `aci_snmp_v3_users` | `(see defaults/main.yml)` | No | — |
| `aci_snmp_trap_destinations` | `(see defaults/main.yml)` | No | — |
| `aci_snmp_allowed_clients` | `(see defaults/main.yml)` | No | SNMP access control - restrict to management subnet |
| `aci_syslog_enabled` | `true` | No | Audit Logging Configuration (STIG CAT II) NIST AU-2, AU-3, AU-9, AU-12 \| STIG CISC-ND-000700/710/720 |
| `aci_syslog_destinations` | `(see defaults/main.yml)` | No | — |
| `aci_audit_all_access` | `true` | No | — |
| `aci_audit_config_changes` | `true` | No | — |
| `aci_audit_auth_events` | `true` | No | — |
| `aci_local_log_retention_days` | `90` | No | — |
| `aci_ntp_enabled` | `true` | No | NTP Configuration (STIG CAT II/III) NIST AU-8 \| STIG CISC-ND-001290, CISC-ND-001420 |
| `aci_ntp_authenticate` | `true` | No | — |
| `aci_ntp_key` | `"{{ vault_aci_ntp_key }}"` | No | — |
| `aci_ntp_key_id` | `1` | No | — |
| `aci_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `aci_dns_servers` | `(see defaults/main.yml)` | No | DNS Configuration |
| `aci_dns_search_domains` | `(see defaults/main.yml)` | No | — |
| `aci_login_banner` | `(multi-line text — see defaults/main.yml)` | No | DoD Login Banner (STIG CAT III) NIST AC-8 \| STIG CISC-ND-000080 |
| `aci_system_contact` | `"{{ vault_aci_system_contact }}"` | No | System Information (STIG CAT III) NIST CM-8 \| STIG CISC-ND-001470 |
| `aci_system_location` | `"{{ vault_aci_system_location }}"` | No | — |
| `aci_system_description` | `"Fourth Estate ACI Fabric - DoD STIG Compliant"` | No | — |
| `aci_security_domains` | `(see defaults/main.yml)` | No | RBAC and Security Domains NIST AC-2, AC-3, AC-6 \| STIG CISC-ND-000360 |
| `aci_local_users` | `(see defaults/main.yml)` | No | Local service accounts (break-glass and automation only) |
| `aci_user_roles` | `(see defaults/main.yml)` | No | RBAC user role mappings from LDAP groups |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

## Example Playbook

```yaml
- name: Use aci_security_hardening
  hosts: all
  gather_facts: false
  roles:
    - role: aci_security_hardening
      vars:
        apply_changes: false   # set true to apply
```

## Tags

| Tag | Description |
|-----|-------------|
| `aci` | Tasks tagged `aci` |
| `artifact` | Tasks tagged `artifact` |
| `audit` | Tasks tagged `audit` |
| `authentication` | Tasks tagged `authentication` |
| `banners` | Tasks tagged `banners` |
| `compliance` | Tasks tagged `compliance` |
| `crypto` | Tasks tagged `crypto` |
| `dns` | Tasks tagged `dns` |
| `ldap` | Tasks tagged `ldap` |
| `logging` | Tasks tagged `logging` |
| `nist_ac` | Tasks tagged `nist_ac` |
| `nist_au` | Tasks tagged `nist_au` |
| `nist_au_2` | Tasks tagged `nist_au_2` |
| `nist_au_3` | Tasks tagged `nist_au_3` |
| `nist_au_8` | Tasks tagged `nist_au_8` |
| `nist_ia` | Tasks tagged `nist_ia` |
| `nist_sc` | Tasks tagged `nist_sc` |
| `nist_sc_8` | Tasks tagged `nist_sc_8` |
| `ntp` | Tasks tagged `ntp` |
| `phase4` | Tasks tagged `phase4` |
| `prerequisites` | Tasks tagged `prerequisites` |
| `query` | Tasks tagged `query` |
| `radius` | Tasks tagged `radius` |
| `rbac` | Tasks tagged `rbac` |
| `report` | Tasks tagged `report` |
| `security` | Tasks tagged `security` |
| `sessions` | Tasks tagged `sessions` |
| `snmp` | Tasks tagged `snmp` |
| `ssh` | Tasks tagged `ssh` |
| `stig` | Tasks tagged `stig` |
| `stig_cat1` | Tasks tagged `stig_cat1` |
| `stig_cat2` | Tasks tagged `stig_cat2` |
| `stig_cat3` | Tasks tagged `stig_cat3` |
| `syslog` | Tasks tagged `syslog` |
| `tacacs` | Tasks tagged `tacacs` |
| `tls` | Tasks tagged `tls` |
| `validation` | Tasks tagged `validation` |

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

## License

MIT
