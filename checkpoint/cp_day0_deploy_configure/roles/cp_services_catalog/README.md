# cp_services_catalog

Cp Services Catalog role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `publish_changes` | `true` | No | — |
| `cp_services_tcp` | `[]` | No | — |
| `cp_services_udp` | `[]` | No | — |
| `cp_app_sites` | `[]` | No | — |
| `cp_app_categories` | `[]` | No | — |

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
