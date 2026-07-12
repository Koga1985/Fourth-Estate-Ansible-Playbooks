# splunk_security_hardening

Applies DoD STIG and NIST 800-53 security hardening to an existing Splunk Enterprise installation. Covers access control, session management, audit logging, password policy, TLS enforcement, and file permissions.

## Requirements

- Ansible 2.15+
- Splunk Enterprise installed (run `splunk_enterprise_install` role first)
- `vault_splunk_admin_password` defined in vault.yml

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_home` | `"/opt/splunk"` | No | Splunk Installation |
| `splunk_user` | `"splunk"` | No | — |
| `splunk_group` | `"splunk"` | No | — |
| `splunk_admin_password` | `"{{ vault_splunk_admin_password }}"` | No | — |
| `stig_cat1_enabled` | `true` | No | STIG Compliance Settings High severity findings |
| `stig_cat2_enabled` | `true` | No | Medium severity findings |
| `stig_cat3_enabled` | `true` | No | Low severity findings |
| `ac_enforce_least_privilege` | `true` | No | Access Control (AC) - NIST 800-53 AC family |
| `ac_session_timeout_minutes` | `15` | No | — |
| `ac_max_failed_login_attempts` | `3` | No | — |
| `ac_account_lockout_duration_minutes` | `15` | No | — |
| `ac_disable_default_accounts` | `true` | No | — |
| `ac_remove_unnecessary_accounts` | `true` | No | — |
| `au_enable_comprehensive_logging` | `true` | No | Audit and Accountability (AU) - NIST 800-53 AU family |
| `au_audit_admin_actions` | `true` | No | — |
| `au_audit_failed_access_attempts` | `true` | No | — |
| `au_audit_privileged_functions` | `true` | No | — |
| `au_log_retention_days` | `365` | No | — |
| `au_protect_audit_logs` | `true` | No | — |
| `au_audit_log_immutable` | `true` | No | — |
| `ia_password_min_length` | `15` | No | Identification and Authentication (IA) - NIST 800-53 IA family |
| `ia_password_complexity_required` | `true` | No | — |
| `ia_password_max_age_days` | `60` | No | — |
| `ia_password_history_count` | `24` | No | — |
| `ia_enforce_mfa` | `true` | No | — |
| `ia_disable_anonymous_access` | `true` | No | — |
| `ia_session_lock_enabled` | `true` | No | — |
| `sc_enforce_fips_140_2` | `true` | No | System and Communications Protection (SC) - NIST 800-53 SC family |
| `sc_tls_min_version` | `"1.2"` | No | — |
| `sc_disable_weak_ciphers` | `true` | No | — |
| `sc_disable_sslv3` | `true` | No | — |
| `sc_disable_tls_10` | `true` | No | — |
| `sc_disable_tls_11` | `true` | No | — |
| `sc_enable_perfect_forward_secrecy` | `true` | No | — |
| `sc_cipher_suite` | `"ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256"` | No | — |
| `cm_disable_unnecessary_services` | `true` | No | Configuration Management (CM) - NIST 800-53 CM family |
| `cm_disable_sample_apps` | `true` | No | — |
| `cm_remove_default_content` | `true` | No | — |
| `cm_baseline_configuration_tracking` | `true` | No | — |
| `cm_config_change_detection` | `true` | No | — |
| `si_enable_integrity_checks` | `true` | No | System and Information Integrity (SI) - NIST 800-53 SI family |
| `si_malware_protection` | `false` | No | External AV recommended |
| `si_file_integrity_monitoring` | `true` | No | — |
| `si_error_handling_secure` | `true` | No | — |
| `si_input_validation` | `true` | No | — |
| `mp_data_at_rest_encryption` | `true` | No | Media Protection (MP) - NIST 800-53 MP family |
| `mp_secure_data_disposal` | `true` | No | — |
| `mp_removable_media_disabled` | `true` | No | — |
| `pe_physical_access_controls` | `true` | No | Physical and Environmental Protection (PE) - NIST 800-53 PE family Organizational control |
| `ra_vulnerability_scanning_enabled` | `true` | No | Risk Assessment (RA) - NIST 800-53 RA family |
| `ra_vulnerability_scan_schedule` | `"weekly"` | No | — |
| `sa_software_integrity_verification` | `true` | No | System and Services Acquisition (SA) - NIST 800-53 SA family |
| `sa_disable_software_updates` | `true` | No | Manual updates in production |
| `ca_continuous_monitoring` | `true` | No | Security Assessment and Authorization (CA) - NIST 800-53 CA family |
| `ca_security_assessment_schedule` | `"monthly"` | No | — |
| `ma_maintenance_logging` | `true` | No | Maintenance (MA) - NIST 800-53 MA family |
| `ma_controlled_maintenance` | `true` | No | — |
| `ir_incident_logging` | `true` | No | Incident Response (IR) - NIST 800-53 IR family |
| `ir_siem_integration` | `true` | No | — |
| `ir_siem_server` | `"{{ vault_siem_server \| default('') }}"` | No | — |
| `hardening_disable_scripted_inputs` | `false` | No | Hardening Specific Settings |
| `hardening_disable_http_event_collector` | `false` | No | — |
| `hardening_restrict_network_access` | `true` | No | — |
| `hardening_remove_search_artifacts` | `true` | No | — |
| `hardening_secure_kvstore` | `true` | No | — |
| `hardening_enable_token_authentication` | `true` | No | — |
| `dod_banner_enabled` | `true` | No | Banner and Notifications |
| `dod_banner_text` | `(multi-line text — see defaults/main.yml)` | No | — |
| `network_allowed_ips` | `"{{ splunk_allowed_management_networks \| default(['10.0.0.0/8', '17...` | No | Network Hardening |
| `network_enable_rate_limiting` | `true` | No | — |
| `network_max_connections` | `1000` | No | — |
| `fs_strict_permissions` | `true` | No | File System Hardening |
| `fs_remove_world_readable` | `true` | No | — |
| `fs_remove_suid_sgid` | `true` | No | — |
| `fs_enable_file_integrity` | `true` | No | — |
| `app_disable_rest_api_logging` | `false` | No | Application Hardening |
| `app_enable_strict_validation` | `true` | No | — |
| `app_disable_debug_mode` | `true` | No | — |
| `app_remove_sample_data` | `true` | No | — |
| `compliance_generate_reports` | `true` | No | Compliance Reporting |
| `compliance_report_path` | `"{{ splunk_home }}/var/log/splunk/compliance"` | No | — |
| `compliance_frameworks` | `(see defaults/main.yml)` | No | — |

