# ot_logging_pipeline
Normalize and forward OT alerts/events to SIEM/SOAR with artifacts.

## Requirements

- Ansible 2.14+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `/tmp/ot-artifacts` | No | — |
| `hec` | `{}` | No | — |
| `syslog` | `{}` | No | — |
| `alerts` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use ot_logging_pipeline
  hosts: all
  gather_facts: false
  roles:
    - role: ot_logging_pipeline
```

## License

MIT
