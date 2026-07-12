# vast_config

Vast Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `vast/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vast_mgmt_host` | `"{{ vault_vast_mgmt_host }}"` | No | VAST Management Server |
| `vast_mgmt_port` | `443` | No | — |
| `vast_mgmt_user` | `"{{ vault_vast_mgmt_user }}"` | No | — |
| `vast_mgmt_password` | `"{{ vault_vast_mgmt_password }}"` | No | — |
| `vast_api_version` | `"v1"` | No | — |
| `vast_verify_ssl` | `true` | No | — |
| `vast_ssl_cert_path` | `"/etc/pki/tls/certs/vast-ca-bundle.crt"` | No | — |
| `vast_api_timeout` | `60` | No | — |
| `vast_cluster_name` | `"production-cluster"` | No | Cluster Configuration |
| `vast_cluster_domain` | `"vast.local"` | No | — |
| `vast_cluster_timezone` | `"America/New_York"` | No | — |
| `vast_cluster_description` | `"Fourth Estate Production Storage Cluster"` | No | — |
| `vast_vip_pools` | `(see defaults/main.yml)` | No | Network Configuration - VIP Pools |
| `vast_dns_servers` | `(see defaults/main.yml)` | No | DNS Configuration |
| `vast_dns_domain_suffix` | `(see defaults/main.yml)` | No | — |
| `vast_ntp_servers` | `(see defaults/main.yml)` | No | NTP Configuration (DoD STIG requirement) |
| `vast_ntp_timezone` | `"America/New_York"` | No | — |
| `vast_smtp_enabled` | `false` | No | SMTP Configuration |
| `vast_smtp_server` | `"{{ vault_smtp_server \| default('') }}"` | No | — |
| `vast_smtp_port` | `25` | No | — |
| `vast_smtp_use_tls` | `true` | No | — |
| `vast_smtp_from_address` | `"vast-cluster@fourthestate.local"` | No | — |
| `vast_smtp_auth_required` | `false` | No | — |
| `vast_smtp_username` | `"{{ vault_smtp_username \| default('') }}"` | No | — |
| `vast_smtp_password` | `"{{ vault_smtp_password \| default('') }}"` | No | — |
| `vast_storage_domains` | `(see defaults/main.yml)` | No | Storage Domains / Pools |
| `vast_view_policies` | `(see defaults/main.yml)` | No | View Policies (Storage Policies) |
| `vast_quota_policies` | `(see defaults/main.yml)` | No | Quota Policies |
| `vast_snapshot_policies` | `(see defaults/main.yml)` | No | Snapshot Policies (Retention) |
| `vast_qos_policies` | `(see defaults/main.yml)` | No | QoS Policies |
| `vast_enable_nfs` | `true` | No | Protocol Configuration |
| `vast_enable_smb` | `true` | No | — |
| `vast_enable_s3` | `true` | No | — |
| `vast_nfs_versions` | `["3", "4.0", "4.1", "4.2"]` | No | — |
| `vast_smb_versions` | `["2.1", "3.0", "3.1.1"]` | No | — |
| `vast_s3_enforce_https` | `true` | No | — |
| `vast_nfs_exports` | `(see defaults/main.yml)` | No | NFS Export Configuration |
| `vast_smb_shares` | `(see defaults/main.yml)` | No | SMB Share Configuration |
| `vast_s3_buckets` | `(see defaults/main.yml)` | No | S3 Bucket Configuration |
| `vast_ad_enabled` | `false` | No | Active Directory Integration |
| `vast_ad_domain` | `"{{ vault_ad_domain \| default('') }}"` | No | — |
| `vast_ad_server` | `"{{ vault_ad_server \| default('') }}"` | No | — |
| `vast_ad_ou` | `"{{ vault_ad_ou \| default('') }}"` | No | — |
| `vast_ad_username` | `"{{ vault_ad_username \| default('') }}"` | No | — |
| `vast_ad_password` | `"{{ vault_ad_password \| default('') }}"` | No | — |
| `vast_ad_use_ldaps` | `true` | No | — |
| `vast_ldap_enabled` | `false` | No | LDAP Integration |
| `vast_ldap_server` | `"{{ vault_ldap_server \| default('') }}"` | No | — |
| `vast_ldap_port` | `636` | No | — |
| `vast_ldap_use_ssl` | `true` | No | — |
| `vast_ldap_base_dn` | `"{{ vault_ldap_base_dn \| default('') }}"` | No | — |
| `vast_ldap_bind_dn` | `"{{ vault_ldap_bind_dn \| default('') }}"` | No | — |
| `vast_ldap_bind_password` | `"{{ vault_ldap_bind_password \| default('') }}"` | No | — |
| `vast_kerberos_enabled` | `false` | No | Kerberos Configuration |
| `vast_kerberos_realm` | `"{{ vault_kerberos_realm \| default('') }}"` | No | — |
| `vast_kerberos_kdc` | `"{{ vault_kerberos_kdc \| default('') }}"` | No | — |
| `vast_multitenancy_enabled` | `false` | No | Multi-tenancy Configuration |
| `vast_tenants` | `(see defaults/main.yml)` | No | — |
| `vast_local_users` | `(see defaults/main.yml)` | No | User and Group Management |
| `vast_custom_roles` | `(see defaults/main.yml)` | No | RBAC Configuration |
| `vast_enforce_secure_protocols` | `true` | No | Security Settings (DoD STIG Aligned) |
| `vast_disable_smb1` | `true` | No | — |
| `vast_require_smb_signing` | `true` | No | — |
| `vast_require_smb_encryption` | `true` | No | — |
| `vast_nfs_kerberos_required` | `false` | No | — |
| `vast_enable_audit_logging` | `true` | No | — |
| `vast_audit_log_retention_days` | `365` | No | — |
| `vast_enable_deduplication` | `true` | No | Data Protection |
| `vast_enable_compression` | `true` | No | — |
| `vast_enable_encryption_at_rest` | `true` | No | — |
| `vast_encryption_algorithm` | `"AES-256-GCM"` | No | — |
| `vast_enable_ha` | `true` | No | High Availability |
| `vast_replication_enabled` | `false` | No | — |
| `vast_replication_target` | `""` | No | — |
| `vast_max_concurrent_connections` | `10000` | No | Performance Tuning |
| `vast_io_scheduler` | `"noop"` | No | — |
| `vast_readahead_kb` | `4096` | No | — |
| `vast_write_cache_size_gb` | `256` | No | — |
| `vast_enable_snmp` | `true` | No | Monitoring and Alerting |
| `vast_snmp_community` | `"{{ vault_vast_snmp_community }}"` | No | — |
| `vast_enable_syslog` | `true` | No | — |
| `vast_syslog_server` | `"{{ vault_syslog_server \| default('') }}"` | No | — |
| `vast_syslog_port` | `514` | No | — |
| `vast_syslog_protocol` | `"tcp"` | No | — |
| `vast_compliance_mode` | `"dod"` | No | Compliance Settings Options: dod, nist, hipaa, pci |
| `vast_fips_mode_enabled` | `true` | No | — |
| `vast_tls_min_version` | `"1.2"` | No | — |
| `vast_cipher_suites` | `(see defaults/main.yml)` | No | — |
| `vast_replication_pairs` | `[]` | No | Replication Configuration |
| `vast_global_settings` | `(see defaults/main.yml)` | No | Global Settings |

