# cp_inventory_prune

Cp Inventory Prune role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `cp_allow_delete` | `false` |  |
| `dry_run` | `true` |  |
| `publish_changes` | `false` |  |
| `artifacts_dir` | `"/tmp/checkpoint-artifacts"` |  |
| `protected_names` | `["Any","Internet","External","LocalNetwork"]` |  |
| `cp_hosts` | `[]` |  |
| `cp_networks` | `[]` |  |
| `cp_address_ranges` | `[]` |  |
| `cp_groups` | `[]` |  |
| `cp_services_tcp` | `[]` |  |
| `cp_services_udp` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

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
