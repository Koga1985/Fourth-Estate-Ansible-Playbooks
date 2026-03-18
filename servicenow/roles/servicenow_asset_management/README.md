# servicenow_asset_management

Servicenow Asset Management role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `servicenow/README.md`

## Requirements

- Ansible 2.15+
- Collection: `servicenow.itsm`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Servicenow Asset Management
  hosts: localhost
  gather_facts: false
  roles:
    - role: servicenow/roles/servicenow_asset_management
```

## License

MIT
