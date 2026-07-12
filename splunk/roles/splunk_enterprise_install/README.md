# splunk_enterprise_install

Installs and configures Splunk Enterprise with full DoD STIG and NIST 800-53 compliance. Covers package installation, TLS hardening, LDAP/SAML authentication, FIPS mode, session controls, file permissions, clustering configuration, and audit logging.

## Requirements

- Ansible 2.15+
- `ansible.posix` collection: `ansible-galaxy collection install ansible.posix`
- Target: RHEL 8/9, CentOS, Rocky, AlmaLinux, Ubuntu, Debian (x86_64)
- Minimum hardware: 12 GB RAM, 500 GB disk

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `splunk_version` | `"9.2.1"` | No | Splunk Version and Package |
| `splunk_build` | `"78803f08aabb"` | No | — |
| `splunk_product` | `"splunk"` | No | Options: splunk, splunkforwarder |
| `splunk_architecture` | `"x86_64"` | No | — |
| `splunk_package_url` | `"{{ vault_splunk_package_url \| default('https://download.splunk.com...` | No | — |
| `splunk_home` | `"/opt/splunk"` | No | Installation Paths (STIG V-258000) |
| `splunk_db` | `"/opt/splunk/var/lib/splunk"` | No | — |
| `splunk_user` | `"splunk"` | No | — |
| `splunk_group` | `"splunk"` | No | — |
| `splunk_user_uid` | `1500` | No | — |
| `splunk_group_gid` | `1500` | No | — |
| `splunk_user_shell` | `"/bin/bash"` | No | — |
| `splunk_min_memory_gb` | `12` | No | System Requirements Validation |
| `splunk_min_disk_gb` | `500` | No | — |
| `splunk_validate_requirements` | `true` | No | — |
| `splunk_accept_license` | `false` | No | License Configuration (STIG V-258002) Must be explicitly set to true |
| `splunk_license_file` | `"{{ vault_splunk_license_file \| default('') }}"` | No | — |
| `splunk_license_master` | `"{{ vault_splunk_license_master \| default('') }}"` | No | — |
| `splunk_web_port` | `8000` | No | Network Configuration (NIST 800-53 SC-7) |
| `splunk_mgmt_port` | `8089` | No | — |
| `splunk_splunktcp_port` | `9997` | No | — |
| `splunk_kvstore_port` | `8191` | No | — |
| `splunk_appserver_port` | `8065` | No | — |
| `splunk_bind_ip` | `"0.0.0.0"` | No | Should be restricted in production |
| `splunk_enable_web_ssl` | `true` | No | — |
| `splunk_enable_splunktcp_ssl` | `true` | No | — |
| `splunk_admin_password` | `"{{ vault_splunk_admin_password }}"` | No | Admin Account Configuration (STIG V-258004, NIST 800-53 IA-2) |
| `splunk_admin_password_min_length` | `15` | No | — |
| `splunk_require_password_change_on_first_login` | `true` | No | — |
| `splunk_enable_fips` | `true` | No | FIPS Mode (NIST 800-53 SC-13, STIG V-258006) |
| `splunk_fips_mode` | `"strict"` | No | — |
| `splunk_tls_min_version` | `"tls1.2"` | No | TLS Configuration (NIST 800-52r2, STIG V-258008) |
| `splunk_ssl_versions` | `"tls1.2, tls1.3"` | No | — |
| `splunk_cipher_suite` | `"ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AE...` | No | — |
| `splunk_ecdh_curves` | `"prime256v1, secp384r1, secp521r1"` | No | — |
| `splunk_use_default_tls_certs` | `false` | No | — |
| `splunk_server_cert` | `"{{ vault_splunk_server_cert \| default('') }}"` | No | — |
| `splunk_server_key` | `"{{ vault_splunk_server_key \| default('') }}"` | No | — |
| `splunk_ca_cert` | `"{{ vault_splunk_ca_cert \| default('') }}"` | No | — |
| `splunk_auth_type` | `"LDAP"` | No | Authentication (NIST 800-63B, STIG V-258010) Options: Splunk, LDAP, SAML |
| `splunk_ldap_host` | `"{{ vault_ldap_host \| default('') }}"` | No | — |
| `splunk_ldap_port` | `636` | No | LDAPS |
| `splunk_ldap_ssl_enabled` | `true` | No | — |
| `splunk_ldap_bind_dn` | `"{{ vault_ldap_bind_dn \| default('') }}"` | No | — |
| `splunk_ldap_bind_password` | `"{{ vault_ldap_bind_password \| default('') }}"` | No | — |
| `splunk_ldap_user_base_dn` | `"{{ vault_ldap_user_base_dn \| default('') }}"` | No | — |
| `splunk_ldap_group_base_dn` | `"{{ vault_ldap_group_base_dn \| default('') }}"` | No | — |
| `splunk_enable_mfa` | `true` | No | Multi-Factor Authentication (NIST 800-53 IA-2(1), STIG V-258012) |
| `splunk_mfa_type` | `"DUO"` | No | Options: DUO, RSA, RADIUS |
| `splunk_ui_session_timeout` | `900` | No | Session Management (STIG V-258014) 15 minutes |
| `splunk_ui_idle_timeout` | `600` | No | 10 minutes |
| `splunk_max_concurrent_sessions` | `3` | No | — |
| `splunk_enable_csrf_protection` | `true` | No | — |
| `splunk_enforce_strict_permissions` | `true` | No | File System Permissions (STIG V-258016) |
| `splunk_file_mode` | `"0600"` | No | — |
| `splunk_dir_mode` | `"0700"` | No | — |
| `splunk_config_mode` | `"0600"` | No | — |
| `splunk_audit_all_searches` | `true` | No | Audit and Logging (NIST 800-53 AU family, STIG V-258018) |
| `splunk_audit_admin_actions` | `true` | No | — |
| `splunk_audit_failed_logins` | `true` | No | — |
| `splunk_log_retention_days` | `365` | No | — |
| `splunk_enable_audit_trail` | `true` | No | — |
| `splunk_audit_log_path` | `"{{ splunk_home }}/var/log/splunk/audit.log"` | No | — |
| `splunk_max_data_size` | `"auto_high_volume"` | No | Indexer Settings (NIST 800-53 AU-11) |
| `splunk_max_hot_buckets` | `10` | No | — |
| `splunk_max_warm_db_count` | `300` | No | — |
| `splunk_frozen_time_period_in_secs` | `31536000` | No | 1 year |
| `splunk_index_replication_factor` | `3` | No | — |
| `splunk_index_search_factor` | `2` | No | — |
| `splunk_deployment_server` | `"{{ vault_splunk_deployment_server \| default('') }}"` | No | Deployment Server (if applicable) |
| `splunk_deployment_client_name` | `"{{ inventory_hostname }}"` | No | — |
| `splunk_cluster_mode` | `"none"` | No | Clustering Configuration Options: none, master, peer, searchhead |
| `splunk_cluster_master_uri` | `"{{ vault_splunk_cluster_master_uri \| default('') }}"` | No | — |
| `splunk_cluster_label` | `"{{ vault_splunk_cluster_label \| default('production') }}"` | No | — |
| `splunk_cluster_secret` | `"{{ vault_splunk_cluster_secret }}"` | No | — |
| `splunk_shc_mode` | `false` | No | Search Head Clustering |
| `splunk_shc_captain_uri` | `"{{ vault_splunk_shc_captain_uri \| default('') }}"` | No | — |
| `splunk_shc_label` | `"{{ vault_splunk_shc_label \| default('sh_cluster') }}"` | No | — |
| `splunk_shc_secret` | `"{{ vault_splunk_shc_secret }}"` | No | — |
| `splunk_shc_replication_factor` | `3` | No | — |
| `splunk_enable_monitoring_console` | `true` | No | Monitoring and Health |
| `splunk_health_report_enabled` | `true` | No | — |
| `splunk_health_report_schedule` | `"0 1 * * *"` | No | Daily at 1 AM |
| `splunk_max_searches_per_cpu` | `1` | No | Resource Usage Limits (STIG V-258020) |
| `splunk_max_concurrent_searches` | `6` | No | — |
| `splunk_search_process_memory_limit` | `4096` | No | MB |
| `splunk_max_upload_size` | `1024` | No | MB |
| `splunk_check_for_updates` | `false` | No | Software Updates (STIG V-258022) Manual updates in production |
| `splunk_send_usage_data` | `false` | No | Privacy requirement |
| `splunk_selinux_enabled` | `true` | No | SELinux Configuration (STIG V-258024) |
| `splunk_selinux_mode` | `"enforcing"` | No | — |
| `splunk_configure_firewall` | `true` | No | Firewall Configuration (NIST 800-53 SC-7) |
| `splunk_allowed_management_networks` | `(see defaults/main.yml)` | No | — |
| `splunk_enable_backup` | `true` | No | Backup Configuration (NIST 800-53 CP-9) |
| `splunk_backup_path` | `"/backup/splunk"` | No | — |
| `splunk_backup_schedule` | `"0 2 * * 0"` | No | Weekly at 2 AM on Sunday |
| `splunk_backup_retention_days` | `90` | No | — |
| `splunk_use_dod_pki_certificates` | `true` | No | Certificate Management (STIG V-258026) |
| `splunk_cert_validation_strict` | `true` | No | — |
| `splunk_cert_expiry_warning_days` | `30` | No | — |
| `splunk_intermediate_ca_certs` | `[]` | No | — |
| `splunk_compliance_frameworks` | `(see defaults/main.yml)` | No | Compliance Frameworks |
| `splunk_login_banner_enabled` | `true` | No | Banner Configuration (STIG V-258028) |
| `splunk_login_banner_text` | `(multi-line text — see defaults/main.yml)` | No | — |
| `splunk_enable_boot_start` | `true` | No | Service Management |
| `splunk_restart_on_config_change` | `false` | No | Manual restart in production |
| `splunk_perform_preinstall_checks` | `true` | No | Pre-installation Checks |
| `splunk_check_disk_space` | `true` | No | — |
| `splunk_check_memory` | `true` | No | — |
| `splunk_check_network_ports` | `true` | No | — |
| `splunk_check_os_compatibility` | `true` | No | — |
| `splunk_supported_os_families` | `(see defaults/main.yml)` | No | Supported Operating Systems |
| `splunk_install_method` | `"package"` | No | Installation Method Options: package, archive |
| `splunk_cleanup_installer` | `true` | No | — |
| `splunk_verify_checksum` | `true` | No | — |

## Example Playbook

```yaml
---
- name: Install Splunk Enterprise
  hosts: splunk_servers
  become: true
  roles:
    - role: splunk/roles/splunk_enterprise_install
      vars:
        splunk_accept_license: true
        splunk_version: "9.2.1"
        splunk_auth_type: "LDAP"
        splunk_enable_fips: true
        splunk_cluster_mode: "none"
```

## Tags

| Tag | Description |
|-----|-------------|
| `install` | Package download and installation |
| `config` | Initial configuration |
| `tls` | TLS certificate setup |
| `ldap` | LDAP/authentication configuration |
| `fips` | FIPS mode configuration |
| `hardening` | STIG security hardening |
| `clustering` | Cluster configuration |
| `firewall` | Firewall port rules |

## License

MIT
