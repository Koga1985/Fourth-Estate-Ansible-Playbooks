# vault_transit_encryption

Vault Transit Encryption role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `hashicorp_vault/README.md`

## Requirements

- Ansible 2.15+
- Collection: `community.hashi_vault`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Vault Transit Encryption
  hosts: localhost
  gather_facts: false
  roles:
    - role: hashicorp_vault/roles/vault_transit_encryption
```

## License

MIT
