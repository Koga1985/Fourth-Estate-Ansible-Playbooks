# ot_metrics_reporting
KPI pack: digests, scorecards, monthly summaries.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |

## Example Playbook

```yaml
- name: Use ot_metrics_reporting
  hosts: all
  gather_facts: false
  roles:
    - role: ot_metrics_reporting
```

## License

MIT
