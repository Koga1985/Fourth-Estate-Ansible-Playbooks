# azure_key_vault

Azure Key Vault role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Azure Key Vault
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_key_vault
```

## License

MIT
