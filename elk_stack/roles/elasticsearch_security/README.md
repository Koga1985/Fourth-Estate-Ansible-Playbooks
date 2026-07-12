# elasticsearch_security

Elasticsearch Security role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `elk_stack/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `elasticsearch_security_enabled` | `true` | No | Security configuration |
| `elasticsearch_security_auto_configure` | `true` | No | — |
| `elasticsearch_tls_enabled` | `true` | No | TLS/SSL configuration |
| `elasticsearch_tls_transport_enabled` | `true` | No | — |
| `elasticsearch_tls_http_enabled` | `true` | No | — |
| `elasticsearch_certs_dir` | `"/etc/elasticsearch/certs"` | No | Certificate configuration |
| `elasticsearch_ca_cert_path` | `"{{ elasticsearch_certs_dir }}/ca/ca.crt"` | No | — |
| `elasticsearch_ca_key_path` | `"{{ elasticsearch_certs_dir }}/ca/ca.key"` | No | — |
| `elasticsearch_node_cert_path` | `"{{ elasticsearch_certs_dir }}/{{ ansible_hostname }}/{{ ansible_ho...` | No | — |
| `elasticsearch_node_key_path` | `"{{ elasticsearch_certs_dir }}/{{ ansible_hostname }}/{{ ansible_ho...` | No | — |
| `elasticsearch_generate_ca` | `true` | No | Certificate generation |
| `elasticsearch_generate_node_certs` | `true` | No | — |
| `elasticsearch_cert_validity_days` | `3650` | No | — |
| `elasticsearch_cert_key_size` | `4096` | No | — |
| `elasticsearch_cert_country` | `"US"` | No | Certificate details |
| `elasticsearch_cert_state` | `"DC"` | No | — |
| `elasticsearch_cert_locality` | `"Washington"` | No | — |
| `elasticsearch_cert_organization` | `"Fourth Estate Media"` | No | — |
| `elasticsearch_cert_organizational_unit` | `"Infrastructure"` | No | — |
| `elasticsearch_tls_versions` | `["TLSv1.2", "TLSv1.3"]` | No | TLS versions and ciphers |
| `elasticsearch_tls_ciphers` | `[]` | No | Empty uses defaults |
| `elasticsearch_tls_client_auth` | `"optional"` | No | Client authentication none, optional, required |
| `elasticsearch_builtin_users` | `(see defaults/main.yml)` | No | Built-in users |
| `elasticsearch_custom_roles` | `(see defaults/main.yml)` | No | Custom roles |
| `elasticsearch_custom_users` | `(see defaults/main.yml)` | No | Custom users |
| `elasticsearch_ldap_enabled` | `false` | No | LDAP/AD integration |
| `elasticsearch_ldap_url` | `"ldaps://ldap.fourthestate.org:636"` | No | — |
| `elasticsearch_ldap_bind_dn` | `"cn=elasticsearch,ou=service-accounts,dc=fourthestate,dc=org"` | No | — |
| `elasticsearch_ldap_bind_password` | `"{{ elasticsearch_ldap_bind_password_vault }}"` | No | — |
| `elasticsearch_ldap_user_search_base` | `"ou=users,dc=fourthestate,dc=org"` | No | — |
| `elasticsearch_ldap_user_search_filter` | `"(cn={0})"` | No | — |
| `elasticsearch_ldap_group_search_base` | `"ou=groups,dc=fourthestate,dc=org"` | No | — |
| `elasticsearch_ldap_group_search_filter` | `"(member={0})"` | No | — |
| `elasticsearch_ad_enabled` | `false` | No | Active Directory integration |
| `elasticsearch_ad_domain` | `"fourthestate.org"` | No | — |
| `elasticsearch_ad_url` | `"ldaps://ad.fourthestate.org:636"` | No | — |
| `elasticsearch_ad_user_search_base` | `"CN=Users,DC=fourthestate,DC=org"` | No | — |
| `elasticsearch_ad_group_search_base` | `"CN=Users,DC=fourthestate,DC=org"` | No | — |
| `elasticsearch_saml_enabled` | `false` | No | SAML SSO |
| `elasticsearch_saml_idp_metadata_path` | `"/etc/elasticsearch/saml/idp-metadata.xml"` | No | — |
| `elasticsearch_saml_sp_entity_id` | `"https://elk.fourthestate.org"` | No | — |
| `elasticsearch_saml_sp_acs` | `"https://elk.fourthestate.org/api/security/saml/callback"` | No | — |
| `elasticsearch_saml_sp_logout` | `"https://elk.fourthestate.org/logout"` | No | — |
| `elasticsearch_api_keys_enabled` | `true` | No | API Keys |
| `elasticsearch_api_keys` | `[]` | No | — |
| `elasticsearch_audit_enabled` | `true` | No | Audit logging |
| `elasticsearch_audit_outputs` | `["logfile"]` | No | logfile, index |
| `elasticsearch_audit_include_request_body` | `false` | No | — |
| `elasticsearch_audit_exclude_users` | `["kibana_system", "logstash_system"]` | No | — |
| `elasticsearch_audit_include_events` | `(see defaults/main.yml)` | No | — |
| `elasticsearch_ip_filter_enabled` | `false` | No | IP filtering |
| `elasticsearch_ip_filter_allow` | `[]` | No | — |
| `elasticsearch_ip_filter_deny` | `[]` | No | Example: elasticsearch_ip_filter_allow: - "10.0.0.0/8" - "172.16.0.0/12" - "192.168.0.0/16" |
| `elasticsearch_anonymous_access_enabled` | `false` | No | Anonymous access |
| `elasticsearch_anonymous_username` | `"anonymous_user"` | No | — |
| `elasticsearch_anonymous_roles` | `["monitoring"]` | No | — |
| `elasticsearch_dls_fls_enabled` | `true` | No | Document and field level security |
| `elasticsearch_encryption_at_rest_enabled` | `false` | No | Encryption at rest |
| `elasticsearch_fourth_estate_security` | `true` | No | Fourth Estate specific |
| `elasticsearch_source_protection_enabled` | `true` | No | — |
| `elasticsearch_journalist_audit_enabled` | `true` | No | — |
| `elasticsearch_compliance_audit_enabled` | `true` | No | — |
| `elasticsearch_password_hashing_algorithm` | `"bcrypt10"` | No | Password policies bcrypt, bcrypt4-10, pbkdf2, pbkdf2_1000-50000 |
| `elasticsearch_token_service_enabled` | `true` | No | Token service |
| `elasticsearch_token_timeout` | `"20m"` | No | — |

## Example Playbook

```yaml
---
- name: Elasticsearch Security
  hosts: localhost
  gather_facts: false
  roles:
    - role: elk_stack/roles/elasticsearch_security
```

## License

MIT
