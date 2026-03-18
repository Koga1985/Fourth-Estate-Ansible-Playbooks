# aws_ec2_snapshots

Aws Ec2 Snapshots role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `snapshot_state` | `"present"` |  |
| `snapshot_enable_cross_region_copy` | `false` |  |
| `snapshot_enable_lifecycle_policy` | `true` |  |
| `snapshot_enable_cleanup` | `true` |  |
| `snapshot_create_catalog` | `true` |  |
| `snapshot_retention_days` | `90` |  |
| `snapshot_retention_count` | `7` |  |
| `snapshot_lifecycle_policy_name` | `"automated-ebs-snapshots"` |  |
| `ebs_snapshots` | `[]` |  |
| `kms_key_id` | `""` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Example Playbook

```yaml
---
- name: Aws Ec2 Snapshots
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_ec2_snapshots
```

## License

MIT
