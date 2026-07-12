# sdwan_security_hardening

## Requirements

- Ansible 2.15+
- Collections: `ansible.builtin`, `ansible.utils`
- Python: `requests`
- vManage reachable from Ansible control node on port 443
- Valid vault variables for credentials (see defaults)

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sdwan_vmanage_host` | `"{{ vault_sdwan_vmanage_host }}"` | No | vManage Connection Parameters |
| `sdwan_vmanage_port` | `443` | No | — |
| `sdwan_vmanage_username` | `"{{ vault_sdwan_vmanage_username }}"` | No | — |
| `sdwan_vmanage_password` | `"{{ vault_sdwan_vmanage_password }}"` | No | — |
| `sdwan_vmanage_verify_ssl` | `true` | No | — |
| `sdwan_vmanage_timeout` | `30` | No | — |
| `apply_changes` | `false` | No | Deployment Control |
| `sdwan_artifacts_dir` | `"/tmp/sdwan-artifacts"` | No | — |
| `fourth_estate_org` | `"FourthEstate"` | No | Fourth Estate Organization |
| `fourth_estate_contact` | `"{{ vault_fourth_estate_contact }}"` | No | — |
| `fourth_estate_environment` | `"production"` | No | — |
| `fourth_estate_region` | `"primary"` | No | — |
| `stig_cat1_enabled` | `true` | No | STIG Category Feature Toggles |
| `stig_cat2_enabled` | `true` | No | — |
| `stig_cat3_enabled` | `true` | No | — |
| `enable_auth_hardening` | `true` | No | Module Feature Toggles |
| `enable_access_control` | `true` | No | — |
| `enable_password_policy` | `true` | No | — |
| `enable_session_management` | `true` | No | — |
| `enable_audit_logging` | `true` | No | — |
| `enable_crypto_tls` | `true` | No | — |
| `enable_ssh_hardening` | `true` | No | — |
| `enable_snmp_security` | `true` | No | — |
| `enable_ntp_hardening` | `true` | No | — |
| `enable_banners` | `true` | No | — |
| `enable_unused_services` | `true` | No | — |
| `enable_fips_mode` | `true` | No | — |
| `enable_compliance_report` | `true` | No | — |
| `sdwan_auth_method` | `"tacacs"` | No | Authentication Configuration (STIG CAT I) NIST IA-2, IA-3 \| CISC-ND-001190 Applies to: vManage, vBond, vSmart, vEdge/cEdge Options: tacacs, radius, local |
| `sdwan_tacacs_servers` | `(see defaults/main.yml)` | No | TACACS+ Servers (preferred for SD-WAN per DoD guidance) |
| `sdwan_radius_servers` | `[]` | No | RADIUS Servers (alternative to TACACS+) |
| `sdwan_aaa_auth_order` | `(see defaults/main.yml)` | No | AAA login order: try AAA server first, fall back to local |
| `sdwan_password_min_length` | `15` | No | Password Policy (STIG CAT I) NIST IA-5 \| CISC-ND-000530, CISC-ND-000570 |
| `sdwan_password_min_uppercase` | `1` | No | — |
| `sdwan_password_min_lowercase` | `1` | No | — |
| `sdwan_password_min_digits` | `1` | No | — |
| `sdwan_password_min_special` | `1` | No | — |
| `sdwan_password_history_count` | `5` | No | — |
| `sdwan_password_max_age_days` | `60` | No | — |
| `sdwan_password_no_change_interval_hours` | `24` | No | — |
| `sdwan_password_strength_check` | `true` | No | — |
| `sdwan_lockout_enabled` | `true` | No | Account Lockout Policy (STIG CAT II) NIST AC-7 \| CISC-ND-000370 Lock after 3 failed attempts per DoD requirement |
| `sdwan_lockout_max_attempts` | `3` | No | — |
| `sdwan_lockout_window_seconds` | `120` | No | — |
| `sdwan_lockout_duration_seconds` | `900` | No | 15-minute lockout |
| `sdwan_session_idle_timeout` | `600` | No | Session Management (STIG CAT II) NIST AC-11, AC-12 \| CISC-ND-000200, CISC-ND-000390 10 minutes idle timeout (CLI/GUI) |
| `sdwan_session_max_duration` | `28800` | No | 8-hour maximum session |
| `sdwan_session_max_concurrent` | `5` | No | per-user concurrent session limit |
| `sdwan_https_enabled` | `true` | No | TLS and Cryptographic Controls (STIG CAT I) NIST SC-8, SC-28 \| CISC-ND-001440 vManage web interface and API transport security |
| `sdwan_http_enabled` | `false` | No | DISABLED per STIG CISC-ND-001440 |
| `sdwan_min_tls_version` | `"TLSv1.2"` | No | TLS 1.2 minimum; prefer TLS 1.3 |
| `sdwan_allowed_tls_ciphers` | `(see defaults/main.yml)` | No | — |
| `sdwan_ssh_enabled` | `true` | No | SSH Configuration (STIG CAT II) NIST AC-17, SC-8 \| CISC-ND-001400 Applies to all SD-WAN controllers and edge devices |
| `sdwan_telnet_enabled` | `false` | No | DISABLED per STIG CISC-ND-001400 |
| `sdwan_ssh_version` | `2` | No | SSHv2 only per STIG |
| `sdwan_ssh_idle_timeout` | `600` | No | 10-minute SSH idle timeout |
| `sdwan_ssh_max_auth_retries` | `3` | No | — |
| `sdwan_ssh_ciphers` | `(see defaults/main.yml)` | No | — |
| `sdwan_ssh_kex_algorithms` | `(see defaults/main.yml)` | No | — |
| `sdwan_ssh_hmacs` | `(see defaults/main.yml)` | No | — |
| `sdwan_fips_enabled` | `true` | No | FIPS 140-2 Mode (STIG CAT I) NIST SC-13, SC-28 \| DoD IA control requirement Enable FIPS 140-2 validated crypto |
| `sdwan_fips_ipsec_dh_group` | `14` | No | Minimum DH group 14 (2048-bit) |
| `sdwan_fips_ipsec_encryption` | `"aes256-gcm-256"` | No | — |
| `sdwan_fips_ipsec_integrity` | `"sha2-256"` | No | — |
| `sdwan_snmp_v1_enabled` | `false` | No | SNMP Configuration (STIG CAT II) NIST SC-8 \| CISC-ND-000090 SNMPv1/v2c DISABLED; SNMPv3 authPriv REQUIRED DISABLED per STIG CISC-ND-000090 |
| `sdwan_snmp_v2c_enabled` | `false` | No | DISABLED per STIG CISC-ND-000090 |
| `sdwan_snmp_v3_enabled` | `true` | No | REQUIRED per STIG CISC-ND-000090 |
| `sdwan_snmp_community` | `""` | No | Empty — v1/v2c disabled |
| `sdwan_snmp_view_name` | `"sdwan-ro-view"` | No | — |
| `sdwan_snmp_v3_groups` | `(see defaults/main.yml)` | No | — |
| `sdwan_snmp_v3_users` | `(see defaults/main.yml)` | No | — |
| `sdwan_snmp_trap_destinations` | `(see defaults/main.yml)` | No | — |
| `sdwan_snmp_allowed_sources` | `(see defaults/main.yml)` | No | Restrict SNMP access to management subnet |
| `sdwan_syslog_enabled` | `true` | No | Audit Logging Configuration (STIG CAT II) NIST AU-2, AU-3, AU-9, AU-12 \| CISC-ND-000700/710/720 |
| `sdwan_syslog_severity` | `"informational"` | No | Log at informational and above |
| `sdwan_syslog_destinations` | `(see defaults/main.yml)` | No | — |
| `sdwan_audit_all_access` | `true` | No | — |
| `sdwan_audit_config_changes` | `true` | No | — |
| `sdwan_audit_auth_events` | `true` | No | — |
| `sdwan_audit_privilege_use` | `true` | No | — |
| `sdwan_local_log_retention_days` | `90` | No | — |
| `sdwan_ntp_enabled` | `true` | No | NTP Configuration (STIG CAT II) NIST AU-8 \| CISC-ND-001290, CISC-ND-001420 Authenticated NTP required; DoD-approved sources |
| `sdwan_ntp_authenticate` | `true` | No | — |
| `sdwan_ntp_key_id` | `1` | No | — |
| `sdwan_ntp_key` | `"{{ vault_sdwan_ntp_key }}"` | No | — |
| `sdwan_ntp_key_type` | `"md5"` | No | Use SHA when platform supports it |
| `sdwan_ntp_servers` | `(see defaults/main.yml)` | No | — |
| `sdwan_ntp_source_interface` | `"{{ vault_sdwan_mgmt_interface }}"` | No | — |
| `sdwan_login_banner` | `(multi-line text — see defaults/main.yml)` | No | DoD Login Banner (STIG CAT III) NIST AC-8 \| CISC-ND-000080 |
| `sdwan_system_contact` | `"{{ vault_sdwan_system_contact }}"` | No | System Information (STIG CAT III) NIST CM-8 \| CISC-ND-001470 |
| `sdwan_system_location` | `"{{ vault_sdwan_system_location }}"` | No | — |
| `sdwan_system_description` | `"Fourth Estate Cisco SD-WAN - DoD STIG Compliant"` | No | — |
| `sdwan_organization_name` | `"FourthEstate"` | No | — |
| `sdwan_rbac_enabled` | `true` | No | RBAC - Role-Based Access Control (STIG CAT II) NIST AC-2, AC-3, AC-6 \| CISC-ND-000360 |
| `sdwan_user_groups` | `(see defaults/main.yml)` | No | User groups for vManage RBAC |
| `sdwan_local_users` | `(see defaults/main.yml)` | No | Local break-glass and automation service accounts |
| `sdwan_disable_http_server` | `true` | No | Unused Services Hardening (STIG CAT II) NIST CM-7 \| CISC-ND-001200, CISC-ND-001210 Disable HTTP; use HTTPS only |
| `sdwan_disable_telnet` | `true` | No | Disable telnet; use SSH only |
| `sdwan_disable_finger` | `true` | No | — |
| `sdwan_disable_tcp_small_servers` | `true` | No | — |
| `sdwan_disable_udp_small_servers` | `true` | No | — |
| `sdwan_disable_ip_identd` | `true` | No | — |
| `sdwan_disable_cdp_global` | `false` | No | CDP may be required; review per site |
| `sdwan_disable_lldp` | `false` | No | LLDP may be required; review per site |
| `sdwan_ipsec_enabled` | `true` | No | Control Plane Security (IPSec) NIST SC-8, SC-17 \| SD-WAN data-plane encryption |
| `sdwan_ipsec_rekey_interval` | `86400` | No | 24-hour rekey |
| `sdwan_ipsec_replay_window` | `512` | No | — |
| `sdwan_ipsec_integrity` | `"ip-udp-esp"` | No | — |
| `sdwan_ipsec_cipher_suite` | `"aes256-gcm"` | No | — |
| `sdwan_dtls_port` | `12346` | No | DTLS for control plane |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |

## Example Playbook

```yaml
- name: Cisco SD-WAN STIG Hardening
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    apply_changes: true   # Remove this line for dry-run

  tasks:
    - name: Apply SD-WAN STIG hardening
      ansible.builtin.include_role:
        name: sdwan_security_hardening
