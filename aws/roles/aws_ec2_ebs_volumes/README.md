# aws_ec2_ebs_volumes

Aws Ec2 Ebs Volumes role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ebs_state` | `"present"` |  |
| `ebs_enforce_encryption_by_default` | `true` |  |
| `ebs_set_default_kms_key` | `true` |  |
| `ebs_enable_automatic_snapshots` | `true` |  |
| `ebs_enable_cloudwatch_alarms` | `true` |  |
| `ebs_alarm_sns_topic` | `""` |  |
| `ebs_volumes` | `[]` |  |
| `kms_key_id` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Ec2 Ebs Volumes
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_ec2_ebs_volumes
```

## License

MIT
