# gcp_bigquery_governance

BQ dataset taxonomy, default CMEK, RLS/CLS, approved locations, DLP job triggers, query-access logs.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `datasets` | `[]` | No | — |
| `approved_locations` | `[]` | No | — |
| `bq_policies` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_bigquery_governance
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_bigquery_governance
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
