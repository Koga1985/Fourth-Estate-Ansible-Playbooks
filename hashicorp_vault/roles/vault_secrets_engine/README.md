# vault_secrets_engine

Vault Secrets Engine role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `vault_kv_engines` | `(see defaults/main.yml)` | No | KV v2 Secrets Engine |
| `vault_ssh_engines` | `(see defaults/main.yml)` | No | SSH Secrets Engine |
| `vault_totp_engines` | `(see defaults/main.yml)` | No | TOTP Secrets Engine |
| `vault_nomad_engines` | `[]` | No | Nomad Secrets Engine |
| `vault_cubbyhole_enabled` | `true` | No | Cubbyhole (always enabled, per-token storage) |
| `vault_enable_generic_engines` | `(see defaults/main.yml)` | No | Generic engines to enable |
| `vault_kv_audit_non_hmac_request_keys` | `[]` | No | Advanced KV configuration |
| `vault_kv_audit_non_hmac_response_keys` | `[]` | No | — |
| `vault_ssh_ca_generate` | `true` | No | SSH CA configuration |
| `vault_ssh_ca_key_type` | `"ssh-rsa"` | No | — |
| `vault_ssh_ca_key_bits` | `4096` | No | — |
| `vault_totp_issuer` | `"Fourth Estate"` | No | TOTP configuration |
| `vault_totp_period` | `30` | No | — |
| `vault_totp_algorithm` | `"SHA256"` | No | — |
| `vault_totp_digits` | `6` | No | — |
| `vault_secrets_namespaces` | `[]` | No | Namespace configuration (Enterprise) |

## Example Playbook

```yaml
---
- name: Vault Secrets Engine
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_secrets_engine
```

## Tags

| Tag | Description |
|-----|-------------|
| `ca` | Tasks tagged `ca` |
| `kv` | Tasks tagged `kv` |
| `list` | Tasks tagged `list` |
| `namespaces` | Tasks tagged `namespaces` |
| `secrets` | Tasks tagged `secrets` |
| `ssh` | Tasks tagged `ssh` |
| `totp` | Tasks tagged `totp` |
| `vault` | Tasks tagged `vault` |

## License

MIT
