# gcp_iam_foundations

IAM baselines for org/folder/project; custom roles; conditional bindings and break-glass; access review CSVs.

## Requirements

- Ansible 2.12+
- No additional Ansible collections required (uses `ansible.builtin`), unless noted below.

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `artifacts_dir` | `"/tmp/gcp-artifacts"` | No | — |
| `apply_changes` | `false` | No | — |
| `gcloud_bin` | `"gcloud"` | No | — |
| `org_id` | `""` | No | — |
| `folders` | `[]` | No | — |
| `projects` | `[]` | No | — |
| `custom_roles` | `[]` | No | — |
| `iam_bindings` | `[]` | No | — |
| `break_glass` | `{}` | No | — |

## Example Playbook

```yaml
- name: Use gcp_iam_foundations
  hosts: all
  gather_facts: false
  roles:
    - role: gcp_iam_foundations
      vars:
        apply_changes: false   # set true to apply
```

## License

MIT
