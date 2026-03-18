# tenable_compliance_checks

Tenable Compliance Checks role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Tenable Compliance Checks
  hosts: localhost
  gather_facts: false
  roles:
    - role: tenable/roles/tenable_compliance_checks
```

## License

MIT
