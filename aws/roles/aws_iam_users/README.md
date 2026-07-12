# aws_iam_users

Aws Iam Users role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `iam_user_state` | `"present"` | No | IAM User Configuration |
| `iam_user_tags` | `(see defaults/main.yml)` | No | Default tags for all IAM users |
| `iam_enforce_mfa` | `true` | No | MFA enforcement |
| `iam_mfa_max_age_days` | `90` | No | — |
| `iam_user_permissions_boundary` | `"arn:{{ aws_partition \| default('aws-us-gov') }}:iam::{{ aws_accoun...` | No | Permissions boundary for all users (FedRAMP requirement) |
| `iam_access_key_max_age_days` | `90` | No | Access key rotation settings |
| `iam_access_key_rotation_enabled` | `true` | No | — |
| `iam_password_min_length` | `15` | No | Password policy requirements (FedRAMP High) |
| `iam_password_require_uppercase` | `true` | No | — |
| `iam_password_require_lowercase` | `true` | No | — |
| `iam_password_require_numbers` | `true` | No | — |
| `iam_password_require_symbols` | `true` | No | — |
| `iam_password_max_age_days` | `60` | No | — |
| `iam_password_reuse_prevention` | `24` | No | — |
| `iam_password_hard_expiry` | `false` | No | — |
| `iam_user_keys_output_dir` | `"/tmp/iam_credentials"` | No | Output directory for credentials (should be encrypted) |
| `iam_users` | `[]` | No | Example user list (override in inventory/playbook) |

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
