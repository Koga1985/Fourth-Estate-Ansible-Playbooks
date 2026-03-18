# azure_logic_apps

Azure Logic Apps role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `azure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `azure.azcollection`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Azure Logic Apps
  hosts: localhost
  gather_facts: false
  roles:
    - role: azure/roles/azure_logic_apps
```

## License

MIT
