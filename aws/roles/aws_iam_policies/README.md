# aws_iam_policies

Aws Iam Policies role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `iam_policy_state` | `"present"` |  |
| `iam_create_fedramp_policies` | `true` |  |
| `iam_enforce_encryption` | `true` |  |
| `iam_restrict_regions` | `true` |  |
| `iam_policies` | `[]` |  |
| `iam_boundary_policies` | `[]` |  |
| `iam_service_policies` | `[]` |  |
| `iam_policy_attachments` | `[]` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Iam Policies
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_iam_policies
```

## License

MIT
