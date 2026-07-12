# aws_iam_mfa

Aws Iam Mfa role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `iam_enforce_mfa` | `true` | No | MFA Configuration |
| `iam_mfa_device_type` | `"virtual"` | No | virtual, hardware |
| `iam_mfa_grace_period_days` | `7` | No | — |
| `iam_generate_mfa_report` | `true` | No | Compliance and Reporting |
| `iam_tag_non_compliant` | `true` | No | — |
| `iam_send_mfa_reminders` | `true` | No | — |
| `iam_revoke_keys_without_mfa` | `false` | No | — |
| `notification_webhook_url` | `""` | No | Notification settings |
| `iam_mfa_users` | `[]` | No | Users to check for MFA (override in inventory/playbook) |
| `iam_mfa_policy_tags` | `(see defaults/main.yml)` | No | MFA policy settings |

## Example Playbook

```yaml
---
- name: Aws Iam Mfa
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_iam_mfa
```

## License

MIT
