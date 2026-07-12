# gcp_inventory_baseline

Cloud Asset Inventory daily exports to GCS/BQ; drift compares (org policies, APIs, CMEK coverage).

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `exports` | `[]` | No | — |
| `drift_checks` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use gcp_inventory_baseline
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_inventory_baseline
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
