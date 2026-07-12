# ot_windows_hmi_patching
Staged patching with prechecks, snapshots, rings, and rollback hooks.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `vmware` | `{ snapshot: true }` | No | — |

## Example Playbook

```yaml
- name: Use ot_windows_hmi_patching
  hosts: all
  gather_facts: false
  roles:
    - role: ot_windows_hmi_patching
```

## License

MIT
