# gcp_cloudrun_locked_down

Cloud Run defaults: internal-only, CMEK, min TLS, CPU/mem limits; domain restrictions; per-service exceptions.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `services` | `[]` | No | — |
| `defaults` | `{}` | No | — |
| `exceptions` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use gcp_cloudrun_locked_down
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_cloudrun_locked_down
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
