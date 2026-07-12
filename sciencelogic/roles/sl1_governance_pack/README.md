# sl1_governance_pack

Dashboards, reports, KPIs, backups, drift.

## Requirements

- Ansible 2.13+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `sl1` | `(see defaults/main.yml)` | No | — |
| `artifacts_dir` | `"/tmp/sl1-artifacts"` | No | — |
| `dry_run` | `true` | No | — |
| `dashboards` | `[]` | No | — |
| `reports` | `[]` | No | — |
| `kpi_filter` | `{}` | No | — |
| `backup_enable` | `true` | No | — |

## Example Playbook

```yaml
- name: Use sl1_governance_pack
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_governance_pack
```

## License

MIT
