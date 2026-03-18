# cp_inventory_model

Cp Inventory Model role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `checkpoint/cp_day0_deploy_configure/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `publish_changes` | `true` |  |
| `artifacts_dir` | `"/tmp/checkpoint-artifacts"` |  |
| `cp_hosts` | `[]` |  |
| `cp_networks` | `[]` |  |
| `cp_address_ranges` | `[]` |  |
| `cp_groups` | `[]` |  |
| `replace_members` | `true` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `See platform requirements.yml`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Cp Inventory Model
  hosts: localhost
  gather_facts: false
  roles:
    - role: checkpoint/cp_day0_deploy_configure/roles/cp_inventory_model
```

## License

MIT
