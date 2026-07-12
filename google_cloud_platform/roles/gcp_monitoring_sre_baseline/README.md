# gcp_monitoring_sre_baseline

Golden alert policies (quota/IAM/VPC-SC), SLOs/error budgets, blackbox uptime checks.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `alerts` | `[]` | No | — |
| `slos` | `[]` | No | — |
| `uptime` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use gcp_monitoring_sre_baseline
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_monitoring_sre_baseline
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