```

Run dry-run first:
```bash
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml --ask-vault-pass
```

Apply changes:
```bash
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml \
  -e apply_changes=true --ask-vault-pass
```

Run specific STIG category only:
```bash
# CAT I controls only
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml \
  --tags stig_cat1 --ask-vault-pass

# Authentication and logging only
ansible-playbook -i inventory cisco/playbooks/06_sdwan_phase5_security_hardening.yml \
  --tags "authentication,logging" -e apply_changes=true --ask-vault-pass
```

## Tags

| Tag | Description |
|-----|-------------|
| `sdwan` | All SD-WAN tasks |
| `security` | All security hardening tasks |
| `stig` | All STIG controls |
| `stig_cat1` | STIG CAT I (High) controls only |
| `stig_cat2` | STIG CAT II (Medium) controls only |
| `stig_cat3` | STIG CAT III (Low) controls only |
| `authentication` | AAA / TACACS+ / RADIUS |
| `passwords` | Password policy |
| `sessions` | Session management |
| `banners` | DoD login banner |
| `snmp` | SNMPv3 configuration |
| `logging` | Audit / syslog configuration |
| `ntp` | NTP authentication |
| `ssh` | SSH hardening |
| `crypto` / `tls` | TLS and cryptographic controls |
| `fips` | FIPS 140-2 mode |
| `rbac` | Role-based access control |
| `services` | Unused service disable |
| `phase19` | All Phase 19 tasks |
| `report` | Generate compliance report only |

## Overview

Hardens Cisco SD-WAN components — vManage, vBond, vSmart, and vEdge/cEdge edge devices — against the **Cisco IOS XE SD-WAN Router NDM STIG V2R1** and **Cisco SD-WAN vManage NDM STIG V1R1**. All controls are mapped to NIST SP 800-53 Rev 5. This is Phase 19 of the Fourth Estate Cisco SD-WAN deployment.

## Features

- **STIG CAT I** — Authentication (TACACS+/RADIUS), Password Policy (15-char min), TLS 1.2+, FIPS 140-2
- **STIG CAT II** — RBAC/Least Privilege, Account Lockout (3 attempts / 15 min), Session Timeout (10 min idle), SNMPv3 authPriv, Audit Logging to SIEM, Authenticated NTP, SSH v2 hardening, Disable unused services
- **STIG CAT III** — DoD Warning Banner (AC-8)
- Generates JSON and text STIG compliance reports in `sdwan_artifacts_dir`
- Defaults to **dry-run mode** (`apply_changes: false`) — safe to run without impacting production

## Dependencies

None. Runs standalone against vManage REST API.

## Compliance

### DISA STIG Controls Implemented

| STIG ID | Title | CAT | NIST Control |
|---------|-------|-----|--------------|
| CISC-ND-000080 | DoD Login Banner | III | AC-8 |
| CISC-ND-000090 | SNMPv3 Required (disable v1/v2c) | II | SC-8 |
| CISC-ND-000200 | Session Idle Timeout (10 min) | II | AC-12 |
| CISC-ND-000360 | RBAC Least Privilege | II | AC-2, AC-3, AC-6 |
| CISC-ND-000370 | Account Lockout (3 attempts) | II | AC-7 |
| CISC-ND-000390 | Idle Timeout Enforcement | II | AC-11 |
| CISC-ND-000530 | Password Complexity | I | IA-5 |
| CISC-ND-000570 | Password Minimum Length (15 chars) | I | IA-5 |
| CISC-ND-000700 | Audit Event Logging | II | AU-2 |
| CISC-ND-000710 | Audit Record Content | II | AU-3 |
| CISC-ND-000720 | Audit Log Protection | II | AU-9 |
| CISC-ND-001190 | TACACS+/RADIUS Authentication | I | IA-2, IA-3 |
| CISC-ND-001200 | Disable Unused Services | II | CM-7 |
| CISC-ND-001290 | Authenticated NTP | II | AU-8 |
| CISC-ND-001400 | SSH v2 / Disable Telnet | II | SC-8, AC-17 |
| CISC-ND-001420 | NTP Trusted Servers | II | AU-8 |
| CISC-ND-001440 | TLS 1.2+ / Disable HTTP / FIPS | I | SC-8, SC-13 |

### NIST SP 800-53 Rev 5 Controls

`AC-2`, `AC-3`, `AC-6`, `AC-7`, `AC-8`, `AC-11`, `AC-12`, `AC-17`, `AU-2`, `AU-3`, `AU-8`, `AU-9`, `AU-12`, `CM-6`, `CM-7`, `IA-2`, `IA-3`, `IA-5`, `SC-8`, `SC-13`, `SC-17`, `SC-28`

## Artifacts Generated

| File | Description |
|------|-------------|
| `sdwan_stig_compliance_<epoch>.json` | Machine-readable compliance status for all STIG controls |
| `sdwan_stig_summary_<epoch>.txt` | Human-readable STIG compliance summary |

## Author

Fourth Estate Infrastructure Team

## License

MIT
