# gcp_audit_governance_pack

Org policy export, CAI snapshots, SCC findings digest, IAM principals matrix, evidence ZIP (schedulable).

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `scopes` | `[]` | No | — |
| `outputs` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_audit_governance_pack
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_audit_governance_pack
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