## Example Playbook

```yaml
---
- name: Harden Splunk Enterprise
  hosts: splunk_servers
  become: true
  roles:
    - role: splunk/roles/splunk_security_hardening
      vars:
        stig_cat1_enabled: true
        stig_cat2_enabled: true
        ac_session_timeout_minutes: 15
        ia_enforce_mfa: true
```

## Tags

| Tag | Description |
|-----|-------------|
| `CAT1` | Tasks tagged `CAT1` |
| `CAT2` | Tasks tagged `CAT2` |
| `CAT3` | Tasks tagged `CAT3` |
| `V-258100` | Tasks tagged `V-258100` |
| `V-258102` | Tasks tagged `V-258102` |
| `V-258104` | Tasks tagged `V-258104` |
| `V-258106` | Tasks tagged `V-258106` |
| `V-258108` | Tasks tagged `V-258108` |
| `V-258110` | Tasks tagged `V-258110` |
| `V-258112` | Tasks tagged `V-258112` |
| `V-258114` | Tasks tagged `V-258114` |
| `V-258116` | Tasks tagged `V-258116` |
| `V-258118` | Tasks tagged `V-258118` |
| `V-258120` | Tasks tagged `V-258120` |
| `V-258122` | Tasks tagged `V-258122` |
| `V-258124` | Tasks tagged `V-258124` |
| `V-258126` | Tasks tagged `V-258126` |
| `V-258128` | Tasks tagged `V-258128` |
| `V-258130` | Tasks tagged `V-258130` |
| `V-258132` | Tasks tagged `V-258132` |
| `V-258134` | Tasks tagged `V-258134` |
| `access_control` | Tasks tagged `access_control` |
| `accounts` | Tasks tagged `accounts` |
| `aide` | Tasks tagged `aide` |
| `application` | Tasks tagged `application` |
| `apps` | Tasks tagged `apps` |
| `audit` | Tasks tagged `audit` |
| `authentication` | Tasks tagged `authentication` |
| `banner` | Tasks tagged `banner` |
| `cat1` | Tasks tagged `cat1` |
| `cat2` | Tasks tagged `cat2` |
| `cat3` | Tasks tagged `cat3` |
| `certificates` | Tasks tagged `certificates` |
| `ciphers` | Tasks tagged `ciphers` |
| `cleanup` | Tasks tagged `cleanup` |
| `compliance` | Tasks tagged `compliance` |
| `config_management` | Tasks tagged `config_management` |
| `content` | Tasks tagged `content` |
| `cron` | Tasks tagged `cron` |
| `cryptography` | Tasks tagged `cryptography` |
| `dod` | Tasks tagged `dod` |
| `dos_protection` | Tasks tagged `dos_protection` |
| `filesystem` | Tasks tagged `filesystem` |
| `fips` | Tasks tagged `fips` |
| `hardening` | Tasks tagged `hardening` |
| `high` | Tasks tagged `high` |
| `integrity` | Tasks tagged `integrity` |
| `logging` | Tasks tagged `logging` |
| `low` | Tasks tagged `low` |
| `medium` | Tasks tagged `medium` |
| `mfa` | Tasks tagged `mfa` |
| `monitoring` | Tasks tagged `monitoring` |
| `network` | Tasks tagged `network` |
| `nist_ac` | Tasks tagged `nist_ac` |
| `nist_au` | Tasks tagged `nist_au` |
| `nist_cm` | Tasks tagged `nist_cm` |
| `nist_ia` | Tasks tagged `nist_ia` |
| `nist_sc` | Tasks tagged `nist_sc` |
| `nist_si` | Tasks tagged `nist_si` |
| `password` | Tasks tagged `password` |
| `permissions` | Tasks tagged `permissions` |
| `protocols` | Tasks tagged `protocols` |
| `rbac` | Tasks tagged `rbac` |
| `reporting` | Tasks tagged `reporting` |
| `retention` | Tasks tagged `retention` |
| `security` | Tasks tagged `security` |
| `services` | Tasks tagged `services` |
| `session` | Tasks tagged `session` |
| `stig` | Tasks tagged `stig` |
| `suid` | Tasks tagged `suid` |
| `tls` | Tasks tagged `tls` |
| `verification` | Tasks tagged `verification` |

## License

MIT
