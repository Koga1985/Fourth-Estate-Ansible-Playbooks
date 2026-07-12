# ot_network_backup
Config backup for L2/L3 network devices with diff and secure offload.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `dry_run` | `true` | No | — |
| `offload` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use ot_network_backup
  hosts: all
  gather_facts: false
  roles:
    - role: ot_network_backup
```

## License

MIT
