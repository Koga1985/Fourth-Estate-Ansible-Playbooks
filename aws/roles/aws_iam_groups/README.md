# aws_iam_groups

Aws Iam Groups role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `iam_group_state` | `"present"` |  |
| `iam_enforce_mfa` | `true` |  |
| `iam_groups` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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
