# aws_s3_buckets

Aws S3 Buckets role for Fourth Estate infrastructure automation.

> For full details, see the platform-level README: `aws/README.md`

## Role Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `s3_bucket_name` | `"ansible-managed-bucket"` |  |
| `s3_region` | `"{{ aws_region | No | default('us-east-1') }}"` |
| `s3_versioning` | `true` |  |
| `s3_encryption` | `"aws:kms"` |  |
| `s3_kms_key_id` | `"alias/aws/s3"` |  |
| `s3_block_public_acls` | `true` |  |
| `s3_block_public_policy` | `true` |  |
| `s3_ignore_public_acls` | `true` |  |
| `s3_restrict_public_buckets` | `true` |  |
| `s3_lifecycle_enabled` | `false` |  |
| `s3_state` | `"present"` |  |

See `defaults/main.yml` for the full variable list.

## Requirements

- Ansible 2.15+
- Collection: `amazon.aws community.aws`
- See platform `requirements.yml` for install instructions

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
