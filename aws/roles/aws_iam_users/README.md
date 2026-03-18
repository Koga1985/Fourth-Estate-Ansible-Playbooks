# aws_iam_users

Aws Iam Users role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `iam_user_state` | `"present"` |  |
| `iam_enforce_mfa` | `true` |  |
| `iam_mfa_max_age_days` | `90` |  |
| `iam_user_permissions_boundary` | `"arn:{{ aws_partition | default('aws-us-gov') }...` |  |
| `iam_access_key_max_age_days` | `90` |  |
| `iam_access_key_rotation_enabled` | `true` |  |
| `iam_password_min_length` | `15` |  |
| `iam_password_require_uppercase` | `true` |  |
| `iam_password_require_lowercase` | `true` |  |
| `iam_password_require_numbers` | `true` |  |
| `iam_password_require_symbols` | `true` |  |
| `iam_password_max_age_days` | `60` |  |
| `iam_password_reuse_prevention` | `24` |  |
| `iam_password_hard_expiry` | `false` |  |
| `iam_user_keys_output_dir` | `"/tmp/iam_credentials"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Iam Users
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_iam_users
```

## License

MIT
