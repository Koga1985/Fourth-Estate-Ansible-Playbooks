# aws_ec2_amis

Aws Ec2 Amis role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ami_state` | `"present"` | No | AMI Configuration |
| `ami_enforce_encryption` | `true` | No | — |
| `ami_enable_cross_region_copy` | `false` | No | — |
| `ami_enable_deprecation` | `true` | No | — |
| `ami_enable_lifecycle_policy` | `true` | No | — |
| `ami_retention_days` | `90` | No | — |
| `ami_deprecation_time` | `"{{ (ansible_date_time.epoch \| int + (ami_retention_days * 86400)) ...` | No | — |
| `ami_tags` | `(see defaults/main.yml)` | No | Default tags |
| `ec2_amis` | `[]` | No | AMIs to create (override in inventory/playbook) |
| `kms_key_id` | `""` | No | KMS key for encryption (required when ami_enforce_encryption is true) |

## Example Playbook

```yaml
---
- name: Aws Ec2 Amis
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_ec2_amis
```

## License

MIT
