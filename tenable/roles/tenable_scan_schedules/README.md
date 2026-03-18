# tenable_scan_schedules

Tenable Scan Schedules role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `tenable/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Tenable Scan Schedules
  hosts: localhost
  gather_facts: false
  roles:
    - role: tenable/roles/tenable_scan_schedules
```

## License

MIT
