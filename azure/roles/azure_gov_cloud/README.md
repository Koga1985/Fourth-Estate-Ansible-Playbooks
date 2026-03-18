# azure_gov_cloud

Azure Gov Cloud role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Azure Gov Cloud
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_gov_cloud
```

## License

MIT
