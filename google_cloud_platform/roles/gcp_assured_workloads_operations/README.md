# gcp_assured_workloads_operations

Assured Workloads: creation/guardrails, residency checks, restricted support personnel controls, evidence exports.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `workloads` | `[]` | No | — |
| `controls` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_assured_workloads_operations
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_assured_workloads_operations
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
