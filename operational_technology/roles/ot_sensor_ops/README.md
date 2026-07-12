# ot_sensor_ops
Sensor/collector deployment, inventory, upgrades, and tuning.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `dry_run` | `true` | No | — |
| `sensors` | `[]` | No | — |
| `tuning` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use ot_sensor_ops
  hosts: all
  gather_facts: false
  roles:
    - role: ot_sensor_ops
```

## License

MIT
