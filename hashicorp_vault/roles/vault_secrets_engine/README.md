# vault_secrets_engine

Vault Secrets Engine role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `vault_nomad_engines` | `[]` |  |
| `vault_cubbyhole_enabled` | `true` |  |
| `vault_kv_audit_non_hmac_request_keys` | `[]` |  |
| `vault_kv_audit_non_hmac_response_keys` | `[]` |  |
| `vault_ssh_ca_generate` | `true` |  |
| `vault_ssh_ca_key_type` | `"ssh-rsa"` |  |
| `vault_ssh_ca_key_bits` | `4096` |  |
| `vault_totp_issuer` | `"Fourth Estate"` |  |
| `vault_totp_period` | `30` |  |
| `vault_totp_algorithm` | `"SHA256"` |  |
| `vault_totp_digits` | `6` |  |
| `vault_secrets_namespaces` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vault Secrets Engine
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_secrets_engine
```

## License

MIT
