# ans_ops_artifacts_retention

Age-based purge of artifacts_dir and optional extra paths; optional size cap. Always writes CSV report.

## Requirements

- Ansible 2.15+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `apply_changes` | `false` | No | — |
| `artifacts_dir` | `"/tmp/ansible-artifacts"` | No | — |
| `validate_certs` | `true` | No | — |
| `artifact_retention_days` | `90` | No | Retention Configuration |
| `log_retention_days` | `365` | No | — |
| `backup_retention_days` | `30` | No | — |
| `cleanup_enabled` | `true` | No | Cleanup Schedule |
| `cleanup_schedule` | `"daily"` | No | — |
| `fourth_estate_compliance_retention` | `2555` | No | Fourth Estate 7 years |
| `fourth_estate_evidence_archival` | `true` | No | — |

## Example Playbook

```yaml
- name: Use ans_ops_artifacts_retention
  hosts: all
  gather_facts: false
  roles:
    - role: ans_ops_artifacts_retention
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
