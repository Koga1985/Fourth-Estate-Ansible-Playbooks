# ans_core_secrets_identity

Vault rotation, plaintext→vault migration, Controller/PAH SSO settings.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | Common settings |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `repo_root` | `"."` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | Controller connection |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `controller_username` | `"{{ lookup('env', 'CONTROLLER_USERNAME') \| default('') }}"` | No | — |
| `controller_password` | `"{{ lookup('env', 'CONTROLLER_PASSWORD') \| default('') }}"` | No | — |
| `vault_enabled` | `true` | No | HashiCorp Vault Configuration |
| `vault_addr` | `"{{ lookup('env', 'VAULT_ADDR') \| default('https://vault.example.mi...` | No | — |
| `vault_token` | `"{{ lookup('env', 'VAULT_TOKEN') \| default('') }}"` | No | — |
| `vault_namespace` | `"{{ lookup('env', 'VAULT_NAMESPACE') \| default('fourth-estate') }}"` | No | — |
| `vault_role_id` | `"{{ lookup('env', 'VAULT_ROLE_ID') \| default('') }}"` | No | — |
| `vault_secret_id` | `"{{ lookup('env', 'VAULT_SECRET_ID') \| default('') }}"` | No | — |
| `vault_kv_mount` | `"secret"` | No | Vault Paths |
| `vault_kv_version` | `"v2"` | No | — |
| `vault_ansible_path` | `"ansible"` | No | — |
| `vault_credentials_path` | `"{{ vault_kv_mount }}/data/{{ vault_ansible_path }}/credentials"` | No | — |
| `vault_ssh_keys_path` | `"{{ vault_kv_mount }}/data/{{ vault_ansible_path }}/ssh"` | No | — |
| `vault_api_keys_path` | `"{{ vault_kv_mount }}/data/{{ vault_ansible_path }}/api-keys"` | No | — |
| `ansible_vault_enabled` | `true` | No | Ansible Vault Configuration |
| `vault_id_label` | `"default"` | No | — |
| `vault_password_file` | `"~/.vault_pass.txt"` | No | — |
| `new_vault_password_file` | `"~/.vault_pass_new.txt"` | No | — |
| `vault_rekey_enabled` | `false` | No | — |
| `files_to_encrypt` | `[]` | No | — |
| `vault_credential_sync_enabled` | `true` | No | Credential Types to Sync from Vault |
| `vault_credentials` | `(see defaults/main.yml)` | No | — |
| `secret_rotation_enabled` | `false` | No | Secret Rotation |
| `secret_rotation_schedule` | `"monthly"` | No | — |
| `secret_rotation_notification` | `true` | No | — |
| `secret_rotation_recipients` | `(see defaults/main.yml)` | No | — |
| `identity_provider` | `"ldap"` | No | Identity Management ldap, saml, oidc, radius |
| `identity_sync_enabled` | `true` | No | — |
| `identity_sync_schedule` | `"hourly"` | No | — |
| `cert_management_enabled` | `true` | No | Certificate Management |
| `cert_vault_path` | `"pki"` | No | — |
| `cert_renewal_threshold_days` | `30` | No | — |
| `cert_auto_renewal` | `false` | No | — |
| `ssh_key_rotation_enabled` | `false` | No | SSH Key Management |
| `ssh_key_rotation_days` | `90` | No | — |
| `ssh_key_vault_storage` | `true` | No | — |
| `api_token_rotation_enabled` | `true` | No | API Token Management |
| `api_token_max_age_days` | `90` | No | — |
| `api_token_vault_storage` | `true` | No | — |
| `fourth_estate_secret_scanning` | `true` | No | Fourth Estate Specific |
| `fourth_estate_secret_leak_prevention` | `true` | No | — |
| `fourth_estate_audit_secret_access` | `true` | No | — |
| `fourth_estate_require_mfa` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_core_secrets_identity
  hosts: all
  gather_facts: false
  roles:
    - role: ans_core_secrets_identity
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
