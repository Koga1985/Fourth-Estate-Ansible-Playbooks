# aws_iam_groups

Aws Iam Groups role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `iam_group_state` | `"present"` | No | IAM Group Configuration |
| `iam_group_tags` | `(see defaults/main.yml)` | No | Default tags for all IAM groups |
| `iam_enforce_mfa` | `true` | No | MFA enforcement for groups |
| `iam_groups` | `[]` | No | Example group list (override in inventory/playbook) |

## Example Playbook

```yaml
---
- name: Aws Iam Groups
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_iam_groups
```

## License

MIT
