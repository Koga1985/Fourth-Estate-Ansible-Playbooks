# sl1_collector_fleet

Provision/upgrade collectors, assign to Collection Groups, drain/evacuate for maintenance.

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
| `collectors` | `[]` | No | — |
| `maintenance` | `{ drain: false, evacuate: false }` | No | — |

## Example Playbook

```yaml
- name: Use sl1_collector_fleet
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_collector_fleet
```

## License

MIT
