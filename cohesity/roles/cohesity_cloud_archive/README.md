# cohesity_cloud_archive

Cohesity Cloud Archive role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `cohesity/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Cohesity Cloud Archive
  hosts: localhost
  gather_facts: false
  roles:
    - role: cohesity/roles/cohesity_cloud_archive
```

## License

MIT
