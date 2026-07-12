# cohesity_cluster_config

Cohesity Cluster Config role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `cohesity/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cohesity_cluster_vip` | `"10.100.1.100"` | No | Cohesity Cluster Connection |
| `cohesity_api_protocol` | `"https"` | No | — |
| `cohesity_api_port` | `443` | No | — |
| `cohesity_api_verify_ssl` | `true` | No | — |
| `cohesity_api_timeout` | `300` | No | — |
| `cohesity_admin_username` | `"admin"` | No | Authentication |
| `cohesity_admin_password` | `"{{ vault_cohesity_admin_password }}"` | No | — |
| `cohesity_api_token` | `""` | No | — |
| `cohesity_ad_enabled` | `true` | No | Active Directory Configuration |
| `cohesity_ad_domain` | `"fourthestate.com"` | No | — |
| `cohesity_ad_preferred_dc` | `[]` | No | — |
| `cohesity_ad_username` | `"cohesity-svc@fourthestate.com"` | No | — |
| `cohesity_ad_password` | `"{{ vault_ad_password }}"` | No | — |
| `cohesity_ad_ou_path` | `"OU=Service Accounts,DC=fourthestate,DC=com"` | No | — |
| `cohesity_ad_trusted_domains` | `[]` | No | — |
| `cohesity_ad_workgroup` | `""` | No | — |
| `cohesity_ad_ldap_provider` | `"OpenLdap"` | No | — |
| `cohesity_ad_user_id_mapping` | `"SFU"` | No | SFU, RFC2307, Centrify, Custom |
| `cohesity_ldap_enabled` | `false` | No | LDAP Configuration |
| `cohesity_ldap_server` | `"ldap.fourthestate.com"` | No | — |
| `cohesity_ldap_port` | `636` | No | — |
| `cohesity_ldap_use_ssl` | `true` | No | — |
| `cohesity_ldap_base_dn` | `"dc=fourthestate,dc=com"` | No | — |
| `cohesity_ldap_bind_dn` | `"cn=cohesity,ou=service accounts,dc=fourthestate,dc=com"` | No | — |
| `cohesity_ldap_bind_password` | `"{{ vault_ldap_password }}"` | No | — |
| `cohesity_ldap_user_search_filter` | `"(objectClass=person)"` | No | — |
| `cohesity_ldap_group_search_filter` | `"(objectClass=group)"` | No | — |
| `cohesity_kerberos_enabled` | `true` | No | Kerberos Configuration |
| `cohesity_kerberos_realm` | `"FOURTHESTATE.COM"` | No | — |
| `cohesity_kerberos_kdc_servers` | `(see defaults/main.yml)` | No | — |
| `cohesity_local_users` | `(see defaults/main.yml)` | No | User Management |
| `cohesity_ad_groups` | `(see defaults/main.yml)` | No | RBAC Configuration |
| `cohesity_custom_roles` | `(see defaults/main.yml)` | No | Privileges and Custom Roles |
| `cohesity_storage_domains` | `(see defaults/main.yml)` | No | Storage Domains (View Boxes) |
| `cohesity_syslog_enabled` | `true` | No | Syslog Configuration |
| `cohesity_syslog_servers` | `(see defaults/main.yml)` | No | — |
| `cohesity_snmp_enabled` | `true` | No | SNMP Configuration |
| `cohesity_snmp_version` | `"v3"` | No | — |
| `cohesity_snmp_user` | `"cohesity-snmp"` | No | — |
| `cohesity_snmp_auth_protocol` | `"SHA"` | No | — |
| `cohesity_snmp_auth_password` | `"{{ vault_snmp_auth_password }}"` | No | — |
| `cohesity_snmp_privacy_protocol` | `"AES128"` | No | — |
| `cohesity_snmp_privacy_password` | `"{{ vault_snmp_privacy_password }}"` | No | — |
| `cohesity_snmp_trap_receivers` | `(see defaults/main.yml)` | No | — |
| `cohesity_ssl_certificate_enabled` | `true` | No | Certificate Management |
| `cohesity_ssl_certificate_type` | `"custom"` | No | self-signed, custom, acme |
| `cohesity_ssl_certificate_path` | `"/etc/ssl/certs/cohesity.crt"` | No | — |
| `cohesity_ssl_private_key_path` | `"/etc/ssl/private/cohesity.key"` | No | — |
| `cohesity_ssl_ca_chain_path` | `"/etc/ssl/certs/ca-bundle.crt"` | No | — |
| `cohesity_security_settings` | `(see defaults/main.yml)` | No | Security Settings |
| `cohesity_ip_allowlist_enabled` | `true` | No | IP Allowlist/Denylist |
| `cohesity_ip_allowlist` | `(see defaults/main.yml)` | No | — |
| `cohesity_ip_denylist_enabled` | `false` | No | — |
| `cohesity_ip_denylist` | `[]` | No | — |
| `cohesity_multi_tenancy_enabled` | `true` | No | Multi-tenancy Configuration |
| `cohesity_organizations` | `(see defaults/main.yml)` | No | — |
| `cohesity_global_settings` | `(see defaults/main.yml)` | No | Global Settings |
| `cohesity_email_notifications` | `(see defaults/main.yml)` | No | Email Notification Settings |
| `cohesity_ransomware_protection` | `(see defaults/main.yml)` | No | Ransomware Protection Settings |
| `cohesity_compliance_settings` | `(see defaults/main.yml)` | No | Compliance Settings for Fourth Estate |
| `cohesity_cluster_preferences` | `(see defaults/main.yml)` | No | Cluster Preferences |
| `cohesity_network_interface_groups` | `(see defaults/main.yml)` | No | Network Configuration |
| `cohesity_qos_policies` | `(see defaults/main.yml)` | No | Quality of Service (QoS) |
| `cohesity_maintenance_windows` | `(see defaults/main.yml)` | No | Maintenance Windows |
| `cohesity_fourth_estate_config` | `(see defaults/main.yml)` | No | Fourth Estate Specific |

## Example Playbook

```yaml
---
- name: Cohesity Cluster Config
  hosts: localhost
  gather_facts: false
  roles:
    - role: cohesity/roles/cohesity_cluster_config
```

## License

MIT
