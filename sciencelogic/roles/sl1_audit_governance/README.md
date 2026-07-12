# sl1_audit_governance

Admin/actions export, change logs, access reviews; weekly compliance bundle.

Defaults in `defaults/main.yml`. Artifacts in `{ artifacts_dir }`.

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
| `week_start` | `"Mon"` | No | — |
| `include_access_reviews` | `true` | No | — |

## Example Playbook

```yaml
- name: Use sl1_audit_governance
  hosts: all
  gather_facts: false
  roles:
    - role: sl1_audit_governance
```

## License

MIT
