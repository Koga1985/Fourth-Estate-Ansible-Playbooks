# azure_cosmos_db

Azure Cosmos Db role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Azure Cosmos Db
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_cosmos_db
```

## License

MIT
