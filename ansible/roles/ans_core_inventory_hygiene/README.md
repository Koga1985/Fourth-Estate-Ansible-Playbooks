# ans_core_inventory_hygiene

Inventory lint (dupes/cycles), variable schema validation.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | — |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `controller_host` | `"{{ lookup('env', 'CONTROLLER_HOST') \| default('https://controller....` | No | — |
| `controller_oauthtoken` | `"{{ lookup('env', 'CONTROLLER_OAUTH_TOKEN') \| default('') }}"` | No | — |
| `cleanup_stale_hosts` | `true` | No | Hygiene Configuration |
| `stale_days` | `90` | No | — |
| `cleanup_empty_groups` | `true` | No | — |
| `cleanup_duplicate_hosts` | `true` | No | — |
| `validate_host_vars` | `true` | No | Inventory Validation |
| `validate_group_vars` | `true` | No | — |
| `validate_inventory_sources` | `true` | No | — |
| `hygiene_report_enabled` | `true` | No | Reporting |
| `hygiene_report_recipients` | `(see defaults/main.yml)` | No | — |
| `fourth_estate_strict_validation` | `true` | No | Fourth Estate |

## Example Playbook

```yaml
- name: Use ans_core_inventory_hygiene
  hosts: all
  gather_facts: false
  roles:
    - role: ans_core_inventory_hygiene
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
