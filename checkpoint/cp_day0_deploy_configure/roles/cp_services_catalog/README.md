# cp_services_catalog

Cp Services Catalog role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `publish_changes` | `true` |  |
| `cp_services_tcp` | `[]` |  |
| `cp_services_udp` | `[]` |  |
| `cp_app_sites` | `[]` |  |
| `cp_app_categories` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Cp Services Catalog
  hosts: localhost
  gather_facts: false
  roles:
    - role: checkpoint/cp_day0_deploy_configure/roles/cp_services_catalog
```

## License

MIT
