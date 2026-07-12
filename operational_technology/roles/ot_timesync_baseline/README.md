# ot_timesync_baseline
Audit NTP/PTP (read-mostly); guarded config push only during maintenance windows.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `dry_run` | `true` | No | — |
| `maintenance_window` | `false` | No | — |
| `timesources` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use ot_timesync_baseline
  hosts: all
  gather_facts: false
  roles:
    - role: ot_timesync_baseline
```

## License

MIT
