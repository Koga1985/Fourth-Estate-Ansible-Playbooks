# aws_s3_buckets

Aws S3 Buckets role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

## Role Variables

All variables below are defined in `defaults/main.yml`. "Required" marks values that ship as a placeholder you must replace (e.g. `CHANGE_ME`); everything else has a working default.

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `s3_bucket_name` | `"ansible-managed-bucket"` | No | defaults file for aws_s3_buckets |
| `s3_region` | `"{{ aws_region \| default('us-east-1') }}"` | No | — |
| `s3_versioning` | `true` | No | — |
| `s3_encryption` | `"aws:kms"` | No | — |
| `s3_kms_key_id` | `"alias/aws/s3"` | No | — |
| `s3_block_public_acls` | `true` | No | — |
| `s3_block_public_policy` | `true` | No | — |
| `s3_ignore_public_acls` | `true` | No | — |
| `s3_restrict_public_buckets` | `true` | No | — |
| `s3_lifecycle_enabled` | `false` | No | — |
| `s3_state` | `"present"` | No | — |
| `s3_tags` | `(see defaults/main.yml)` | No | — |

## Example Playbook

```yaml
---
- name: Aws S3 Buckets
  hosts: localhost
  gather_facts: false
  roles:
    - role: aws/roles/aws_s3_buckets
```

## License

MIT
