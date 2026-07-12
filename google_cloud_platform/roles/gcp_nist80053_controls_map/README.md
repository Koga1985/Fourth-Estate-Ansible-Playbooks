# gcp_nist80053_controls_map

Control→implementation registry with automated evidence hooks into other roles.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `controls` | `[]` | No | — |

## Example Playbook

```yaml
- name: Use gcp_nist80053_controls_map
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_nist80053_controls_map
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
