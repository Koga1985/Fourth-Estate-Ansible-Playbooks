# sl1_upgrade_window

Preflight checks, backup/snapshots, rolling SL1/collector upgrades with guards.

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
| `targets` | `{ sl1_core: true, collectors: [] }` | No | — |
| `backup` | `{ enabled: true }` | No | — |
| `window` | `{ start: "", end: "" }` | No | — |
| `gates` | `{ fail_on_active_incidents: true, min_free_space_gb: 10 }` | No | — |

## Example Playbook

```yaml
- name: Use sl1_upgrade_window
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_upgrade_window
```

## License

MIT