## Example Playbook

```yaml
---
- name: Vast Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: vast/roles/vast_config
```

## Tags

| Tag | Description |
|-----|-------------|
| `active_directory` | Tasks tagged `active_directory` |
| `ad` | Tasks tagged `ad` |
| `alerts` | Tasks tagged `alerts` |
| `audit` | Tasks tagged `audit` |
| `authentication` | Tasks tagged `authentication` |
| `backup` | Tasks tagged `backup` |
| `capacity` | Tasks tagged `capacity` |
| `cluster` | Tasks tagged `cluster` |
| `cluster_name` | Tasks tagged `cluster_name` |
| `cluster_timezone` | Tasks tagged `cluster_timezone` |
| `compliance` | Tasks tagged `compliance` |
| `connectivity` | Tasks tagged `connectivity` |
| `data_protection` | Tasks tagged `data_protection` |
| `discovery` | Tasks tagged `discovery` |
| `dns` | Tasks tagged `dns` |
| `domain_join` | Tasks tagged `domain_join` |
| `dr` | Tasks tagged `dr` |
| `encryption` | Tasks tagged `encryption` |
| `fips` | Tasks tagged `fips` |
| `ha` | Tasks tagged `ha` |
| `health` | Tasks tagged `health` |
| `integrity` | Tasks tagged `integrity` |
| `isolation` | Tasks tagged `isolation` |
| `kerberos` | Tasks tagged `kerberos` |
| `keytab` | Tasks tagged `keytab` |
| `ldap` | Tasks tagged `ldap` |
| `logging` | Tasks tagged `logging` |
| `monitoring` | Tasks tagged `monitoring` |
| `multitenancy` | Tasks tagged `multitenancy` |
| `network` | Tasks tagged `network` |
| `nfs` | Tasks tagged `nfs` |
| `nist` | Tasks tagged `nist` |
| `ntp` | Tasks tagged `ntp` |
| `optimization` | Tasks tagged `optimization` |
| `password_policy` | Tasks tagged `password_policy` |
| `performance` | Tasks tagged `performance` |
| `policies` | Tasks tagged `policies` |
| `prerequisites` | Tasks tagged `prerequisites` |
| `protocols` | Tasks tagged `protocols` |
| `qos` | Tasks tagged `qos` |
| `rbac` | Tasks tagged `rbac` |
| `replication` | Tasks tagged `replication` |
| `roles` | Tasks tagged `roles` |
| `s3` | Tasks tagged `s3` |
| `security` | Tasks tagged `security` |
| `session` | Tasks tagged `session` |
| `smb` | Tasks tagged `smb` |
| `snapshots` | Tasks tagged `snapshots` |
| `snmp` | Tasks tagged `snmp` |
| `ssl` | Tasks tagged `ssl` |
| `stig` | Tasks tagged `stig` |
| `storage` | Tasks tagged `storage` |
| `syslog` | Tasks tagged `syslog` |
| `tenants` | Tasks tagged `tenants` |
| `time_sync` | Tasks tagged `time_sync` |
| `tls` | Tasks tagged `tls` |
| `user_mapping` | Tasks tagged `user_mapping` |
| `users` | Tasks tagged `users` |
| `validation` | Tasks tagged `validation` |
| `vast_config` | Tasks tagged `vast_config` |
| `views` | Tasks tagged `views` |
| `vip` | Tasks tagged `vip` |
| `worm` | Tasks tagged `worm` |

## License

MIT
