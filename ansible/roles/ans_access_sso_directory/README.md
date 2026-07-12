# ans_access_sso_directory

SSO (SAML/LDAP) for Controller, group mappings to org roles, access review CSVs.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | AAP Controller connection |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | — |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `controller_username` | `"{{ lookup('env', 'CONTROLLER_USERNAME') \| default('') }}"` | No | — |
| `controller_password` | `"{{ lookup('env', 'CONTROLLER_PASSWORD') \| default('') }}"` | No | — |
| `sso_provider` | `"saml"` | No | SSO Configuration saml, oidc, ldap, radius |
| `sso_enabled` | `true` | No | — |
| `access_reviews` | `true` | No | — |
| `access_review_output_format` | `"csv"` | No | csv, json, yaml |
| `saml_auto_create_objects` | `true` | No | SAML Settings |
| `saml_attr_user_permanent_id` | `"name_id"` | No | — |
| `saml_attr_first_name` | `"first_name"` | No | — |
| `saml_attr_last_name` | `"last_name"` | No | — |
| `saml_attr_username` | `"username"` | No | — |
| `saml_attr_email` | `"email"` | No | — |
| `saml_entity_id` | `"https://controller.example.mil"` | No | — |
| `saml_callback_url` | `"https://controller.example.mil/sso/complete/saml/"` | No | — |
| `saml_idp_url` | `"https://sso.example.mil/saml/sso"` | No | — |
| `saml_idp_x509cert` | `""` | No | — |
| `saml_team_map` | `{}` | No | — |
| `saml_organization_map` | `{}` | No | — |
| `saml_security_config` | `{}` | No | — |
| `oidc_key` | `""` | No | OIDC Settings |
| `oidc_secret` | `""` | No | — |
| `oidc_provider_url` | `"https://sso.example.mil"` | No | — |
| `oidc_verify_ssl` | `true` | No | — |
| `ldap_server_uri` | `"ldaps://ldap.example.mil:636"` | No | LDAP Settings |
| `ldap_bind_dn` | `"cn=ansible,ou=service-accounts,dc=example,dc=mil"` | No | — |
| `ldap_bind_password` | `""` | No | — |
| `ldap_start_tls` | `false` | No | — |
| `ldap_user_dn_template` | `"uid=%(user)s,ou=users,dc=example,dc=mil"` | No | — |
| `ldap_user_search` | `(see defaults/main.yml)` | No | — |
| `ldap_group_search` | `(see defaults/main.yml)` | No | — |
| `ldap_require_group` | `""` | No | — |
| `ldap_deny_group` | `""` | No | — |
| `ldap_user_attr_map` | `(see defaults/main.yml)` | No | — |
| `ldap_team_map` | `{}` | No | — |
| `ldap_organization_map` | `{}` | No | — |
| `radius_server` | `""` | No | RADIUS Settings |
| `radius_port` | `1812` | No | — |
| `radius_secret` | `""` | No | — |
| `rbac_roles_to_create` | `[]` | No | RBAC Configuration |
| `fourth_estate_team_mappings` | `(see defaults/main.yml)` | No | Team Mappings for Fourth Estate |
| `access_review_frequency` | `"weekly"` | No | Access Review Settings daily, weekly, monthly |
| `access_review_recipients` | `(see defaults/main.yml)` | No | — |
| `access_review_include_inactive_users` | `false` | No | — |
| `access_review_retention_days` | `90` | No | — |

## Example Playbook

```yaml
- name: Use ans_access_sso_directory
  hosts: all
  gather_facts: false
  roles:
    - role: ans_access_sso_directory
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
