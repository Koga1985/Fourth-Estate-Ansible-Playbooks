# aws_ec2_amis

Aws Ec2 Amis role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ami_state` | `"present"` |  |
| `ami_enforce_encryption` | `true` |  |
| `ami_enable_cross_region_copy` | `false` |  |
| `ami_enable_deprecation` | `true` |  |
| `ami_enable_lifecycle_policy` | `true` |  |
| `ami_retention_days` | `90` |  |
| `ami_deprecation_time` | `"{{ (ansible_date_time.epoch | int + (ami_reten...` |  |
| `ec2_amis` | `[]` |  |
| `kms_key_id` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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
