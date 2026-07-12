# aws_ec2_snapshots

Aws Ec2 Snapshots role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `snapshot_state` | `"present"` | No | Snapshot Configuration |
| `snapshot_enable_cross_region_copy` | `false` | No | — |
| `snapshot_enable_lifecycle_policy` | `true` | No | — |
| `snapshot_enable_cleanup` | `true` | No | — |
| `snapshot_create_catalog` | `true` | No | — |
| `snapshot_retention_days` | `90` | No | — |
| `snapshot_retention_count` | `7` | No | — |
| `snapshot_lifecycle_policy_name` | `"automated-ebs-snapshots"` | No | Lifecycle policy configuration |
| `snapshot_lifecycle_target_tags` | `(see defaults/main.yml)` | No | — |
| `snapshot_tags` | `(see defaults/main.yml)` | No | Default tags |
| `ebs_snapshots` | `[]` | No | Snapshots to create (override in inventory/playbook) |
| `kms_key_id` | `""` | No | KMS key for encryption |

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
