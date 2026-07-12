# cp_inventory_prune

Cp Inventory Prune role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `cp_allow_delete` | `false` | No | — |
| `dry_run` | `true` | No | — |
| `publish_changes` | `false` | No | — |
| `artifacts_dir` | `"/tmp/checkpoint-artifacts"` | No | — |
| `protected_names` | `["Any","Internet","External","LocalNetwork"]` | No | — |
| `cp_hosts` | `[]` | No | — |
| `cp_networks` | `[]` | No | — |
| `cp_address_ranges` | `[]` | No | — |
| `cp_groups` | `[]` | No | — |
| `cp_services_tcp` | `[]` | No | — |
| `cp_services_udp` | `[]` | No | — |

## Example Playbook

```yaml
---
- name: Cp Inventory Prune
  hosts: localhost
  gather_facts: false
  roles:
    - role: checkpoint/cp_day0_deploy_configure/roles/cp_inventory_prune
```

## License

MIT
