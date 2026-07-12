# aws_ec2_ebs_volumes

Aws Ec2 Ebs Volumes role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ebs_state` | `"present"` | No | EBS Volume Configuration |
| `ebs_enforce_encryption_by_default` | `true` | No | — |
| `ebs_set_default_kms_key` | `true` | No | — |
| `ebs_enable_automatic_snapshots` | `true` | No | — |
| `ebs_enable_cloudwatch_alarms` | `true` | No | — |
| `ebs_tags` | `(see defaults/main.yml)` | No | Default tags |
| `ebs_alarm_sns_topic` | `""` | No | CloudWatch alarm configuration |
| `ebs_volumes` | `[]` | No | EBS volumes to create (override in inventory/playbook) |
| `kms_key_id` | `""` | No | KMS key for encryption (required) |

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
