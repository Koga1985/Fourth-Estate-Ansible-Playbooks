# servicenow_reporting

Servicenow Reporting role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `servicenow/README.md`

## Requirements

- Ansible 2.15+
- Collection: `servicenow.itsm`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Servicenow Reporting
  hosts: localhost
  gather_facts: false
  roles:
    - role: servicenow/roles/servicenow_reporting
```

## License

MIT
